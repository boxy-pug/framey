# Framey 🖼️

Framey is a command-line interface (CLI) tool designed for framing images. This project was developed as a personal assignment for Boot.dev, aiming to enhance skills in Python programming and CLI tool development.

## Usage

To use Framey, run the following command in your terminal:

```bash
python framey.py <source> <width> [options]
```

### Arguments

-  `<source>`: URL or path to the image.
-  `<width>`: Width of the image in centimeters.

### Options

-  `-v`, `--verbose`: Enable verbose output.
-  `-o`, `--output-size`: Set the width of the output image in pixels.
-  `-bc`, `--background-color`: Set the background color (default: white).
-  `-fw`, `--frame-width`: Set the thickness of the frame, in cm (float, default 2 cm)

## Example

```bash
python framey.py "path/to/image.jpg" 10 -v --output-size 1080 --background-color "#f0f0f0" -fw 1.5
```

This command frames the specified image with a width of 10 cm, outputs verbose information, sets the output size to 1080 pixels wide, uses a light grey background color and specifies a 1.5 cm frame thickness.

## License

This project is licensed under the MIT License.
d