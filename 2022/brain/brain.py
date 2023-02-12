from manim import *
import networkx as nx
from numpy import sign
from numpy.random import rand
from sympy import flatten


class Shapes(Scene):
    def construct(self):
        textintro = Tex('Why are they all curvy and convex?')
        textintro.to_corner(UP)

        nut_text = Tex('Greek nut')
        nut = SVGMobject('/Users/isaigordeev/Desktop/HOBBY/VIDEOS/DRAWINGS FOR'
                         ' MY VIDEOS/2022/brain/greeknut.svg')
        nut.shift(2 * LEFT)
        nut_text.next_to(nut, DOWN)
        nut_upfix = Tex(r'Curvy, convex\\ and delicious..')
        nut_upfix.scale(0.7)
        nut_upfix.next_to(nut, UP * 1.5)
        # nut = VGroup(nut, nut_text)

        finger_text = Tex('Wet finger')
        finger = SVGMobject('/Users/isaigordeev/Desktop/HOBBY/VIDEOS/DRAWINGS FOR'
                            ' MY VIDEOS/2022/brain/wetfinger.svg').scale(0.5)
        finger.next_to(nut, 5 * LEFT)
        finger_text.next_to(finger, DOWN)
        finger_upfix = Tex(r'Curvy, convex\\ and wet..')
        finger_upfix.scale(0.7)
        finger_upfix.next_to(finger, UP * 1.5)
        # finger = VGroup(finger, finger_text)

        brain_text = Tex('Brain')
        brain_upfix = Tex(r'Curvy, convex\\ and smart..')
        brain = SVGMobject('/Users/isaigordeev/Desktop/HOBBY/VIDEOS/DRAWINGS FOR'
                           ' MY VIDEOS/2022/brain/brainstart0.svg').scale(2)
        # brain.next_to(nut, 4*RIGHT)
        brain_text.next_to(brain, DOWN)
        brain_upfix.scale(0.7)
        brain_upfix.next_to(brain, 1.5 * UP)
        # brain = VGroup(brain, brain_text)

        self.play(Create(brain))
        self.wait()
        self.play(FadeIn(brain_upfix))
        # brain = VGroup(brain, brain_upfix)
        self.play(brain.animate.shift(3 * RIGHT),
                  brain_upfix.animate.shift(3 * RIGHT))
        self.wait()

        self.play(Create(nut))
        self.wait()
        self.play(FadeIn(nut_upfix))
        # nut = VGroup(nut, nut_upfix)
        # self.play(nut.animate.shift(3*RIGHT))
        self.wait()

        self.play(Create(finger))
        self.wait()
        self.play(FadeIn(finger_upfix))
        # finger = VGroup(finger, finger_upfix)
        # self.play(finger.animate.shift(3*RIGHT))
        self.wait()

        texts = VGroup(finger_upfix, brain_upfix, nut_upfix)
        objects = VGroup(brain, finger, nut)

        self.play(TransformMatchingTex(texts, textintro), objects.animate.shift(DOWN * 1))

        self.wait()

        text_1 = Tex('Consider the brain')
        text_1.to_corner(UP)

        self.play(nut.animate.shift(10 * LEFT), finger.animate.shift(10 * LEFT), brain.animate.shift(3 * LEFT + UP))
        self.wait()
        self.play(brain.animate.scale(1.2), TransformMatchingTex(textintro, text_1))


