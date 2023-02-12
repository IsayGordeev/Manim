import random

from manim import *


class Helvetica(Scene):
    def construct(self):
        func = lambda pos: (pos[0] * UP + pos[1] * LEFT) / 3
        a = ArrowVectorField(func, x_range=[-2, 2], y_range=[-2, 2])
        b = SurroundingRectangle(a)
        circle = Circle(color=BLUE, radius=2)
        circle0 = Circle(color=BLUE, radius=0.3, fill_opacity=1)
        dot = Dot(color=RED)
        Itext = Tex(r'$I$').set_color(RED).shift(1.7 * LEFT)
        atext = Tex('B vector field').next_to(b, DOWN)

        Tex.font = 'CMU Serif'
        Tex1 = Tex('Recently, I had a ', 'ls', '$^{*}$', ' and a ', 'lme', '$^{*}$', color=WHITE).to_edge(UP)
        Tex1.scale(0.75)

        # Tex1[1].set_color(YELLOW)
        Tex1[2].set_color(YELLOW)
        # Tex1[4].set_color(YELLOW)
        Tex1[5].set_color(YELLOW)

        Tex10 = Tex('$^{*}$..nevermind..').scale(0.6).to_edge(UP + RIGHT).set_color(YELLOW)

        self.play(Write(VGroup(Tex1[0], Tex1[1], Tex1[3], Tex1[4])))
        self.wait()
        self.play(FadeIn(VGroup(Tex1[2], Tex1[5]), rate_func=there_and_back_with_pause),
                  FadeIn(Tex10, rate_func=there_and_back_with_pause), run_time=5)
        self.wait()

        Tex2 = Tex('can not just finish my two videos about ', 'Biot-Savart law', color=WHITE)
        Tex2.scale(0.75)
        Tex2.next_to(Tex1, DOWN)

        self.play(Write(Tex2))
        c = Underline(Tex2[1], color=YELLOW)
        self.play(Create(a, rate_func=linear),
                  Create(b),
                  FadeIn(atext),
                  FadeIn(Itext, circle0, dot),
                  Create(circle),
                  Create(c),
                  run_time=3
                  )
        self.wait()
        Tex4 = Tex(
            "zettel is going well, credits are closed, qm is passed and\\ the list of preferable topics have been prepared:",
            color=WHITE)
        Tex4.scale(0.75)
        Tex4.next_to(Tex2, DOWN)
        self.play(FadeOut(a,
                          b,
                          atext,
                          Itext,
                          circle0,
                          dot,
                          circle,
                          c),

                  FadeIn(Tex4)
                  )

        self.wait()
        blist = BulletedList("Finish the Biot-Savart", "Wave equation", "Membrane potential", 'Brain convolution',
                             'Quantum mechanics basics', font_size=0.75 * DEFAULT_FONT_SIZE)
        blist.set_color_by_tex("Finish the Biot-Savart", BLUE)
        blist.set_color_by_tex("Wave equation", BLUE)
        blist.set_color_by_tex("Membrane potential", BLUE)
        blist.set_color_by_tex("Brain convolution", BLUE)
        blist.set_color_by_tex("Quantum mechanics basics", BLUE)

        self.play(Create(blist),
                  FadeOut(Tex1,run_time=0.3),
                  FadeOut(Tex2,run_time=0.3),
                  FadeOut(Tex4, run_time=0.3))
        self.wait()


