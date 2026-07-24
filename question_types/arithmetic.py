from base import BaseQuestion
from paper import Pair

class Addition1(BaseQuestion):
    marks = 1
    dependencies = ()
    workings_height = 30

    ops_ranges = ((2, 11), (2, 11))

    @classmethod
    def question(cls, pdf, ops):
        pdf.cell(0, 10, f"What is {ops[0]} + {ops[1]}")

    @classmethod
    def workings(cls, pdf, ops):
        pdf.ln(15)
        pdf.set_text_color(255, 0, 0)
        pdf.set_font(style="B")

        answer = str(ops[0] + ops[1])

        pdf.cell(0, 10, f"{ops[0]} + {ops[1]} = {answer}")

        pdf.ln(15)

        length = pdf.get_string_width(answer)

        pdf.set_x(pdf.w - pdf.r_margin - length - 10)

        pdf.cell(0, 10, answer)

        pdf.set_text_color(0, 0, 0)

if __name__ == "__main__":
    test = Pair("output/QP1.pdf", "output/MS1.pdf")

    for _ in range(10):
        Addition1.write(test.QP, test.MS)

    test.output()
