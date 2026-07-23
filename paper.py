from fpdf import FPDF
import matplotlib.pyplot as plt
import numpy as np
import copy

class Paper(FPDF):
    def __init__(self, seed=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self._x_indent = self.l_margin
        self.skip_header = False
        self.q_num = 0  # Question Number

        # Seed Generation
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

    def add_cover(self, title):
        # TODO: Add skip_header paramater to add_page
        self.skip_header = True  # Ensures border isn't generated
        self.add_page()
        self.skip_header = False

        self.set_font("Helvetica", "", 30)
        self.multi_cell(0, 20, title)

        self.ln(10)
        
        self.add_page()

    def header(self):
        if self.skip_header == True:
            return

        # Draw border inside the margin
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

            # Test if it fits on a carbon copy
            function(temp_pdf, *args, **kwargs)

            if temp_pdf.page_no() != self.page_no():
                self.add_page()

            return function(self, *args, **kwargs)
        return wrapper

    @continuous 
    def write_question(self, func, marks, d_line=True, func_params={}):
        # TODO: Move marks and dotted line behavior into question class
        self.q_num += 1

        # Write quesiton number
        self.set_font("helvetica", "B", 18)
        self.cell(self.get_string_width(str(self.q_num)) + 10, 10, str(self.q_num))
        self.set_font("helvetica", "", 18)

        # Write question indented
        self.indent("u")
        func(self, **func_params)
        self.indent("r")

        # TODO: Move this to dotted line function
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

        # Display marks
        self.set_font("helvetica", "B", 14)

        marks_msg = f"(Total for Question {self.q_num} is {marks} mark{"s"*(marks>1)})"
        
        self.set_x(self.w - self.r_margin - self.get_string_width(marks_msg))
        self.cell(w = self.get_string_width(marks_msg),
                  h= 10,
                  text=marks_msg)

        self.ln(15)

        # Draw line to seperate between questions
        self.line(x1 = self.l_margin,
                  x2 = self.w - self.r_margin,
                  y1 = self.get_y(),
                  y2 = self.get_y())

        self.ln(10)

class Pair():
    def __init__(self, QP_path: str, MS_path: str):
        self.QP_path = QP_path
        self.MS_path = MS_path

        self.seed = gen_seed()

        self.QP = Paper(self.seed)
        self.QP.add_cover("Question Paper")  # TODO: Show current day functionality?

        self.MS = Paper(self.seed)
        self.MS.add_cover("Mark Scheme")

    def output(self):
        self.QP.output(self.QP_path)  # TODO: Add path variable to Paper class
        self.MS.output(self.MS_path)

    def add_question(self, quesion_name):
        # TODO: Make this fetch from REGISTRY at later date
        pass

def gen_seed():
    seed = np.random.randint(100_000, 1_000_000)
    return seed

if __name__ == "__main__":
    test = Pair("output/QP.pdf", "output/MS.pdf")

    test.output()
