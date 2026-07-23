class BaseQuestion:
    marks = 1
    dependencies = ()
    
    @classmethod
    def gen_ops(cls, pdf):
        ops = [
            pdf.rng.integers(1, 10),
            pdf.rng.integers(1, 10)
        ]
        return ops

    @classmethod
    def add_q(cls, pdf):
        ops = cls.gen_ops(pdf)
        pdf.cell(0, 10, f"Example question {ops[0]} {ops[1]}")

        pdf.ln(15)

    @classmethod
    def add_a(cls, pdf):
        ops = cls.gen_ops(pdf)
        pdf.cell(0, 10, f"Example question {ops[0]} {ops[1]}")

        pdf.ln(15)

        pdf.set_text_color(255, 0, 0)
        
        pdf.set_x(pdf.w-pdf.r_margin-pdf.get_string_width("Example answer"))

        pdf.cell(0, 10, "Example answer")

        pdf.set_text_color(0, 0, 0)

    @classmethod
    def write(cls, qp, ms):
        cls.add_q(qp)
        cls.add_a(ms)

if __name__ == "__main__":
    from paper import Pair

    test = Pair("output/QP.pdf", "output/MS.pdf")
    
    for _ in range(10):
        test.QP.write_question(BaseQuestion.add_q, 1)
        test.MS.write_question(BaseQuestion.add_a, 1)

    test.output()
