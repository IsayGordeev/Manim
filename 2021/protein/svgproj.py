from manim import *

class intro(Scene):
    def construct(self):
        # self.camera.background_color = WHITE
        scatter = SVGMobject('/Users/isajgordeev/Desktop/УЧЕБА/IV/scatter/diffraction.svg').scale(3)
        diffr = SVGMobject('/Users/isajgordeev/Desktop/УЧЕБА/IV/scatter/scattering.svg').scale(3)
        patter = SVGMobject('/Users/isajgordeev/Desktop/УЧЕБА/IV/scatter/patterson.svg').scale(3)
        protdot = SVGMobject('/Users/isajgordeev/Desktop/УЧЕБА/IV/scatter/proteindot.svg').scale(3)
        protein = SVGMobject('/Users/isajgordeev/Desktop/УЧЕБА/IV/scatter/protein.svg').scale(3)


        self.play(Create(scatter), run_time=7)
        self.wait(3)
        self.play(ReplacementTransform(scatter, diffr), run_time=7)
        self.wait(3)
        self.play(ReplacementTransform(diffr, patter), run_time=7)
        self.wait(3)

        self.play(ReplacementTransform(patter, protdot), run_time=7)
        self.wait(3)
        self.play(Uncreate(protdot), Create(protein), run_time=7)
        self.wait(3)

class introone(MovingCameraScene):
    def construct(self):
        # self.camera.background_color = WHITE
        scatter = SVGMobject('/Users/isajgordeev/Desktop/УЧЕБА/IV/scatter/diffraction.svg').move_to(3*LEFT+2*UP)
        diffr = SVGMobject('/Users/isajgordeev/Desktop/УЧЕБА/IV/scatter/scattering.svg').move_to(3*RIGHT+2*UP)
        patter = SVGMobject('/Users/isajgordeev/Desktop/УЧЕБА/IV/scatter/patterson.svg').move_to(3*RIGHT+2*DOWN)
        protdot = SVGMobject('/Users/isajgordeev/Desktop/УЧЕБА/IV/scatter/proteindot.svg').move_to(3.2*LEFT+2*DOWN)
        protein = SVGMobject('/Users/isajgordeev/Desktop/УЧЕБА/IV/scatter/protein.svg').move_to(3.2*LEFT+2*DOWN)

        text1 = Tex(r'Measure intensity $I$\\',r'of each maximum\\',r'to plot 3D \\' ,r'intensity map').move_to(2*UP).scale(0.25)
        text2 = Tex(r'Fourier transform of intensity map to plot Patterson map\\',r'$	P(\textbf r) = \frac{1}{V}\sum_{i\in\, lattice}|\textbf F(\textbf S_{i})|^{2}e^{-i2\pi\textbf r\cdot\textbf  S_{i}}$').move_to(3*RIGHT).scale(0.25)
        text3 = Tex(r'Solve linear equations\\' ,r' of relative distances \\'r'to determine \\' ,r' atomic structure').move_to(2*DOWN).scale(0.25)
        text4 = Tex('Cartoon determination by human\'s intelligence').next_to(protein,0.07*DOWN).scale(0.25)

        self.camera.frame.save_state()
        # self.play(self.camera.frame.animate.set(width=scatter.width*1.5).move_to(scatter),Create(scatter), run_time=15)
        self.camera.frame.set(width=scatter.width * 1.5).move_to(scatter)
        self.add(scatter)
        self.add(text1,diffr)
        self.wait(5)

        self.play(self.camera.frame.animate.set(width=scatter.width*1.5).move_to(diffr), run_time=20)
        self.add(text2,patter)
        self.wait(5)
        self.play(self.camera.frame.animate.set(width=scatter.width*1.5).move_to(patter), run_time=20)
        self.add(text3, protdot)
        self.wait(5)

        self.play(self.camera.frame.animate.set(width=scatter.width * 1.5).move_to(protdot), run_time=20)
        self.wait(5)

        self.play(Uncreate(protdot),Create(protein), Create(text4), run_time = 14)
        self.wait(3.5)
        self.play(Uncreate(protein),Uncreate(text4), run_time=2 )
        self.wait(1.5)