class wave_equation(Scene):
    def construct(self):
        blist = BulletedList("Finish the Biot-Savart", "Wave equation", "Membrane potential", 'Brain convolution',
                             'Quantum mechanics basics', font_size=0.75 * DEFAULT_FONT_SIZE)
        blist.set_color_by_tex("Finish the Biot-Savart", BLUE)
        blist.set_color_by_tex("Wave equation", BLUE)
        blist.set_color_by_tex("Membrane potential", BLUE)
        blist.set_color_by_tex("Brain convolution", BLUE)
        blist.set_color_by_tex("Quantum mechanics basics", BLUE)
        vertical_line = Line(start=3 * DOWN, end=3 * UP)
        self.add(blist)
        self.play(blist.animate.shift(3 * LEFT),
                  Create(vertical_line))
        self.play(blist.animate.fade_all_but(1, opacity=0.4),
                  )
        self.wait()

        we1text = Tex('Nature of ', r'$\vec E$', ' and ', r'$\vec B$')
        we1text[1].set_color(RED)
        we1text[3].set_color(BLUE)
        we1text.move_to(vertical_line.get_top() + 3 * RIGHT)
        we1text.scale(0.75)

        Evec = Arrow(start=2 * RIGHT, end=2 * RIGHT + UP, buff=0)
        Evec.set_color(RED)
        Evectext = Tex(r'$\vec E$')
        Evectext.set_color(RED)
        Evectext.move_to(Evec.get_end() + 0.5 * UP)

        Bvec = Arrow(start=Evec.get_start(), end=Evec.get_start() + RIGHT, buff=0)
        Bvec.set_color(BLUE)
        Bvectext = Tex(r'$\vec B$')
        Bvectext.set_color(BLUE)
        Bvectext.move_to(Bvec.get_end() + 0.5 * UP)

        Kvec = Arrow(start=Evec.get_start(), end=Evec.get_start() + RIGHT * np.cos(PI / 6) + DOWN * np.sin(PI / 6),
                     buff=0)
        Kvec.set_color(GREEN)
        Kvectext = Tex(r'$\vec k$')
        Kvectext.move_to(Kvec.get_end() - 0.5 * UP)
        Kvectext.set_color(GREEN)

        Kvec = VGroup(Kvectext, Kvec)
        Bvec = VGroup(Bvectext, Bvec)
        Evec = VGroup(Evectext, Evec)

        self.play(FadeIn(we1text, Evec, Bvec), )
        self.play(Rotate(mobject=Bvec[1], angle=PI / 6, about_point=Evec[1].get_start()), FadeIn(Kvec))

        self.play(Evec.animate.shift(2 * (RIGHT * np.cos(PI / 6) + DOWN * np.sin(PI / 6))),
                  MaintainPositionRelativeTo(mobject=Bvec[1], tracked_mobject=Evec[1]),
                  MaintainPositionRelativeTo(mobject=Kvec[1], tracked_mobject=Evec[1]),
                  MaintainPositionRelativeTo(mobject=Bvec[0], tracked_mobject=Bvec[1]),
                  MaintainPositionRelativeTo(mobject=Evec[0], tracked_mobject=Evec[1]),
                  MaintainPositionRelativeTo(mobject=Kvec[0], tracked_mobject=Kvec[1]),
                  )

        sin_func_1 = FunctionGraph(
            lambda t: 0.1 * np.sin(t * 15),
            x_range=[-1, 1],
            # x_range=[-2, 2],
            color=GREEN,
        )

        sin_func_1.rotate(angle=-PI / 6)
        sin_func_1.move_to(Kvec[1])

        self.play(ReplacementTransform(Kvec[1], sin_func_1), FadeOut(Evec, Bvec, Kvec[0]))
        self.play(sin_func_1.animate.shift(6 * (RIGHT * np.cos(PI / 6) + DOWN * np.sin(PI / 6))))
        sin_func_1.rotate(angle=-PI / 3)
        sin_func_1.next_to(we1text, 3 * UP)
        self.play(sin_func_1.animate.move_to(we1text.get_top() + UP))
        self.wait(2)

        we2text = Tex('Skin effect')
        we2text.move_to(we1text)
        we2text.scale(0.75)

        conductor = Circle(1, fill_opacity=0.7, fill_color=GREY, color=None)
        conductor.next_to(we2text, 3 * DOWN)
        self.play(ReplacementTransform(we1text, we2text), FadeIn(conductor))

        f = lambda pos: ((pos[1]) * LEFT + (pos[0]) * UP) if np.linalg.norm(pos) > 0.5 and np.linalg.norm(
            pos) < 1 else 0
        vector_field = StreamLines(f, colors=[GREEN], stroke_color=GREEN, stroke_width=3)
        vector_field.move_to(conductor)

        forbidden_zone = Circle(0.5, color=GREEN, fill_color=RED, fill_opacity=0.7)
        forbidden_zone.move_to(conductor)
        forbidden_zone_text = Tex('forbidden zone for current')
        forbidden_zone_text.scale(0.6)
        forbidden_zone_text.next_to(conductor, 4 * DOWN)
        forbidden_zone_text_pointer = Arrow(start=forbidden_zone_text.get_center(),
                                            end=forbidden_zone)
        forbidden_zone_text = VGroup(forbidden_zone_text,
                                     Underline(forbidden_zone_text))

        conductor_zone_text = Tex('conductor')
        conductor_zone_text.scale(0.6)
        conductor_zone_text.next_to(conductor, RIGHT + UP)
        conductor_zone_text_pointer = Arrow(start=conductor_zone_text,
                                            end=conductor, buff=SMALL_BUFF)
        conductor_zone_text = VGroup(conductor_zone_text,
                                     Underline(conductor_zone_text))
        self.wait(2)
        self.play(sin_func_1.animate.move_to(conductor.get_top() + UP),
                  we2text.animate.shift(1.5 * RIGHT))

        self.play(FadeIn(vector_field))
        self.wait(2)
        self.play(FadeIn(forbidden_zone,
                         forbidden_zone_text,
                         forbidden_zone_text_pointer,
                         conductor_zone_text,
                         conductor_zone_text_pointer
                         ))
        self.wait(4)
        self.play(FadeOut(forbidden_zone,
                          forbidden_zone_text,
                          forbidden_zone_text_pointer,
                          conductor_zone_text,
                          conductor_zone_text_pointer,
                          conductor,
                          we2text,
                          vector_field,
                          sin_func_1,
                          shift=DOWN),
                  )
        self.wait(2)
        self.play(blist.animate.fade_all_but(2, opacity=0.4))
        self.wait()


