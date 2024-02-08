from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle
import calendar
from Constants import *
from Elements import *

#This generates the first title page
def print_titlePage(pdf, title):
    pdf.setFont('UniSans', 50)
    pdf.setFillColorRGB(text_color[0],text_color[1],text_color[2])
    pdf.drawCentredString(300, 500, title)

    #showPage() finishes the page and moves to the next one
    pdf.showPage()

#This generates the monthly calendar pages
def print_monthPage(pdf, month, year):
    header_location_x = 30
    month_name = calendar.month_name[month]
    pdf.bookmarkPage(month_name,left=0,top=20)
    pdf.setFont('UniSans', 36)
    pdf.setFillColorRGB(text_color[0],text_color[1],text_color[2])
    pdf.drawString(header_location_x, 770, month_name)

    header = [['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']]
    header_height = 10

    #I made the headers separate because I didn't realize you could pass in an array
    #and specify the individual sizes of cells. Oops.
    header_table = Table(header, table_cell_width, header_height)
    header_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, 0), 'UniSansHeavy'),
        ('TEXTCOLOR', (0, 0), (-1, 0), text_color),
        ('TEXTCOLOR', (0, 0), (-1, -1), dark_color),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BACKGROUND', (0, 0), (-1, -1), light_bg_color)
    ]))
    w, h = header_table.wrapOn(pdf, 400, 100)
    header_location_y = 700
    header_table.drawOn(pdf, header_location_x, header_location_y)

    cal = calendar.monthcalendar(year,month)

    #Finding where all the 0s are so I can color them the page
    #background color
    lastrow = len(cal) - 1
    first_zero = 0
    last_zero = 0
    first_day = 0
    for j in range(7):
        if cal[lastrow][j] == 0:
            break
        first_zero+=1

    for j in range(7):
        if cal[0][j] == 1:
            first_day = j
        if cal[0][j] == 0:
            last_zero = j

    table = Table(cal, table_cell_width, table_cell_height)
    if first_zero > 6:
        table.setStyle(TableStyle([
            ('FONT', (0, 0), (-1, -1), 'UniSans'),
            ('TEXTCOLOR', (0, 0), (-1, -1), dark_color),
            ('TEXTCOLOR', (0, 0), (last_zero, 0), paper_color),
            ('TEXTCOLOR', (first_day, 0), (first_day, 0), dark_color),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, light_line_color),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LINEABOVE',(0,0),(-1,-1),1, text_color)
        ]))
    else:
        table.setStyle(TableStyle([
            ('FONT', (0, 0), (-1, -1), 'UniSans'),
            ('TEXTCOLOR', (0, 0), (-1, -1), dark_color),
            ('TEXTCOLOR', (first_zero, lastrow), (-1, -1), paper_color),
            ('TEXTCOLOR', (0, 0), (last_zero, 0), paper_color),
            ('TEXTCOLOR', (first_day, 0), (first_day, 0), dark_color),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, light_line_color),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LINEABOVE',(0,0),(-1,-1),1, text_color)
        ]))
    w, h = table.wrapOn(pdf, 0, 0)
    table.drawOn(pdf, header_location_x, header_location_y -h - header_height)

    pdf.setFont('UniSans', 12)
    pdf.setFillColorRGB(text_color[0],text_color[1],text_color[2])
    pdf.drawString(header_location_x, header_location_y -h - header_height - 20, "goals")

    
    sideBar(pdf)
    pdf.showPage()