class Oldschool(Scene):
    def construct(self):
        text_1 = Tex(r'– It was thought the neurons interacts\\ with each other during the brain growth')
        text_2 = Tex(r'– Biochemical reactions in the neurons')
        text_2.next_to(text_1, 2 * DOWN)

        self.add(text_1, text_2)

        self.play(text_1.animate.set_color(WHITE))
        self.play(text_1.animate.scale(1.1))

        close_rect = Rectangle(fill_color=BLACK, width=10, height=10, fill_opacity=1, color=BLACK)

        # brain =
        brain1 = SVGMobject('/Users/isaigordeev/Desktop/HOBBY/VIDEOS/DRAWINGS '
                            'FOR MY VIDEOS/2022/brain/brain0.svg').scale(1)
        brain2 = SVGMobject('/Users/isaigordeev/Desktop/HOBBY/VIDEOS/DRAWINGS '
                            'FOR MY VIDEOS/2022/brain/brain2.svg').scale(1.5)
        brain3 = SVGMobject('/Users/isaigordeev/Desktop/HOBBY/VIDEOS/DRAWINGS '
                            'FOR MY VIDEOS/2022/brain/brain3.svg').scale(2.5)
        brain4 = SVGMobject('/Users/isaigordeev/Desktop/HOBBY/VIDEOS/DRAWINGS '
                            'FOR MY VIDEOS/2022/brain/brain4.svg').scale(3)
        self.wait(3)
        self.add(close_rect, brain1)

        graphs = [Graph.from_networkx(nx.erdos_renyi_graph(x, 0.1),
                                      layout='circular',
                                      layout_scale=0.1 + x ** 1.2 * 0.04) for x in [2, 3, 7, 10]]

        i = 1
        colors = [PURE_RED, RED, ORANGE, GREEN]
        for graph in graphs:
            for ind, v in enumerate(graph.vertices):
                graph[v].set_color(PURE_BLUE)
            graph[0].set_color(PURE_RED).scale(1.5)
            graph[i].set_color(PURE_RED).scale(1.5)
            if (0, i) not in graph.edges:
                graph.add_edges((0, i))
            graph.edges[0, i].set_color(colors[i - 1])
            graph.edges[0, i].set(stroke_width=5)
            i += 1

        brain1text = Tex('Gestation week – 22').scale(0.75)
        brain1text.next_to(brain1, 1.5 * DOWN)

        brain2text = Tex('Gestation week – 29').scale(0.75)
        brain2text.next_to(brain1, 1.5 * DOWN)

        brain3text = Tex('Gestation week – 40').scale(0.75)
        brain3text.next_to(brain1, 1.5 * DOWN)

        brain4text = Tex('Gestation week – Adult').scale(0.75)
        brain4text.next_to(brain1, 1.5 * DOWN)
        #
        self.play(Create(graphs[0]))

        self.play(ReplacementTransform(brain1,
                                       brain2.move_to(brain1)),
                  ReplacementTransform(brain1text,
                                       brain2text.next_to(brain1text, DOWN)),
                  ReplacementTransform(graphs[0],
                                       graphs[1])
                  )

        self.wait(1.5)

        self.play(ReplacementTransform(brain2text,
                                       brain3text.next_to(brain2text, DOWN)),
                  ReplacementTransform(brain2,
                                       brain3.move_to(brain2)),
                  ReplacementTransform(graphs[1],
                                       graphs[2])
                  )

        self.wait(1.5)

        self.play(ReplacementTransform(brain3text,
                                       brain4text.next_to(brain3text, DOWN)),
                  ReplacementTransform(brain3,
                                       brain4.move_to(brain3)),
                  ReplacementTransform(graphs[2],
                                       graphs[3])
                  )

        self.wait(3)

        text_3 = Tex('But does a greek nut have the neurons?').next_to(text_1, DOWN).set_color(WHITE).scale(0.8)
        nut = SVGMobject('/Users/isaigordeev/Desktop/HOBBY/VIDEOS/DRAWINGS FOR MY VIDEOS/2022/brain/greeknut.svg')
        nut.next_to(text_1, UP * 1.5)
        text_2.shift(DOWN)

        self.remove(graphs[3], brain4, close_rect, brain4text)
        self.add(text_3, nut)
        self.wait(2)
        self.play(text_3.animate(rate_func=there_and_back, run_time=3).scale(1.3), Wiggle(nut, run_time=3))

        self.wait(2)

        self.play(text_1.animate.set_color(WHITE), (text_2.animate.set_color(WHITE)))
        self.play(text_1.animate.scale(1 / 1.1), (text_2.animate.scale(1.1)))
        self.wait()

        self.play(FadeOut(text_1, text_3, nut, shift=UP), text_2.animate.move_to(ORIGIN))
        self.wait()

        close_rect = Rectangle(fill_color=BLACK, width=10, height=10, fill_opacity=1, color=BLACK)

        brain1 = SVGMobject('/Users/isaigordeev/Desktop/HOBBY/VIDEOS/DRAWINGS '
                            'FOR MY VIDEOS/2022/brain/brain0.svg').scale(1)
        brain2 = SVGMobject('/Users/isaigordeev/Desktop/HOBBY/VIDEOS/DRAWINGS '
                            'FOR MY VIDEOS/2022/brain/brain2.svg').scale(1.5)
        brain3 = SVGMobject('/Users/isaigordeev/Desktop/HOBBY/VIDEOS/DRAWINGS '
                            'FOR MY VIDEOS/2022/brain/brain3.svg').scale(2.5)
        brain4 = SVGMobject('/Users/isaigordeev/Desktop/HOBBY/VIDEOS/DRAWINGS '
                            'FOR MY VIDEOS/2022/brain/brain4.svg').scale(3)

        self.add(close_rect, brain1)

        graphs = [Graph.from_networkx(nx.erdos_renyi_graph(x, 0.1),
                                      layout='kamada_kawai',
                                      layout_scale=0.1 + x ** 1.2 * 0.04) for x in [2, 3, 7, 14]]

        for graph in graphs:
            for indv in graph:
                indv.set_color(random_bright_color())

        brain1text = Tex('Gestation week – 22').scale(0.75)
        brain1text.next_to(brain1, 1.5 * DOWN)

        brain2text = Tex('Gestation week – 29').scale(0.75)
        brain2text.next_to(brain1, 1.5 * DOWN)

        brain3text = Tex('Gestation week – 40').scale(0.75)
        brain3text.next_to(brain1, 1.5 * DOWN)

        brain4text = Tex('Gestation week – Adult').scale(0.75)
        brain4text.next_to(brain1, 1.5 * DOWN)
        #
        self.play(Create(graphs[0]))

        self.play(ReplacementTransform(brain1,
                                       brain2.move_to(brain1)),
                  ReplacementTransform(brain1text,
                                       brain2text.next_to(brain1text, DOWN)),
                  ReplacementTransform(graphs[0],
                                       graphs[1])
                  )

        self.wait(1.5)

        self.play(ReplacementTransform(brain2text,
                                       brain3text.next_to(brain2text, DOWN)),
                  ReplacementTransform(brain2,
                                       brain3.move_to(brain2)),
                  ReplacementTransform(graphs[1],
                                       graphs[2])
                  )

        self.wait(1.5)

        self.play(ReplacementTransform(brain3text,
                                       brain4text.next_to(brain3text, DOWN)),
                  ReplacementTransform(brain3,
                                       brain4.move_to(brain3)),
                  ReplacementTransform(graphs[2],
                                       graphs[3])
                  )

        self.wait(3)

        text_4 = Tex('Water chemically reacts with fingers?').next_to(text_2, DOWN).set_color(WHITE).scale(0.8)
        finger = SVGMobject('/Users/isaigordeev/Desktop/HOBBY/VIDEOS/DRAWINGS FOR MY VIDEOS/2022/brain/wetfinger.svg')
        finger.next_to(text_1, UP * 1.5)

        self.remove(graphs[3], brain4, close_rect, text_3, brain4text)
        self.add(text_4, finger)
        self.wait(2)
        self.play(text_4.animate(rate_func=there_and_back, run_time=3).scale(1.3), Wiggle(finger, run_time=3))

        self.wait(2)


