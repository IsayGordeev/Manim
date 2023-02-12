from manim import *


def functwo(p):
    func = lambda pos: [pos[0] - 2, pos[1], 0]
    func1 = lambda pos: [pos[0] + 2, pos[1], 0]

    return func(p) + func1(p)


class qulomb(ZoomedScene):

    def construct(self):
        text = Tex(r'Qulomb conducted an experiment with two point charges \\',
                   ' and the result was that force of interaction $\\vec F$  between two these charges').scale(0.65)
        qulomblaw = MathTex(r'\vec F =\frac{q^2}{r^3}\vec r').scale(0.65)
        self.play(Write(text))
        self.wait(2.5)
        self.play(Write(qulomblaw), text.animate.shift(UP))
        self.wait(2.5)
        text2 = Tex(r'But there was a problem. How exactly two point charges feel each other?\\ ',
                    r' Nowadays, the assumption is that point charge creates electric field, and that field exerts on another one point charge.').move_to(
            text).scale(0.65)
        self.play(ReplacementTransform(text, text2[0]))
        self.wait(2.5)
        self.play(Write(text2[1]))
        self.wait(2.5)

        text3 = Tex(
            r'And a total field is a vector sum of two fields in the point. This is a principle of superposition.').scale(
            0.65).move_to(DOWN)
        self.play(Write(text3))
        self.wait(2.5)
        Sphere
        func = lambda pos: [-(pos[0] - 2) / (np.sqrt((pos[0] - 2) ** 2 + pos[1] ** 2 + 0.1)) ** 3,
                            -pos[1] / (np.sqrt((pos[0] - 2) ** 2 + pos[1] ** 2 + 0.1)) ** 3, 0]
        vector_field = ArrowVectorField(func)
        self.play(Create(vector_field), run_time=3)
        self.wait(2)
        text4 = Tex('This is vector field of single negative point charge').scale(0.65).to_corner(UP)
        field = MathTex(r'\vec E =\frac{q}{r^3}\vec r').scale(0.65).next_to(text4, DOWN)
        self.play(ReplacementTransform(text3, text4), ReplacementTransform(text2, text4),
                  ReplacementTransform(qulomblaw, field), run_time=3)
        self.wait()

        self.play(Indicate(text4))
        self.wait(2)

        func1 = lambda pos: [(pos[0] + 2) / (np.sqrt((pos[0] + 2) ** 2 + pos[1] ** 2 + 0.1)) ** 3,
                             pos[1] / (np.sqrt((pos[0] + 2) ** 2 + pos[1] ** 2 + 0.1)) ** 3, 0]
        vector_field_two = ArrowVectorField(func1)
        text5 = Tex('This is vector field of single positive point charge').scale(0.65).to_corner(UP)
        self.play(ReplacementTransform(vector_field, vector_field_two), ReplacementTransform(text4, text5), run_time=3)
        self.wait()
        self.play(Indicate(text5), run_time=1.5)
        self.wait(2)

        functwo = lambda pos: [func1(pos)[0] + func(pos)[0], func1(pos)[1] + func(pos)[1], 0]

        text6 = Tex('This is total vector field of negative and positive point charges').scale(0.65).to_corner(UP)

        vector_field_superp = ArrowVectorField(functwo)
        vector_field_superp1 = ArrowVectorField(functwo, opacity=0)

        vector_field1 = ArrowVectorField(func)

        self.play(Create(vector_field1), ReplacementTransform(text5, text6), run_time=3)
        self.wait(3)
        self.play(ReplacementTransform(vector_field_two, vector_field_superp),
                  ReplacementTransform(vector_field1, vector_field_superp1), run_time=3)
        self.wait()
        self.play(Indicate(text6))
        self.wait(3)
        self.play(Uncreate(vector_field_superp), Unwrite(text6), Unwrite(field))
        self.wait(2)


