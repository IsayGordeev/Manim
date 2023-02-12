from manim import *
class Tanya(Scene):
    def construct(self):
        textxray = Tex('X-Ray ', 'on visible light', ' scale')
        subtext = Tex('on its scale').shift(UP)
        self.play(Write(textxray))
        self.play(Transform(textxray,subtext, rate_func=there_and_back))
        # self.play(Transform(subtext,textxray, rate_func=there_and_back))

