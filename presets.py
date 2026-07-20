from pdf import PDF

# Some day use Pandas for this

REGISTRY = {}

def register(name):
    def wrapper(func):
        REGISTRY[name] = func
        return func
    return wrapper

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
    worksheet = PDF()
    worksheet.add_page()
    worksheet.set_font("helvetica", "", 14)
    
    REGISTRY["addition"](worksheet)

    worksheet.output("output/preset.pdf")
