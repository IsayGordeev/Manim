from abc import ABC

from manim import *


class trajectory(VGroup):
    def __init__(self, alpha, start, color, g, v, STEP=20, run_time=0.01, **kwargs):
        super().__init__(**kwargs)

        self.dot = Dot(start)
        self.path = VMobject()
        self.vel0 = [v * np.cos(alpha), v * np.sin(alpha), 0]
        self.vel00 = self.vel0
        self.disp = [0, 0, 0]
        self.last_pos0 = start
        self.start = start
        self.STEP = STEP
        self.v = v
        self.g = g
        self.alpha = alpha
        self.run_rime = run_time
        self.velocityvector0 = Arrow(self.last_pos0, self.last_pos0 + self.vel0, buff=2)
        self.velocity = Line((ORIGIN + start), self.vel0 + start, buff=2)

        self.length = Line((self.start), self.dot.get_x() + self.start, buff=2)
        self.brlen = Brace(self.length)
        self.brlentext = self.brlen.get_text('L')

        self.velocityinit = Line(ORIGIN + start, self.vel00 + start, buff=2)
        self.gt = Line(ORIGIN + start,
                                       [v * np.sin(alpha), v * np.sin(alpha) - g * (0.1), 0] + self.start,
                                       buff=2)
        self.gttext = Tex('$\\vec gt$').scale(0.3).move_to(self.gt.get_center() + RIGHT * 10)
        self.votext = Tex('$\\vec v_0$').scale(0.3).move_to(self.velocityinit.get_center() + UP * 0.1)
        self.vtext = Tex('$\\vec v$').scale(0.3).move_to(self.velocity.get_center() - 0.15 * UP)
        self.dot.set_color(color)
        self.t = ValueTracker(0)

    def update_path(self, path):
        previous_path = path.copy()
        previous_path.add_points_as_corners([self.dot.get_center()])
        path.become(previous_path)

    def define_path(self):
        self.path.set_points_as_corners([self.dot.get_center(), self.dot.get_center()])
        self.path.add_updater(self.update_path)

    def text_and_vectors(self):
        self.velocity.add_updater(
            lambda z: z.become(Line(ORIGIN + self.start, self.vel0 + self.start).set_color(LIGHT_BROWN)))
        self.velocityvector0.add_updater(
            lambda z: z.become(Arrow(self.last_pos0, self.last_pos0 + self.vel0, buff=2).set_color(RED)))
        self.velocityinit.add_updater(
            lambda z: z.become(Line(ORIGIN + self.start, self.vel00 + self.start).set_color(YELLOW)))
        self.gt.add_updater(
            lambda z: z.become(Line(self.vel00 + self.start, self.vel0 + self.start, buff=2).set_color(PURPLE)))
        self.brlen.add_updater(lambda z: z.become(
            Brace(Line((ORIGIN + 6 * LEFT) + 2 * DOWN, 2 * DOWN + ORIGIN + [self.dot.get_x(), 0, 0], buff=2))))
        self.brlentext.add_updater(lambda z: z.become(self.brlen.get_text('L')))

        self.vtext.add_updater(
            lambda z: z.become(Tex('$\\vec {v}$').scale(0.3).move_to(self.velocity.get_center() - 0.15 * UP)))

        self.gttext.add_updater(
            lambda z: z.become(
                Tex('$\\vec {g}t$').scale(0.3).move_to(self.gt.get_center() + RIGHT * 0.1)))
        self.dot.add_updater(lambda x: x.move_to([self.t.get_value(), self.func(self.t.get_value()), 0] + self.start))

    def moving(self):
        for x in np.arange(0, self.STEP, 0.1):
            self.last_pos0 = self.dot.get_center()
            if self.dot.get_y() > -1.9:
                self.vel0 = [self.v * np.sin(self.alpha), self.v * np.sin(self.alpha) - self.g * (x), 0]
                self.play(self.dot.animate(run_time=0.01).shift(self.vel0))
            else:
                break

    def add_text(self):
        self.play(Write(self.vtext), Write(self.votext), Write(self.gttext))

    def add_vectors(self):
        return self.velocityvector0, self.path, self.velocity, self.gt, self.velocityinit

    def func(self, x):
        return x * np.tan(self.alpha) - (self.g * x ** 2 * (1 + np.tan(self.alpha) ** 2)) / (2 * self.v ** 2)


