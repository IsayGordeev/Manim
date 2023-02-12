from manim import *

class SineCurveUnitCircle(Scene):
    # contributed by heejin_park, https://infograph.tistory.com/230
    def construct(self):
        self.show_axis()
        self.wait()
        path = VMobject()

        dot = Dot()
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)

        path.add_updater(update_path)
        self.add(path, dot)
        for x in range(5):
            self.play(dot.animate.shift([np.random.uniform(0,1),0.1,0]))
    def show_axis(self):
        x_start = np.array([0,0,0])
        x_end = np.array([3,0,0])
        y_start = np.array([0,0,0])
        y_end = np.array([0,3,0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)
        self.add_x_labels()


    def add_x_labels(self):
        x_labels = [
            MathTex("\pi"), MathTex("2 \pi"),
            MathTex("3 \pi"), MathTex("4 \pi"),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([ 2*i, 0, 0]), DOWN)
            self.add(x_labels[i])