class Gauss(ZoomedScene):
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
        func1 = lambda pos: [(pos[0] + 2) / (np.sqrt((pos[0] + 2) ** 2 + pos[1] ** 2 + 0.1)) ** 3,
                             pos[1] / (np.sqrt((pos[0] + 2) ** 2 + pos[1] ** 2 + 0.1)) ** 3, 0]

        scenetext = Tex('Let\'s add contour on our field with an area $S$',
                        r'\\Consider a flow $\Phi$').scale(0.65)
        scenetext.shift(3.5 * RIGHT + 2.7 * UP)

        scenetextformula = MathTex('\displaystyle\Phi =', r' \int_S ', r'\vec E', r'\cdot ', r'd\vec S').scale(
            0.65).next_to(scenetext, DOWN)
        scenetext[0].move_to(ORIGIN)

        scenetextformula[1].set_color(RED)
        scenetextformula[2].set_color(GREEN)
        scenetextformula[4].set_color(RED)
        chargeq = Dot(2 * LEFT, radius=0.08).set_color(BLUE)
        q = Tex('q').next_to(chargeq, (UP + RIGHT) / 3).scale(0.65).set_color(BLUE)
        self.play(Write(scenetext[0]))
        self.wait(2)
        vector_field_tworeduced = ArrowVectorField(func1, opacity=0.5)
        self.play(Create(vector_field_tworeduced), scenetext[0].animate.shift(3.5 * RIGHT + 3 * UP), Create(chargeq),
                  Write(q))
        contour = SVGMobject('/Users/isajgordeev/Desktop/contour.svg').shift(1.9 * LEFT)
        contour1 = SVGMobject('/Users/isajgordeev/Desktop/contour2.svg').shift(2.9 * LEFT)
        contour2 = SVGMobject('/Users/isajgordeev/Desktop/contour3.svg').shift(1.9 * LEFT)

        E = Tex(r'$\vec E$').shift(contour.get_right() + 0.3 * RIGHT + 0.2 * UP).scale(0.3).set_color(GREEN)
        Evec = Arrow(contour.get_right(), contour.get_right() + 0.27 * RIGHT).set_color(GREEN)
        normal = Arrow(contour.get_right(), contour.get_right() + 0.3 * (2 * DOWN / 3 + RIGHT)).set_color(RED)
        dS = Tex(r'$d\vec S$').move_to(normal.get_end() + DOWN * 0.1).scale(0.3).set_color(RED)
        # angle = Angle(normal,Evec, stroke_width=0.4)
        angletext = MathTex(r"\theta").move_to(
            Angle(
                normal, Evec, radius=0.2, other_angle=False
            ).point_from_proportion(0.5)).scale(0.2)
        self.play(Create(contour))
        self.wait(2)

        self.zoomed_camera.frame.shift(contour.get_right())
        self.zoomed_display.to_corner(LEFT + UP)
        self.play(Create(self.zoomed_camera.frame))

        self.activate_zooming()

        self.play(self.get_zoomed_display_pop_out_animation(), run_time=2)
        self.wait(2)

        self.play(Write(scenetext[1]), Write(scenetextformula), Write(E), Write(dS), Create(normal), Create(Evec),
                  Write(angletext), run_time=3)
        self.wait(2)

        textformula1 = Tex('Using definition of dot product').next_to(scenetextformula, DOWN).scale(0.65)
        formula1 = MathTex(r'\displaystyle\Phi = ', r'\int_S', r' E', r' dS ', r'\cos \theta').next_to(scenetextformula,
                                                                                                       DOWN).scale(0.65)
        formula1[1].set_color(RED)
        formula1[2].set_color(GREEN)
        formula1[3].set_color(RED)

        self.play(Write(textformula1))
        self.wait(3)

        self.play(ReplacementTransform(textformula1, formula1))
        textformula2 = Tex('Using formula for electric field of point particle').next_to(formula1, DOWN).scale(0.65)
        formula2 = MathTex(r'\displaystyle\Phi = ', r'\int_S', r' \frac{q}{r^2} ', r'dS ', r'\cos \theta').next_to(
            formula1, DOWN).scale(0.65)
        formula2[1].set_color(RED)
        formula2[2].set_color(BLUE)
        formula2[3].set_color(RED)

        self.play(Write(textformula2))
        self.wait(3)

        self.play(ReplacementTransform(textformula2, formula2))
        textformula3 = MathTex(r'\displaystyle\frac{1}{r^2}', r'dS',
                               r'\cos \theta = d\Omega - \text{is a solid angle}\\',
                               r' \text{of our infinitesimal area}').next_to(formula2, DOWN).scale(0.65)
        formula3 = MathTex(r'\displaystyle\Phi = ', r'q', r'\int_S', r' d\Omega').next_to(formula2, DOWN).scale(0.65)
        formula3[2].set_color(RED)
        formula3[1].set_color(BLUE)

        textformula3[0].set_color(BLUE)
        textformula3[1].set_color(RED)

        self.play(Write(textformula3))
        self.wait(3)

        self.play(ReplacementTransform(textformula3, formula3))
        textformula4 = Tex(r'All space is visible at the $4\pi$ solid angle\\',
                           r' or $\displaystyle\int_S d\Omega = 4\pi$').next_to(formula3, DOWN).scale(0.65)
        formula4 = MathTex(r'\displaystyle\Phi = 4\pi ', r' q').next_to(formula3, DOWN).scale(0.65)
        formula4[1].set_color(BLUE)
        self.play(Write(textformula4))
        self.wait(3)
        self.play(ReplacementTransform(textformula4, formula4))
        self.wait(3)
        scenetext1 = Tex(r'So we obtained, that no matter what shape\\',
                         r'flow $\displaystyle\Phi$ of electric field is constant, depending on charge').move_to(
            3 * UP).scale(0.65)
        self.play(self.get_zoomed_display_pop_out_animation(), rate_func=lambda t: smooth(1 - t),
                  run_time=2)
        self.play(FadeOut(self.zoomed_camera.frame), Uncreate(self.zoomed_display.display_frame), Uncreate(normal),
                  Unwrite(dS), Uncreate(Evec), Unwrite(E), Unwrite(angletext), Uncreate(scenetextformula), run_time=5)

        self.play(Write(scenetext1), Uncreate(scenetext), Unwrite(formula1), Unwrite(formula2), Unwrite(formula3),
                  Unwrite(formula4), run_time=3)
        self.play(ReplacementTransform(contour, contour1))
        self.play(ReplacementTransform(contour1, contour2))
        # self.play(Write(scenetext1[1] ))

        endtext1 = Tex('The Gauss\'s law').move_to(3 * UP + 2 * UP).move_to(3 * RIGHT + 2 * UP).scale(0.65)
        endtext2 = Tex(r'Particularly, we can easily prove that electric field \\',
                       r'of point charge is spherically symmetric\\', 'using the Gauss\'s law').next_to(endtext1,
                                                                                                        3 * DOWN).scale(
            0.65)
        endformula = MathTex(' \int_S ', r'\vec E', r'\cdot ', r'd\vec S', r'=4\pi', r'q').scale(0.65).next_to(endtext1,
                                                                                                               DOWN)
        endformula[0].set_color(RED)
        endformula[1].set_color(GREEN)
        endformula[3].set_color(RED)
        endformula[5].set_color(BLUE)

        self.play(FadeIn(endtext1), FadeIn(endformula))
        sphercontour = Circle(radius=1).set_color(RED).shift(2 * LEFT)
        self.wait(2)
        self.play(ReplacementTransform(contour2, sphercontour), TransformFromCopy(endtext1, endtext2))
        self.wait(3)
        self.play(Uncreate(sphercontour), scenetext1.animate.shift(3 * UP), Unwrite(q), Uncreate(chargeq),
                  Uncreate(endtext2), endformula.animate.move_to(ORIGIN), endtext1.animate.move_to(UP), run_time=3)
        self.wait(2)
        self.play(Uncreate(endtext1), Uncreate(endformula), Uncreate(vector_field_tworeduced), run_time=2)
        self.wait(1.5)


