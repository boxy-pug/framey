from PIL import Image
from utils import get_new_filename


class FramedImage:

    def __init__(self, image, args):
        self.image = image
        self.args = args
        self.scaling_factor = image.width / args.width
        self.aspect_ratio = image.height / image.width
        self.art_w_cm, self.art_h_cm = args.width, image.height / self.scaling_factor
        self.art_w_px, self.art_h_px = image.width, image.height
        self.pasp_w_cm, self.pasp_h_cm = self.calculate_pasp_size_cm(args)
        self.pasp_w_px, self.pasp_h_px = int(self.pasp_w_cm * self.scaling_factor), int(
            self.pasp_h_cm * self.scaling_factor
        )
        self.frame_w_cm, self.frame_h_cm = self.calculate_frame_size_cm(args)
        self.frame_w_px, self.frame_h_px = int(
            self.frame_w_cm * self.scaling_factor
        ), int(self.frame_h_cm * self.scaling_factor)
        self.total_w_cm, self.total_h_cm = self.calculate_background_width_cm(args)
        self.total_w_px, self.total_h_px = int(
            self.total_w_cm * self.scaling_factor
        ), int(self.total_h_cm * self.scaling_factor)
        self.pasp_border_width_px = self.frame_w_px // 100

    def calculate_pasp_size_cm(self, args):
        p_width = 4
        if args.pasp_width:
            p_width = args.pasp_width
        else:
            p_width += self.art_w_cm / 10
        return self.art_w_cm + (p_width * 2), self.art_h_cm + (p_width * 2)

    def calculate_pasp_border_width(self):
        return 5

    def calculate_frame_size_cm(self, args):
        return self.pasp_w_cm + (args.frame_width * 2), self.pasp_h_cm + (
            args.frame_width * 2
        )

    def calculate_background_width_cm(self, args):
        return self.frame_w_cm + (args.background_width * 2), self.frame_h_cm + (
            args.background_width * 2
        )

    def calculate_position(self, x, y):
        w = (self.total_w_px - x) // 2
        h = (self.total_h_px - y) // 2
        return w, h

    def create_framed_picture(self):
        background = Image.new(
            "RGB", (self.total_w_px, self.total_h_px), self.args.background_color
        )

        frame = Image.new(
            "RGB", (self.frame_w_px, self.frame_h_px), self.args.frame_color
        )

        passepartout = Image.new("RGB", (self.pasp_w_px, self.pasp_h_px), "white")

        passepartout_inner_border = Image.new(
            "RGB",
            (
                self.art_w_px + self.pasp_border_width_px,
                self.art_h_px + self.pasp_border_width_px,
            ),
            "whitesmoke",
        )

        artwork = self.image

        background.paste(
            frame,
            (self.calculate_position(self.frame_w_px, self.frame_h_px)),
        )

        background.paste(
            passepartout,
            (self.calculate_position(self.pasp_w_px, self.pasp_h_px)),
        )
        background.paste(
            passepartout_inner_border,
            (
                self.calculate_position(
                    self.art_w_px + self.pasp_border_width_px,
                    self.art_h_px + self.pasp_border_width_px,
                )
            ),
        )
        background.paste(
            artwork,
            (self.calculate_position(self.art_w_px, self.art_h_px)),
        )

        final_width, final_height = self.get_final_image_size(background)
        final_image = background.resize((final_width, final_height))
        new_filename = get_new_filename(self.image.filename)
        print(new_filename)

        final_image.save(new_filename)

        return

    def get_final_image_size(self, img):
        final_aspect_ratio = img.height / img.width
        w = self.image.width
        if self.args.output_size:
            w = self.args.output_size
        return int(w), int(w * final_aspect_ratio)

    def __repr__(self):
        return (
            f"FramedImage("
            f"scaling_factor={self.scaling_factor:.2f}\n"
            f"aspect_ratio={self.aspect_ratio:.2f}\n"
            f"art_w_cm={self.art_w_cm:.2f}\n"
            f"art_h_cm={self.art_h_cm:.2f}\n"
            f"art_w_px={self.art_w_px}\n"
            f"art_h_px={self.art_h_px}\n"
            f"pasp_border_w_px={self.pasp_border_width_px:.2f}\n"
            f"pasp_w_cm={self.pasp_w_cm:.2f}\n"
            f"pasp_h_cm={self.pasp_h_cm:.2f}\n"
            f"frame_w_cm={self.frame_w_cm:.2f}\n"
            f"frame_h_cm={self.frame_h_cm:.2f}\n"
            f"total_w_cm={self.total_w_cm:.2f}\n"
            f"total_h_cm={self.total_h_cm:.2f}\n"
            f")"
        )