class triangle(ZoomedScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.3,
            zoomed_display_height=5,
            zoomed_display_width=3.5,
            image_frame_stroke_width=20,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
            },
            **kwargs
        )

    def construct(self):

        text = Tex(
            'What are the optimal conditions($v$, $\\alpha$) for stone needed to reach the maximim lenght L?').scale(
            0.7)
        text.move_to(3 * UP)
        self.play(Write(text, run_time=2))
        formula = MathTex(
            '\\begin{cases}\\vec s = \\vec s_0 + \\vec v t + \\frac {\\vec g}{2}t^2 \\\\ \\vec v = \\vec v_0 +\\vec g t\\end{cases}')
        formula.to_corner(UP + LEFT)
        self.play(ReplacementTransform(text, formula, run_time=4))
        v = 0.65
        g = 0.2
        l = 3
        h = 2
        start = 3 * LEFT + 2 * DOWN
        dot3 = trajectory(PI / 3, start + l * LEFT + h * UP, GREEN, g, v)
        dot2 = trajectory(0, start + l * LEFT + h * UP, BLUE, g, v)
        dot1 = trajectory(np.arctan(v / (np.sqrt(v * v + 2 * g * 2))), start + l * LEFT + h * UP, RED, g, v)
        dot1.path.set_color(RED)
        dot2.path.set_color(BLUE)
        dot3.path.set_color(GREEN)

        # zoom
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame

        frame.move_to(start + l * LEFT + h * UP + 0.3 * RIGHT + 0.3 * DOWN)
        frame.set_color(PURPLE)
        zoomed_display_frame.set_color(RED)
        zoomed_display.shift(DOWN)

        zoomed_camera_text = Text("Vector velocity triangle").scale(0.7)
        zoomed_camera_text.next_to(zoomed_display_frame, UP)
        zoomed_camera_text.shift(0.2 * LEFT)

        zd_rect = BackgroundRectangle(zoomed_display, fill_opacity=0, buff=MED_SMALL_BUFF)
        self.add_foreground_mobject(zd_rect)

        unfold_camera = UpdateFromFunc(zd_rect, lambda rect: rect.replace(zoomed_display))

        surface = [Line(start + l * LEFT, start + l * LEFT + h * UP), Line(3 * RIGHT + start, start + l * LEFT), Line
        (start + l * LEFT + h * UP, start + l * LEFT + h * UP + LEFT)]
        brheight = Brace(surface[0], direction=surface[0].copy().rotate(PI / 2).get_unit_vector())
        brheighttext = brheight.get_text('h')

        dot1.text_and_vectors()
        dot2.text_and_vectors()
        dot3.text_and_vectors()

        self.play(Create(surface[0]))
        self.play(Create(surface[1]))
        self.play(Create(surface[2]))
        self.play(TransformFromCopy(formula, dot1.votext, run_time=2),
                  TransformFromCopy(formula, dot1.vtext, run_time=2),
                  TransformFromCopy(formula, dot1.gttext, run_time=2),
                  TransformFromCopy(formula, brheighttext, run_time=2))

        self.add(dot1.votext, dot1.vtext, dot1.gttext, dot1.dot, dot2.dot, dot3.dot,
                 )
        self.add(brheight, dot1.brlen, dot1.brlentext)
        self.add(dot1.path)
        dot1.define_path()
        self.add(dot2.path)
        dot2.define_path()
        self.add(dot3.path)
        dot3.define_path()

        self.play(Create(frame))
        self.activate_zooming()
        self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera, run_time=2)
        self.add(*dot1.add_vectors())
        self.wait(2)

        for x in np.arange(0, 5.6, 0.1):
            dot1.last_pos0 = dot1.dot.get_center()
            if dot1.func(x) > -2.1:
                dot1.vel0 = [(dot1.v * np.cos(dot1.alpha)),
                             (dot1.v * np.sin(dot1.alpha) - dot1.g * (x) / (dot1.v * np.cos(dot1.alpha))), 0]
                self.play(dot1.t.animate(run_time=0.03).set_value(x))
            if dot2.func(x) > -2:
                self.play(dot2.t.animate(run_time=0.03).set_value(x))
            if dot3.func(x) > -2.2:
                self.play(dot3.t.animate(run_time=0.03).set_value(x))
        self.wait(2)

        self.play(FadeOut(zoomed_camera_text))
        self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera, rate_func=lambda t: smooth(1 - t),
                  run_time=2)
        self.play(Uncreate(zoomed_display_frame), FadeOut(frame), run_time=2)
        self.wait(1.5)

        text2 = Tex(
            ' Is the red trajectory optimal? $\\newline$ We clearly see, that the greater angle  doesn\'t satisfy the maximum $L$.').scale(
            0.7)
        text2.shift(RIGHT + 1.7 * UP)
        self.play(Indicate(dot1.path, run_time=2), Write(text2, run_time=2))
        self.wait(2.5)
        self.remove(brheight, dot1.brlen)
        self.play(
            Unwrite(dot1.vtext, run_time=2),
            Unwrite(dot1.votext, run_time=2),
            Unwrite(dot1.gttext, run_time=2),
            Uncreate(dot1.velocityvector0),
            Uncreate(dot1.velocityinit),
            Uncreate(dot1.velocity),
            Uncreate(dot1.gt),
            Uncreate(dot1.path),
            Uncreate(dot2.path),
            Uncreate(dot3.path),
            Uncreate(dot1.dot),
            Uncreate(dot2.dot),
            Uncreate(dot3.dot),

            Uncreate(surface[0]),
            Uncreate(surface[1]),
            Uncreate(surface[2]),

            Uncreate(dot1.brlentext),
            Uncreate(brheighttext),
        )
        self.remove(dot1.vtext, dot1.gttext)
        self.play(FadeOut(text2), FadeOut(formula))
        self.wait()



