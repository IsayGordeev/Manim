from manim import *


class Intro_fin(MovingCameraScene):
    def construct(self):
        self.camera.background_color = DARKER_GRAY
        bio_intro = ImageMobject('/Users/isajgordeev/Desktop/bf video/HumanZoom_ManimCE_v0.9.0.png').move_to(
            3 * UP + 3 * LEFT).scale(0.15)
        bio_intro1 = SurroundingRectangle(bio_intro, color=WHITE)
        bio_intro_text = Tex('Important biophysics problem').next_to(bio_intro, 5 * RIGHT)
        bio_intro_label = MathTex(r'\# 1').next_to(bio_intro, 4 * LEFT)
        bio_intro_final = ImageMobject('/Users/isajgordeev/Desktop/bf video/Protein_ManimCE_v0.9.0.png').move_to(
            3 * UP + 3 * LEFT).scale(0.15)

        exp_intro = ImageMobject(
            '/Users/isajgordeev/Desktop/bf video/crystal.png').move_to(
            0.98 * UP + 3 * LEFT).scale(0.15)
        exp_intro1 = SurroundingRectangle(exp_intro, color=WHITE)
        exp_intro_text = Tex('Experimental solution').next_to(exp_intro, 5 * RIGHT)
        exp_intro_label = MathTex(r'\# 2').next_to(exp_intro, 4 * LEFT)
        exp_intro_final = ImageMobject('/Users/isajgordeev/Desktop/bf video/WhyXRay_ManimCE_v0.9.0.png').move_to(
            0.98 * UP + 3 * LEFT).scale(0.15)

        theor_intro = ImageMobject('/Users/isajgordeev/Desktop/bf video/ScatteringElectron_ManimCE_v0.9.0.png').move_to(
            -1.03 * UP + 3 * LEFT).scale(0.15)
        theor_intro1 = SurroundingRectangle(theor_intro, color=WHITE)
        theor_intro_text = Tex('Theoretical explanation').next_to(theor_intro, 5 * RIGHT)
        theor_intro_label = MathTex(r'\# 3').next_to(theor_intro, 4 * LEFT)
        theor_intro_final = ImageMobject('/Users/isajgordeev/Desktop/bf video/protein.png').move_to(
            -1.03 * UP + 3 * LEFT).scale(0.15)

        quick_intro = ImageMobject('/Users/isajgordeev/Desktop/bf video/introone_ManimCE_v0.9.0.png').move_to(
            -3.04 * UP + 3 * LEFT).scale(0.15)
        quick_intro1 = SurroundingRectangle(quick_intro, color=WHITE)
        quick_intro_text = Tex('Quick review').next_to(quick_intro, 5 * RIGHT)
        quick_intro_label = MathTex(r'\# 4').next_to(quick_intro, 4 * LEFT)

        self.add(bio_intro, bio_intro1, bio_intro_text, bio_intro_label,
                 exp_intro, exp_intro1, exp_intro_text, exp_intro_label,
                 theor_intro, theor_intro1, theor_intro_text, theor_intro_label,
                 quick_intro, quick_intro1, quick_intro_text, quick_intro_label,
                 )
        # self.wait(3)
        self.camera.frame.save_state()
        # self.play(self.camera.frame.animate(run_time=2.5).set(width=bio_intro.width).move_to(bio_intro), )
        # self.wait(2)
        self.remove(bio_intro)
        self.wait()

        self.add(bio_intro_final)
        # self.wait(2)

        # self.play(Restore(self.camera.frame), run_time=1.5)
        # self.play(self.camera.frame.animate(run_time=2.5).set(width=exp_intro.width).move_to(exp_intro), )
        # self.wait(2)
        self.remove(exp_intro)
        self.wait()

        self.add(exp_intro_final)
        # self.wait(2)

        # self.play(Restore(self.camera.frame), run_time=1.5)
        self.play(self.camera.frame.animate(run_time=2.5).set(width=theor_intro.width).move_to(theor_intro), )
        # self.wait(2)
        self.remove(theor_intro)
        self.wait()

        self.add(theor_intro_final)
        # self.wait(2)

        self.play(Restore(self.camera.frame), run_time=1.5)
        self.wait(4)

        # self.play(self.camera.frame.animate(run_time=2.5).set(width=quick_intro.width).move_to(quick_intro), )
        self.wait()


class HumanZoom(MovingCameraScene):
    def construct(self):
        thhuman = SVGMobject('/Users/isajgordeev/Desktop/bf video/thhuman.svg').scale(3)
        speech = SVGMobject('/Users/isajgordeev/Desktop/bf video/speech.svg').move_to(RIGHT * 1.8 + 2.7 * UP)
        text = Tex('What\'s inside', r'\\me?').move_to(speech.get_center() + RIGHT * 0.6 + DOWN * 0.3).set_color(
            BLACK).scale(0.65)
        cell_lattice = SVGMobject('/Users/isajgordeev/Desktop/bf video/cell.svg').scale(0.7).move_to(
            ORIGIN + UP * 0.8 + RIGHT * 0.25)
        self.add(thhuman)
        self.play(Create(speech), Write(text))
        self.wait(2)
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate(run_time=4).set(width=0.5).move_to(ORIGIN + UP * 0.8 + RIGHT * 0.25), )
        self.wait()


class CellHuman(MovingCameraScene):
    def construct(self):
        cell_lattice = SVGMobject('/Users/isajgordeev/Desktop/bf video/cell.svg').scale(0.7).move_to(
            ORIGIN + UP * 0.8 + RIGHT * 0.25)
        back = SVGMobject('/Users/isajgordeev/Desktop/bf video/back.svg').scale(8)
        np.random.seed(3)
        boxes = VGroup(*[
            SVGMobject('/Users/isajgordeev/Desktop/bf video/cell.svg').scale(0.7).move_to(
                [np.random.random(), np.random.random(), np.random.random()])
            for i in range(32)
        ])
        # self.add(boxes)

        boxes.arrange_in_grid(rows=4)
        boxes.shift(0.5 * LEFT + DOWN)

        cell = SVGMobject('/Users/isajgordeev/Desktop/bf video/cell.svg').scale(2.5).shift(DOWN)
        self.add(back)
        self.play(FadeIn(boxes), FadeOut(back), run_time=4)

        text1 = Tex(r'These cells form our organs, skin.\\', ' A cell is a unit of life').to_edge(UP)
        self.play(FadeIn(text1[0]))
        self.wait(2)
        self.play(FadeOut(boxes), Transform(boxes[10], cell), FadeIn(text1[1]), run_time=3.5)
        self.add(cell)
        self.wait(1.5)


