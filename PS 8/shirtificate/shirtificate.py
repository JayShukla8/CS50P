from fpdf import FPDF
pdf = FPDF()

def main():
    name = input("Name: ")
    pdf.add_page()
    pdf.set_font("helvetica", "B", 50)
    pdf.set_y(20)             #page is by default A4 size and measured in mm's (297mm x 210mm)
    pdf.cell(0, text='CS50 Shirtificate', align='C')
    pdf.set_y(0)
    pdf.image("shirtificate.png", x="C", y=70, w=pdf.epw)
    pdf.set_text_color(255, 255, 255) #white text
    pdf.set_font_size(30)
    pdf.cell(0, 300, text=f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
