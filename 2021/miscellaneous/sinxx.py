from manim import *

class sin(Scene):
    def construct(self):
        formula = MathTex(
        "I(\lambda)=",
        "\int_0^{+\infty}",
        r"\frac{\sin x}{x}",
        "e^{-\lambda x}",
        "dx"
        )
        formula[0].set_color(GOLD_E)
        formula[2].set_color(PURPLE)
        formula1 = MathTex(
        "I'(\lambda)",
        "=-\int_0^{+\infty}",
         "e^{-\lambda x}",
         "\sin x",
         "dx",
        )
        text1 = MathTex(r"\text{$\underbrace{\text{Dirichlet integral}}_{\displaystyle\int_0^{+\infty}\frac{\sin x}{x}dx}$ deriving by Feynman's trick}")
        formula1[0].set_color(BLUE)
        formula1[3].set_color(GREEN)
        formula2 = MathTex(
        "I'(\lambda)",
        "=",
        r"Im\,\,\overbrace{\int_0^{+\infty}",
        "e^{-\lambda x+ix}",
        r"dx}^{\frac{1}{\lambda-i}}",
        )
        formula2.shift(0.5*UP)
        formula2[0].set_color(BLUE)
        formula3 = MathTex(
        "I'(\lambda)",
        "=",
        "-Im",
        "\\frac{1}{\lambda-i}",
        "=",
        r"-",
        r"\frac{1}{\lambda^2+1}"
        )
        formula3[0].set_color(BLUE)
        formula4 = MathTex(
            "I(\lambda)",

        "=",
            "\int I'(\lambda)",
        "=",
        r"\underbrace{\int -\frac{1}{\lambda^2+1}dx}_{-\arctan\lambda + C}",
        "\,",
        "\,"
        )
        formula4[0].set_color(GOLD_E)
        formula4[2].set_color(BLUE)
        formula5 = MathTex(
        "I(\lambda)",
        "=",
        r"-\arctan\lambda + C",
        r"\stackrel{\lambda\to +\infty}{=}",
        "-\cfrac{\pi}{2}+C",
            "\,"
        )
        formula5[0].set_color(GOLD_E)
        formula5.shift(DOWN)
        formula50 = MathTex(
        "\lim_{\lambda\\to +\infty}I(\lambda)",
        "=",
        "\,",
        "\,",
        "-\cfrac{\pi}{2}+C"
        )
        formula50[0].set_color(GOLD_E)
        formula6 = MathTex(
        "\lim_{\lambda\\to +\infty} I(\lambda)",
        r"=\lim_{\lambda\to +\infty}\int_0^{+\infty}\frac{\sin x}{x}",
        r"\underbrace{e^{-\lambda x}}_{\to 0}",
        "dx=",
        "0"
        )
        formula6[0].set_color(GOLD_E)
        formula60 = MathTex(
        "-\cfrac{\pi}{2}+C=0",
        "\,",
        r"\Rightarrow\,",
        r"\boxed{C=\cfrac{\pi}{2}}",
        "\,"
        )
        formula60[3].set_color(PINK)
        formula7 = MathTex(
         "I(0)=",
         "\int_0^{+\infty}\\frac{\sin x}{x}dx",
         r"= \underbrace{-\arctan 0}_0 + \cfrac{\pi}{2}",
         "=",
         "\cfrac{\pi}{2}"
         )
        formula8 = MathTex(
          "\int_0^{+\infty}\\frac{\sin x}{x}dx",
          "=",
          "\cfrac{\pi}{2}",
          "\,",
          "\,"
          )
        text2 = Tex(r"\textit {Im} - imagine part")
        text2.shift(DOWN*2)
        formul = MathTex(
          r"e^{ix}",
          "=",
          r"\cos x",
          "+i",
          r"\sin x"
          )
        formul[4].set_color(GREEN)
        formul1 = MathTex(
          r"Im\,\,e^{ix}",
          "=",
          "\,",
          "\,",
          r"\sin x"
        )
        formul1[4].set_color(GREEN)
        formul2 = MathTex(
            r"=-Im\,\,\frac{1}{\lambda-i}",
            "\,",
            r"=-Im\,\,\frac{\lambda+i}{(\lambda-i)(\lambda+i)}",
            "=",
            "\,"
        )
        formul3 = MathTex(
            r"=-Im\,\,\left(\frac{\lambda}{\lambda^2+1}+\underbrace{\frac{i}{\lambda^2+1}}\right)=",
            "\,",
            "\,",
            "\,",
            r"-\frac{1}{\lambda^2+1}"
        )
        text = Tex(
            "On the other hand.."
        )

        text.set_color(BLUE)
        text1.set_color(PINK)
        formula1.shift(UP)
        formula6[2].set_color(BLUE)
        for size,pos,formula in [(1,2*UP,formula)]:
            formula.scale(size)
            formula.move_to(pos)
        self.play(Write(formula))
        self.play(ShowCreationThenFadeOut(text1), run_time=5)
        formula3.shift(UP)
        formul3.shift(1.2*DOWN)
        self.wait()
        text.shift(DOWN)
        formula6.move_to(0.2*DOWN)
        changes = [
            [(0,1,3),
            # | | | | |
            # v v v v v
             (0,1,2)],
            [(2,4),
             
             
             (3,4)]
        ]

        for pre_ind,post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    formula[i],formula1[j]
                    )
                for i,j in zip(pre_ind,post_ind)
                ],
                run_time=2
            )

        for mob in [formula1[0]]:
            self.play(Indicate(mob))


        formul1.shift(DOWN)
        self.play(Write(formul))
        self.wait
        self.play(ShowCreationThenFadeOut(text2), run_time=2)
        changes = [
            [(0, 1, 2, 3, 4),
             # | | | | |
             # v v v v v
             (0, 1, 2, 3, 4)]

        ]
        for pre_ind, post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    formul[i], formul1[j]
                )
                for i, j in zip(pre_ind, post_ind)
            ],
                      run_time=2
            )

        changes = [
            [(0,2,3),
            # | | | | |
            # v v v v v
             (0,3,4)],
            [(4,1),

             (1,2)]
        ]
        for pre_ind,post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    formula1[i],formula2[j]
                    )
                for i,j in zip(pre_ind,post_ind)
                ],
                run_time=2
            )

        changes = [
            [(0,1),
            # | | | | |
            # v v v v v
             (0,1)],

            [(2,3,4),

             (2,3,4)]
           
        ]
        for pre_ind,post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    formula2[i],formula3[j]
                    )
                for i,j in zip(pre_ind,post_ind)
                ],
                run_time=2
            )

        changes = [
            [(0, 1),
             # | | | | |
             # v v v v v
             (0, 1)],
            [(4,2,3),

             (2,4,3)]
        ]
        for pre_ind, post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    formul1[i], formul2[j]
                )
                for i, j in zip(pre_ind, post_ind)
            ],
                      run_time=2
            )
        changes = [
            [( 3, 4,2),

             (2, 0,3)],
            [(0, 1),
             # | | | | |
             # v v v v v
             (4, 1)]
        ]
        for pre_ind, post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    formul2[i], formul3[j]
                )
                for i, j in zip(pre_ind, post_ind)
            ],
                      run_time=2
            )
        changes = [
            [(4,0),
             # | | | | |
             # v v v v v
             (5,6)]
        ]
        for pre_ind, post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    formul3[i], formula3[j]
                )
                for i, j in zip(pre_ind, post_ind)
            ],
                      run_time=2
            )


        changes = [
            [(2,3),
            # | | | | |
            # v v v v v
             (1,0)],
            [(0,1),

             (2,3)],
            [(4,5,6),

             (5,6,4)]
           
        ]
        for pre_ind,post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    formula3[i],formula4[j]
                    )
                for i,j in zip(pre_ind,post_ind)
                ],
                run_time=2
            )
        changes = [
            [(0,1),
            # | | | | |
            # v v v v v
             (0,1)],
            [(4,3),

             (2,3)],
            [(2,5),

            (4,5)]
        ]
        for pre_ind,post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    formula4[i],formula5[j]
                    )
                for i,j in zip(pre_ind,post_ind)
                ],
                run_time=2
            )

        changes = [
            [(0,1,2,3,4),
            # | | | | |
            # v v v v v
             (0,1,2,3,4)]
        ]
        formula50.shift(UP)
        for pre_ind,post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    formula5[i],formula50[j]
                    )
                for i,j in zip(pre_ind,post_ind)
                ],
                run_time=2
            )


            self.play(ShowCreationThenDestruction(text),run_time=2.5)
            self.play(ShowCreationThenFadeOut(formula6),run_time=2.5)


        changes = [
            [(0,1,2,3,4),
            # | | | | |
            # v v v v v
             (0,1,2,3,4)]
           
        ]
        for pre_ind,post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    formula50[i],formula60[j]
                    )
                for i,j in zip(pre_ind,post_ind)
                ],
                run_time=2
            )


        self.play(FadeOut(formula60),run_time = 1.75)
        formula7.shift(UP)
        self.play(Write(formula7))
        changes = [
            [(1, 2),
             # | | | | |
             # v v v v v
             (0, 1)],
            [(0, 3, 4),

             (4, 3, 2)]

        ]
        for pre_ind, post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    formula7[i], formula8[j]
                )
                for i, j in zip(pre_ind, post_ind)
            ],
                      run_time=2
                      )
        self.wait(2)
        self.play(FadeOutAndShift(formula8,UP))
        
        self.wait()
    
