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
    parser.add_argument(
        "-o",
        "--output-size",
        type=int,
        help="The width of output image in px. Defaults to same as input",
    )
    parser.add_argument(
        "-bc",
        "--background-color",
        default="white",
        help="Add background color, hex, rgb or html color names. Defaults to white",
    )
    parser.add_argument(
        "-fw",
        "--frame-width",
        default=2.0,
        type=float,
        help="Specify the thickness of the frame, in cm (accepts float, default is 2.0)",
    )
    parser.add_argument(
        "-pw",
        "--pasp-width",
        type=float,
        help="Thickness of passepartout in cm, float. Gets calculated based on artwork size if not specified",
    )
    parser.add_argument(
        "-bw",
        "--background-width",
        type=float,
        default=2,
        help="The width of background/wall visible behand the framed picture, cm float, default 2 cm",
    )
    parser.add_argument(
        "-fc",
        "--frame_color",
        default="black",
        help="Choose frame color, RGB, HEX, html color names. Default is black",
    )

    return parser.parse_args()
