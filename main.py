import requests
from PIL import Image
from io import BytesIO
import argparse
from cli import parse_arguments
from image_processing import load_image, create_framed_image
from utils import log


def main():
    args = parse_arguments()
    log("Verbose mode enabled", args.verbose)
    image = load_image(args.source)
    log(f"Loading image {args.source}", args.verbose)
    create_framed_image(image, args)


if __name__ == "__main__":
    main()
