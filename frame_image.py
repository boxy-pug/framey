from PIL import Image


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
        # self.pasp_border_width_px = self.calculate_pasp_border_width_px()
        self.frame_w_cm, self.frame_h_cm = self.calculate_frame_size_cm(args)
        self.frame_w_px, self.frame_h_px = int(
            self.frame_w_cm * self.scaling_factor
        ), int(self.frame_h_cm * self.scaling_factor)
        self.total_w_cm, self.total_h_cm = self.calculate_background_width_cm(args)
        self.total_w_px, self.total_h_px = int(
            self.total_w_cm * self.scaling_factor
        ), int(self.total_h_cm * self.scaling_factor)

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

    def create_framed_picture(self):
        background = Image.new(
            "RGB", (self.total_w_px, self.total_h_px), self.args.background_color
        )

        frame = Image.new(
            "RGB", (self.frame_w_px, self.frame_h_px), self.args.frame_color
        )
        background.paste(
            frame,
            (
                (self.total_w_px - self.frame_w_px) // 2,
                (self.total_h_px - self.frame_h_px) // 2,
            ),
        )

        passepartout = Image.new("RGB", (self.pasp_w_px, self.pasp_h_px), "white")
        passepartout.paste(
            self.image,
            (
                (self.pasp_w_px - self.art_w_px) // 2,
                (self.pasp_h_px - self.art_h_px) // 2,
            ),
        )
        background.paste(
            passepartout,
            (
                (self.total_w_px - self.pasp_w_px) // 2,
                (self.total_h_px - self.pasp_h_px) // 2,
            ),
        )

        output_width_px = self.image.width
        if self.args.output_size:
            output_width_px = self.args.output_size

        resized = background.resize(
            (output_width_px, int(output_width_px * self.aspect_ratio))
        )
        resized.save("samples/test2.jpg")

        return

    def __repr__(self):
        return (
            f"FramedImage("
            f"scaling_factor={self.scaling_factor:.2f}\n"
            f"aspect_ratio={self.aspect_ratio:.2f}\n"
            f"art_w_cm={self.art_w_cm:.2f}\n"
            f"art_h_cm={self.art_h_cm:.2f}\n"
            f"art_w_px={self.art_w_px}\n"
            f"art_h_px={self.art_h_px}\n"
            f"pasp_w_cm={self.pasp_w_cm:.2f}\n"
            f"pasp_h_cm={self.pasp_h_cm:.2f}\n"
            f"frame_w_cm={self.frame_w_cm:.2f}\n"
            f"frame_h_cm={self.frame_h_cm:.2f}\n"
            f"total_w_cm={self.total_w_cm:.2f}\n"
            f"total_h_cm={self.total_h_cm:.2f}\n"
            f")"
        )
