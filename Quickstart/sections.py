from manim import *

class SectionAnimations(Scene):
    
    def construct(self):

        circle = Circle()
        self.play(Create(circle))

        self.next_section()
        square = Square()
        self.play(Transform(circle, square))
        self.wait(1)
        self.remove(circle)

        self.next_section('Now We Will Move')
        self.play(square.animate.shift(2 * RIGHT))
        self.play(Rotate(square, angle = PI))
        self.play(square.animate.shift(2 * DOWN))
        
        self.next_section('Now We Split!')
        square1 = Square()
        square1.move_to(square)
        self.play(Create(square1))
        self.play(square1.animate.shift(3 * LEFT))