class Cell_and_Protein(Scene):
    def construct(self):
        cell = SVGMobject('/Users/isajgordeev/Desktop/bf video/cell.svg').scale(2.5).shift(DOWN)
        cell1 = SVGMobject('/Users/isajgordeev/Desktop/bf video/cell.svg').scale(1.75).shift(DOWN + 2 * RIGHT)
        text1 = Tex(r'These cells form our organs, skin.\\', ' A cell is a unit of life').to_edge(UP)
        self.add(cell, text1)
        text2 = Tex(r'But ', 'proteins ', r'sustain all functions in a cell. \\', 'They catalyze biochemical reactions',
                    ' such as a cell fission.').to_edge(UP)

        text2[3].shift(2 * RIGHT)
        text2[1].set_color(RED)
        self.play(ReplacementTransform(text1[0], text2[3]), ReplacementTransform(text1[1], text2[2]),
                  Write(VGroup(text2[0], text2[1])))
        self.wait(2)
        self.play(FadeIn(text2[4], shift=RIGHT), cell.animate.shift(2 * LEFT), text2[3].animate.shift(2 * LEFT),
                  run_time=2)
        self.play(TransformFromCopy(cell, cell1), cell.animate.scale(0.7), run_time=3)
        self.wait(2)
        text3 = Tex(r'Knowing structure of a', ' protein ', r'is equal\\', r' knowing a function of the ', r'protein',
                    r'.\\', 'This is important when scientists explore new drugs.')
        text3[1].set_color(RED)
        text3[4].set_color(RED)
        self.play(FadeOut(cell, cell1, text2), FadeIn(text3), run_time=1.5)
        self.wait(3.5)

        text4 = Tex('So, how does ', 'protein', ' look like and', r'\\how its structure can be determined?')
        text4[1].set_color(RED)
        self.play(FadeIn(text4, shift=UP), FadeOut(text3, shift=UP), run_time=2)
        self.wait(2)
        self.play(FadeOut(text4, shift=UP))
        self.wait()


class Protein(ZoomedScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.3,
            zoomed_display_height=3,
            zoomed_display_width=3,
            image_frame_stroke_width=20,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
            },
            **kwargs
        )

    def construct(self):
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame

        frame.move_to(2 * UP)
        frame.set_color(WHITE)
        zoomed_display_frame.set_color(WHITE)
        zoomed_display.shift(DOWN)

        carbo = Tex('C').scale(0.3)
        carbo1 = Tex('C').scale(0.3)
        carbo2 = Tex('C').scale(0.3)

        carbo.move_to(2.1 * UP)
        carbo1.shift(2 * UP + 0.3 * RIGHT)
        carbo2.shift(1.8 * UP + 0.2 * LEFT)

        self.line1 = Line(carbo.get_center(), carbo1.get_center(), stroke_width=0.6)
        self.line2 = Line(carbo.get_center(), carbo2.get_center(), stroke_width=0.6)
        chain = VGroup(carbo, carbo2, carbo1, self.line1, self.line2)

        self.a = SVGMobject('/Users/isajgordeev/Desktop/1.svg').scale(2)
        self.b = SVGMobject('/Users/isajgordeev/Desktop/2.svg').scale(2)
        self.c = SVGMobject('/Users/isajgordeev/Desktop/3.svg').scale(2)
        text = Tex('This is a ', 'protein')
        text[1].set_color(RED)
        text1 = Tex(r'In a living organism it is constantly\\', ' moving as a result of brownian motion.')

        text.next_to(self.a, DOWN).scale(0.8)
        text1.next_to(self.a, DOWN).scale(0.8)

        self.play(Write(self.a), Write(text))
        self.wait(0.2)
        self.play(Create(frame))
        self.activate_zooming()
        self.play(self.get_zoomed_display_pop_out_animation(), run_time=2)
        self.play(Write(carbo), Write(carbo1), Write(carbo2), Create(self.line1), Create(self.line2))
        self.wait(2)

        self.moving_protein()
        self.play(ReplacementTransform(text, text1))
        self.moving_protein()
        self.moving_protein()

        self.play(self.get_zoomed_display_pop_out_animation(), rate_func=lambda t: smooth(1 - t),
                  run_time=2)
        self.play(Uncreate(zoomed_display_frame), FadeOut(frame), Uncreate(chain), run_time=2)
        self.wait(2)
        text2 = Tex(r'As I claimed, one of the most important task of biology\\', ' is to determine its',
                    ' structure').scale(0.8)
        text2.to_corner(RIGHT + UP)
        self.play(self.a.animate.shift(3 * LEFT), ReplacementTransform(text1, text2))
        self.wait()
        self.play(Indicate(self.a), Indicate(text2[2]), run_time=2.5)
        text3 = Tex('Let\'s find out a possible solution of this problem').scale(0.8)
        text3.to_corner(UP + RIGHT)
        text3.shift(DOWN)

        self.wait(2)
        self.play(TransformFromCopy(text2, text3))
        self.wait(2)
        # self.play(Unwrite(self.a), Unwrite(text2), Unwrite(text3), run_time=2)
        # self.wait(1)

    def moving_protein(self):
        self.add(self.line1, self.line2)
        self.play(ReplacementTransform(self.a, self.b))
        self.add(self.line1, self.line2)

        self.play(ReplacementTransform(self.b, self.c))
        self.add(self.line1, self.line2)
        self.play(ReplacementTransform(self.c, self.a))
        self.add(self.line1, self.line2)


