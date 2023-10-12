from manim import *

class Projectile(Scene):

    def construct(self):

        circle = Circle().set_fill(WHITE, opacity=1.0)
        self.play(FadeIn(circle))
        self.wait(2)