from manim import *

class ArgMinExample(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 5], y_range=[0, 10, 5], axis_config={"include_tip": False}
        )
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")

        t = ValueTracker(0)
        l = 2
        alpha = PI/3
        g = 0.1
        v= 1
        def func(x):
            return x*np.tan(alpha)-(g*x**2*(1+np.tan(alpha)**2))/(2*v**2)
        graph = ax.get_graph(func, color=MAROON)

        initial_point = [ax.coords_to_point(t.get_value(), func(t.get_value()))]
        dot = Dot(initial_point)

        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), func(t.get_value()))))
        x_space = np.linspace(*ax.x_range[:2],200)
        print(x_space)
        minimum_index = func(x_space).argmin()

        self.add(ax, labels,graph,  dot)
        for x in range(10):
            self.play(t.animate.set_value(x))
        self.wait()