class Gaussdiff(Scene):
    def construct(self):
        introtext = Tex('The Gauss\'s law can be written', r' in two forms\\', 'integral ', 'and',
                        ' differential').scale(0.65).shift(UP)
        introformula = MathTex(' \int_S ', r'\vec E', r'\cdot ', r'd\vec S', r'=4\pi', r'q').scale(0.65)
        introformula1 = MathTex(r' \div ', r'\vec E', r'=4\pi', r'\rho', ',\quad ', r'\rho ', '= ', '{dq', '\over',
                                'dV}').scale(0.65).shift(DOWN)

        introformula[0].set_color(RED)
        introformula[1].set_color(GREEN)
        introformula[3].set_color(RED)
        introformula[5].set_color(BLUE)

        introformula1[1].set_color(GREEN)
        introformula1[3].set_color(BLUE)
        introformula1[5].set_color(BLUE)
        introformula1[7].set_color(BLUE)
        introformula1[9].set_color(RED)

        self.play(FadeIn(introtext), run_time=2)
        self.wait(3)

        self.play(Write(introformula), run_time=2)
        self.wait(3)

        self.play(Indicate(introtext[2]), Indicate(introformula), run_time=2)
        self.wait(3)

        self.play(Write(introformula1), run_time=2)
        self.wait(3)

        self.play(Indicate(introtext[4]), Indicate(introformula1[0]), Indicate(introformula1[1]),
                  Indicate(introformula1[2]), Indicate(introformula1[3]), run_time=2)
        self.wait(3)

        text1 = Tex('Let\'s see it').shift(UP).scale(0.65)
        self.play(ReplacementTransform(introtext, text1))

        formula1 = MathTex(r' \div ', r'\vec E', r'=4\pi', r'\rho').scale(0.65)
        formula1[1].set_color(GREEN)
        formula1[3].set_color(BLUE)
        self.wait(3)
        self.play(Uncreate(text1), Uncreate(introformula1), run_time=2)
        self.wait(3)

        formula2 = MathTex(' \int_S ', r'\vec E', r'\cdot ', r'd\vec S', r'=4\pi', r'\int_V', r'\rho', r'dV').scale(
            0.65)
        formula2[0].set_color(RED)
        formula2[1].set_color(GREEN)
        formula2[3].set_color(RED)
        formula2[5].set_color(RED)
        formula2[6].set_color(BLUE)
        formula2[7].set_color(RED)
        self.play(introformula.animate.shift(UP), FadeIn(formula2), run_time=3)
        self.wait(3)

        stockstext = MathTex(r'\text{Stocks theorem -}', r' \int_{\partial V}', r' dw =', r' \int_V ', r'w ').scale(
            0.65)
        stockstext[1].set_color(RED)
        stockstext[2].set_color(BLUE)
        stockstext[3].set_color(RED)
        stockstext[4].set_color(BLUE)

        difftext = MathTex(r'w ', r'\text{ - differential form}').next_to(stockstext, DOWN).scale(0.65)
        difftext[0].set_color(BLUE)
        self.play(formula2.animate.shift(DOWN), Write(stockstext), run_time=3)
        self.wait(3)
        self.play(formula2.animate.shift(0.5 * DOWN), Write(difftext), run_time=3)
        self.wait(3)
        self.play(formula2.animate.shift(1.5 * UP), Unwrite(stockstext), Unwrite(difftext), run_time=3)
        self.wait(3)

        formula21 = MathTex(' \int_{S\equiv\partial V }', r'\vec E', r'\cdot ', r'd\vec S', r'=4\pi', r'\int_V',
                            r'\rho', r'dV').scale(
            0.65)
        formula21[0].set_color(RED)
        formula21[1].set_color(GREEN)
        formula21[3].set_color(RED)
        formula21[5].set_color(RED)
        formula21[6].set_color(BLUE)
        formula21[7].set_color(RED)

        formula3 = MathTex(' \int_V ', r'\div', r'\vec E', r'dV', r'=4\pi', r'\int_V', r'\rho', r'dV').scale(
            0.65).next_to(formula2, DOWN)
        formula3[0].set_color(RED)
        formula3[2].set_color(GREEN)
        formula3[3].set_color(RED)
        formula3[5].set_color(RED)
        formula3[6].set_color(BLUE)
        formula3[7].set_color(RED)

        self.play(ReplacementTransform(formula2, formula21), TransformFromCopy(formula2, formula3), run_time=2)
        self.wait(3)
        text2 = Tex('This integral doesn\'t depend on choosing volume').next_to(formula3, DOWN).scale(0.65)
        self.play(FadeIn(text2), run_time=2)

        endformula = MathTex(r' \div ', r'\vec E', r'=4\pi', r'\rho').scale(0.65)

        endformula[1].set_color(GREEN)
        endformula[3].set_color(BLUE)
        endformula.next_to(formula3, DOWN)
        self.wait(3)

        self.play(FadeOut(text2), FadeIn(endformula), run_time=2)
        self.wait(1.5)
        self.play(FadeOut(formula3), FadeOut(formula21), endformula.animate.move_to(ORIGIN), run_time=2)
        self.wait(1.5)
        self.play(Wiggle(endformula), run_time=2)
        self.play(FadeOut(endformula), FadeOut(introformula), run_time=2)
        self.wait(1.5)