class vectors(VGroup):
    def __init__(self, start, v, g, alpha, **kwargs):
        super().__init__( **kwargs)
        self.v = v
        self.g = g
        self.alpha = alpha
        self.start = start
        self.vel0 = [v * np.cos(alpha), abs(v * np.sin(alpha)), 0]
        self.vel00 = self.vel0
        self.vel0 = [v * np.cos(alpha), abs(v * np.sin(alpha))- self.g*2, 0]

        self.velocity = Line(self.start, self.vel0 + self.start, buff=2).set_color(LIGHT_BROWN)

        self.velocityinit = Line(self.start, self.vel00 + self.start, buff=2).set_color(YELLOW)
        self.gt = Line(self.start + self.vel00,self.start + self.vel0,
                                       buff=2).set_color(PURPLE)

        self.gttext = Tex('$\\vec gt$').move_to(self.gt.get_center() + RIGHT * 0.3)
        self.votext = Tex('$\\vec v_0$').move_to(self.velocityinit.get_center() + UP * 0.5)
        self.vtext = Tex('$\\vec v$').move_to(self.velocity.get_center()-UP*0.3)

        self.t = ValueTracker(2)
        
    def update0(self):
        self.velocityinit.add_updater(
            lambda z: z.become(Line(self.start, self.vel00 + self.start).set_color(YELLOW)))

        self.velocity.add_updater(
            lambda z: z.become(Line(self.start, self.vel0 + self.start).set_color(LIGHT_BROWN)))

        # self.gt.add_updater(
        #     lambda z: z.become(Line(self.start + self.vel00,self.start + self.vel0, buff=2).set_color(PURPLE)))
        # self.gt.add_updater(
        #     lambda z: z.become(Line(self.velocity.get_end(),self.velocityinit.get_end(), buff=2).set_color(PURPLE)))
        self.gt.add_updater(
            lambda z: z.become(Line(self.start + self.vel0, self.start +[self.v * np.cos(self.alpha), self.v *abs( np.sin(self.alpha)), 0], buff=2).set_color(PURPLE)))

        self.vtext.add_updater(
            lambda z: z.become(Tex('$\\vec {v}$').move_to(self.velocity.get_center()-UP*0.3 )))

        self.gttext.add_updater(
            lambda z: z.become(
                Tex('$\\vec {g}t$').move_to(self.gt.get_center() + RIGHT * 0.3)))





        
        
    