class ProteinCrystalplusPlan(Scene):
    def construct(self):
        poly_2 = RegularPolygon(n=6, start_angle=30 * DEGREES, color=GREEN)
        self.a = SVGMobject('/Users/isajgordeev/Desktop/1.svg').scale(0.5)
        self.a.move_to(poly_2.get_center())
        crystal = VGroup(poly_2, self.a)
        crystal.shift(4 * RIGHT + 2 * UP)
        self.add(crystal)

        text = Tex('The method based on ', 'X-Ray', ' scattering on a', ' protein', ' crystal').scale(0.8)
        text[1].set_color(BLUE_D)
        text[3].set_color(RED)
        self.add(text)

        # self.play(text.animate.to_edge(UP))
        # text1 = Tex(r'First of all we need to make a', r' protein crystal \\',
        #             r'Likewise a saline solution, a saturated solution of\\'
        #             , 'protein ', 'gives a sediment, in the form of', ' protein', ' crystals').scale(0.8)
        # text1[3].set_color(RED)
        # text1[5].set_color(RED)
        #
        # self.play(Write(text1))
        # self.wait()
        #
        # self.play(text1.animate.shift(2 * LEFT))
        # self.wait()
        #
        # self.play(Circumscribe(crystal), Indicate(text1[1]))
        # self.wait()
        #
        # self.play(text1.animate.shift(2 * UP))
        # self.wait()
        #
        # text3 = Tex(r'Then we obtain ', 'X-Ray ', r'2D diffraction pattern\\', ' on this crystal').scale(0.8)
        # text3[1].set_color(BLUE_D)
        # axes = Axes(x_range=[-4, 4]).scale(0.5)
        # axes.shift(5 * RIGHT + DOWN)
        # dots = VGroup(
        #     *[Dot([np.random.uniform(-1, 1), np.random.uniform(-1, 1), np.random.uniform(-1, 1)]) for x in range(10)])
        # dots1 = VGroup(
        #     *[Dot([np.random.uniform(-1, 1), np.random.uniform(-1, 1), np.random.uniform(-1, 1)]) for x in range(10)])
        # crystal1 = crystal
        # dots.shift(5 * RIGHT + DOWN)
        # dots1.shift(5 * RIGHT + DOWN)
        #
        # beama = Line(text.get_center(), crystal.get_center(), stroke_color=BLUE_B)
        # beamb = Line(crystal.get_center(), axes.get_center(), stroke_color=BLUE_B)
        # self.play(Write(text3))
        # self.wait()
        # self.play(text3.animate.shift(2 * LEFT), Create(beama), Create(beamb))
        # self.wait()
        #
        # self.play(Indicate(beama), Indicate(beamb), Indicate(text3[1]), run_time=2)
        # self.wait()
        #
        # self.play(text3.animate.shift(0.35 * UP), Create(axes), Create(dots))
        # self.play(Indicate(dots), Indicate(text3[2]), run_time=2)
        # self.wait()
        #
        # text4 = Tex(r'The rotating', ' of the sample gives a ', r'3D diffraction pattern\\',
        #             r'that is, information about 3D structure of the sample.').scale(0.8)
        # text5 = Tex('But how exactly determine structure from this pattern?').scale(0.8)
        # text4.shift(2 * LEFT + DOWN)
        # text5.shift(2 * LEFT + 2.5 * DOWN)
        #
        # self.play(Write(text4))
        # self.wait()
        #
        # self.play(Rotate(crystal), ClockwiseTransform(dots, dots1), Indicate(text4[0]), run_time=2)
        # self.wait()
        #
        # self.play(Write(text5))
        # self.wait(2)
        # self.play(Uncreate(text), Uncreate(text1), Uncreate(text3), Uncreate(text4), Uncreate(text5), Uncreate(crystal),
        #           Uncreate(beamb), Uncreate(beama), Uncreate(axes), Uncreate(dots1), Uncreate(dots))
        # self.wait(1)


class Wave(VGroup):
    def __init__(self, start, a, r, ampl, color, **kwargs):
        super().__init__(**kwargs)
        self.a = a
        self.r = r
        self.ampl = ampl
        self.start = start
        self.color = color
        self.ada = ValueTracker(self.a)
        self.rdr = ValueTracker(self.r)
        self.move = ValueTracker(start[0])

        self.curve = ParametricFunction(
            lambda u: np.array([
                self.r * u + start[0],
                self.ampl * np.sin(u + self.a) + start[1],
                0
            ]), t_range=np.array([0, 2 * TAU]), stroke_color=color, stroke_width=10
        )

    def get_wave(self, a, r, color1, move):
        curve1 = ParametricFunction(
            lambda u: np.array([
                r * u + move + self.start[0],
                self.ampl * np.sin(u + a) + self.start[1],
                0
            ]), t_range=np.array([0, 2 * TAU]), stroke_color=color1, stroke_width=10
        )
        return curve1

    def wave_updater(self):
        self.curve.add_updater(
            lambda z: z.become(
                self.get_wave(self.ada.get_value(), self.rdr.get_value(), self.color, self.move.get_value())))


