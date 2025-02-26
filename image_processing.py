import requests
from PIL import Image
from io import BytesIO
from utils import log


PASSEPARTOUT_WIDTH = 3 * 2
FRAME_WIDTH = 1.5 * 2
BACKGROUND_WIDTH = 3 * 2
OUTPUT_PATH = "samples/test.jpg"

def download_image(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(
                f"Failed to download image, status code: {response.status_code}"
            )
        image = Image.open(BytesIO(response.content))
        return image
    except Exception as e:
        print(f"Error: {str(e)}")
        return None


def load_image(url_or_path):
    if url_or_path.startswith("https://") or url_or_path.startswith("http://"):
        return download_image(url_or_path)
    else:
        return Image.open(url_or_path)


def calculate_dimensions(width, height, padding):
    return width + padding, height + padding


def create_framed_image(image, args):
    scaling_factor = image.width / args.width
    log(f"Determined scaling factor {image.width} / {args.width} = {scaling_factor}", args.verbose)

    aspect_ratio = image.height / image.width

    artwork_width_cm, artwork_height_cm = args.width, int(image.height / scaling_factor)
    artwork_width_px, artwork_height_px = image.width, image.height
    log(f"Artwork width: {artwork_width_cm}, artwork height: {artwork_height_cm}\nArtwork width px: {artwork_width_px}, height: {artwork_height_px}", args.verbose)

    pasp_width_cm, pasp_height_cm = calculate_dimensions(
        artwork_width_cm, artwork_height_cm, PASSEPARTOUT_WIDTH
    )
    pasp_width_px, pasp_height_px = int(pasp_width_cm * scaling_factor), int(pasp_height_cm * scaling_factor)
    log(f"Passepartout w: {pasp_width_cm}, h: {pasp_height_cm}", args.verbose)

    frame_width_cm, frame_height_cm = calculate_dimensions(pasp_width_cm, pasp_height_cm, FRAME_WIDTH)
    frame_width_px, frame_height_px = int(frame_width_cm * scaling_factor), int(frame_height_cm * scaling_factor)
    log(f"Frame w: {frame_width_cm}, h: {frame_height_cm}\nFrame w px: {frame_width_px}, h px: {frame_height_px}", args.verbose)

    total_width_cm, total_height_cm = calculate_dimensions(frame_width_cm, frame_height_cm, BACKGROUND_WIDTH)
    total_width_px, total_height_px = int(total_width_cm * scaling_factor), int(total_height_cm * scaling_factor)
    log(f"Total w: {total_width_cm}, h: {total_height_cm}\nTotal in px w: {total_width_px}, h: {total_height_px}", args.verbose)


    background = Image.new("RGB", (total_width_px, total_height_px), args.background_color)

    frame = Image.new("RGB", (frame_width_px, frame_height_px), "black")
    background.paste(frame, ((total_width_px - frame_width_px) // 2, (total_height_px - frame_height_px) // 2))

    passepartout = Image.new("RGB", (pasp_width_px, pasp_height_px), "white")
    passepartout.paste(image, ((pasp_width_px - artwork_width_px) // 2, (pasp_height_px - artwork_height_px) // 2))
    background.paste(passepartout, ((total_width_px - pasp_width_px) // 2, (total_height_px - pasp_height_px) // 2))

    output_width_px = image.width
    if args.output_size:
        output_width_px = args.output_size


    resized = background.resize((output_width_px, int(output_width_px * aspect_ratio)))
    resized.save(OUTPUT_PATH)

    return