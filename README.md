# Framey 🖼️

Framey is a command-line interface (CLI) tool designed for framing images. It allows users to easily create framed versions of their images by specifying various parameters such as frame width, background color, and output size. This project was developed as a personal assignment for Boot.dev.

## Usage

To use Framey, run the following command in your terminal:

```bash
python framey.py <source> <width> [options]
```

### Arguments

-   `<source>`: URL or path to the image.
-   `<width>`: Width of the image in centimeters (cm).

### Options

-   `-v`, `--verbose`: Enable verbose output.
-   `-o`, `--output-size`: Set the width of the output image in pixels (px). Defaults to the same width as the input image.
-   `-bc`, `--background-color`: Set the background color (default: white). Accepts hex, RGB, or HTML color names.
-   `-fw`, `--frame-width`: Specify the thickness of the frame in centimeters (cm). Accepts float values (default: 2.0 cm).
-   `-pw`, `--pasp-width`: Thickness of the passepartout in centimeters (cm). If not specified, it is calculated based on the artwork size.
-   `-bw`, `--background-width`: The width of the background/wall visible behind the framed picture in centimeters (cm). Defaults to 2 cm.
-   `-fc`, `--frame_color`: Choose the frame color (default: black). Accepts RGB, HEX, or HTML color names.

## Example

```bash
python framey.py "path/to/image.jpg" 10 -v --output-size 1080 --background-color "#f0f0f0" -fw 1.5
```

This command frames the specified image with a width of 10 cm, outputs verbose information, sets the output size to 1080 pixels wide, uses a light grey background color, and specifies a 1.5 cm frame thickness.

## Installation

To clone the repository and run Framey, follow these steps:

1. **Clone the Repository**:
   Open your terminal and run the following command:

   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/framey.git
   ```
   Replace YOUR_GITHUB_USERNAME with your actual GitHub username.

2.	Navigate to the Project Directory:

Change to the project directory:

```bash
cd framey
```

	3.	Set Up a Virtual Environment (Optional):

It is recommended to use a virtual environment to manage dependencies. You can create one using:

```bash
python -m venv ven
```

Activate the virtual environment:

	▪	On Windows:

```bash
venv\Scripts\activate
```

	▪	On macOS/Linux:

```bash
source venv/bin/activate
```

	4.	Install Required Packages:
Install the package and dependencies using:

```bash
pip install .
```

## License

This project is licensed under the MIT License.