class lattice1(Square):
    def __init__(self, bound=1, **kwargs):
        super().__init__(**kwargs)
        self.bound = bound
        self.delta = 0.5
        self.number_dots = 20
        self.dots = [Dot(np.random.uniform(low=-self.bound + 0.1, high=self.bound - 0.1, size=3),
                         radius=DEFAULT_DOT_RADIUS).set_color(BLUE_E) for x in
                     range(self.number_dots)]
        self.add(*self.dots)


class lattice(VGroup):

    def __init__(self, origin, bound, number_dots, **kwargs):
        super().__init__(**kwargs)
        self.bound = bound
        self.delta = 0.5
        self.number_dots = number_dots
        self.origin = origin
        self.square = Square(side_length=self.bound * 2).move_to(origin)

        self.dots = [Dot(np.random.uniform(low=-self.bound + 0.1, high=self.bound - 0.1, size=3) + origin,
                         radius=DEFAULT_DOT_RADIUS).set_color(BLUE_E) for x in
                     range(self.number_dots)]
        self.add(self.square, *self.dots)
        init_vels = [np.random.uniform(low=-self.bound, high=self.bound, size=3) for x in range(self.number_dots)]
        self.vels = init_vels

    def force(self, coord1, coord2, delta):
        if (np.linalg.norm(coord1 - coord2)) > 1:
            return (-delta / (np.linalg.norm(coord1 - coord2)) ** 4 - delta / (
                np.linalg.norm(coord1 - coord2)) ** 2) * (coord1 - coord2)
        else:
            return coord1 - coord2

    def forces_at_a_moment(self, dots, delta):
        forces = []
        for dot1 in dots:
            force = 0
            for dot2 in dots:
                if dot1 != dot2:
                    force += self.force(dot1.get_center(), dot2.get_center(), delta)
            forces.append(force)
        return forces

    def reflection(self, dot, vels):
        if dot.get_x() + self.origin[0] > self.bound - dot.radius or dot.get_x() + self.origin[
            0] < -self.bound + dot.radius:
            vels[0] = -vels[0]
        if dot.get_y() + self.origin[1] > self.bound - dot.radius or dot.get_y() + self.origin[
            1] < -self.bound + dot.radius:
            vels[1] = -vels[1]
        if dot.get_z() + self.origin[2] > self.bound - dot.radius or dot.get_z() + self.origin[
            2] < -self.bound + dot.radius:
            vels[2] = -vels[2]

        return dot.animate(run_time=0.05).shift(vels / 1000)

    def cur_reflection(self, dot, box):
        if dot.get_x() + self.origin[0] > box.get_right() - dot.radius or dot.get_x() + self.origin[
            0] < -self.bound + dot.radius:
            new_dot = Dot([box.get_left(), dot.get_y(), 0])
            dot.remove()
            new_dot.animate(run_time=0.05).shift(RIGHT / 3)
        else:
            return dot.animate(run_time=0.05).shift(RIGHT / 3)


