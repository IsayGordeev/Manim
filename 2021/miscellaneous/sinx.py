from manim import *

class FollowingGraphCamera(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        # create the axes and the curve
        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
        graph = ax.get_graph(lambda x: np.sin(x), color=BLUE, x_range=[0, 3 * PI])

        # create dots based on the graph
        moving_dot = Dot(ax.i2gp(graph.t_min, graph), color=ORANGE)
        dot_1 = Dot(ax.i2gp(graph.t_min, graph))
        dot_2 = Dot(ax.i2gp(graph.t_max, graph))

        self.add(ax, graph, dot_1, dot_2, moving_dot)
        self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dot))


        a = SVGMobject('/Users/isajgordeev/Desktop/1.svg')
        b = SVGMobject('/Users/isajgordeev/Desktop/2.svg')
        c = SVGMobject('/Users/isajgordeev/Desktop/3.svg')

        self.play(Write(a))
        self.play(ReplacementTransform(a,b))
        self.play(ReplacementTransform(b,c))