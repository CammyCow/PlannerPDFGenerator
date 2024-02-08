#Follow geeksforgeeks.org tutorial for report lab
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
import calendar


def print_titlePage(pdf, title):
    pdf.setFont('UniSans', 36)
    pdf.drawCentredString(300, 770, title)

    pdf.showPage()

def print_monthPage(pdf, month):
    month_name = calendar.month_name[month]
    pdf.setFont('UniSans', 36)
    pdf.drawCentredString(300, 770, month_name)

    cal = [['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']]
    cal.extend(calendar.monthcalendar(2024,1))

    table = Table(cal, 7*[inch], len(cal) * [inch])
    table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'UniSans'),
        ('FONT', (0, 0), (-1, 0), 'UniSansHeavy'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.green),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    w, h = table.wrapOn(pdf, 400, 100)
    table.drawOn(pdf, w, h)
    pdf.showPage()

fileName = 'sample.pdf'
documentTitle = 'sample'
title = '2024'

pdf = canvas.Canvas(fileName)

pdf.setTitle(documentTitle)

pdfmetrics.registerFont(TTFont('UniSans', 'UniSansDemo-ThinCAPS.ttf'))
pdfmetrics.registerFont(TTFont('UniSansHeavy', 'UniSansDemo-HeavyCAPS.ttf'))

pdf.setFont('UniSans', 36)
pdf.drawCentredString(300, 770, title)

print_titlePage(pdf, title)
print_monthPage(pdf,1)

pdf.save()

