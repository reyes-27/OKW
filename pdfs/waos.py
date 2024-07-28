from fpdf import FPDF
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font('helvetica', "B", size=42)
# pdf.cell(60, 10, text="OKW", align="C", center=True)
# pdf.output("hello_world.pdf")

# from .invoice import InvoicePDF

class InvoicePDF(FPDF):
    def header(self):
        self.set_font()
        self.set_font('helvetica', "B", size=42)
        self.cell(60, 10, text="OKW", align="C", center=True)
        self.set_font('helvetica', size=14)
        self.cell(80, 10, text="Tienda de lamparas genéricas OKW dsdsds", center=True, border=True, new_x="LMARGIN", new_y="NEXT")
pdf = InvoicePDF()
pdf.add_page()
pdf.output("hello_world.pdf")