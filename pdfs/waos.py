from fpdf import FPDF
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font('helvetica', "B", size=42)
# pdf.cell(60, 10, text="OKW", align="C", center=True)
# pdf.output("hello_world.pdf")

# from .invoice import InvoicePDF

class InvoicePDF(FPDF):
    def header(self):
        self.set_font('helvetica', "B", size=42)
        self.cell(60, 10, text="OKW", align="C", center=True)
        self.ln(15)
        self.set_font('helvetica', size=14)
        self.cell(
            100,
            50, 
            center=True, 
            border=True, 
            markdown=True
            )
        self.cell(
            100,
            10, 
            text=" == Tienda de lamparas genéricas OKW ==", 
            center=True, 
        )
        self.ln(10)
        self.cell(
            30,
            10,
            text="RUT:111777999",
            center=True,
        )
        self.ln(45)
        self.cell(text="Detalle", center=1)
pdf = InvoicePDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

for m in ["Hola", "como", "estás?"]:
    pdf.ln(10)
    pdf.cell(text=m)
pdf.output("hello_world.pdf")