class triangle_trig(Scene):
    def construct(self):
        start = 6.5*LEFT+1.6*UP
        trig = vectors(start, 3,0.5, PI/6)
        self.intro_words()
        self.vec_create(trig, start)


    def intro_words(self):
        text1 = Tex('Yes, it is. Just because I know the solution)')
        text2 = Tex('But, let\'s find out, how I determined this trajectory.')
        text3 = Tex('Consider our vector triangle attentively')
        formula = MathTex('\\vec v = \\vec v_0 +\\vec g t')
        formula.to_corner(UP+LEFT)
        text1.shift(2 * UP)
        text2.shift(1.4 * UP)
        self.play(Write(text1))
        self.play(Write(text2))
        self.play( FadeOut(text1,run_time=2),FadeOut(text2, run_time=2))
        self.play(ShowCreationThenFadeOut(text3,run_time=2))
        self.play(ShowCreationThenFadeOut(formula,run_time=2))

    def vec_create(self,trig, start):
        self.play(Create(trig.velocityinit),Create(trig.velocity),Create( trig.gt))
        print(trig.velocity.get_center(),trig.velocityinit.get_center() )
        self.play(Write(trig.vtext),
                  Write(trig.gttext),
                  Write(trig.votext))
        trig.update0()
        self.play(trig.t.animate.set_value(2))


        a = Angle( trig.velocity,trig.velocityinit, 0.5)
        atex = MathTex(r"\beta").move_to(
            Angle(
                 trig.velocity, trig.velocityinit,radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )
        a.add_updater(
            lambda x: x.become(Angle( trig.velocity,trig.velocityinit, radius=0.5, other_angle=False))
        )
        atex.add_updater(
            lambda x: x.move_to(
                Angle(
                    trig.velocity, trig.velocityinit, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
                ).point_from_proportion(0.5)
            )
        )

        self.play(Create(a), Write(atex))

        for x in np.arange(2,7.5,0.2):
            trig.vel0 = [trig.v * np.cos(trig.alpha), trig.v * np.sin(trig.alpha) - trig.g * trig.t.get_value(), 0]
            self.play(trig.t.animate(run_time=0.05).set_value(x))
        # for x in np.arange(7.5, 6, -0.5):
        #     trig.vel0 = [trig.v * np.cos(trig.alpha), trig.v * np.sin(trig.alpha) - trig.g * trig.t.get_value(), 0]
        #     self.play(trig.t.animate(run_time=0.05).set_value(x))
        self.play(atex.animate.shift(0.5*DOWN))


        def scal(a, b):
            s= 0
            for x in range(3):
                s+= (a.get_end()-a.get_start())[x]*(b.get_end()-b.get_start())[x]
            return s
        h = (np.linalg.norm(trig.velocityinit.get_end()-trig.velocityinit.get_start())) * (np.linalg.norm(trig.velocity.get_end()-trig.velocity.get_start())) * np.sin(
            np.arccos(scal(trig.velocity,trig.velocityinit) / ((np.linalg.norm(trig.velocityinit.get_end()-trig.velocityinit.get_start())) * (np.linalg.norm(trig.velocity.get_end()-trig.velocity.get_start())))))/(np.linalg.norm(trig.gt.get_end()-trig.gt.get_start()))
        height = DashedLine(start,start+[h,0,0])
        htext = Tex('h').move_to(height.get_end()-0.3*UP-0.3*RIGHT)

        b = Angle(height, trig.velocityinit, 1.25)
        btex = MathTex(r"\alpha").move_to(
            Angle(
                 height, trig.velocityinit,radius=1.25 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )
        qw = Line([-6.5,  1.6,  0. ], [-3.90192379, -3.65 ,       0.        ])
        qw1 = Line([-6.5, 1.6, 0.], [-3.90192379, 3.1, 0.])
        ar = RightAngle(qw, qw1)

        self.play(Create(height, run_time=2), Write(htext, run_time=2), Write(b, run_time=2), Write(btex, run_time=2))

        text1 = Tex('Area of this triangle can be written in two ways').scale(0.8)
        text1.shift(2*RIGHT+3*UP)
        self.play(Write(text1, run_time=2))
        formula1 = MathTex(r'\frac{1}{2}',r'v_0 v \sin{\beta} =' ,r'\frac{1}{2}\overbrace{v_0\cos\alpha}^h g','t')
        formula1.shift(2*RIGHT+2*UP)
        self.play(Write(formula1, run_time=2))
        formula2 = MathTex(r'v_0 v \sin{\beta} =', r'v_0\cos\alpha ','g', 't')
        formula2.shift(2*RIGHT+0.75*UP)
        formula2[1].set_color(RED)
        formula2[3].set_color(RED)
        formula3 = MathTex(r'v_0 v \sin{\beta} =', r'L','g')
        formula3.shift(2*RIGHT)
        formula3[1].set_color(RED)
        formula3.shift(0.7*LEFT)
        self.play(TransformFromCopy(formula1,formula2, run_time=2))
        self.play(TransformFromCopy(formula2,formula3, run_time=2))
        self.play(Indicate(formula2[1],run_time=2),Indicate(formula2[3], run_time=2))

        formula4 = MathTex(r'\frac{v_0 v }{g}\sin{\beta} = L').scale(1.5)
        formula4.shift(2*RIGHT+0.75*UP)
        text2 = Tex(r'Maximum $L$ satisfies $\sin\beta = 1$, so initial and terminate velocities must be orthogonal').scale(0.7)
        text2.shift(0.5*RIGHT+3.2*UP)

        self.wait()

        self.remove(trig.gttext)
        self.play(ReplacementTransform(formula1, formula4, run_time=3),ReplacementTransform(formula2, formula4, run_time=3),ReplacementTransform(formula3, formula4, run_time=3), ReplacementTransform(text1,text2, run_time=2), Uncreate(trig.gt), Unwrite(htext) )
        self.wait()
        for x in np.arange(7.5, 15, 0.1):
            if(scal(trig.velocity, trig.velocityinit) > 0.1):
                trig.vel0 = [trig.v * np.cos(trig.alpha), trig.v * np.sin(trig.alpha) - trig.g * trig.t.get_value(), 0]
                self.play(trig.t.animate(run_time=0.02).set_value(x))
        self.wait()
        self.play(ReplacementTransform(a, ar, run_time=2),FadeOut(atex , run_time=2))

        formula5 = MathTex(r'\frac{v_0 v }{g} = L').scale(1.5)
        formula5.shift(2 * RIGHT + 0.75 * UP)

        dot1 = trajectory(PI/6, 6*LEFT+1.6*UP, YELLOW, 1.2, 3 )
        dot1.dot.scale(1.5)
        dot1.text_and_vectors()
        dot1.path.set_color(YELLOW)
        dot1.define_path()
        self.add(dot1.path)





        self.play(ReplacementTransform(formula4, formula5))
        self.wait(2)
        self.play( Uncreate(trig.velocity), Uncreate(height), Uncreate(ar), Unwrite(btex), Uncreate(b), Uncreate(trig.velocityinit))
        self.remove(trig.vtext, trig.votext)
        self.play(Create(dot1.dot))

        for x in np.arange(0, 6, 0.1):
            dot1.last_pos0 = dot1.dot.get_center()
            dot1.vel0 = [(dot1.v * np.cos(dot1.alpha)),
                            (dot1.v * np.sin(dot1.alpha) - dot1.g * (x) / (dot1.v * np.cos(dot1.alpha))), 0]
            self.play(dot1.t.animate(run_time=0.03).set_value(x))
        self.play(Uncreate(dot1.dot),Uncreate(dot1.path),Uncreate(formula5), FadeOut(text2) )













        