class membrane_potential(Scene):
    def construct(self):
        blist = BulletedList("Finish the Biot-Savart",
                             "Wave equation",
                             "Membrane potential",
                             'Brain convolution',
                             'Quantum mechanics basics', font_size=0.75 * DEFAULT_FONT_SIZE)
        blist.set_color_by_tex("Finish the Biot-Savart", BLUE)
        blist.set_color_by_tex("Wave equation", BLUE)
        blist.set_color_by_tex("Membrane potential", BLUE)
        blist.set_color_by_tex("Brain convolution", BLUE)
        blist.set_color_by_tex("Quantum mechanics basics", BLUE)
        vertical_line = Line(start=3 * DOWN, end=3 * UP)
        blist.shift(3 * LEFT)
        self.add(blist,
                 vertical_line)
        blist.fade_all_but(2, opacity=0.4)
        cell = SVGMobject('/Users/isajgordeev/Desktop/bf video/cell.svg')
        cell.scale(1.5)
        cell.shift(3 * RIGHT + 2 * UP)
        self.play(FadeIn(cell))

        volt = Circle(0.3, color=WHITE)
        metr = Tex('V')
        metr.move_to(volt.get_center())
        voltmetr = VGroup(volt, metr)
        voltmetr.next_to(cell, DOWN)
        circ1 = Line(start=voltmetr.get_right(), end=voltmetr.get_right() + UP)
        circ2 = Line(start=voltmetr.get_left(), end=voltmetr.get_left() + UP)
        circuit = VGroup(circ1, circ2, voltmetr)
        self.play(FadeIn(circuit))

        n = 11
        ticks = [Line(start=0 * LEFT, end=0.2 * UP).rotate(PI / 2 + PI / n * (x + 1)).move_to(
            [np.cos(PI / n * (x + 1)), np.sin((PI) / n * (x + 1)), 0]) for x in range(n)]

        arrow_tick = Line(start=ORIGIN, end=[0.8 * np.cos(PI / n * (5 + 1)), 0.8 * np.sin((PI) / n * (5 + 1)), 0])
        arrow_tick.rotate(angle=-PI / (n * 2))
        arrow_tick.set_color(LIGHT_BROWN)
        point_tick = Dot(arrow_tick.get_start(), color=WHITE)

        ticks0 = VGroup(*ticks, arrow_tick, point_tick)
        ticks0.rotate(angle=-PI / (n * 2))
        ticks0.next_to(voltmetr, DOWN + 2 * RIGHT)

        wire = CubicBezier(voltmetr.get_bottom(),
                           voltmetr.get_bottom() + LEFT + 2 * DOWN,
                           voltmetr.get_bottom() + LEFT + 3 * DOWN + RIGHT,
                           point_tick.get_center())

        self.play(FadeIn(ticks0, wire))
        self.wait(2)

        K = Circle(0.15, color=RED, fill_opacity=1)

        Ktex = Tex('+')
        Ktex.scale(0.8)
        Ktex.move_to(K.get_center())
        Ktex.set_color(BLACK)
        K = VGroup(K, Ktex)
        K.move_to(7 * RIGHT + 6 * UP)

        # self.add(K, Ktex)
        self.play(K.animate.move_to(cell.get_right() + 0.2 * LEFT), Rotate(mobject=arrow_tick, angle=PI/24, about_point=point_tick.get_center(),rate_func=wiggle))
        self.play(Rotate(mobject=arrow_tick, angle=PI/24, about_point=point_tick.get_center(),rate_func=wiggle))
        self.play(Rotate(mobject=arrow_tick, angle=PI/12, about_point=point_tick.get_center()))
        self.wait()

        mp1text = Tex(r'Is there a dependence between an ion kind\\ and the membrane potential?')
        mp1text.next_to(wire, 3.5*DOWN)
        mp1text.scale(0.65)

        self.play(FadeIn(mp1text))
        self.wait(3)
        self.play(FadeOut(mp1text,
                          cell,
                          circuit,
                          wire,
                          ticks0,
                          K, direction=DOWN),)
        self.play(blist.animate.fade_all_but(3, opacity=0.4))
        self.wait()

