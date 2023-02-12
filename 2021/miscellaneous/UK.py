from manim import *

class Ukraine(Scene):
    def construct(self):
        #
        # text = Tex('What can be if democratic world and citizens of the country\\ close their eyes on the dictatorship?')
        #
        # self.play(FadeIn(text))
        #
        # image1 = ImageMobject('/Users/isaigordeev/Downloads/1.jpg').scale(0.6)
        # image2 = ImageMobject('/Users/isaigordeev/Downloads/2.jpg').scale(0.6)
        # image3 = ImageMobject('/Users/isaigordeev/Downloads/3.jpg').scale(0.6)
        # image4 = ImageMobject('/Users/isaigordeev/Downloads/4.jpeg').scale(0.6)
        # image5 = ImageMobject('/Users/isaigordeev/Downloads/5.jpeg').scale(0.6)
        # image6 = ImageMobject('/Users/isaigordeev/Downloads/6.jpg').scale(0.6)
        # image7 = ImageMobject('/Users/isaigordeev/Downloads/7.jpg').scale(0.6)
        # #
        # self.wait(2)
        # self.play(FadeOut(text))
        # self.play(FadeIn(image1))
        # self.play(ReplacementTransform(text, image1))
        # self.play(ReplacementTransform(image1, image2))
        # self.play(ReplacementTransform(image2, image3))
        # self.play(ReplacementTransform(image3, image4))
        # self.play(ReplacementTransform(image4, image5))
        # self.play(ReplacementTransform(image5, image6))
        # self.play(ReplacementTransform(image6, image7))

        # self.play(FadeOut(image7))

        rectangle = Rectangle(color = BLUE_D,  fill_opacity=1, width=6, height=2)
        rectangle_ye = Rectangle(color = YELLOW, fill_opacity=1, width=6, height=2 )
        rectangle_ye.next_to(rectangle, DOWN, buff=0)

        flag = Group(rectangle, rectangle_ye)
        flag.scale(0.6)

        text = Tex('Stand with Ukraine')

        text.next_to(flag, 1.5*UP)

        flag = Group(flag, text)
        flag.shift(UP)
        self.play(FadeIn(flag))
        #
        # self.wait()
        #
        # self.play(FadeOut(flag), run_time = 3)