class WhyXRay(MovingCameraScene):
    def construct(self):
        self.Wave_scene()

    def Wave_scene(self):
        text1 = Tex('Why do we use X-Ray? Why can\'t we just look at the microscope?').scale(0.8)
        text1.to_corner(UP)
        self.play(Create(text1), run_time=2)
        self.wait()
        text2 = Tex(r'The length of the waves in visible range \\', 'starts from ', '400 nm ', ' and reaches ',
                    '700 nm').scale(0.8)
        text2.next_to(text1, DOWN)
        text2[2].set_color(PURPLE)
        text2[4].set_color(RED)

        self.play(Unwrite(text1), Create(text2), run_time=2)
        self.wait()

        start = ORIGIN + 2.5 * LEFT
        text = Tex('Wave', ' of visible light').scale(0.8)
        textxray = Tex('X-Ray ', 'on visible light', ' scale').scale(0.8)
        textxray[0].set_color(BLUE_D)
        textxrayafter = Tex('X-Ray ', 'on its', ' scale').scale(0.8)
        textxrayafter[0].set_color(BLUE_D)
        wave = Wave(start, 0, 0.3, 1, RED)
        xray = Line(wave.curve.get_start(), wave.curve.get_end(), stroke_width=10).set_color(BLUE_D)
        xray.shift(3.5 * RIGHT + 0.5 * RIGHT)
        text.next_to(text2, DOWN)
        textxray.next_to(text2, DOWN)
        textxray.shift(3.5 * RIGHT)
        textxrayafter.next_to(text2, DOWN)
        textxrayafter.shift(3.5 * RIGHT)
        textxrayagain = textxray.copy()

        wavelen = (r'\frac{2\pi}{\lambda}')
        period = BraceBetweenPoints([wave.curve.get_start()[0], 0, 0], [wave.curve.get_end()[0], 0, 0])
        periodtext = period.get_tex(wavelen)
        wave.wave_updater()
        period.add_updater(lambda z: z.become(
            BraceBetweenPoints([wave.curve.get_start()[0], -1.5, 0], [wave.curve.get_end()[0], -1.5, 0])))
        periodtext.add_updater(lambda z: z.become((period.get_tex(wavelen))))
        colors = [RED, RED, RED, RED, ORANGE, ORANGE, ORANGE, YELLOW, YELLOW, YELLOW, GREEN, GREEN, GREEN, BLUE, BLUE,
                  BLUE, PURPLE, PURPLE, PURPLE, PURPLE]
        text[0].set_color(colors[0])
        self.play(Create(wave.curve), Write(text))
        self.add(period, periodtext)

        for x in zip(range(20), np.arange(0.3, 0.8, 0.025), colors):
            self.play(wave.ada.animate(run_time=0.1).set_value(x[0]), wave.rdr.animate(run_time=0.1).set_value(x[1]))
            wave.color = x[2]
            text[0].set_color(x[2])
            periodtext.set_color(x[2])

        for x in zip(range(20, 40, 1), np.arange(0.8, 0.3, -0.025), reversed(colors)):
            self.play(wave.ada.animate(run_time=0.1).set_value(x[0]), wave.rdr.animate(run_time=0.1).set_value(x[1]))
            wave.color = x[2]
            text[0].set_color(x[2])
            periodtext.set_color(x[2])
        self.wait(2)
        text3 = Tex(r'Protein size is 1000 times smaller \\', r'than the length of visible light wave,\\',
                    'but its size is comparable to', ' X-Ray ', 'length').scale(0.8)
        text3.to_corner(UP)
        text3.shift(0.1 * UP)
        text3[3].set_color(BLUE_D)

        wavexray = Wave(xray.get_left(), 0, 0.3, 1, BLUE_D)
        xrayafter = xray.copy()

        visiblelight_scale = NumberLine(
            x_range=[0, 750, 250],
            color=RED,
            include_numbers=True,
            length=wave.curve.width,
            numbers_with_elongated_ticks=[6],
        ).next_to(wave.curve, DOWN)

        xray_scale = visiblelight_scale.copy().shift(6.5 * RIGHT)

        xray_scaleback = xray_scale.copy()

        xray_true_scale = NumberLine(
            x_range=[0, 0.75, 0.25],
            color=BLUE_D,
            include_numbers=True,
            length=wavexray.curve.width,
            numbers_with_elongated_ticks=[0, 0.75],
        ).next_to(wavexray.curve, DOWN)

        self.remove(periodtext, period)
        self.play(Create(visiblelight_scale))

        self.play(TransformFromCopy(wave.curve, xray),
                  TransformFromCopy(text, textxray),
                  text.animate.shift(3 * LEFT),
                  TransformFromCopy(visiblelight_scale, xray_scale),
                  run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(text2, text3))
        self.wait(2)

        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=xray.get_length() * 2).move_to(xray.get_center()),
                  ReplacementTransform(xray, wavexray.curve),
                  ReplacementTransform(textxray, textxrayafter),
                  ReplacementTransform(xray_scale, xray_true_scale),
                  run_time=4)
        self.wait()
        self.play((Restore(self.camera.frame)),
                  ReplacementTransform(wavexray.curve, xrayafter),
                  ReplacementTransform(textxrayafter, textxrayagain),
                  ReplacementTransform(xray_true_scale, xray_scaleback),
                  run_time=4)

        text40 = Tex('Eye can only detect an amplitude $\\textbf{A}$ of a wave').to_edge(DOWN).scale(0.8)
        text4 = Tex('That\'s why we need to use', r' X-Ray \\', r'instead of a microscope').scale(0.8)
        text4.to_edge(DOWN)
        text4[1].set_color(BLUE_D)
        amplitude = BraceBetweenPoints(6 * LEFT + DOWN, 6 * LEFT + UP).rotate(PI)
        amplitude_text = Tex('Amplitude').move_to(amplitude).shift(0.5 * LEFT).rotate(PI / 2).scale(0.8)
        self.play(Write(text40), FadeIn(amplitude), FadeIn(amplitude_text))
        # self.add(amplitude)

        self.wait(2)
        self.play(ReplacementTransform(text40, text4))
        self.wait(2)
        # self.play(Uncreate(text4),Uncreate(text3), Uncreate(text),Uncreate(textxrayagain),Uncreate(wave.curve),Uncreate(xrayafter))
        # self.wait(1)


