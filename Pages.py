from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle
import calendar
from datetime import datetime
from Constants import * 
from Elements import *

#This generates the first title page
def print_titlePage(pdf, title):

    #draws the year in the middle of the page
    pdf.setFont('UniSans', 50)
    pdf.setFillColorRGB(text_color[0],text_color[1],text_color[2])
    pdf.drawCentredString(300, 500, title)

    #showPage() finishes the page and moves to the next one
    pdf.showPage()

#This generates the monthly calendar pages
def print_monthPage(pdf, month, year):
    #Month name as header
    month_name = calendar.month_name[month]
    pdf.bookmarkPage(month_name,left=0,top=20)
    pdf.setFont('UniSans', 36)
    pdf.setFillColorRGB(text_color[0],text_color[1],text_color[2])
    pdf.drawString(header_location_x, 770, month_name)

    #setting up table to hold weekday name headers
    header = [['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']]
    #HARDCODED
    header_height = 10

    #I made the headers separate because I didn't realize you could pass in an array
    #and specify the individual sizes of cells. Oops.
    header_table = Table(header, table_cell_width, header_height) 
    header_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, 0), 'UniSansHeavy'), #setting header font
        ('TEXTCOLOR', (0, 0), (-1, -1), dark_color), #setting header font color
        ('FONTSIZE', (0, 0), (-1, -1), 8), #setting header font size
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'), #aligns left
        ('VALIGN', (0, 0), (-1, -1), 'TOP'), #alignt header to the top of the cell
        ('BACKGROUND', (0, 0), (-1, -1), light_bg_color) #gives header nice light bg
    ]))
    w, h = header_table.wrapOn(pdf, 400, 100) #this is important for tables else they don't work or something
    header_table.drawOn(pdf, header_location_x, header_location_y) #displaying the table

    #monthcalendar outputs a 2d array representing the month starting from Monday
    #days not in the month are filled with 0
    cal = calendar.monthcalendar(year,month)

    #Finding where all the 0s are so I can color them the page
    #background color
    lastrow = len(cal) - 1
    first_zero = 0
    last_zero = 0
    first_day = 0
    for j in range(7): #iterate through the last row and check for zeros. If no zero, then first_zero will equal 7
        if cal[lastrow][j] == 0:
            break
        first_zero+=1

    for j in range(7): #iterate through to find the start of the first day and last occuring zero in the first row
        if cal[0][j] == 1:
            first_day = j
        if cal[0][j] == 0:
            last_zero = j

    table = Table(cal, table_cell_width, table_cell_height)
    #this if and else statement is yuck but too lazy to thing of something cleaner
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

    #Adding links to table
    for row in range(len(cal)):
        for col in range(7):
            if cal[row][col] == 0:
                continue
            page_name = calendar.month_name[month] + " " + str(cal[row][col])
            table_top = header_location_y -h - header_height + len(cal)*table_cell_height
            link_x = header_location_x+col*table_cell_width
            link_y = table_top - row * table_cell_height
            pdf.linkRect(page_name, page_name,(link_x,link_y ,link_x + table_cell_width,link_y -table_cell_height), relative = 1)
    #bottom half of the page below the table

    middle = page_width / 2
    #Setting up the colors and fonts I want
    pdf.setFillColor(light_line_color)
    pdf.setStrokeColor(light_line_color)
    #Drawing rectangles where the goals and reflections are going to be
    pdf.rect(header_location_x-2, header_location_y -h - header_height - 42, 225,16, fill = 1)
    pdf.rect(middle-2, header_location_y -h - header_height - 42, 225,16, fill = 1)
    pdf.setFont('UniSans', 12)
    pdf.setFillColorRGB(dark_color[0],dark_color[1],dark_color[2])

    #drawing string that says goals on the left
    pdf.drawString(header_location_x, header_location_y -h - header_height - 40, "goals")
    #drawing string that says "reflection" in the middle
    pdf.drawString(middle, header_location_y -h - header_height - 40, "reflection")

    #drawing questions
    pdf.setFillColorRGB(text_color[0],text_color[1],text_color[2])
    pdf.setFont('UniSans', 8)
    pdf.drawString(middle, header_location_y -h - header_height - 60, "What did you acheive this month?")
    pdf.drawString(middle, header_location_y -h - header_height - 120, "How did you feel about this month?")
    pdf.drawString(middle, header_location_y -h - header_height - 180, "List 3 things you are grateful for.")

    pdf.drawString(header_location_x, header_location_y -h - header_height - 60, "What aspects of yourself do you want to work on?")
    pdf.drawString(header_location_x, header_location_y -h - header_height - 120, "What skills do you want to work on?")
    pdf.drawString(header_location_x, header_location_y -h - header_height - 180, "How do you plan to take care of yourself?")
    
    #drawing a dividing line 
    pdf.line(header_location_x,header_location_y -h - header_height - 240,page_width-header_location_x-40, header_location_y -h - header_height - 240)

    #adding a spent and earned section at the bottom so I know how much money I don't have
    pdf.setFont('UniSans', 12)
    pdf.setFillColorRGB(dark_color[0],dark_color[1],dark_color[2])
    pdf.drawString(header_location_x, header_location_y -h - header_height - 280, "spent:")

    pdf.drawString(header_location_x  + 100, header_location_y -h - header_height - 280, "earned:")
    pdf.setFillColorRGB(text_color[0],text_color[1],text_color[2])

    #adding the tabs to the side
    sideBar(pdf)
    pdf.showPage()

