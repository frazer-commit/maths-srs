from fpdf import FPDF
import matplotlib.pyplot as plt
import numpy as np
import copy

class QP(FPDF):
    def __init__(self, seed=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self._x_indent = 10
        self.skip_header = False
        self.q_num = 0  

        if seed == None:
            self.seed = np.random.randint(100_000, 1_000_000)
        else:
            self.seed = seed
        self.rng = np.random.default_rng(self.seed)

    def indent(self, behaviour=None):
        match behaviour:
            case "u":
                self._x_indent = self.x
            case "r":
                self._x_indent = self.l_margin

        return self._x_indent

    def add_cover(self):
        self.skip_header = True
        self.add_page()
        self.skip_header = False

        self.set_font("Helvetica", "", 30)
        self.multi_cell(0, 20, "This is a cover")

        self.ln(10)
        
        self.add_page()

    def header(self):
        if self.skip_header == True:
            return

        x = self.l_margin - 5
        y = self.t_margin - 5
        w = self.w - self.l_margin - self.r_margin + 10
        h = self.h - self.t_margin - self.b_margin + 10


        self.set_draw_color(0, 0, 0)
        self.set_line_width(1)
        self.rect(x, y, w, h, round_corners=True, corner_radius=5)

        self.set_xy(self.l_margin, self.t_margin)

    def footer(self):
        self.set_y(-15)
        self.set_font("times", "", 12)

        self.set_char_spacing(5)
        self.cell(0, 10, f"{self.seed}", align='C')
        self.set_char_spacing(0)

    def ln(self, *args, **kwargs):
        super().ln(*args, **kwargs)

        self.set_x(self.indent())

    @staticmethod
    def continuous(function):
        def wrapper(self, *args, **kwargs):
            temp_pdf = copy.deepcopy(self)

            # Missing Code
            function(temp_pdf, *args, **kwargs)

            if temp_pdf.page_no() != self.page_no():
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

        self.set_font("helvetica", "", 18)

        self.indent("u")
        func(self, **func_params)
        self.indent("r")

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


if __name__ == "__main__":
    worksheet = QP()
    worksheet.add_cover()

    worksheet.output("output/test.pdf")