class ScatteringElectron(Scene):
    def construct(self):
        text = Tex('When ', 'X-Ray ', 'wave reaches an electron ', r'(electron cloud)\\',
                   r'electron turns to the source of spherical wavelets').scale(0.8)
        text.to_corner(UP)
        text[1].set_color(BLUE_D)
        self.add(text)
        cloud = SVGMobject('/Users/isajgordeev/Desktop/cloud.svg')
        clouddensity = MathTex(r'\rho(\textbf{r})').set_color(ORANGE).move_to(cloud.get_center() + 0.5 * RIGHT)
        self.add(cloud, clouddensity)
        self.wait()
        self.play(Wiggle(cloud), Indicate(text[3]), Wiggle(clouddensity), run_time=4)
        self.wait()
        self.play(cloud.animate.shift(4.5 * RIGHT), clouddensity.animate.shift(4.5 * RIGHT),
                  text.animate.shift(LEFT * 1.5), run_time=3)
        xray = Arrow(cloud.get_center() + 3 * UP, cloud.get_center(), buff=0).set_color(BLUE_D)
        xraytext = MathTex(r'E_0e^{i(\textbf{k}_0\cdot \textbf{r} -wt)}').move_to(
            xray.get_center() + 1.2 * RIGHT).scale(0.8)
        kotext = MathTex(r'\textbf {k}_0').move_to(xray.get_center() + 0.3 * LEFT).scale(0.8).set_color(LIGHT_BROWN)

        self.play(Create(xray), Write(xraytext), Write(kotext), run_time=3)
        self.wait(2)
        self.play(Wiggle(xray), Wiggle(kotext), Wiggle(xraytext), Indicate(text[1]), run_time=3)
        self.wait(2)
        spher1 = ArcBetweenPoints(LEFT, UP)
        spher2 = ArcBetweenPoints(LEFT + [0, 0.2, 0], UP + [-0.2, 0, 0])
        spher3 = ArcBetweenPoints(LEFT + [0, 0.4, 0], UP + [-0.4, 0, 0])

        spher = VGroup(spher1, spher2, spher3)

        spher.move_to(cloud.get_center() + 2 * DOWN + RIGHT).set_color(BLUE_D)
        ktext = MathTex(r'\text{ k}').move_to(spher.get_center() + LEFT + DOWN).scale(0.8).set_color(LIGHT_BROWN)

        sphertext = MathTex(r'\psi(\textbf{S})').next_to(spher, UP + 0.01 * RIGHT).set_color(RED)
        self.play(Write(spher),
                  Write(sphertext),
                  Write(ktext))
        self.play(Indicate(text[4]),
                  Wiggle(ktext),
                  Indicate(spher),
                  Wiggle(sphertext), run_time=3)

        self.wait(2)

        text1 = Tex('Wave equation on ', 'X-Ray', ' scale').scale(0.8)
        text1[1].set_color(BLUE_D)
        text1.next_to(text, DOWN)
        formula = MathTex(r'\left[\Delta +', ' k^2_0', r'+\nu', r'\rho(\textbf{r}', r')\right]', r'\psi(\textbf{r})',
                          '=0').scale(0.8)
        formula.next_to(text1, DOWN)
        formula[1].set_color(LIGHT_BROWN)
        formula[3].set_color(ORANGE)
        formula[5].set_color(RED)

        self.play(Write(text1), Write(formula))
        text2 = Tex(r'This item ', r'$\nu$', r'$\rho(\textbf{r})$ ', r'concerned with\\',
                    ' interaction between wave and cloud').next_to(formula, DOWN).scale(0.8)
        text2[2].set_color(ORANGE)
        self.wait(4)
        self.play(Write(text2))
        self.wait(3)

        self.play(Indicate(text2[2]),
                  Indicate(text2[1]),
                  Indicate(formula[3]),
                  Indicate(formula[2]),
                  Wiggle(xray),
                  Wiggle(cloud),
                  run_rime=3)
        self.wait()
        text3 = Tex(r'Normalized solution of the wave equation, \\ for the spherical wavelets ',
                    r'$\psi(\textbf{r})$').move_to(text2).scale(0.8)
        text3[1].set_color(RED)

        solut = MathTex(r'\psi(\textbf S)', r'=\int', r'_{cloud}', r'\rho(r)',
                        r'\exp(i\textbf{r} \cdot \textbf{S} + \varphi(\textbf S))d^3\textbf{r}').scale(0.8).next_to(
            text2, DOWN)
        subsolut = MathTex(r'\textbf{S} = ', r'\textbf{ k} ', r'-', r'\textbf{ k}_0').next_to(solut, DOWN).scale(0.8)
        subsolut[1].set_color(LIGHT_BROWN)
        subsolut[3].set_color(LIGHT_BROWN)
        solut[0].set_color(RED)
        solut[3].set_color(ORANGE)
        solut[2].set_color(BLUE_B)

        self.play(ReplacementTransform(text2, text3),
                  FadeIn(solut),
                  FadeIn(subsolut), run_rime=2)

        self.wait(3)

        self.play(Indicate(solut),
                  Indicate(spher),
                  Indicate(sphertext), run_rime=2)

        self.wait()
        text4 = Tex(r'$\textbf{S}$ -  direction of waves on detector, \\',
                    r'$\varphi(\textbf S)$ - phase of the wavelet').next_to(subsolut, DOWN).scale(0.8)
        self.play(FadeIn(text4))
        self.wait(4)
        self.play(FadeOut(text4),
                  FadeOut(subsolut),
                  FadeOut(text3),
                  FadeOut(text2),
                  FadeOut(text1),
                  FadeOut(text),
                  FadeOut(formula),
                  FadeOut(ktext),
                  FadeOut(kotext),
                  FadeOut(xraytext),
                  FadeOut(clouddensity),
                  FadeOut(sphertext),
                  solut.animate.to_corner(UP + LEFT),
                  # solut.animate.scale(0.8),
                  cloud.animate.to_edge(LEFT),
                  run_rime=3)
        xray1 = Arrow(cloud.get_center() + 2.5 * UP + LEFT, cloud.get_center(), buff=0).set_color(BLUE_D)
        self.play(spher.animate.next_to(cloud.get_center() + 2 * DOWN + LEFT),
                  ReplacementTransform(xray, xray1),
                  Rotate(cloud, angle=PI / 6),
                  solut.animate.scale(0.8), )
        dots = VGroup(Dot(UP, fill_opacity=0.75, radius=1.5 * 0.08),
                      *[Dot([np.random.uniform(-0.3, 0.5), np.random.uniform(-0.3, 0.5), np.random.uniform(-0.3, 0.5)],
                            fill_opacity=np.random.uniform(0.5, 1), radius=0.08 * 1.5) for x in range(10)]).to_corner(
            DOWN + LEFT).shift(2 * RIGHT)
        self.play(Create(dots))
        self.wait(2)
        solut_j = MathTex(r'\psi(\textbf S)_j',
                          r'=\int', r'_{cloud}',
                          r'\rho(r_j)',
                          r'\exp(i\textbf{r}_j \cdot \textbf{S} + \varphi(\textbf S)_j)d^3\textbf{r}_j').scale(
            0.64).to_corner(UP + LEFT)
        solut_j[0].set_color(RED)
        solut_j[3].set_color(ORANGE)
        solut_j[2].set_color(BLUE_B)
        text5 = Tex(r'Denote some wavelet as', r' $\psi(\textbf S)_j$, ', r'so \\',
                    r'using principle of superposition, the total wave\\',
                    r'$\textbf F(\textbf S) = $', r' $\displaystyle\sum_{j\in \, molecule}$', r' $\psi(\textbf S)_j$',
                    ).shift(3 * (RIGHT + UP)).scale(0.65)
        text5[1].set_color(RED)
        text5[4].set_color(YELLOW)
        text5[6].set_color(RED)

        text50 = Tex(r'Since a molecule has many atoms, \\',
                     'we need to take into account them all').shift(3 * (RIGHT + UP)).scale(0.65)

        self.play(Write(text50))
        self.wait(2.5)
        self.play(ReplacementTransform(text50, text5[0:3]),
                  TransformMatchingTex(solut, solut_j))
        self.wait(2)
        solutmol = MathTex(r'\textbf F(\textbf S) ', r'= \sum_{j\in \, molecule}\int', r'_{cloud}',
                           r'\rho(\textbf r_{j})',
                           r'\exp(2\pi i\textbf r_{j}\cdot \textbf S+\varphi(\textbf S)_j)d^{3}\textbf r_{j}').next_to(
            text5, DOWN).scale(0.65)
        solutmol[0].set_color(YELLOW)
        solutmol[2].set_color(BLUE_B)
        solutmol[3].set_color(ORANGE)
        solutmol.shift(LEFT + 0.3 * UP)
        self.play(FadeIn(text5[3:7]))
        self.wait(1.5)
        self.play(FadeIn(solutmol, target_position=solut_j), run_time=2)
        self.wait(3)
        magn = Arrow(cloud.get_center(), dots[0].get_center(), buff=0.1).set_color(YELLOW)
        magntext = MathTex(r'\textbf F(\textbf S) ').move_to(magn.get_end() + 0.5 * RIGHT).set_color(YELLOW).scale(0.5)
        self.play(Write(magn),
                  FadeOut(spher),
                  FadeIn(magntext, target_position=dots[3].get_center()), run_time=2)
        self.wait(3)

        text6 = Tex(r'$\textbf F(\textbf S)$ ', r'- is total wave vector from cloud,\\',
                    r'$\varphi(\textbf S)_j$ - phase of the wavelet ,',r'$\psi(\textbf S)_j$').to_corner(UP + RIGHT).scale(0.65).shift(RIGHT)
        text6[0].set_color(YELLOW)
        text6[3].set_color(RED)

        self.play(ReplacementTransform(text5, text6), run_time=2)
        self.wait(3)

        wave = Wave(ORIGIN+LEFT*1.25, 0, 0.3, 0.5, BLUE_D)
        wave.wave_updater()
        detector = Line(DOWN, UP, stroke_width=3).shift(5.1 * RIGHT)
        axes = DashedLine(wave.curve.get_start(), detector.get_center()).set_color(YELLOW)
        ampl = BraceBetweenPoints(DOWN / 2, UP / 2).shift(5.4 * RIGHT)
        ampltext = ampl.get_tex(r'\sqrt{\textbf{I}}').scale(0.65)
        textdet = Tex('detector').next_to(detector, UP).scale(0.65)

        phase = Arrow(2 * RIGHT + 1.5 * DOWN, wave.curve.get_end())
        phasetext = MathTex(r'\exp(i\varphi(\textbf S_{j}))').scale(0.8).move_to(phase.get_start()).shift(0.4 * DOWN)

        text7 = Tex(r'Intensity $\textbf{I}$ of points on the detector is ', r'$\textbf F(\textbf S)$',
                    r'$^2$').next_to(phasetext, DOWN).scale(0.65)
        text7[1].set_color(YELLOW)
        intens = MathTex(r'\textbf{I} =', r'\textbf F(\textbf S)', r'^2 ').next_to(text7, DOWN).scale(0.65)
        intens[1].set_color(YELLOW)

        self.play(Create(wave.curve),
                  Create(detector),
                  FadeIn(textdet),
                  Create(axes),
                  FadeIn(text7),
                  Create(intens),
                  run_time=3)
        self.add(ampl,
                 ampltext)
        self.wait(1.5)

        for x in range(30):
            self.play(wave.ada.animate(run_time=0.01).set_value(x / 3),
                      wave.move.animate(run_time=0.01).set_value(-1.25 + 4 * x / 30), Wiggle(detector, run_time=0.3))

        self.wait(2)
        phase = Arrow(2 * RIGHT + 1.5 * DOWN, wave.curve.get_end())

        self.play(TransformFromCopy(ampl, phase),
                  FadeIn(phasetext), run_time=2)

        self.wait(3)
        real_wave = SVGMobject('/Users/isajgordeev/Desktop/wave.svg').move_to(magn.get_center())
        self.play(ReplacementTransform(wave.curve, real_wave), run_time=1.5)
        self.wait(3)
        self.remove(ampl, ampltext)
        self.play(Uncreate(solutmol),
                  Uncreate(axes),
                  Uncreate(real_wave),
                  Uncreate(detector),
                  Uncreate(textdet),
                  Uncreate(phasetext),
                  Uncreate(phase),
                  Uncreate(text7),
                  Uncreate(text6),
                  Uncreate(intens),
                  Uncreate(xray1),
                  Uncreate(cloud),
                  Uncreate(magn),
                  Uncreate(magntext),
                  Uncreate(dots),
                  FadeOut(solut_j),
                  run_time=2)
        self.wait(1.5)


