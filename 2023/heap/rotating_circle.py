from manim import *

class RotatingCircleOnParabola(Scene):
    def construct(self):
        TAU = 2
        parabola = ParametricFunction(
            lambda t: np.array([t, t**2, 0]),
            t_min=-TAU, t_max=TAU,
        )
        parabola_path = ParametricFunction(
            lambda t: np.array([t, t**2, 0]),
            t_min=-TAU, t_max=TAU,
        )

        circle = Circle(radius=0.5)
        circle.move_to(parabola.point_from_proportion(0))

        moving_circle = MovingAlongPath(circle, parabola_path)
        self.add(parabola)
        self.add(moving_circle)

        self.play(Rotating(moving_circle, about_point=parabola.point_from_proportion(0),radians=TAU, run_time=5), moving_circle.update)
