import requests
from PIL import Image
from io import BytesIO
from utils import log


PASSEPARTOUT_WIDTH = 2.5
FRAME_WIDTH = 1.5
BACKGROUND_WIDTH = 2
OUTPUT_PATH = "test.jpg"


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
    return width + (padding * 2), height + (padding * 2)


def create_framed_image(image, args):
    scaling_factor = image.width / args.width
    log(f"Determined scaling factor {scaling_factor}", args.verbose)

    image_width_cm, image_height_cm = args.width, image.height / scaling_factor
    log(f"Image width: {image_width_cm}, image height: {image_height_cm}", args.verbose)

    pasp_width_cm, pasp_height_cm = calculate_dimensions(
        image_width_cm, image_height_cm, PASSEPARTOUT_WIDTH
    )
    pasp_width_px, pasp_height_px = int(pasp_width_cm * scaling_factor), int(pasp_height_cm * scaling_factor)
    log(f"Passepartout w: {pasp_width_cm}, h: {pasp_height_cm}", args.verbose)

    frame_width_cm, frame_height_cm = calculate_dimensions(pasp_width_cm, pasp_height_cm, FRAME_WIDTH)
    frame_width_px, frame_height_px = int(frame_width_cm * scaling_factor), int(frame_height_cm * scaling_factor)
    log(f"Frame w: {frame_width_cm}, h: {frame_height_cm}\nFrame w px: {frame_width_px}, h px: {frame_height_px}", args.verbose)

    total_width_cm, total_height_cm = frame_width_cm + (
        BACKGROUND_WIDTH * 2
    ), frame_height_cm + (BACKGROUND_WIDTH * 2)
    total_width_px, total_height_px = int(total_width_cm * scaling_factor), int(total_height_cm * scaling_factor)
    log(f"Total w: {total_width_cm}, h: {total_height_cm}\nTotal in px w: {total_width_px}, h: {total_height_px}", args.verbose)


    background = Image.new("RGB", (total_width_px, total_height_px), "white")

    frame = Image.new("RGB", (frame_width_px, frame_height_px), "black")
    background.paste(frame, ((total_width_px - frame_width_px) // 2, (total_height_px - frame_height_px) // 2))

    passepartout = Image.new("RGB", (pasp_width_px, pasp_height_px), "white")
    background.paste(passepartout, ((total_width_px - pasp_width_px) // 2, (total_height_px - pasp_height_px) // 2))

    # artwork = image.resize()

    background.save(OUTPUT_PATH)

    return