class ReflexiaNotWorkingHypotheses(MovingCameraScene):
    def construct(self):
        ASPECT_RATIO = 16.0 / 9
        FRAME_HEIGHT = 8.0
        FRAME_WIDTH = FRAME_HEIGHT * ASPECT_RATIO

        size_factor = 2.3

        self.camera.background_color = DARKER_GRAY

        background = Rectangle(
            width=FRAME_WIDTH,
            height=FRAME_HEIGHT,
            fill_color=BLACK,
            stroke_opacity=0,
            fill_opacity=1)

        surrounding = SurroundingRectangle(background,
                                           stroke_width=DEFAULT_STROKE_WIDTH * 1.5,
                                           color=WHITE)

        self.add(background, surrounding)

        title = Title('Actually, there are three main hypotheses.')
        text = Tex(r'Two of them did not find an experimental\\ and a '
                   r'theoretical approvement. Take a closer look on them.\\ A wondering thing '
                   r'is that the third the most\\ promising hypothesis was presented 7 years ago.')
        self.add(title, text)

        TEXT = Tex(r'And what about new hypotheses?').next_to(surrounding, 2 * size_factor * DOWN).scale(size_factor)

        self.add(TEXT)

        # sad = SVGMobject(
        #     '/Users/isaigordeev/Desktop/HOBBY/VIDEOS/DRAWINGS FOR MY VIDEOS/miscellaneous/stone_sad.svg').scale(1.5)
        # sad.next_to(TEXT, 2 * LEFT).shift(3*DOWN)

        cur = SVGMobject(
            '/Users/isaigordeev/Desktop/HOBBY/VIDEOS/DRAWINGS FOR MY VIDEOS/miscellaneous/stone_misunderstanding.svg').scale(
            3)
        cur.next_to(TEXT, 0.1 * RIGHT).shift(3 * DOWN)

        # mis = SVGMobject(
        #     '/Users/isaigordeev/Desktop/HOBBY/VIDEOS/DRAWINGS FOR MY VIDEOS/miscellaneous/stone_misunderstanding.svg').scale(
        #     2)
        # mis.next_to(cur, 3 * RIGHT)

        self.add(cur)

        (self.camera.frame.set(width=FRAME_WIDTH * size_factor, run_time=6).shift(
            (size_factor + 4.5 * abs(1.5 - size_factor) / (size_factor)) * DOWN))

        self.wait(4)


