from fpdf import FPDF

class InvoicePDF(FPDF):
    def header(self):
        self.set_font()
        self.set_font('helvetica', "B", size=42)
        self.cell(60, 10, text="OKW", align="C", center=True)