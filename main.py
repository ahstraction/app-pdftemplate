from fpdf import FPDF
import pandas as pd
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df= pd.read_csv("C:/Users/Dell/OneDrive/Documents/Python/app-pdftemplate/topics.csv")

# Set the header 
for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0,  h=12, txt=row["Topic"], align="L", ln=1)
    for y in range(20,280,20):
        pdf.line(10,y,200,y )
#Set the Footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=10,txt=row["Topic"],align="R")
# Added extra page    
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(265)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0,h=10,txt=row["Topic"],align="R")
        for y in range(20,280,15):
            pdf.line(10,y,200,y )
pdf.output("output.pdf")