import requests
from PIL import Image
from io import BytesIO
from utils import log


PASSEPARTOUT_WIDTH = 2.5
FRAME_WIDTH = 1.5
BACKGROUND_WIDTH = 2


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
    aspect_ratio = args.width / image.width
    log(f"Determined aspect ratio {aspect_ratio}", args.verbose)

    image_width_cm, image_height_cm = args.width, image.height * aspect_ratio
    log(f"Image width: {image_width_cm}, image height: {image_height_cm}", args.verbose)

    pasp_width_cm, pasp_height_cm = calculate_dimensions(
        image_width_cm, image_height_cm, PASSEPARTOUT_WIDTH
    )
    log(f"Passepartout w: {pasp_width_cm}, h: {pasp_height_cm}", args.verbose)

    frame_width_cm, frame_height_cm = calculate_dimensions(pasp_width_cm, pasp_height_cm, FRAME_WIDTH)
    log(f"Frame w: {frame_width_cm}, h: {frame_height_cm}", args.verbose)

    total_width_cm, total_height_cm = frame_width_cm + (
        BACKGROUND_WIDTH * 2
    ), frame_height_cm + (BACKGROUND_WIDTH * 2)
    log(f"Total w: {total_width_cm}, h: {total_height_cm}", args.verbose)
    return
