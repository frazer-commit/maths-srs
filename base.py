class BaseQuestion:
    marks = 1
    dependencies = ()
    workings_height = 15

    ops_ranges = ((1, 10), (1, 10))

    @classmethod
    def gen_ops(cls, pdf):
        ops = [pdf.rng.integers(*r) for r in cls.ops_ranges]
        return ops

    @classmethod
    def add_question(cls, pdf, space=True):
        ops = cls.gen_ops(pdf)

        cls.question_detail(pdf, ops)

        if space:
            pdf.ln(cls.workings_height)
    
    @classmethod
    def question_detail(cls, pdf, ops):
        pdf.cell(0, 10, f"Example question {ops[0]} {ops[1]}")

    @classmethod
    def workings(cls, pdf):
        pdf.ln(15)

        pdf.set_text_color(255, 0, 0)
        
        pdf.set_x(pdf.w-pdf.r_margin-pdf.get_string_width("Example answer"))

        pdf.cell(0, 10, "Example answer")

        pdf.set_text_color(0, 0, 0)

    @classmethod
    def write(cls, qp, ms):
        qp.write_question(cls.add_question, cls.marks)  # TODO: Rename write_question to question format or similar

        ms_func = lambda x: (cls.add_question(x, space=False), cls.workings(x))

        ms.write_question(ms_func, cls.marks)

if __name__ == "__main__":
    from paper import Pair

    test = Pair("output/QP.pdf", "output/MS.pdf")
    
    for _ in range(10):
        BaseQuestion.write(test.QP, test.MS)

    test.output()