class Newschool(MovingCameraScene):
    def construct(self):
        label = Tex(r'nature\\', 'physics').to_edge(UP).shift(4.4 * LEFT + 0.25 * UP)
        label[1].scale(1.15)
        label_right = Tex('LETTERS').to_edge(UP).shift(4.2 * RIGHT)
        under_label = Tex('PUBLISHED ONLINE: 1 FEBRUARY 2016', 'DOI: 10.1038/NPHYS3622').scale(0.45)
        under_label[1].next_to(label_right, DOWN)
        under_label[0].next_to(under_label[1], LEFT).shift(0.02 * UP)

        title = Tex('On the growth and form of cortical convolutions').shift(2 * UP)
        rect = Line(6 * LEFT, 5.5 * RIGHT).next_to(title, UP)

        authors = Tex(r'Tuomas Tallinen, Jun Young Chung, François Rousseau,'
                      r' Nadine Girard, Julien Lefèvre and L. Mahadevan').scale(0.6).next_to(title, DOWN * 1.5)

        abstract = Tex(r'The rapid growth of the human cortex during development is\\'
                       r' accompanied by the folding of the brain into a highly convoluted\\'
                       r' structure1–3. Recent studies have focused on the genetic and\\'
                       r' cellular regulation of cortical growth4–8, but understanding\\'
                       r' the formation of the gyral and sulcal convolutions also\\'
                       r' requires consideration of the geometry and physical shaping\\'
                       r' of the growing brain9–15. To study this, we use magnetic\\'
                       r' resonance images to build a 3D-printed layered gel '
                       r'mimic\\').set(width=5.5).next_to(authors, DOWN).shift(2.5 * LEFT)

        abstract1 = Tex(r'of the developing smooth fetal brain; when immersed in a\\'
                        r', solvent, the outer layer swells relative to the core, mimicking\\'
                        r' cortical growth. This relative growth puts the outer layer\\'
                        r' into mechanical compression and leads to sulci and gyri similar to\\'
                        r' those in fetal brains. Starting with the same initial geometry,\\'
                        r' we also build numerical simulations of the brain modelled\\'
                        r' as a soft tissue with a growing cortex, and show that this\\'
                        r' also produces the characteristic patterns of convolutions over\\'
                        r' a realistic developmental course. All together, our results\\'
                        r' show that although many molecular determinants control the\\'
                        r' tangential expansion of the cortex, the size, shape, placement\\'
                        r' and orientation of the folds arise through iterations and\\'
                        r' variations of an elementary mechanical instability modulated\\'
                        r' by early fetal brain geometry.').set(width=5.5).next_to(abstract, 0.5 * DOWN)

        text1 = Tex(r'of axonal tension driving gyrification10 . At present, the most\\'
                    r' likely hypothesis is also the simplest one: tangential expansion\\'
                    r' of the cortical layer relative to sublayers generates compressive\\'
                    r' stress, leading to the mechanical folding of the cortex9–15,22–25. This\\'
                    r' mechanical folding model produces realistic sizes and shapes of\\'
                    r' gyral and sulcal patterns15 that are presumably modulated by brain\\'
                    r' geometry26, but the hypothesis has not been tested before with real\\'
                    r' three-dimensional (3D) fetal brain geometries in'
                    r' a developmental').set(width=5.5).next_to(abstract, RIGHT)

        text2 = Tex(r'setting. Here we substantiate and quantify this notion using both\\'
                    r' physical and numerical models of the brain, guided by the use of\\'
                    r' 3D magnetic resonance images (MRI) of a smooth fetal brain as a\\'
                    r'starting point.\\'
                    r'We construct a physical simulacrum of brain folding by\\'
                    r' taking advantage of the observation that soft physical gels swell\\'
                    r' superficially when immersed in solvents. This swelling relative to\\'
                    r' the interior puts the outer layers of the gel into compression, yielding\\'
                    r' surface folding patterns qualitatively similar to sulci and gyri15. An\\'
                    r' MRI image of a smooth fetal brain at gestational week (GW) 22\\'
                    r' (Fig. 1b; see Supplementary Methods) serves as a template for a\\'
                    r' 3D-printed cast of the brain. A mould of this form allows us to\\'
                    r' create a gel-brain (mimicking the white matter) that is then coated\\'
                    r' with a thin layer of elastomer gel (mimicking the cortical grey').set(width=5.5).next_to(text1,
                                                                                                                0.5 * DOWN)

        self.add(label, label_right, under_label, authors, title, rect, abstract, abstract1, text2, text1, )

        picture = SVGMobject('/Users/isaigordeev/Desktop/HOBBY/VIDEOS/DRAWINGS '
                             'FOR MY VIDEOS/2022/brain/article.svg').set_color(WHITE).scale(3).shift(8 * DOWN)

        self.add(label, label_right, under_label, authors, title, rect, picture)

        self.wait()

        self.play(self.camera.frame.animate.move_to(picture), run_time=20)

        self.wait()