class electrons(MovingCameraScene):
    def construct(self):

        bound = 0.2
        num = 1
        origin = ORIGIN
        boxes = VGroup(*[lattice(ORIGIN, bound=0.2, number_dots=num) for s in range(0, 217)])
        boxes.arrange_in_grid(rows=7, buff=0.1)
        boxes_stable = boxes.copy()
        smboxes = VGroup(*[lattice(ORIGIN, bound=0.2, number_dots=num) for s in range(0, 21)])
        smboxes.arrange_in_grid(rows=3, buff=0.1)
        self.remove(*[x.square for x in smboxes])

        conductor = Rectangle(color=GRAY, width=self.camera.frame_width * 0.75, fill_opacity=1)
        text1 = Tex('This is ', r'metall', r' - matter, that is able to conduct a ', r'current').next_to(conductor,
                                                                                                         20 * UP).scale(
            5)
        text1[1].set_color(GRAY)
        text1[3].set_color(RED)

        text11 = Tex('x1').next_to(conductor, 20 * DOWN).scale(5)
        text2 = Tex('Abundance of ', r'free electrons', r' gives matter ', r'metallic', r' properties').next_to(boxes,
                                                                                                                2 * UP)
        text2[1].set_color(BLUE)
        text2[3].set_color(GREY)

        text22 = Tex(r'Electrons', r' are constantly moving in ', r'metallic lattice\\', ' shaping ', r'metall',
                     r' itself').next_to(boxes, UP)
        text22[0].set_color(BLUE)
        text22[2].set_color(GRAY)
        text22[4].set_color(GRAY)

        text21 = Tex('x$10^9$').next_to(boxes, DOWN)
        text23 = Tex(r'When we apply ', 'electrical field $E$ ', r'electrons start \\',
                     'to move in order of direction of', ' $E$').next_to(boxes, UP)
        text23[1].set_color(RED)
        text23[4].set_color(RED)

        E = Arrow(LEFT, RIGHT).set_color(RED).scale(2).next_to(text21, DOWN)
        Etext = Tex('$E$').set_color(RED).move_to(E.get_center() + 0.5 * DOWN)
        I = Line(LEFT, RIGHT, stroke_width=20).set_color(RED).scale(6).add_tip()
        I1 = Line(LEFT, RIGHT, stroke_width=20).set_color(RED).scale(6).add_tip().next_to(I, 0.25 * DOWN)
        I2 = Line(LEFT, RIGHT, stroke_width=20).set_color(RED).scale(6).add_tip().next_to(I1, 0.25 * DOWN)
        J = VGroup(I, I1, I2)
        Itext = Tex('$I$').set_color(RED).move_to(I.get_center() + 2.5 * UP).scale(7)

        conductor.height *= 4

        self.camera.frame.save_state()
        self.camera.frame.set(width=self.camera.frame_width * 6).move_to(ORIGIN)
        self.add(conductor, text1, text11)
        self.wait()
        self.play(Wiggle(conductor))

        self.play(Restore(self.camera.frame), run_time=10)
        self.wait(0.3)
        self.play(FadeIn(smboxes), FadeIn(boxes), FadeOut(conductor), Write(text21), run_time=10)
        self.play(Write(text2), run_time=2)
        self.wait(1)
        self.play(Transform(text2, text22), run_time=2)

        self.wait(2)

        self.play(self.camera.frame.animate(run_time=10).set(width=3).move_to(ORIGIN))

        for x in range(1):
            for a in smboxes:
                a.vels = [x + y for x, y in zip(a.vels, a.forces_at_a_moment(a.dots, a.delta))]
                self.play(*[dot.animate(run_time=0.25).shift(vel * 1.5) for dot, vel in zip(a.dots, a.vels)])
        self.remove(text2, text22, text1)
        self.add(text23, E, Etext)
        self.wait(2)

        self.play(Restore(self.camera.frame), FadeOut(smboxes), run_time=10)
        self.wait(2)

        self.add(boxes_stable)
        for y in range(6):
            self.play(*[VGroup(*lat.dots).animate.shift(RIGHT / 3) for lat in boxes])

        self.play(self.camera.frame.animate(run_time=10).set(width=self.camera.frame_width * 6).move_to(ORIGIN),
                  FadeOut(boxes, boxes_stable, run_time=1), FadeIn(conductor, run_time=10), Uncreate(E, run_time=1),
                  FadeOut(text21, run_time=1), Create(J, run_time=6), Create(Itext, run_time=6))
        self.wait(2)
        self.remove(Etext, text23)
        self.play(Uncreate(J), Uncreate(Itext), Uncreate(text11), Uncreate(conductor))
        self.wait(2)


