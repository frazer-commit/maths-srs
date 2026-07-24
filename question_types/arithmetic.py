from base import BaseQuestion
from paper import Pair
import numpy as np

class Addition1(BaseQuestion):
    marks = 1
    dependencies = ()
    workings_height = 30

    ops_ranges = ((2, 11), (2, 11))

    @classmethod
    def question(cls, pdf, ops):
        pdf.cell(0, 10, f"What is {ops[0]} + {ops[1]}?")

    @classmethod
    def workings(cls, pdf, ops):
        pdf.ln(15)

        answer = str(ops[0] + ops[1])

        pdf.cell(0, 10, f"{ops[0]} + {ops[1]} = {answer}")

        pdf.ln(15)

        length = pdf.get_string_width(answer)

        pdf.set_x(pdf.w - pdf.r_margin - length - 10)

        pdf.cell(0, 10, answer)


class Addition2(Addition1):
    marks = 2
    dependencies = (Addition1)
    workings_height = 60

    ops_ranges = ((100, 1000), (100, 1000))
        
    @classmethod
    def workings(cls, pdf, ops):
        answer = ops[0] + ops[1]

        carries = []
        for i in range(3):
            get_digit = lambda n: (n // (10**i)) % 10
            if max(get_digit(ops[0]), get_digit(ops[1])) > get_digit(answer):
                carries.append("1")
            else:
                carries.append(" ")

        carries = carries[::-1]

        table_data = (
            (" ", *str(ops[0])),
            ("+", *str(ops[1])),
            list(str(answer).rjust(4)),
            (*carries, " ")
        )
        
        pdf.ln(15)


        with pdf.table(width=40,
                       text_align="C",
                       line_height=10,
                       first_row_as_headings=False,
                       align="LEFT") as table:
            row = table.row()
            for element in table_data[0]:
                row.cell(element, border="None")

            row = table.row()
            for element in table_data[1]:
                row.cell(element, border="None")

            row = table.row()
            for element in table_data[2]:
                row.cell(element, border="TOP")
 
            old_font = pdf.font_size_pt

            pdf.set_font(size=14)

            row = table.row()
            for element in table_data[3]:
                row.cell(element, border="None")
            
            pdf.set_font(size=old_font, style="B")


        pdf.ln(5)

        length = pdf.get_string_width(str(answer))
        pdf.set_x(pdf.w - pdf.r_margin - length - 10)
        pdf.cell(0, 10, str(answer))

if __name__ == "__main__":
    test = Pair("output/QP1.pdf", "output/MS1.pdf")

    for _ in range(4):
        Addition1.write(test.QP, test.MS)

    for _ in range(4):
        Addition2.write(test.QP, test.MS)
    test.output()
