import matplotlib.pyplot as plt

@register("addition")
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


if __name__ == "__main__":
    pass