class ReflexiaNewHypothesis(MovingCameraScene):
    def construct(self):
        ASPECT_RATIO = 16.0 / 9
        FRAME_HEIGHT = 8.0
        FRAME_WIDTH = FRAME_HEIGHT * ASPECT_RATIO

        self.camera.background_color = DARKER_GRAY

        background = Rectangle(
            width=FRAME_WIDTH,
            height=FRAME_HEIGHT,
            fill_color=BLACK,
            stroke_opacity=0,
            fill_opacity=1)

        surrounding = SurroundingRectangle(background,
                                           stroke_width=DEFAULT_STROKE_WIDTH * 1.5,
                                           color=WHITE)

        self.add(background, surrounding)

        # reflexia scene

        text_1 = Tex(r'– It was thought the neurons interacts\\'
                     r' with each other during the brain growth').set_color(YELLOW_B)
        text_2 = Tex(r'– Biochemical reactions in the neurons').set_color(YELLOW_B)
        text_2.next_to(text_1, 2 * DOWN)

        text_3 = Tex('But does a greek nut have the neurons?').next_to(text_1, DOWN).set_color(WHITE).scale(0.8)
        nut = SVGMobject('/Users/isaigordeev/Desktop/HOBBY/VIDEOS/DRAWINGS FOR MY VIDEOS/2022/brain/greeknut.svg')
        nut.next_to(text_1, UP * 1.5).shift(2 * LEFT)
        text_2.shift(DOWN)

        text_4 = Tex('Water chemically reacts with fingers?').next_to(text_2, DOWN).set_color(WHITE).scale(0.8)
        finger = SVGMobject('/Users/isaigordeev/Desktop/HOBBY/VIDEOS/DRAWINGS FOR MY VIDEOS/2022/brain/wetfinger.svg')
        finger.next_to(nut, RIGHT * 6)

        self.add(text_1, text_2)
        self.add(text_3, nut)
        self.add(text_4, finger)

        TEXT = Tex(r'So, here is the third hypothesis – '
                   r'biomechanical\\How it matches with experimental facts?').next_to(surrounding, 3 * DOWN).scale(1.5)
        TEXT.set_color(WHITE)  # blue c is very good

        self.add(TEXT)

        self.wait(2)

        self.play(self.camera.frame.animate.set(width=FRAME_WIDTH * 1.5, run_time=6).shift(DOWN))  # reflexia scene

        bio = SVGMobject(
            '/Users/isaigordeev/Desktop/HOBBY/VIDEOS/DRAWINGS FOR MY VIDEOS/2022/brain/biomechanics.svg').set_color(
            WHITE)
        bio.next_to(finger, 0.3 * RIGHT)

        text_5 = Tex('– Biomechanical growth of tissues').set_color(YELLOW_B).move_to(text_4).shift(0.25 * DOWN)

        self.wait(4)
        self.play((Group(text_2, text_4).animate.shift(0.5 * UP)),
                  nut.animate.shift(LEFT),
                  finger.animate.shift(1.3 * LEFT),
                  FadeIn(bio, shift=LEFT),
                  FadeIn(text_5, shift=UP))

        self.wait(4)


