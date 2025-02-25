import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="Framey", description="A CLI tool for framing images"
    )

    parser.add_argument("source", help="URL or path to image")
    parser.add_argument("width", help="Width of image, in cm", type=int, default=10)
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output"
    )

    return parser.parse_args()
