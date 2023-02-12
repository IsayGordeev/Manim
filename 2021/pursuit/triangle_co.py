from abc import ABC

from manim import *

class trajectory(VGroup):
    def __init__(self,  alpha , start,color, g,v,STEP=20,run_time = 0.01, **kwargs):
        super().__init__( **kwargs)

        self.dot = Dot(start)
        self.path = VMobject()
        self.vel0 = [v * np.cos(alpha), v * np.sin(alpha), 0]
        self.vel00 = self.vel0
        self.disp = [0,0,0]
        self.last_pos0 = start
        self.start = start
        self.STEP = STEP
        self.v = v
        self.g = g
        self.alpha = alpha
        self.run_rime = run_time
        self.velocityvector0 = Arrow(self.last_pos0, self.last_pos0 + self.vel0, buff=2)
        self.velocityvector000 = Line((ORIGIN + start), self.vel0 + start, buff=2)
        self.velocityvector00 = Line(ORIGIN + start, self.vel0, buff=2)
        self.velocityvector0000 = Line(ORIGIN + start, [v * np.sin(alpha), v * np.sin(alpha) - g * (0.1), 0] + self.start,
                                  buff=2)
        self.gttext = Tex('$\\vec gt$').scale(0.3).move_to(self.velocityvector0000.get_center() + RIGHT * 10)
        self.votext = Tex('$\\vec v_0$').scale(0.3).move_to(self.velocityvector00.get_end() + self.start + LEFT * 0.17)
        self.vtext = Tex('$\\vec v$').scale(0.3).move_to(self.velocityvector000.get_center() - 0.15 * UP)
        self.dot.set_color(color)




    def update_path(self, path):
        previous_path = path.copy()
        previous_path.add_points_as_corners([self.dot.get_center()])
        path.become(previous_path)

    def define_path(self):
        self.path.set_points_as_corners([self.dot.get_center(), self.dot.get_center()])
        self.path.add_updater(self.update_path)

    def text_and_vectors(self):
        self.velocityvector000.add_updater(lambda z: z.become(Line(ORIGIN + self.start, self.vel0 + self.start).set_color(RED)))
        self.velocityvector0.add_updater(
            lambda z: z.become(Arrow(self.last_pos0, self.last_pos0 + self.vel0, buff=2).set_color(RED)))
        self.velocityvector00.add_updater(lambda z: z.become(Line(ORIGIN + self.start, self.vel00 + self.start).set_color(BLUE)))
        self.velocityvector0000.add_updater(
            lambda z: z.become(Line(self.vel00 + self.start, self.vel0 + self.start, buff=2).set_color(GREEN)))

        self.vtext.add_updater(
            lambda z: z.become(Tex('$\\vec {v}$').scale(0.3).move_to(self.velocityvector000.get_center() - 0.15 * UP)))

        self.gttext.add_updater(
            lambda z: z.become(Tex('$\\vec {g}t$').scale(0.3).move_to(self.velocityvector0000.get_center() + RIGHT * 0.1)))

    def moving(self):
        for x in np.arange(0, self.STEP, 0.1):
            self.last_pos0 = self.dot.get_center()
            if self.dot.get_y() > -1.9:
                self.vel0 = [self.v * np.sin(self.alpha), self.v * np.sin(self.alpha) - self.g * (x), 0]
                self.play(self.dot.animate(run_time=0.01).shift(self.vel0))
            else:
                break

    def add_text(self):
        self.play(Write(self.vtext),Write(self.votext),Write(self.gttext))

    def add_vectors(self):
        return (self.path, self.velocityvector000, self.velocityvector0000, self.velocityvector00, self.velocityvector0)



class triangle(ZoomedScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.3,
            zoomed_display_height=4,
            zoomed_display_width=3.5,
            image_frame_stroke_width=20,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
            },
            **kwargs
        )

    def construct(self):

        text = Tex('What are the optimal conditions for stone needed to reach the height?')
        formula = MathTex(
            '\\begin{cases}\\vec s = \\vec s_0 + \\vec v t + \\frac {\\vec g}{2}t^2 \\\\ \\vec v = \\vec v_0 +\\vec g t\\end{cases}')
        formula.to_corner(UP + LEFT)
        text.move_to(3 * UP)
        self.play(ReplacementTransform(text, formula, run_time=2))
        v = 0.5
        g = 0.1
        l = 2
        h = 1
        start = 3*LEFT+2*DOWN
        dot3 = trajectory(PI/4, start,GREEN,g,v)
        dot2 = trajectory(0.5, start,BLUE,g,v)
        dot1 = trajectory(1.3, start, RED ,g,v)
        print(np.arctan(v / (np.sqrt(v * v + 2 * g * 2))))


        # zoom
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame

        frame.move_to(start)
        frame.set_color(PURPLE)
        zoomed_display_frame.set_color(RED)
        zoomed_display.shift(DOWN)

        zd_rect = BackgroundRectangle(zoomed_display, fill_opacity=0, buff=MED_SMALL_BUFF)
        self.add_foreground_mobject(zd_rect)

        unfold_camera = UpdateFromFunc(zd_rect, lambda rect: rect.replace(zoomed_display))

        surface = [Line(start+l*RIGHT, start+l*RIGHT+h*UP), Line(start  , start+l*RIGHT), Line
        (start+l*RIGHT+h*UP, start+l*RIGHT+h*UP+RIGHT)]
        brheight = Brace(surface[0], direction=surface[0].copy().rotate(3 * PI / 2).get_unit_vector())
        brheighttext = brheight.get_text('h')

        dot1.text_and_vectors()

        self.play(Create(surface[0]))
        self.play(Create(surface[1]))
        self.play(Create(surface[2]))
        self.play(TransformFromCopy(formula, dot1.votext), TransformFromCopy(formula, dot1.vtext),
                  TransformFromCopy(formula, dot1.gttext), TransformFromCopy(formula, brheight),
                  TransformFromCopy(formula, brheighttext))

        self.add(brheighttext, brheight, dot1.votext, dot1.vtext, dot1.gttext, dot1.dot, dot2.dot,dot3.dot)
        self.add(dot1.path)
        dot1.define_path()
        self.add(dot2.path)
        dot2.define_path()
        self.add(dot3.path)
        dot3.define_path()

        self.activate_zooming()
        self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera)

        self.add(*dot1.add_vectors())
        self.wait()
        n = -1
        for x in np.arange(0, l/(dot1.v * np.cos(dot1.alpha)), 1):
            if np.linalg.norm(dot1.dot.get_center() - (start + 3*RIGHT+2*UP)) > 0.05:
                dot1.vel0 = [(dot1.v * np.cos(dot1.alpha)), (dot1.v * np.sin(dot1.alpha) - dot1.g * x ), 0]
                dot2.vel0 = [dot2.v * np.cos(dot2.alpha), dot2.v * np.sin(dot2.alpha) - dot2.g * (x), 0]
                dot3.vel0 = [dot3.v * np.cos(dot3.alpha), dot3.v * np.sin(dot3.alpha) - dot3.g * (x), 0]
                print(dot1.vel0, n*x)
                self.play(dot1.dot.animate(run_time=0.01).shift(dot1.vel0),
                          dot2.dot.animate(run_time=0.01).shift(dot2.vel0),
                          dot3.dot.animate(run_time=0.01).shift(dot3.vel0) )
                n = n + 1
            else: break





        self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera, rate_func=lambda t: smooth(1 - t))
        self.play(Uncreate(zoomed_display_frame), FadeOut(frame))
        self.wait()

        # self.play(Uncreate(path), Uncreate(dots[0]))

