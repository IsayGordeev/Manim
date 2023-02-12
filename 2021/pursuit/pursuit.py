from manim import *

class tesst(Scene):
    def construct(self):
        # circ = Circle(color=RED).shift(4 * LEFT)
        # dot = Dot(color=RED).move_to(circ.get_bottom())
        # rolling_circle = VGroup(circ, dot)
        # trace = TracedPath(dot.get_start)
        # rolling_circle.add_updater(lambda m: m.rotate(-0.1))
        # self.add(trace, rolling_circle)
        # self.play(rolling_circle.animate.shift(8 * RIGHT), run_time=4, rate_func=linear)

        dot1 = Dot(color=RED).move_to(2*LEFT)
        dot2 = Dot(color=GREEN).move_to(-2*LEFT)

        # trace = TracedPath(dot2.get_center)
        dot2.add_updater(lambda m: m.shift(normalize(dot1.get_center()-m.get_center())/15))
        self.add(dot2, dot1)
        self.play(dot1.animate.shift(2*UP), run_time=2, rate_func=linear)
        dot2.clear_updaters()
        self.play(dot2.animate.move_to(dot1.get_center()), run_time=2, rate_func=linear)
        self.wait()

class Example(Scene):
    def construct(self):

        dot1 = Dot(color=RED).move_to(2 * LEFT)
        dot2 = Dot(color=GREEN).move_to(-2 * LEFT)

        trace = TracedPath(dot2.get_center)
        self.add(dot2, dot1)
        dot2.add_updater(lambda m: m.shift(normalize(dot1.get_center() - dot2.get_center()) / 15))

        self.play(dot1.animate.shift(2 * UP), run_time=2, rate_func=linear)
        dot2.clear_updaters()
        self.play(dot2.animate.move_to(dot1.get_center()), run_time=2, rate_func=linear)
        self.play(dot1.animate(run_time=1).shift(UP/2), dot2.animate(run_time=1).shift(UP+LEFT*2))
        # mob = Circle(radius=4, color=TEAL_A)
        # graph = ImplicitFunction(
        #     lambda x, y: np.sin(x*y),
        #     color=YELLOW
        # )
        # self.add(NumberPlane(), graph)
        # self.play(Broadcast(mob))
        # trace1 = TracedPath(dot1.get_center, color= GREEN)
        # self.add(trace1)
        # self.play(MoveAlongPath(dot1, graph))