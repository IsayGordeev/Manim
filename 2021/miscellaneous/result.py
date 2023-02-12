from manim import *

class BrownMotion(Scene):
    # contributed by heejin_park, https://infograph.tistory.com/230
    def construct(self):
        start = [1,0,0]
        langevensolutsimple = MathTex(
            '\\overline{\\textbf r^2} = r^2_0+6kTBt'
        )
        moving_dot = Dot(start)
        origin = Dot([1,0,0])
        introtext = Tex('Let\'s check model - linear dependence between average squared distance from origin of the time ')
        introtext.scale(0.7)
        introtext.move_to(UP)
        self.play(Write(introtext))
        self.wait(2)
        self.play(ReplacementTransform(introtext,langevensolutsimple))
        self.wait(2)
        self.play(ReplacementTransform(langevensolutsimple, moving_dot ))
        self.add(origin)
        self.wait(2)

        self.play(Create(self.show_axis_x(start)),Create(self.show_axis_y()),Create(self.show_predict(start)))
        self.add_xlabels()
        self.add(origin)
        self.play(Write(self.add_ylabels()))
        self.wait(2)



        path = VMobject()
        STEP = 30
        circle = Circle(radius=2)
        circle.move_to([-3,0,0])
        # self.add(circle)

        path.set_points_as_corners([moving_dot.get_center(), moving_dot.get_center()])

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([moving_dot.get_center()])
            path.become(previous_path)

        path.add_updater(update_path)

        d1 = Dot([-3,0,0],color=RED,radius=0.08 * 0.5)
        dots = [Dot([-3,0,0], color=random_color(), radius=0.08 * 2) for x in range(8)]
        # self.add(d1)
        self.play(TransformFromCopy(moving_dot, dots[0]))
        self.wait(2)
        self.play(TransformFromCopy(self.show_predict(start), circle))
        self.wait(2)

        vectors = [Line(d1.get_center(), dots[x].get_center(), path_arc=0.1) for x in range(8)]
        vectors[0].add_updater(lambda z: z.become(Line(d1.get_center(), dots[0].get_center())))
        self.add(vectors[0])
        vectors[1].add_updater(lambda z: z.become(Line(d1.get_center(), dots[1].get_center())))
        self.add(vectors[1])
        vectors[2].add_updater(lambda z: z.become(Line(d1.get_center(), dots[2].get_center())))
        self.add(vectors[2])
        vectors[3].add_updater(lambda z: z.become(Line(d1.get_center(), dots[3].get_center())))
        self.add(vectors[3])
        vectors[4].add_updater(lambda z: z.become(Line(d1.get_center(), dots[4].get_center())))
        self.add(vectors[4])
        vectors[5].add_updater(lambda z: z.become(Line(d1.get_center(), dots[5].get_center())))
        self.add(vectors[5])
        vectors[6].add_updater(lambda z: z.become(Line(d1.get_center(), dots[6].get_center())))
        self.add(vectors[6])
        vectors[7].add_updater(lambda z: z.become(Line(d1.get_center(), dots[7].get_center())))
        self.add(vectors[7])

        self.add(path, moving_dot)
        r1 = 0
        for x in range(STEP):
            r2 = 0
            for dot in dots:
                r2 += (np.linalg.norm(dot.get_center()-d1.get_center())) / 8
                coord = np.random.uniform(-0.15, 0.15, 3)
                self.play(dot.animate(run_time=0.01).shift(coord))
            self.play(moving_dot.animate(run_time=0.01).shift([0.1*0.1*6,2.5*(r2-r1),0]))
            print(r1,r2)
            r1 = r2

    def show_axis_x(self,start):
        x_start = np.array([0.8,0,0])
        x_end = np.array([4,0,0])


        x_axis = Arrow(x_start, x_end)
        self.add(x_axis)
        return x_axis

    def show_axis_y(self):
        y_start = np.array([1, -0.2, 0])
        y_end = np.array([1, 3, 0])
        y_axis = Arrow(y_start, y_end)
        return y_axis
    def show_predict(self, x_start):
        predict = Line(x_start, [2.8,2,0]).set_color(RED)
        self.add(predict)
        return predict




    def add_xlabels(self):
        x_labels = [
            MathTex("0"), MathTex("10"),
            MathTex("20"), MathTex("t^2, \\text{s}"),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([ 1+ i, 0, 0]), DOWN)
            x_labels[3].move_to([4.5, -0.1, 0])
        x_labels[3].move_to([4.5, -0.45, 0])
        x_labels[0].move_to([0.5, -0.45, 0])
        for i in range(len(x_labels)):
            self.play(Write(x_labels[i]))


    def add_ylabels(self):

        y_label = MathTex('\\overline {r^2} ')
        y_label.move_to(np.array([0.5, 3, 0]))
        y_val = MathTex('2')
        y_val.move_to([0.5,2,0])
        y_val1 = MathTex('1')
        y_val1.move_to([0.5, 1, 0])
        self.play(Write(y_val1))
        self.play(Write(y_val))

        return y_label





