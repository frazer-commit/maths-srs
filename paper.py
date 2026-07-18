from fpdf import FPDF
import matplotlib.pyplot as plt
import numpy as np
import copy

class PDF(FPDF):
    q_num = 0  # Make a part of init

    @staticmethod
    def continuous(function):
        def wrapper(self, *args, **kwargs):
            temp_pdf = copy.deepcopy(self)

            # Missing Code
            function(temp_pdf, *args, **kwargs)

            if temp_pdf.page_no() != 1:
                print("Page added")
                self.add_page()
            else:
                print("Page not added")

            return function(self, *args, **kwargs)
        return wrapper

    @continuous 
    def write_question(self, func, marks, d_line=True, func_params={}):
        self.q_num += 1

        self.set_font("helvetica", "B", 18)
        self.cell(self.get_string_width(str(self.q_num)) + 10, 10, str(self.q_num))
 
        func(self, **func_params)

        if d_line:
            self.ln(10)
            self.set_draw_color(0, 0, 0)
            self.set_dash_pattern(dash=1, gap=1)
            
            self.line(x1 = self.w - self.r_margin - 45,
                      x2 = self.w- self.r_margin,
                      y1 = self.get_y(),
                      y2 = self.get_y())

            self.set_dash_pattern()

            self.ln(5)

        self.set_font("helvetica", "B", 14)

        marks_msg = f"(Total for Question {self.q_num} is {marks} mark{"s"*(marks>1)})"
        
        self.set_x(self.w - self.r_margin - self.get_string_width(marks_msg))
        self.cell(w = self.get_string_width(marks_msg),
                  h= 10,
                  text=marks_msg)

        self.ln(15)

        self.line(x1 = self.l_margin,
                  x2 = self.w - self.r_margin,
                  y1 = self.get_y(),
                  y2 = self.get_y())

        self.ln(10)

def addition(pdf, *, n1=3, n2=5):
    i_x = pdf.x 

    pdf.set_font("helvetica", "", 18)
    q = f"What is {n1}+{n2}?"

    pdf.cell(pdf.get_string_width(q), 10, q)
    
    pdf.ln(10)
    pdf.set_x(i_x)

    pdf.cell(50, 10, "You must show all your workings")

    pdf.ln(50)

worksheet = PDF()
worksheet.add_page()

worksheet.write_question(addition, 2, func_params={"n1": 1})
worksheet.write_question(addition, 2)
worksheet.write_question(addition, 2)

worksheet.output("output/test.pdf")
