# Quesiton Template
"""
class NAME_HERE(BaseQuestion):
    marks = 
    dependencies = ()
    workings_height = 

    ops_ranges = ((x, y), (x, y))

    @classmethod
    def question_details(cls, pdf, ops):
        pass

    @classmethod
    def workings(cls, pdf, ops):
        pass
"""

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
    def insert(cls, pdf, workings=False):
        ops = cls.gen_ops(pdf)

        cls.question(pdf, ops)

        if workings:
            pdf.set_text_color(255, 0, 0)
            pdf.set_font(style="B")
            
            pdf.set_draw_color(255, 0, 0)
            pdf.set_line_width(0.5)

            cls.workings(pdf, ops)

            pdf.set_text_color(0, 0, 0)
            pdf.set_draw_color(0, 0, 0)
            pdf.set_line_width(0.2)

        else:
            pdf.ln(cls.workings_height)
    
    @classmethod
    def question(cls, pdf, ops):
        pdf.cell(0, 10, f"Example question {ops[0]} {ops[1]}")

    @classmethod
    def workings(cls, pdf, ops):
        pdf.ln(15)

        pdf.set_text_color(255, 0, 0)
        
        answer = f"Example answer {ops[0]}"

        pdf.set_x(pdf.w-pdf.r_margin-pdf.get_string_width(answer))

        pdf.cell(0, 10, answer)

        pdf.set_text_color(0, 0, 0)

    @classmethod
    def write(cls, qp, ms):
        qp.write_question(cls.insert, cls.marks)  # TODO: Rename write_question to question format or similar

        ms.write_question(cls.insert, cls.marks, func_params={"workings": True})

if __name__ == "__main__":
    from paper import Pair

    test = Pair("output/QP.pdf", "output/MS.pdf")
    
    for _ in range(10):
        BaseQuestion.write(test.QP, test.MS)

    test.output()