class IntroSavar(ThreeDScene):
    def construct(self):
        conductor = Cylinder(color=GRAY, radius=0.3, height=6, fill_opacity=0.7)
        circle0 = Circle(color=BLUE, radius=0.3, fill_opacity=1)
        vec = Arrow3D(start=np.array([2, 0, 0]), end=np.array([2, 0, 2]), color=RED)
        text1 = Tex(r'Experimentally known, that  ', r'current I\\', 'creates ', r'magnetic field B',
                    r' outside').scale(1)
        text1[1].set_color(RED)
        text1[3].set_color(BLUE)
        text2 = Tex(r'This is Biot–Savart law')
        formula1 = MathTex(r'{\displaystyle \vec {B}(\vec{r})', r' = \frac{1}{c}\int_{\Gamma} ', r'I',
                           r' \frac{(\vec{r}-\vec{l})\times d\vec{l}}{|(\vec{r}-\vec{l}|)^3} ')
        Itext = Tex(r'$I$').set_color(RED).shift(1.7 * RIGHT)
        formula1[0].set_color(BLUE)
        formula1[2].set_color(RED)

        self.play(FadeIn(text1, run_time=1.5))
        self.play(ApplyWave(text1[3], ripples=2, run_time=2, amplitude=0.05), Circumscribe(text1[1], color= RED, run_time=2))
        self.play(FadeOut(text1, run_time=1, shift=UP), FadeIn(text2, run_time=1, shift=UP))
        self.wait(2)
        self.play(FadeIn(formula1, run_time=1, shift=UP), text2.animate.shift(UP))
        self.wait(2)
        self.play(FadeOut(formula1, run_time=1, shift=UP), FadeOut(text2, run_time=1, shift=UP))
        self.wait(2)
        text3 = Tex('Drawing an analogy with the Gauss\'s law, we can write that')
        self.play(Write(text3))
        self.wait(2)
        formula2 = MathTex(' \int_S ', r'\vec B', r'\cdot ', r'd\vec S', r'=4\pi', r' q')
        formula2[1].set_color(BLUE)
        formula2[5].set_color(BLUE)
        self.play(FadeIn(formula2, run_time=1, shift=UP), text3.animate.shift(UP))
        text4 = Tex(r'Vector ', r'B ', r'can not be created by point charge ', r'$q$', r',\\',
                    r'because its end forms a continuous trajectory,\\',
                    r'  as it is integral according Biot-Savart law').next_to(formula2, UP)
        text4[1].set_color(BLUE)
        text4[3].set_color(BLUE)
        self.wait(2)
        self.play(ReplacementTransform(text3, text4))
        text5 = Tex(r'So, ', r' $q\ $', r'$=0$').next_to(formula2, DOWN)
        text5[1].set_color(BLUE)
        self.wait(4)
        formula3 = MathTex(' \int_S ', r'\vec B', r'\cdot ', r'd\vec S', r'=0')
        formula3[1].set_color(BLUE)

        self.play(TransformMatchingTex(formula2, formula3), FadeIn(text5, target_position=text4))
        self.wait(2)
        self.play(FadeOut(formula3, run_time=1, shift=UP), FadeOut(text5, run_time=1, shift=UP),
                  FadeOut(text4, run_time=1, shift=UP), )

        self.set_camera_orientation(phi=90 * DEGREES, theta=90 * DEGREES, gamma=0)

        conductortext = Tex(r'Conductor with a', ' current I')
        conductortext.to_corner(UP)
        conductortext[1].set_color(RED)

        self.add_fixed_in_frame_mobjects(conductortext)

        self.play(Create(conductor), Create(vec), Create(Itext), run_time=3)
        vec1 = Arrow3D(start=np.array([0, 0, 0]), end=np.array([0, 0, 2]), color=RED)
        dot = Dot(color=RED)

        self.move_camera(phi=0, run_time=3)
        self.play(FadeOut(conductortext))
        self.add(circle0)
        self.wait(2)
        self.play(Transform(vec, vec1), run_time=1)
        self.add(dot)
        self.wait()


