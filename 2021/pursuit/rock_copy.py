from manim import *

class SineCurveUnitCircle(Scene):
    # contributed by heejin_park, https://infograph.tistory.com/230

    def construct(self):
        g = 0.1
        v = 0.7
        alpha = [np.pi/4, np.pi/6,np.pi/8]
        path = VMobject()
        self.vel = [v*np.sin(alpha[0]),v*np.sin(alpha[0]),0]
        self.last_pos = ORIGIN
        dots = [Dot(2*UP-2*RIGHT) for x in range(3)]
        paths = [VMobject() for x in range(3)]
        mega = [dots[0], paths[0]]
        velocityvector = Arrow(self.last_pos,self.last_pos+ self.vel, buff=2)
        # velocityvector1 = Arrow(ORIGIN, dots[0].get_center(), buff=0)
        # velocityvector1.add_updater(lambda z: z.become(Arrow(ORIGIN, dots[0].get_center(), buff=0)))
        velocityvector.add_updater(lambda z: z.become(Arrow(self.last_pos, self.last_pos + self.vel, buff=2)))

        velocityvector.scale(2)
        self.add(velocityvector )
        for x in range(3):
            paths[x].set_points_as_corners([dots[x].get_center(), dots[x].get_center()])


        def update_path0(mega):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        mega.add_updater(update_path0)
        self.add(mega[0], mega[1])


        for x in range(10):
            self.last_pos = mega[0].get_center()
            self.vel = [v*np.sin(alpha[0]),v*np.sin(alpha[0])-g*(x),0]
            self.play(mega[0].animate(run_time=0.01).shift(self.vel))
