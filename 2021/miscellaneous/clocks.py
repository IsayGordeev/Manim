

class Clock(VGroup):
    CONFIG = {}

    def __init__(self, **kwargs):
        circle = Circle(color=WHITE)
        ticks = []
        for x in range(12):
            alpha = x / 12.
            point = complex_to_R3(
                np.exp(2 * np.pi * alpha * complex(0, 1))
            )
            length = 0.2 if x % 3 == 0 else 0.1
            ticks.append(
                Line(point, (1 - length) * point)
            )
        self.hour_hand = Line(ORIGIN, 0.3 * UP)
        self.minute_hand = Line(ORIGIN, 0.6 * UP)
        # for hand in self.hour_hand, self.minute_hand:
        #     #Balance out where the center is
        #     hand.add(VectorizedPoint(-hand.get_end()))

        VGroup.__init__(
            self, circle,
            self.hour_hand, self.minute_hand,
            *ticks
        )

class ClockPassesTime(Animation):
    CONFIG = {
        "run_time": 5,
        "hours_passed": 12,
        "rate_func": linear,
    }

    def __init__(self, clock, **kwargs):
        self.run_time = 5
        self.hours_passed = 12
        self.rate_func = linear
        assert(isinstance(clock, Clock))
        rot_kwargs = {
            "axis": OUT,
            "about_point": clock.get_center()
        }
        hour_radians = -self.hours_passed * 2 * np.pi / 12
        self.hour_rotation = Rotating(
            clock.hour_hand,
            angle=hour_radians,
            **rot_kwargs
        )
        self.hour_rotation.begin()
        self.minute_rotation = Rotating(
            clock.minute_hand,
            angle=12 * hour_radians,
            **rot_kwargs
        )
        self.minute_rotation.begin()
        Animation.__init__(self, clock, **kwargs)

    def interpolate_mobject(self, alpha):
        for rotation in self.hour_rotation, self.minute_rotation:
            rotation.interpolate_mobject(alpha)