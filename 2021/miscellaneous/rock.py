from manim import *

class SineCurveUnitCircle(Scene):
    # contributed by heejin_park, https://infograph.tistory.com/230

    def construct(self):
        g = 0.1
        v = 0.5
        displ = (LEFT + UP)*2 + LEFT
        start = 2*UP-2*RIGHT
        alpha = [np.pi/4, np.pi/6,np.pi/8]
        path = VMobject()
        self.vel0 = [v*np.sin(alpha[0]),v*np.sin(alpha[0]),0]
        self.vel00 = self.vel0
        self.vel1 = [v * np.sin(alpha[1]), v * np.sin(alpha[1]), 0]
        self.last_pos0 = start
        self.last_pos1 = start

        dots = [Dot(start) for x in range(3)]
        paths = [VMobject() for x in range(3)]
        velocityvector0 = Arrow(self.last_pos0,self.last_pos0+ self.vel0, buff=2)
        velocityvector00 = Arrow(ORIGIN+ displ, self.vel0+ displ, buff=2)
        velocityvector000 = Arrow(ORIGIN, self.vel0, buff=2).set_color(BLUE)
        velocityvector0000 = Arrow(self.vel00,  self.vel0).set_color(BLUE)
        velocityvector0.add_updater(lambda z: z.become(Arrow(self.last_pos0, self.last_pos0 + self.vel0, buff=2).set_color(RED)))
        velocityvector000.add_updater(lambda z: z.become(Arrow(ORIGIN + displ,  self.vel0+ displ).set_color(RED))).scale(3)
        # velocityvector0000.add_updater(lambda z: z.become(Arrow(self.vel00+ displ,  self.vel0+ displ).set_color(BLUE))).scale(3)


        velocityvector1 = Arrow(self.last_pos1,self.last_pos1+ self.vel1, buff=2)
        velocityvector1.add_updater(lambda z: z.become(Arrow(self.last_pos1, self.last_pos1 + self.vel1, buff=2).set_color(BLUE)))

        self.add(velocityvector0)
        for x in range(3):
            paths[x].set_points_as_corners([dots[x].get_center(), dots[x].get_center()])


        def update_path0(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dots[0].get_center()])
            path.become(previous_path)
        paths[0].add_updater(update_path0)
        
        def update_path1(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dots[1].get_center()])
            path.become(previous_path)
        paths[1].add_updater(update_path1)
        
        
        
        
        self.add(paths[0], dots[0], paths[1], dots[1])


        for x in range(20):
            self.last_pos0 = dots[0].get_center()
            self.last_pos1 = dots[1].get_center()
            self.vel0 = [v*np.sin(alpha[0]),v*np.sin(alpha[0])-g*(x)/2,0]
            self.vel1 = [v*np.sin(alpha[1]),v*np.sin(alpha[1])-g*(x)/2,0]
            self.play(dots[0].animate(run_time=0.01).shift(self.vel0),dots[1].animate(run_time=0.01).shift(self.vel1) )

        self.play(Create(velocityvector00),Create(velocityvector000))
        dots[0].move_to(start)
        for x in range(20):
            self.last_pos0 = dots[0].get_center()
            self.last_pos1 = dots[1].get_center()
            self.vel0 = [v * np.sin(alpha[0]), v * np.sin(alpha[0]) - g * (x) / 2, 0]
            self.play(dots[0].animate(run_time=0.01).shift(self.vel0))