#This generates the daily planner pages
def print_day_page(pdf,year, month, day):

    #heading
    #weekday is in one style starting from the left
    title = weekdays[calendar.weekday(year, month, day)]
    pdf.setFont('UniSans', 36)
    pdf.setFillColor(text_color)
    pdf.drawString(header_location_x, 770, title)
    #month and day of month are in a different style starting from the middle
    subtitle = calendar.month_name[month] + " " + str(day)
    pdf.setFont('UniSansHeavy', 24)
    pdf.setFillColor(dark_color)
    pdf.drawString(middle, 770, subtitle)

    pdf.bookmarkPage(subtitle,left=0,top=20)
    #time table
    hours = []
    #checking constants from Constants.py that specify how the table should be built
    end = activeHoursHalf if halfhoursubvision else activeHoursFull
    for i in range(starttime, starttime + end + 1):
        hours.append([str(i%24)])
        if(halfhoursubvision): #change halfhoursubvision to true if you want the 30 minute subdivision
            hours.append([" "])

    #HARDCODED: the height of the time table cells 
    cell_width  = page_width/2 - header_location_x - 20
    table = Table(hours, cell_width, halftimesheetcellheight if halfhoursubvision else singletimesheetcellheight)
    table.setStyle(TableStyle([
            ('FONT', (0, 0), (-1, -1), 'UniSans'),
            ('TEXTCOLOR', (0, 0), (-1, -1), dark_color),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, light_line_color),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LINEBELOW',(0,0),(-1,-1),1, light_line_color)
        ]))
    w, h = table.wrapOn(pdf, 0, 0)
    table.drawOn(pdf, header_location_x, header_location_y+50-h)

    #Fillable mood faces
    #size of faces
    faceSize = 10
    pdf.setFont("UniSans", 18)
    pdf.drawString(middle, 730, "mood:")
    pdf.setStrokeColor(text_color)
    #happyface
    face(pdf, middle + 100, 730 + faceSize/2, -faceSize/2, faceSize)
    #neutralface
    face(pdf, middle + 150, 730 + faceSize/2, 0, faceSize)
    #sad face
    face(pdf, middle + 200, 730 + faceSize/2, faceSize/2, faceSize)

    pdf.drawString(middle, 700, "ToDo:")
    todo_list(pdf, todoLength, middle+10, 680)

    pdf.line(middle + 5, 680 - todoInterval * todoLength, page_width-header_location_x-40, 680 - todoInterval * todoLength)
    
    pdf.drawString(middle, 650 - todoInterval * todoLength, "notes:")

    pdf.line(middle + 5, 60, page_width-header_location_x-40, 60)
    pdf.setFont("UniSans", 12)
    pdf.setStrokeColor(light_line_color)
    daily_affirmation(pdf, datetime(year, month, day).timetuple().tm_yday)
    sideBar(pdf)
    pdf.showPage()

def testPage(pdf):
    face(pdf, header_location_x, header_location_y, -10)
    pdf.showPage()

def sticker_page(pdf):
    pdf.bookmarkPage("stickers",left=0,top=20)
    #heading
    pdf.setFont('UniSans', 36)
    pdf.setFillColor(text_color)
    pdf.drawString(header_location_x, 770, "stickers")

    sideBar(pdf)
    pdf.showPage()