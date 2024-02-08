from Constants import *
import calendar

def sideBar(pdf):
    
    pdf.setStrokeColorRGB(light_line_color[0],light_line_color[1],light_line_color[2])
    pdf.setFont('UniSans', 12)
    tabWidth = 40
    tabHeight = page_height/12

    for i in range(1,13):
        month_name=calendar.month_name[i]
        pdf.saveState()
        pdf.translate(page_width - tabWidth,tabHeight*(13-i))
        pdf.rotate(270)
        pdf.setFillColorRGB(medium_bg_color[0],medium_bg_color[1],medium_bg_color[2])
        pdf.rect(0,0,tabHeight,tabWidth, stroke=1,fill = 1)
        pdf.linkRect(month_name, month_name,(0,0,tabHeight,tabWidth), relative = 1)
        pdf.setFillColorRGB(dark_color[0],dark_color[1],dark_color[2])
        pdf.drawString(5,5, calendar.month_name[i])
        pdf.restoreState()