class BrainConvolution(Scene):
    def construct(self):
        blist = BulletedList("Finish the Biot-Savart",
                             "Wave equation",
                             "Membrane potential",
                             'Brain convolution',
                             'Quantum mechanics basics', font_size=0.75 * DEFAULT_FONT_SIZE)
        blist.set_color_by_tex("Finish the Biot-Savart", BLUE)
        blist.set_color_by_tex("Wave equation", BLUE)
        blist.set_color_by_tex("Membrane potential", BLUE)
        blist.set_color_by_tex("Brain convolution", BLUE)
        blist.set_color_by_tex("Quantum mechanics basics", BLUE)
        vertical_line = Line(start=3 * DOWN, end=3 * UP)
        blist.shift(3 * LEFT)
        self.add(blist,
                 vertical_line)
        blist.fade_all_but(3, opacity=0.4)

        brain1 = SVGMobject('/Users/isajgordeev/Desktop/УЧЕБА/lll/ПОСТЕР/brain0.svg')
        brain2 = SVGMobject('/Users/isajgordeev/Desktop/УЧЕБА/lll/ПОСТЕР/brain2.svg').scale(1.5)
        brain3 = SVGMobject('/Users/isajgordeev/Desktop/УЧЕБА/lll/ПОСТЕР/brain3.svg').scale(2)
        brain4 = SVGMobject('/Users/isajgordeev/Desktop/УЧЕБА/lll/ПОСТЕР/brain4.svg').scale(2.5)
        brain4inner = SVGMobject('/Users/isajgordeev/Desktop/УЧЕБА/lll/ПОСТЕР/brain4inner.svg').scale(2.5)

        brain4.move_to(RIGHT*3)
        brain4inner.move_to(RIGHT*3)

        brain1text = Tex('Gestation week – 22').scale(0.75)
        brain1text.next_to(brain1, 1.5*DOWN)

        brain2text = Tex('Gestation week – 29').scale(0.75)
        brain2text.next_to(brain1, 1.5 * DOWN)

        brain3text = Tex('Gestation week – 40').scale(0.75)
        brain3text.next_to(brain1, 1.5 * DOWN)

        brain4text = Tex('Gestation week – Adult').scale(0.75)
        brain4text.next_to(brain1, 1.5 * DOWN)

        self.play(FadeIn(brain4inner.set_color(RED), shift=DOWN))
        # print(brain1.get_all_points())
        self.play(*[Indicate(Dot(random.choice(brain4inner.get_points_defining_boundary()))) for x in range(20)])
        # brain1.get_num_points()
        # self.play(FadeIn(brain1,brain1text, shift=DOWN))
        # self.wait(1.5)
        # self.play(ReplacementTransform(brain1,
        #                                brain2.move_to(brain1)),
        #           ReplacementTransform(brain1text,
        #                                brain2text.next_to(brain1text,DOWN)),
        #           )
        # self.wait(1.5)
        # self.play(ReplacementTransform(brain2text,
        #                                brain3text.next_to(brain2text,DOWN)),
        #           ReplacementTransform(brain2,
        #                                brain3.move_to(brain2))
        #           )
        # self.wait(1.5)
        # self.play(ReplacementTransform(brain3text,
        #                                brain4text.next_to(brain3text,DOWN)),
        #           ReplacementTransform(brain3,
        #                                brain4.move_to(brain3))
        #           )
        # text = Tex('What contributes to the brain\'s growth?').scale(0.75)
        # text.next_to(brain4, UP)
        # self.play(FadeIn(text,shift=UP))
        # self.wait(1.5)
        # self.play(FadeOut(brain4text, brain4, text, shift=DOWN))
        # self.wait(0.7)
        # self.play(blist.animate.fade_all_but(4, opacity=0.4))
        # self.wait()

