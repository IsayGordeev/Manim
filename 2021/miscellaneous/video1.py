from manim import *


class vectorcalc(Scene):
    def construct(self):
        self.intro()
        # self.sum()
        # self.levi()
        # self.vec_prod()

    def intro(self):
        text1 = Tex('We consider index contraction in vector analysis')
        text2 = Tex('and then its application to linear algebra')
        text1.move_to(2 * UP)
        text2.move_to(UP)
        formula = MathTex(r'Ax=\lambda x')
        formula.rotate(PI / 8)
        formula.shift(3 * LEFT + 2 * DOWN)
        formula1 = MathTex(
            r'{\displaystyle \det A=\sum _{\alpha _{1},\alpha _{2},\ldots ,\alpha _{n}}(-1)^{N(\alpha _{1},\alpha _{2},\ldots ,\alpha _{n})}\cdot a_{1\alpha _{1}}a_{2\alpha _{2}}\dots a_{n\alpha _{n}}}').scale(
            0.6)
        formula1.rotate(-PI / 7)
        formula1.shift(-2 * LEFT + 2 * DOWN)
        self.play(Write(text1, run_time=2), Write(text2, run_time=2), Write(formula, run_time=2),
                  Write(formula1, run_time=2))
        self.wait()
        self.play(Unwrite(text1), Unwrite(text2), Unwrite(formula, run_time=2), Unwrite(formula1, run_time=2))
        self.wait(0.4)

    def sum(self):
        formula = MathTex(r'\sum_{0=i}^n ', 'a_i b_i', '=(a,b)')
        formula.shift(0.5 * RIGHT)
        self.play(Write(formula[0]), Write(formula[1]))
        formula[2].shift(UP)
        self.play(formula[0].animate.shift(UP),
                  formula[1].animate.shift(UP)
                  )
        text = Tex('This sum is scalar product in Euclidean space')
        self.play(Write(text, run_time=2))
        self.play(formula[0].animate.shift(-0.5 * RIGHT),
                  formula[1].animate.shift(-0.5 * RIGHT),
                  Write(formula[2]),
                  formula[2].animate.shift(-0.5 * RIGHT)
                  )
        text1 = Tex('It can be simplified if we contract sum')
        self.play(ReplacementTransform(text, text1, run_time=2))
        self.play(Unwrite(formula[0]),
                  formula[1].animate.shift(-0.5 * RIGHT),
                  formula[2].animate.shift(-0.5 * RIGHT)
                  )
        text2 = Tex(r'In general case, when we have metrics $g_{ij}$ \\', 'index contraction can be written')
        self.play(ReplacementTransform(text1, text2, run_time=2))
        formula1 = MathTex(r'\sum_{0=i}^n ', 'a_i b^j', '=(a,b)')
        formula1.shift(UP + 0.5 * LEFT)
        self.play(ReplacementTransform(formula[1], formula1[1]), ReplacementTransform(formula[2], formula1[2]))
        self.play(Indicate(formula1[1], run_time=2))
        subtext2 = Tex(r'where $g_{ij}, g^{ij}$ matrices, $a_i$ string,\\',
                       ' $b^j$ column, $e_i$, $e_j$ basis vectors ')
        subtext2.shift(UP)
        self.play(formula1[1].animate(run_time=2).shift(UP), formula1[2].animate(run_time=2).shift(UP),
                  text2.animate(run_time=2).shift(UP))
        self.play(ReplacementTransform(text2, subtext2, run_time=2))
        subformula1 = MathTex(r'b^j=g^{ij}a_i,\  g^{ij}g_{ij}=E,\  ')
        subformula2 = MathTex(r'g_{ij} = {(e_i, e_j)}')
        subformula2.shift(DOWN)
        self.play(Write(subformula1, run_time=2), Create(subformula2, run_time=2))
        self.wait(4)
        self.play(Uncreate(subformula1), Uncreate(subformula2), Unwrite(subtext2), Uncreate(formula1[1]),
                  Uncreate(formula1[2]))
        self.wait((0.5))

    def levi(self):
        start = ORIGIN
        scale = 2
        x = Arrow(start, start + scale * RIGHT, buff=0)
        y = Arrow(start, start + scale * ((LEFT + DOWN) / np.sqrt(2)), buff=0)
        z = Arrow(start, start + scale * UP, buff=0)
        xtext = Tex('x').move_to(x.get_end() + x.get_unit_vector() * 0.15)
        ytext = Tex('y').move_to(y.get_end() + y.get_unit_vector() * 0.15)
        ztext = Tex('z').move_to(z.get_end() + z.get_unit_vector() * 0.15)
        a = Line(start, start + RIGHT, buff=0).set_color(RED)
        b = Line(start, start + ((LEFT + DOWN) / np.sqrt(2)), buff=0).set_color(BLUE)
        c = Line(start, start + UP, buff=0).set_color(GREEN)
        atext = Tex('a').move_to(a.get_end() - z.get_normal_vector() * 0.3).set_color(RED)
        btext = Tex('b').move_to(b.get_end() - x.get_normal_vector() * 0.3).set_color(BLUE)
        ctext = Tex('c').move_to(c.get_end() - x.get_normal_vector() * 0.3).set_color(GREEN)
        ad = DashedLine(b.get_end(), a.get_end() + b.get_end()).set_color(RED)
        ad1 = DashedLine(c.get_end(), a.get_end() + c.get_end()).set_color(RED)
        ad2 = DashedLine(c.get_end() + +b.get_end(), a.get_end() + c.get_end() + b.get_end()).set_color(RED)

        bd = DashedLine(a.get_end(), b.get_end() + a.get_end()).set_color(BLUE)
        bd1 = DashedLine(c.get_end(), b.get_end() + c.get_end()).set_color(BLUE)
        bd2 = DashedLine(c.get_end() + a.get_end(), b.get_end() + c.get_end() + a.get_end()).set_color(BLUE)

        cd = DashedLine(b.get_end() + a.get_end(), c.get_end() + b.get_end() + a.get_end()).set_color(GREEN)
        cd1 = DashedLine(a.get_end(), c.get_end() + a.get_end()).set_color(GREEN)
        cd2 = DashedLine(b.get_end(), c.get_end() + b.get_end()).set_color(GREEN)
        volumetext = Tex('V').move_to(cd1.get_end() + z.get_unit_vector() * 0.3)
        self.play(Create(x),
                  Create(y),
                  Create(z),
                  Write(xtext),
                  Write(ytext),
                  Write(ztext)
                  )
        self.play(Create(a),
                  Create(b),
                  Create(c),
                  Write(atext),
                  Write(btext),
                  Write(ctext)
                  )
        self.play(Create(ad),
                  Create(ad1),
                  Create(ad2),
                  Create(bd),
                  Create(bd1),
                  Create(bd2),
                  Create(cd),
                  Create(cd1),
                  Create(cd2),
                  )
        all1 = VGroup(ad, ad1, ad2, bd, bd1, bd2, cd, cd1, cd2, x, y, z, a, b, c, xtext, ytext, ztext, volumetext,
                      )
        lab = VGroup(atext, btext, ctext)
        self.play(all1.animate.shift(RIGHT), lab.animate.shift(0.6 * RIGHT))
        self.play(atext.animate.shift(0.3 * DOWN + 0.4 * RIGHT))
        text1 = Tex('Volume of this parallelepiped is a mixed product')
        formula1 = MathTex(r'V = ', 'a', '\cdot(', 'b', r'\times ', 'c', ')')
        formula1[1].set_color(RED)
        formula1[3].set_color(BLUE)
        formula1[5].set_color(GREEN)

        formula2 = MathTex(r'V = ', 'e_i a^i', '\cdot(', 'e_j b^j', r'\times ', 'e_k c^k', ')')
        formula2[1].set_color(RED)
        formula2[3].set_color(BLUE)
        formula2[5].set_color(GREEN)
        text2 = Tex('Using coordinate view of vectors and index contraction')
        formula3 = MathTex(r'V = ', 'e_i ', '\cdot(', 'e_j', r'\times ', 'e_k', ')', 'a^i', 'b^j', 'c^k')
        formula3[1].set_color(RED)
        formula3[3].set_color(BLUE)
        formula3[5].set_color(GREEN)
        formula3[7].set_color(RED)
        formula3[8].set_color(BLUE)
        formula3[9].set_color(GREEN)

        text1.to_corner(LEFT + UP)
        formula1.to_corner(LEFT + UP)
        formula1.shift(DOWN)
        text2.to_corner(LEFT + UP)
        formula2.to_corner(LEFT + UP)
        formula2.shift(2 * DOWN)
        formula3.to_corner(LEFT + UP)
        formula3.shift(3 * DOWN)

        text3 = Tex(
            'Define Levi-Civita symbol $\epsilon_{ijk}$ as antisymmetric symbol - volume of unit parallelepiped').scale(
            0.7)
        text3.to_corner(LEFT + UP)

        self.play(Write(text1, run_time=2), Write(formula1, run_time=2), Write(volumetext, run_time=2))
        self.wait()
        self.play(TransformFromCopy(formula1, formula2, run_time=2), ReplacementTransform(text1, text2, run_time=2))
        self.wait()

        self.play(TransformFromCopy(formula2, formula3, run_time=2))
        self.wait()

        formula4 = MathTex(r'V = ', r'\epsilon_{ijk}',
                           'a^i', 'b^j', 'c^k')
        formula4.to_corner(LEFT + UP)
        formula4.shift(4 * DOWN)
        formula5 = MathTex(r'\epsilon_{ijk}=', 'e_i ', '\cdot(', 'e_j', r'\times ', 'e_k', ')')
        formula5.to_corner(LEFT + UP)
        formula5.shift(5 * DOWN)

        formula4[2].set_color(RED)
        formula4[3].set_color(BLUE)
        formula4[4].set_color(GREEN)
        formula5[1].set_color(RED)
        formula5[3].set_color(BLUE)
        formula5[5].set_color(GREEN)

        self.play(ReplacementTransform(text2, text3, run_time=2), TransformFromCopy(formula3, formula4, run_time=2),
                  TransformFromCopy(formula3, formula5, run_time=2))
        self.wait(3)
        self.play(Uncreate(all1), Uncreate(lab), Uncreate(text3), Uncreate(formula1), Uncreate(formula2),
                  Uncreate(formula3), Uncreate(formula4), Uncreate(formula5))
        self.wait(1)

    def vec_prod(self):
        text = Tex('We defined').scale(0.75)
        text.shift(2.5*UP)
        self.play(Write(text))
        formula1 = MathTex('(a,b)=a_ib^j')
        formula2 = MathTex(r'a\cdot',r'(b\times c) ','= \epsilon_{ijk}a^ib^jc^k')
        formula1.shift(UP)
        self.play(Write(formula1), Write(formula2))
        text1 = Tex('Scalar product in index notation',', but what about cross product?').scale(0.75)
        text1.shift(2.75*UP)
        text1[0].shift(2.5*RIGHT)
        self.play(ReplacementTransform(text, text1[0]))
        self.play(formula1.animate.shift(UP), formula2.animate.shift(UP))
        self.play(Indicate(formula1,run_time=2))
        self.play(text1[0].animate.shift(2.5*LEFT),Write(text1[1]))
        self.play(Indicate(formula2[1],run_time=2))
        self.wait()
        self.play(FadeOut(text1,run_time=2))
        self.wait()
        text2 = Tex(r'Let $d = (b\times c) $')
        self.play(ShowCreationThenDestruction(text2, run_time=6))
        formula3 = MathTex(r'a\cdot d=', r'  \epsilon_{ijk}', 'a^i', 'b^jc^k')
        formula4 = MathTex(r'a\cdot d=', 'a^i', r'  \epsilon_{ijk}', 'b^jc^k')
        formula5 = MathTex(r'd\cdot a=', '\epsilon_{ijk}b^jc^k ', 'a^i')
        formula6 = MathTex(r'd_i', '=\epsilon_{ijk}b^jc^k')
        formula7 = MathTex(r'(b\times c)_i', r'=\epsilon_{ijk}b^jc^k')
        formula6.shift(DOWN)
        formula7.shift(2 * DOWN)
        text3 = Tex(', so..')
        text3.next_to(formula6, RIGHT)
        self.play(TransformFromCopy(formula2, formula3,run_time=2))
        self.play(ReplacementTransform(formula3[1], formula4[1],run_time=2), ReplacementTransform(formula3[2], formula4[2],run_time=2))
        self.wait()
        self.play(FadeOut(formula3), ReplacementTransform(formula4[0], formula5[0]),
                  ReplacementTransform(formula4[1], formula5[2],run_time=2), ReplacementTransform(formula4[2], formula5[1],run_time=2))
        self.wait()

        self.remove(formula4, formula3)
        self.play(Indicate(formula1))
        self.wait()

        self.play(TransformFromCopy(formula5, formula6,run_time=2))
        self.wait()

        self.play(Write(text3))
        self.wait()

        self.play(TransformFromCopy(formula6[0], formula7[0],run_time=2), TransformFromCopy(formula6[1], formula7[1],run_time=2))
        self.wait()

        self.play(formula1.animate.shift(DOWN), formula7.animate.shift(2 * UP),
                  Uncreate(formula2),
                  Uncreate(formula6),
                  Uncreate(formula5),
                  Unwrite(text3)
                  )
        self.wait(2)
        self.play((Uncreate(formula1)),Uncreate(formula7))
        self.wait()

class Intro(Scene):
    def construct(self):
        self.a = SVGMobject('/Users/isajgordeev/Desktop/1.svg').scale(3)
        self.play(Write(self.a))




