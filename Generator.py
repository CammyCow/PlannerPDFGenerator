from Pages import *
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

#main start if python had main functions
fileName = 'sample.pdf'
documentTitle = 'sample'
year = 2024

pdf = canvas.Canvas(fileName)

pdf.setTitle(documentTitle)

pdfmetrics.registerFont(TTFont('UniSans', 'UniSansDemo-ThinCAPS.ttf'))
pdfmetrics.registerFont(TTFont('UniSansHeavy', 'UniSansDemo-HeavyCAPS.ttf'))

print_titlePage(pdf, str(year))
for i in range(1, 13):
    print_monthPage(pdf,i, year)
    days_in_month = calendar.monthrange(year, i)[1]
    for day in range(1, days_in_month + 1):
        print_day_page(pdf, year, i, day)
#testPage(pdf)
sticker_page(pdf)
pdf.save()