class quantum_mech(Scene):
    def construct(self):
        blist = BulletedList("Finish the Biot-Savart",
                             "Wave equation",
                             "Membrane potential",
                             'Brain convolution',
                             'Quantum mechanics basics', font_size=0.75 * DEFAULT_FONT_SIZE)
        blist.set_color_by_tex("Finish the Biot-Savart", BLUE)
        blist.set_color_by_tex("Wave equation", BLUE)
        blist.set_color_by_tex("Membrane potential", BLUE)
        blist.set_color_by_tex("Brain convolution", BLUE)
        blist.set_color_by_tex("Quantum mechanics basics", BLUE)
        vertical_line = Line(start=3 * DOWN, end=3 * UP)
        blist.shift(3 * LEFT)
        self.add(blist,
                 vertical_line)
        blist.fade_all_but(4, opacity=0.4)

        blist1 = BulletedList("Dirac\'s notation",
                             "Schrödinger equation",
                             "Oscillator quantization",
                             r'Nature of the spin $\textbf S$',
                             font_size=0.65 * DEFAULT_FONT_SIZE)
        blist1.set_color_by_tex("Dirac\'s notation", BLUE_D)
        blist1.set_color_by_tex("Schrödinger equation", BLUE_D)
        blist1.set_color_by_tex("Oscillator quantization", BLUE_D)
        blist1.set_color_by_tex(r'Nature of the spin $\textbf S$', BLUE_D)
        blist1.shift(2.5 * LEFT)
        blist1.save_state()

        self.play(blist.animate.shift(4*UP), FadeIn(blist1,shift=UP), FadeOut(vertical_line))
        self.play(blist.animate.fade_all_but(4, opacity=0))
        self.wait(3)
        # dirac = MathTex(r'\mathcal H:\ |\Psi(x)\rangle = \sum_n\Psi_nn\rangle\right\mathcal V:\ \textbf a = \sum_na_nn\textbf e_n').scale(0.75)
        dirac = MathTex(r'\mathcal H:\ |\Psi(x)\rangle = \sum_n\Psi_n|n\rangle').scale(0.6)
        dirac.next_to(blist1[0],RIGHT*5)
        dirac.shift(DOWN*0.1)

        self.play(blist1.animate.fade_all_but(0, opacity=0.4), FadeIn(dirac, shift=RIGHT))
        self.wait(2)

        shr = MathTex(r'i\hbar\frac{\partial}{\partial t}|\Psi\rangle = \hat H|\Psi\rangle').scale(0.6)
        shr.next_to(blist1[1], RIGHT * 4)

        self.play(blist1.animate.fade_all_but(1, opacity=0.4), FadeIn(shr, shift=RIGHT), dirac.animate.set_opacity(0.4))
        self.wait(2)

        e = MathTex(r'E_n=\hbar\omega\left(n+\frac12\right)').scale(0.6)
        e.next_to(blist1[2], RIGHT * 3)

        self.play(blist1.animate.fade_all_but(2, opacity=0.4), FadeIn(e, shift=RIGHT), shr.animate.set_opacity(0.4))
        self.wait(2)

        a = MathTex(r'\hat R|\Psi, P\rangle =\ ? \ \ \hat R\in\text{SO}(3)').scale(0.6)
        a.next_to(blist1[3], RIGHT * 3)

        self.play(blist1.animate.fade_all_but(2, opacity=0.4), FadeIn(a, shift=RIGHT), e.animate.set_opacity(0.4))
        self.wait(2)

        self.play(blist1.animate.restore(),
                  shr.animate.set_opacity(1),
                  dirac.animate.set_opacity(1),
                  e.animate.set_opacity(1))
        self.wait(2)

        self.play(FadeOut(blist1,
                          blist,
                          dirac,
                          e,
                          shr,
                          a))
        self.wait()