class SavarFurther(MovingCameraScene):
    def construct(self):
        circle = Circle(color=BLUE, radius=2)
        circle0 = Circle(color=BLUE, radius=0.3, fill_opacity=1)
        dot = Dot(color=RED)
        Itext = Tex(r'$I$').set_color(RED).shift(1.7 * LEFT)
        self.add(Itext, circle0, dot)
        self.wait()
        func = lambda pos: (pos[0] * UP + pos[1] * LEFT) / 3
        func1 = lambda pos: (pos[0] * UP + pos[1] * LEFT) / 3
        a = ArrowVectorField(func)
        atext = Tex('B vector field').to_edge(UP)
        btext = Tex('B continuous vector field').to_edge(UP)
        b = StreamLines(func1)
        self.play(Create(a), Write(atext), run_time=3)
        self.wait(2)
        self.play(Create(circle), run_time=2)
        self.wait(3)

        Btext = Tex(r'$B$').set_color(BLUE).move_to(Itext)
        B = Arrow(2 * LEFT, 2 * LEFT + DOWN, buff=0).set_color(BLUE)

        self.play(FadeIn(Btext, run_time=1, shift=UP), Itext.animate.next_to(circle0, UP), DrawBorderThenFill(B))
        self.wait()
        self.play(Uncreate(a), Create(b), ReplacementTransform(atext, btext), FadeOut(circle), run_time=5)
        self.wait(3)
        self.play(FadeOut(B, Btext, Itext, btext))
        self.wait(1.5)

class SavarTube(ThreeDScene):
    def construct(self):
        conductor = Cylinder(color=GRAY, radius=0.3, height=6, fill_opacity=0.7)
        circle0 = Circle(color=BLUE, radius=0.3, fill_opacity=1)
        dot = Dot(color=RED)

        vec1 = Arrow3D(start=np.array([0, 0, 0]), end=np.array([0, 0, 2]), color=RED)

        func1 = lambda pos: (pos[0] * UP + pos[1] * LEFT) / 3
        b = StreamLines(func1)
        # self.set_camera_orientation(phi=90 * DEGREES, theta=90 * DEGREES, gamma=0)

        self.add(conductor, b, circle0, dot, vec1)
        self.move_camera(phi=45*DEGREES, run_time=3,frame_center=0*RIGHT)
        self.begin_ambient_camera_rotation(0.2)
        self.wait(3.5)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(b))
        self.move_camera(phi=90*DEGREES, run_time=3,frame_center=0*RIGHT)
        self.wait()