class Phaseproblem(Scene):
    def construct(self):
        text = Tex(r'We obtained that, the root of intensity is the Fourier transform of electron cloud density. ',
                   r'So, if make inverted discrete transform to the rooted intensity we must get electron cloud density').scale(
            0.65).to_edge(UP)
        self.play(FadeIn(text[0]))

        solutmol = MathTex(r'\textbf F(\textbf S) ', r'= \sum_{j\in \, molecule}\int', r'_{cloud}',
                           r'\rho(\textbf r_{j})',
                           r'\exp(2\pi i\textbf r_{j}\cdot \textbf S_{j}+\varphi(\textbf S_{j}))d^{3}\textbf r_{j}').scale(
            0.65)
        solutmol[0].set_color(YELLOW)
        solutmol[2].set_color(BLUE_B)
        solutmol[3].set_color(ORANGE)
        self.play(Write(solutmol))
        self.wait(7)

        invertFT = MathTex(r'	\rho(x,y,z) ', r' = \frac{1}{V}\sum_{h,k,l\in\, molecule}|', r'F(h,k,l)',
                           r'|\cos\left[  2\pi(hx+ky+lz) + \varphi(h,k,l) \right]').scale(0.65)
        invertFT[0].set_color(ORANGE)
        invertFT[2].set_color(YELLOW)
        self.play(Create(invertFT),
                  solutmol.animate.shift(UP),
                  FadeIn(text[1]), run_time=3)
        self.wait(7)

        cloud = SVGMobject('/Users/isajgordeev/Desktop/cloud.svg').to_corner(DOWN + LEFT)
        cloudvolume = MathTex(r'V').set_color(GREEN).move_to(cloud.get_center() + 0.5 * RIGHT)

        spher1 = ArcBetweenPoints(LEFT, UP)
        spher2 = ArcBetweenPoints(LEFT + [0, 0.2, 0], UP + [-0.2, 0, 0])
        spher3 = ArcBetweenPoints(LEFT + [0, 0.4, 0], UP + [-0.4, 0, 0])

        spher = VGroup(spher1, spher2, spher3).next_to(cloud, 3 * RIGHT).rotate(PI / 4).set_color(BLUE_D)

        self.play(Create(cloud),
                  Create(spher), run_time=2.5)

        wave = Wave(2.5 * LEFT + 2.5 * DOWN, 0, 0.3, 0.5, BLUE_D)

        wave.wave_updater()

        self.wait(2)

        self.play(ReplacementTransform(spher, wave.curve), run_time=2.5)

        for x in range(150):
            self.play(wave.ada.animate(run_time=0.01).set_value(x / 3),
                      wave.move.animate(run_time=0.01).set_value(-2.5 + 3 * x / 150))
        dots = VGroup(Dot(UP, fill_opacity=0.75, radius=2 * 0.08),
                      *[Dot([np.random.uniform(-0.3, 0.5), np.random.uniform(-0.3, 0.5), np.random.uniform(-0.3, 0.5)],
                            fill_opacity=np.random.uniform(0.5, 1), radius=0.08 * 2) for x in range(10)]).to_corner(
            DOWN + LEFT).next_to(wave.curve, RIGHT)
        indicate_dot = Dot(wave.curve.get_end(), fill_opacity=0.75, radius=2 * 0.08)
        hkl = Tex('$(h,k,l)$').next_to(dots[0], 0.5 * RIGHT).scale(0.65)
        self.wait(0.7)
        self.play(Create(dots),
                  Create(indicate_dot),
                  Create(hkl), run_time=2.5)
        initphase = wave.ada.get_value()
        text1 = Tex('We can measure ', r'pattern intensity $\textbf{I}$ ', r'$=0.75$',
                    r', but what about phase $\varphi(h,k,l)?$', r' $\varphi(h,k,l) = 0.3\pi $?').next_to(invertFT,
                                                                                                          DOWN).scale(
            0.65)
        text2 = Tex(r'or $\varphi(h,k,l) = 0.3\pi + 2\pi $?').next_to(text1[4], DOWN).scale(0.65)
        self.play(FadeIn(text1[0], target_position=indicate_dot),
                  FadeIn(text1[1], target_position=indicate_dot),
                  run_time=4)
        self.wait(2)
        direct = Arrow(text1[2].get_center() + 0.3 * DOWN, indicate_dot.get_center())
        self.play(Create(text1[2]), Create(direct), run_time=2.5)
        self.wait(2)
        self.play(Indicate(indicate_dot), run_time=2)
        self.wait(2)
        self.play(FadeIn(text1[3]), FadeOut(direct), run_time=3)
        text2.shift(0.7 * UP)
        self.play(FadeIn(text1[4], target_position=wave.curve.get_center()), run_time=3)
        self.wait()
        self.play(Wiggle(wave.curve), run_time=3)
        self.wait(2)
        self.play(text1.animate.shift(0.7 * UP), solutmol.animate.shift(0.7 * UP), invertFT.animate.shift(0.7 * UP),
                  run_time=3)
        self.wait(1.5)
        for x in range(15):
            self.play(wave.ada.animate(run_time=0.05).set_value(initphase + 2 * PI * x / 14))
        self.play(FadeIn(text2, target_position=wave.curve.get_center()), run_time=3)
        self.play(Wiggle(wave.curve), run_time=3)
        self.wait(2.5)
        text3 = Tex(r'Ambiguity? Is is known as X-Ray scattering phase problem.\\',
                    r'Particularly, it can be solved by Patterson map method').to_edge(UP).scale(0.65)
        self.play(Uncreate(indicate_dot),
                  Uncreate(text1[0]),
                  Uncreate(text1[1]),
                  Uncreate(text1[2]),
                  Uncreate(text1[3]),
                  Uncreate(solutmol),
                  Uncreate(invertFT),
                  ReplacementTransform(text, text3),
                  text1[4].animate.next_to(text3, DOWN),
                  text2.animate.next_to(text3, 3 * DOWN),
                  Uncreate(hkl),
                  run_time=4)
        self.wait(4)
        self.play(Uncreate(text3),
                  Uncreate(wave.curve),
                  Uncreate(dots),
                  Uncreate(cloud),
                  Uncreate(text2),
                  Uncreate(text1[4]), run_time=4)
        self.wait(2)


