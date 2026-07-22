import matplotlib.pyplot as plt

def addition(pdf, n1=None, n2=None):
    if n1 == None:
        n1 = pdf.rng.integers(2, 20)

    if n2 == None:
        n2 = pdf.rng.integers(2, 20)

    q = f"What is {n1}+{n2}?"

    pdf.cell(pdf.get_string_width(q), 10, q)
    
    pdf.ln(10)

    pdf.cell(50, 10, "You must show all your workings")

    pdf.ln(50)


def multiplication(pdf, n1=None, n2=None):
    if n1 == None:
        n1 = pdf.rng.integers(2, 20)

    if n2 == None:
        n2 = pdf.rng.integers(2, 20)

    q = f"What is {n1}x{n2}?"

    pdf.cell(pdf.get_string_width(q), 10, q)
    pdf.ln(10)

if __name__ == "__main__":
    from pdf import PDF

    worksheet = PDF()
    worksheet.add_cover()

    worksheet.write_question(addition, 1)
    worksheet.write_question(multiplication, 1)

    worksheet.output("output/preset.pdf")
