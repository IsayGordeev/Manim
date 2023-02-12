from manim import *
class easy1(Scene):
    def construct(self):
        a = MathTex('2+2 = 4','|\ /2')
        self.play(Write(a[0]))
        self.wait(2)
        self.play(Write(a[1]))
        b = MathTex(r'\frac 2 2 +\frac 2 2  = \frac 4 2')
        self.wait(2)
        self.play(ReplacementTransform(a,b))
        c = MathTex('1+1 = 2').next_to(b,UP)
        self.wait(2)
        self.play(TransformFromCopy(b,c))
        self.wait(2)

        b1 = MathTex('{2^','1','\\over','2^','1','}','+', '{2^','1','\\over','2^','1','}','+ ', '{2^','2','\\over','2^','1','}' ).next_to(b,DOWN)
        b1[1].set_color(RED)
        b1[4].set_color(BLUE)
        b1[8].set_color(RED)
        b1[11].set_color(BLUE)
        b1[15].set_color(RED)
        b1[18].set_color(BLUE)



        self.play(TransformFromCopy(b,b1))
        self.wait(2)
        c1= MathTex('2^0+2^0 = 2^1').next_to(c,UP)
        self.play(TransformFromCopy(c,c1))
        self.wait(2)

        self.play(Uncreate(c),Uncreate(b),b1.animate.shift(UP), c1.animate.shift(DOWN) )
        self.wait(2)

        c2= MathTex('2^{',r'1',r'-',r'1}',r'+2^{',r'1',r'-',r'1}',r' = 2^{',r'2',r'-',r'1}',r'').next_to(c1,UP)
        c2[1].set_color(RED)
        c2[3].set_color(BLUE)
        c2[5].set_color(RED)
        c2[7].set_color(BLUE)
        c2[9].set_color(RED)
        c2[11].set_color(BLUE)
        # c3 = MathTex('2^{','1','}',r'\cdot',r'2^{','1','}' ).next_to(c2,UP)


        self.play(TransformFromCopy(c1,c2))
        # self.play(Write(c3))
        self.wait(2)

class FormulaColor3Fixed2(Scene):
    def construct(self):
        text = MathTex("\\sqrt{","\\int_","{a}^","{b}","{\\left(","{x","\\over","y}","\\right)}","d","x",".}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        text[8].set_color(TEAL)
        text[9].set_color(GOLD)
        self.play(Write(text))
        self.wait(3)


