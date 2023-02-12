from manim import *

class pdffile(MovingCameraScene):
    def construct(self):
        Re = Tex('tex')

        ASPECT_RATIO = 4 / 9
        FRAME_HEIGHT = 8.0
        FRAME_WIDTH = FRAME_HEIGHT * ASPECT_RATIO

        background = Rectangle(
            width=FRAME_WIDTH,
            height=FRAME_HEIGHT,
            fill_color=WHITE,
            stroke_opacity=0,
            fill_opacity=1)

        self.camera.frame.set(width=FRAME_HEIGHT, height=FRAME_WIDTH , run_time=6).shift

        self.add(Re, background)