class SavarEquations(ThreeDScene):
    def construct(self):

        # self.move_camera(phi=-90*DEGREES, run_time=3,frame_center=0*RIGHT)
        self.set_camera_orientation(phi=90*DEGREES , frame_center=0*LEFT)
        # self.set_camera_orientation(phi=45 * DEGREES, theta=-90 * DEGREES, gamma=0, frame_center=0*RIGHT)

        conductor = Cylinder(color=GRAY, radius=0.3, height=6, fill_opacity=0.7)
        circle0 = Circle(color=BLUE, radius=0.3, fill_opacity=1)
        dot = Dot(color=RED)
        vec1 = Arrow3D(start=np.array([0, 0, 0]), end=np.array([0, 0, 2]), color=RED)
        vecB = Arrow3D(start=np.array([-2, 0, 0]), end=np.array([-2, -1, 0]), color=BLUE)
        vecr = Arrow3D(start=np.array([0, 0, 0]), end=np.array([-2,0 , 0]), color=BLUE)

        contour = Circle(color= GREEN, radius = 2)
        tcontour = CubicBezier([0.8,0,0], [0,3.5,0], [-4,-2 , 0], [0.8,0,0])
        tcontour.set_color(PURPLE)
        tcontour.scale(1.5)
        tcontour.shift(DOWN*0.3)

        self.add(conductor,  circle0, dot, vec1)


        formula1 = MathTex(r'{\displaystyle \vec {B}(\vec{r})', r' = \frac{1}{c}\int_{\text{Circle}} ', r'I',
                           r' \frac{(\vec{r}-\vec{l})\times d\vec{l}}{|(\vec{r}-\vec{l}|)^3} ')
        formula1[0].set_color(BLUE)
        formula1[2].set_color(RED)
        formula1.to_corner(RIGHT+UP)
        formula1.scale(0.8)

        text1 = Tex(r'Integration is made on\\ the green circle contour')
        text1.to_corner(UP+LEFT)
        text1.scale(0.8)

        formula2 = MathTex(r'B(\vec{r})|\vec r|',r'=\frac{2}{c}','I')
        formula2[0].set_color(BLUE)
        formula2[2].set_color(RED)
        formula2.next_to(contour, 2*LEFT)
        formula2.scale(1)

        # self.play(Write(text1), )

        text2 = Tex(r'Using the symmetry of the magnetic field\\we can generalize our result on any contour ')
        text2.scale(0.8)
        text2.to_edge(UP)
        self.add_fixed_in_frame_mobjects(formula1, text1)
        # self.play(Write(formula1 , text1 ))


        self.wait(0.5)

        self.move_camera(phi=15 * DEGREES, theta=-90 * DEGREES, gamma=0 )

        textr = MathTex(r'\vec r').set_color(BLUE)
        textr.next_to(vecr, UP)

        self.play(FadeIn(contour))

        # self.add(contour, tcontour, formula2)
        self.play(TransformMatchingTex(formula1, formula2),
                  Create(vecB), Create(vecr),
                  Write(textr))

        self.wait(1.5)

        self.play(FadeIn(text2), FadeOut(textr,text1, vecr, vecB, shift=DOWN))

        self.wait()

        self.move_camera(phi=0, theta=-90*DEGREES)

        formula3 = MathTex(r'\int_{\text{Purple } \Gamma}',r'\vec B(\vec{r}) ',r'\cdot',r'\vec dr',r'=\frac{4\pi}{c}','I')
        formula3[0].set_color(PURPLE)
        formula3[1].set_color(BLUE)
        formula3[3].set_color(BLUE)
        formula3[5].set_color(RED)
        formula3.next_to(contour,DOWN, buff=SMALL_BUFF)


        self.wait(2)

        self.play(ReplacementTransform(formula2, formula3), ReplacementTransform(contour, tcontour))

        self.wait(3)

        self.play(FadeOut(tcontour, circle0, dot, conductor, text2, vec1))

        formula4 = MathTex(r'\int_{\Gamma}',r'\vec B(\vec{r}) ',r'\cdot',r'\vec{dr}',r'=\frac{4\pi}{c}','I',r'+',r'\int_S \frac{\partial \vec E}{\partial t}\vec{dS}')
        formula4[0].set_color(PURPLE)
        formula4[1].set_color(BLUE)
        formula4[3].set_color(BLUE)
        formula4[5].set_color(RED)
        formula4[0:6].shift(RIGHT)
        formula4[7].set_color(BLUE_D)

        textfinal = Tex(r'This is the Ampère circuital law\\', r'This equation has a mistake concerned with\\',
                                                               r' the law of conservation of charge.\\',
                                                               r' It can be resolved by an additional term called',' displacement current.')
        textfinal.scale(0.8)
        textfinal.to_edge(UP)
        textfinal[4].set_color(BLUE_D)

        self.play(ReplacementTransform(formula3, formula4[0:6]), ReplacementTransform(text2, textfinal[0:3]))
        self.wait(3)

        self.play( formula4[0:6].animate.shift(LEFT),FadeIn(textfinal[3:5]))
        self.wait(2)
        self.play(FadeIn(formula4[5:8] ))

        self.wait(3)

        self.move_camera(phi=90*DEGREES)

        self.wait()