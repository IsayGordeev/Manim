from manim import *


class protein(VGroup):
    def __init__(self, start, a, r, color, **kwargs):
        super().__init__(**kwargs)
        self.a = a
        self.r = r
        self.start = start
        self.color = color
        self.ada = ValueTracker(self.a)
        self.rdr = ValueTracker(self.r)
        self.curve = ParametricFunction(
            lambda u: np.array([
                self.r * np.cos(60 * u) + start[0],
                self.r * np.sin(60 * u) + start[1],
                self.a * u + start[2]
            ]), color=RED, t_min=-TAU, t_max=TAU, stroke_color=color
        ).set_shade_in_3d(True)

    def get_spring(self, a, r, color1):
        curve1 = ParametricFunction(
            lambda u: np.array([
                r * np.cos(60 * u) + self.start[0],
                r * np.sin(60 * u) + self.start[1],
                a * u + self.start[2]
            ]), color=RED, t_min=-TAU, t_max=TAU, stroke_color=color1
        ).set_shade_in_3d(True)
        return curve1

    # def spring_updater_height(self):
    #     self.curve.add_updater(lambda z: z.become(self.get_spring(self.ada.get_value(),self.r)))
    # def spring_updater_rad(self):
    #     self.curve.add_updater(lambda z: z.become(self.get_spring(self.a,self.rdr.get_value())))

    def spring_updater(self):
        self.curve.add_updater(
            lambda z: z.become(self.get_spring(self.ada.get_value(), self.rdr.get_value(), self.color)))


# class scatter(Scene):
#     def construct(self):
#         text = Tex('Hello')

class Example3DNo5(ThreeDScene):
    def construct(self):
        a = protein(ORIGIN, 1.5, 0.25, RED)
        b = protein(RIGHT, 1.5, 0.25, GREEN)
        line1 = Line(a.curve.get_end(), a.curve.get_end() + [1, -1, 1])
        line2 = Line(b.curve.get_end(), a.curve.get_end() + [1, -1, 1])
        line3 = Line(a.curve.get_start(), a.curve.get_start() + [-1, 1, 0])
        line4 = Line(b.curve.get_start(), b.curve.get_start() + [-1, 1, 0])


        surface = Group(line1,line2,line3, line4)

        a.spring_updater()
        b.spring_updater()
        axes = ThreeDAxes()

        self.add(axes, a.curve, b.curve, *surface)

        self.set_camera_orientation(phi=80 * DEGREES, theta=60 * DEGREES)
        self.wait()
        self.spring_oscillation([a])
        print(0.25 * np.cos(60 * TAU),
              0.25 * np.sin(60 * TAU),
              1.5 * TAU)
        print(a.curve.get_end())

    def spring_oscillation(self, all):
        for a in all:
            for x in zip(np.arange(a.a, a.a + 0.05, 0.01), np.arange(a.r, a.r + 0.05, 0.01)):
                self.moving(a, x)
            # for x in zip(np.arange(a.a+0.05, a.a, -0.01),np.arange( a.r+0.05,a.r, -0.01)):
            #     self.moving(a, x)

    def moving(self, a, x):
        self.play(a.ada.animate(run_time=0.05).set_value(x[0]))
        self.play(a.rdr.animate(run_time=0.05).set_value(x[1]))
