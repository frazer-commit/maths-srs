import matplotlib.pyplot as plt
import pandas as pd
import json

# Set the "deck" containing question data
with open("config.json") as f:
    CONFIG = json.load(f)

try:
    deck = pd.read_csv(CONFIG["save_path"], index_col="name")
except:
    deck = pd.DataFrame(columns=["name"]).set_index("name")

print(deck)

# Dict to link function names in deck to functions
REGISTRY = {}

def register(**kwargs):
    def decorator(fn):
        fn_name = fn.__name__
        REGISTRY[fn_name] = fn

        for column, value in kwargs.items():
            deck.loc[fn_name, column] = value

        return fn
    return decorator

@register(marks=1)
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

@register(marks=2)
def multiplication(pdf, n1=None, n2=None):
    if n1 == None:
        n1 = pdf.rng.integers(2, 20)

    if n2 == None:
        n2 = pdf.rng.integers(2, 20)

    q = f"What is {n1}x{n2}?"

    pdf.cell(pdf.get_string_width(q), 10, q)
    pdf.ln(10)

deck.to_csv(CONFIG["save_path"])

if __name__ == "__main__":
    from pdf import PDF

    worksheet = PDF()
    worksheet.add_cover()

    worksheet.write_question(addition, 1)
    worksheet.write_question(multiplication, 1)

    worksheet.output("output/preset.pdf")