class PattersonMap(Scene):
    def construct(self):
        text1 = Tex(r'Patterson map method consists in special\\ transform of electron density.\\',
                    'This transform is convolution').to_edge(UP).scale(0.8)
        self.play(FadeIn(text1[0]))
        self.wait(2)

        formula1 = MathTex(r'f*g = \int_{-\infty}^{+\infty} f(t-\tau)g(\tau)d\tau').next_to(text1, DOWN).scale(0.8)
        self.play(FadeIn(text1[1], shift=DOWN),
                  FadeIn(formula1, shift=DOWN))
        self.wait(2)

        text2 = Tex(r'So, Patterson map $P(\textbf{r})$ is ').next_to(formula1, DOWN).scale(0.8)
        formula2 = MathTex(r'P(r) = ', r'\rho(r)', '*', r'\rho(r)').next_to(text2, DOWN).scale(0.8)
        formula2[1].set_color(ORANGE)
        formula2[3].set_color(ORANGE)
        self.play(TransformFromCopy(text1, text2),
                  TransformFromCopy(formula1, formula2))
        self.wait(2)

        text3 = Tex(r'Using our result of electron cloud density').scale(0.8)
        formula3 = MathTex(
            r' P(\textbf{r}) = \frac{1}{V}\sum_{i\in\, lattice}\textbf{I}(\textbf{r})e^{-i2\pi\textbf r\cdot\textbf  S_{i}}').next_to(
            text3, DOWN).scale(0.8)
        self.play(FadeOut(text1),
                  FadeOut(formula1),
                  text2.animate.move_to(text1[1]),
                  formula2.animate.move_to(formula1),
                  Create(formula3),
                  Create(text3))
        self.wait(2.5)

        invertFT = MathTex(r'	\rho(x,y,z) ', r' = \frac{1}{V}\sum_{h,k,l\in\, molecule}|', r'F(h,k,l)',
                           r'|\cos\left[  2\pi(hx+ky+lz) + \varphi(h,k,l) \right]').scale(0.7).move_to(formula2)
        invertFT[0].set_color(ORANGE)
        invertFT[2].set_color(YELLOW)

        text7 = Tex(r'Intensity $\textbf{I}(\textbf r)$ of points on the detector is ', r'$\textbf F(\textbf S)$',
                    r'$^2$').next_to(invertFT, UP).scale(0.7)
        text7[1].set_color(YELLOW)

        result = SurroundingRectangle(VGroup(text7, invertFT), color=WHITE)

        self.play(FadeIn(invertFT, text7, result),
                  FadeOut(formula2), FadeOut(text2))
        self.wait(3)

        text4 = Tex(r'If we have an ', r'intensity plot,\\','we always can transform it by Patterson map').to_edge(UP).scale(0.8)
        self.play(FadeOut(text3, formula3, text7, invertFT, result),
                  FadeIn(text4))

        dots0 = VGroup(
            *[Dot([np.random.uniform(-1, 1), np.random.uniform(-1, 1), np.random.uniform(-1, 1)], fill_opacity=np.random.uniform(0, 1)) for x in range(15)]).shift(3*LEFT)

        self.play(Create(dots0))
        self.play(Indicate(text4[1]), Indicate(dots0))

        self.wait()
        map = Arrow(LEFT,RIGHT)
        text_map = Tex(r'Patterson map $P(\textbf r)$').next_to(map,UP).scale(0.7)

        self.play(FadeIn(map,target_position=dots0.get_center()),
                  FadeIn(text_map, target_position=map.get_center()))

        self.wait()

        dots_pat = VGroup(
            *[Dot([np.random.uniform(-1.5, 1), np.random.uniform(-1.5, 1.5), np.random.uniform(-1.5, 1.5)],
                  color=random_color(), radius=DEFAULT_DOT_RADIUS*1.5 ) for x in range(15)]).shift(3.5*RIGHT)

        self.play(FadeIn(dots_pat,target_position=dots0.get_center()))




        text5 = Tex(r'For example, we have a molecule, that has three atoms.\\',
                    'We obtain an intensity plot and then transform it').to_edge(UP).scale(0.8)
        trig = SVGMobject('/Users/isajgordeev/Desktop/bf video/particles.svg')
        theor = SVGMobject('/Users/isajgordeev/Desktop/bf video/pattheor.svg').next_to(trig, 3 * RIGHT).scale(2)
        theor_text = Tex(r'Expectable Patterson map \\ of this molecule').next_to(theor, DOWN).scale(0.8)
        self.wait(4)

        exp = SVGMobject('/Users/isajgordeev/Desktop/bf video/patexp.svg').shift(4 * LEFT).scale(2)
        lines = SVGMobject('/Users/isajgordeev/Desktop/bf video/finalp1.svg').scale(1.6)
        final = SVGMobject('/Users/isajgordeev/Desktop/bf video/finalp.svg').scale(1)
        dots = SVGMobject('/Users/isajgordeev/Desktop/bf video/dotsp.svg').scale(1.1)

        exp_text = Tex(r'On practice we have a noise and\\ the large spot at the origin').next_to(exp, DOWN).scale(0.8)
        self.play(ReplacementTransform(text4, text5),
                  Create(trig),
                  FadeOut(dots0, dots_pat, map, text_map))
        self.wait(2)

        self.play(trig.animate.shift(4 * LEFT),
                  Create(theor),
                  Create(theor_text))
        self.wait(2)

        self.play(ReplacementTransform(trig, exp), Create(exp_text))
        self.wait(2)

        text6 = Tex(r'So, the beauty of this method is to obtain \\ all the relative distances between all atoms').to_edge(
            UP).scale(0.8)
        self.play(ReplacementTransform(text5, text6),
                  VGroup(exp, exp_text).animate.shift(4 * RIGHT),
                  FadeOut(theor, theor_text, exp_text))
        self.wait(3)

        text7 = Tex(r'If we know all the relative distances between atoms\\',
                    r'we can reconstruct a molecule structure \\with the algorythms help').to_edge(DOWN).shift(DOWN * 0.2).scale(0.8)
        self.play(Create(text7[0]),
                  ReplacementTransform(exp, lines))
        self.wait(2)

        self.play(FadeIn(text7[1]))
        self.wait(2)

        self.play(ReplacementTransform(lines, final))

        self.wait(2)

        self.play(FadeIn(dots))
        self.wait(2)
        finaltext0 = Tex(r'As a result, we obtained the atomic structure').next_to(dots, 2 * UP).scale(0.8)
        self.play(FadeOut(text7, text6),
                  Uncreate(final),
                  FadeIn(finaltext0))
        self.wait(2)

        protdot = SVGMobject('/Users/isajgordeev/Desktop/УЧЕБА/IV/scatter/proteindot.svg').scale(2.5)
        protein = SVGMobject('/Users/isajgordeev/Desktop/УЧЕБА/IV/scatter/protein.svg').scale(2.5)

        self.play(FadeOut(finaltext0), ReplacementTransform(dots, protdot))

        self.wait()

        self.play(Create(protein), Uncreate(protdot), run_time=8)

        self.wait()