class IntuitionScene1(Scene):

    def lines(self, leng):
        rect_fast = Line(LEFT * leng * PI / 2, RIGHT * leng * PI / 2).shift(2 * UP)
        init = rect_fast.get_center()

        rect_slow = Line(LEFT * leng * PI / 2, RIGHT * leng * PI / 2).shift(UP)

        return VGroup(rect_slow, rect_fast)

    def border_lines(self, rect_slow, rect_fast):
        line_r = Line(rect_slow.get_right(), rect_fast.get_right())
        line_l = Line(rect_slow.get_left(), rect_fast.get_left())

        line_r.add_updater(lambda line_r: line_r.become(Line(rect_slow.get_right(), rect_fast.get_right())))
        line_l.add_updater(lambda line_l: line_l.become(Line(rect_slow.get_left(), rect_fast.get_left())))

        return line_r, line_l

    def construct(self):
        # attempt on the real analysis – ne och = debil prosto ne otnormiroval
        # angle = 0.3
        # rect_fast = Line(LEFT*angle*PI/2, RIGHT*angle*PI/2).shift(UP)
        # rect_slow = Line(LEFT*angle*PI/2, RIGHT*angle*PI/2).shift(UP*0.8)
        #
        # init_pos = rect_fast.get_center()
        # rect_fast.add_updater(lambda rect_fast: rect_fast.move_to(init_pos) )
        # self.add(rect_fast)
        #
        #
        # def func(pos):
        #     if pos[0] < angle*PI:
        #         return [pos[1] * np.sin(pos[0]),pos[1]* np.cos(pos[0]), 0]
        #     else:
        #         return pos
        #
        # self.play(rect_fast.animate.apply_function(func), rect_slow.animate.apply_function(func))

        plane = NumberPlane()
        self.add(plane)

        circle1 = Circle(1)
        circle2 = Circle(2)

        leng = 0.5

        # rect_fast = Line(LEFT * leng * PI / 2, RIGHT * leng * PI / 2).shift(2*UP)
        # init = rect_fast.get_center()
        #
        # rect_slow = Line(LEFT * leng * PI / 2, RIGHT * leng * PI / 2).shift( UP)
        #
        # line_r = Line(rect_slow.get_right(), rect_fast.get_right())
        # line_l = Line(rect_slow.get_left(), rect_fast.get_left())
        #
        # line_r.add_updater(lambda line_r: line_r.become(Line(rect_slow.get_right(), rect_fast.get_right())))
        # line_l.add_updater(lambda line_l: line_l.become(Line(rect_slow.get_left(), rect_fast.get_left())))
        #
        # self.play(rect_fast.animate.apply_complex_function(lambda z: np.exp(complex(np.log(2),
        #                                                                     -z.real-z.real/abs(z.real)*angle_fast*PI/2)
        #                                                                     +complex(0, 1) * PI / 2
        #                                                    )),
        #           rect_slow.animate.apply_complex_function(lambda z: np.exp(complex(np.log(1), -z.real)
        #                                                                     + complex(0, 1) * PI / 2
        #                                                                     ))
        #           )

        text = Tex('Relative angular velocity of growth')
        text1 = Tex('0.1')
        text2 = Tex('0.2')
        text3 = Tex('0.3')
        n = 3
        num = n

        angle_fast = [x for x in np.arange(0.1, 0.4, 0.3 / num)]
        angle_fast[0] = 0

        lines = [self.lines(0.4) for x in range(n)]

        lines = VGroup(*lines).arrange(buff=2 * LARGE_BUFF).shift(UP)

        text1.next_to(lines[0][0], 1.5 * DOWN)
        text2.next_to(lines[1][0], 1.5 * DOWN)
        text3.next_to(lines[2][0], 1.5 * DOWN)

        text.to_edge(UP)
        self.add(text1, text2, text3, text)

        border_lines = [self.border_lines(lines[x][0], lines[x][1]) for x in range(n)]
        for x in border_lines:
            self.add(*x)

        # def fast_grow(z):

        self.play(*[AnimationGroup(
            lines[n][0].animate.apply_complex_function(
                lambda z: np.exp(complex(np.log(lines[n][0].get_y()), -z.real + lines[n][0].get_x() + PI / 2))
                          + complex(lines[n][0].get_x())),
            lines[n][1].animate.apply_complex_function(
                lambda z: np.exp(complex(np.log(lines[n][1].get_y()), -z.real + lines[n][1].get_x() +
                                         PI / 2 * (1 - sign(z.real - lines[n][0].get_x()) * angle_fast[n])))
                          + complex(lines[n][1].get_x(), 0)))

            for n in range(num)], run_time=10)

        self.wait(2)

        giri = [self.lines(0.6) for x in range(1)]

        giri = VGroup(*giri).arrange(buff=2 * LARGE_BUFF).shift(UP)

        text1.next_to(giri[0][0], 1.5 * DOWN)

        text.to_edge(UP)
        self.add(text1, text2, text3, text)

        border_giri = [self.border_lines(giri[x][0], giri[x][1]) for x in range(1)]


class Premise(Scene):
    def construct(self):
        layer = Rectangle(height=1, width=3)
        self.play(layer.animate.set(width=5))

# class ModelBasements(Scene):
#     def construct(self):
