import requests
from PIL import Image
from io import BytesIO
from utils import log


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
