from Constants import *
import calendar

def sideBar(pdf):
    
    pdf.setStrokeColor(light_line_color)
    pdf.setFont('UniSansHeavy', 10)
    tabWidth = 40
    number_of_tabs = 12 + len(tabs)
    tabHeight = page_height/number_of_tabs

    for i in range(1,13):
        month_name=calendar.month_name[i]
        pdf.saveState()
        pdf.translate(page_width - tabWidth,tabHeight*(len(tabs) + 13-i))
        pdf.rotate(270)
        pdf.setFillColor(medium_bg_color)
        pdf.rect(0,0,tabHeight,tabWidth, stroke=1,fill = 1)
        pdf.linkRect(month_name, month_name,(0,0,tabHeight,tabWidth), relative = 1)
        pdf.setFillColor(dark_color)
        pdf.drawString(5,5, calendar.month_name[i])
        pdf.restoreState()

    for i in range(len(tabs)):
        pdf.saveState()
        pdf.translate(page_width - tabWidth,tabHeight*(len(tabs) -i))
        pdf.rotate(270)
        pdf.setFillColor(medium_bg_color)
        pdf.rect(0,0,tabHeight,tabWidth, stroke=1,fill = 1)
        pdf.linkRect(tabs[i], tabs[i],(0,0,tabHeight,tabWidth), relative = 1)
        pdf.setFillColor(dark_color)
        pdf.drawString(5,5, tabs[i])
        pdf.restoreState()
def face(pdf, locationx, locationy, mouthcurve,size):
    radius = size
    mouthadjustment = radius/4 if mouthcurve <= 0 else radius/2
    pdf.circle(locationx,locationy,radius)
    pdf.circle(locationx- radius/2, locationy + radius/4, size/5)
    pdf.circle(locationx+ radius/2, locationy + radius/4, size/5)
    pdf.bezier(locationx- radius/2, locationy - mouthadjustment, locationx- radius/4,  locationy -mouthadjustment + mouthcurve,locationx+ radius/4,  locationy - mouthadjustment+mouthcurve,locationx + radius/2, locationy - mouthadjustment)

def todo_list(pdf, lines, locationx, locationy):
    radius = 3
    for i in range(lines):
        pdf.circle(locationx,locationy - i*todoInterval,radius)

def wrap_text(canvas, text, max_width):
    lines = []
    while text:
        # Find the index of the first space that fits within the max_width
        index = len(text)
        if(canvas.stringWidth(text[:index], "UniSans", 12) > max_width):
            while canvas.stringWidth(text[:index], "UniSans", 12) > max_width:
                index -= 1
            index = int(text.rfind(' ', 0, index))
            if index == -1:
                # No space found that fits, so just use the max width
                index = int(max_width)
        lines.append(text[:index].strip())
        text = text[index:].strip()
    return lines

def draw_wrapped_text(canvas, text, x, y, max_width, leading):
    lines = wrap_text(canvas, text, max_width)
    for line in lines:
        canvas.drawString(x, y, line)
        y -= leading

def daily_affirmation(pdf, day):
    draw_wrapped_text(pdf, listofaffirmations[day%len(listofaffirmations)], middle + 5, 40, wordwrap, 15 )

