from reportlab.lib import colors

#constants
#colors
light_bg_color = (246/256, 255/256, 248/256)
light_line_color = (234/256, 244/256, 244/256)
medium_bg_color = (204/256,227/256,222/256)
text_color = (164/256,195/256,178/256)
dark_color = (107/256,144/256,128/256)
paper_color = colors.white

#tabs
tabs = ["stickers"]
#sizing
table_cell_width = 70
table_cell_height = 75
page_width = 595
page_height = 842
header_location_x = 30
header_location_y = 700
middle = page_width / 2
todoInterval = 25
todoLength = 10
#time
starttime = 6
activeHoursHalf = 19
activeHoursFull = 23
halfhoursubvision = False
halftimesheetcellheight = 20
singletimesheetcellheight = 30
weekdays = ['Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

#affirmations source: https://www.ellduclos.blog/100-positive-affirmations/
wordwrap =  middle-header_location_x-40
affirmationcounter = 0
listofaffirmations = [
    "I choose what I become",
    "Today and everyday I choose to be happy",
    "I am capable of achieving anything I set my mind to.",
    "I am worthy of increasing my income.",
    "The setbacks are just redirecting me to something bigger and better.",
    "Today and everyday I release all the negativity.",
    "I make peace with what I can't control.",
    "I make peace with my past and I am ready to receive the good that comes my way.",
    "I am thankful for all I have and all I will accomplish.",
    "I am a magnet for positivity and blessings.",
    "I forgive myself.",
    "I believe in myself and all of my abilities.",
    "I am strong and I am powerful.",
    "I deserve to be happy.",
    "I am enough.",
    "I am brave and I will go after what makes me happy.",
    "I am proud of who I am and all that I have and will accomplish.",
    "Today is going to be the best day.",
    "I deserve self-care.",
    "I will trust the timing of my life and be grateful for the good that is to come.",
    "I am beautiful and I love all aspects of me and who I am.",
    "I attract opportunity.",
    "I love my body.",
    "I am determined to succeed.",
    "I choose to be optimistic.",
    "I know who I am and I know what I deserve.",
    "I am resilient.",
    "I strive to have a growth mindset.",
    "I accept the good things that are coming my way.",
    "I no longer fear the unknown.",
    "I choose to focus only on what I can control.",
    "I am enough.",
    "I am resilient enough to take on every obstacle that stands in my way.",
    "My past does not define my future.",
    "I choose to be fearless today and everyday.",
    "I choose to step outside of my comfort zone and do the unthinkable.",
    "I trust myself, I trust my intuition, I trust my judgement and I will make the best choices for me.",
    "Done is better than perfect.",
    "I will accomplish anything I focus on.",
    "I am a positive person who attracts positivity.",
    "I release all doubts and insecurities about myself.",
    "Today I choose to make myself happy.",
    "I have the courage to be the happiest, healthiest and most successful version of myself.",
    "I will attract what belongs to me.",
    "I am a money magnet.",
    "I have the power to create the life I desire.",
    "Today I let go of anything that doesn't add to my happiness and goals.",
    "I am allowed to say no to others and yes to myself.",
    "All that I need comes to me at the right time.",
    "I will not compare myself to others.",
    "I am talented and intelligent.",
    "My possibilities are endless.",
    "I am doing my best.",
    "I believe in my ability to go after my dreams and succeed.",
    "I am loved.",
    "I have a purpose.",
    "My courage and strength are more powerful than my doubts.",
    "My goals are attainable.",
    "I choose to live my life to the fullest.",
    "I am grateful to be alive.",
    "I trust my intuition and I always make wise decisions.",
    "I am motivated.",
    "My grateful heart is a magnet that attracts everything I desire.",
    "I breathe in courage and exhale doubt.",
    "There are no limits to the amount of money I can make.",
    "I am confident.",
    "I am limitless.",
    "I am always growing and ready to learn.",
    "Today I have the power to accomplish everything I need to do.",
    "I am in control.",
    "I am proud of who I am.",
    "I allow new beginnings in my life.",
    "I forgive myself for having a bad day.",
    "I have the ability to solve every problem I face.",
    "Everyday I am becoming wealthier.",
    "I am in alignment with my soul purpose.",
    "Every obstacle is an opportunity to grow.",
    "I am stronger than my excuses.",
    "Good things are going to happen.",
    "I believe in the woman I am becoming.",
    "I am unaffected by the judgement of others.",
    "I am healthy and happy.",
    "I am valuable.",
    "Money making opportunities are always coming my way.",
    "I am ready to manifest abundance.",
    "I am worthy of love and happiness.",
    "I am creative and I will create the best life for me.",
    "I am grateful for all that I have.",
    "I don't fail, I learn.",
    "I will achieve the goals I set.",
    "I take action towards my goals everyday.",
    "I am worthy of my goals and dreams.",
    "I am kind and I am patient.",
    "I am manifesting my dream life.",
    "I choose to see the bright side.",
    "I choose to let go of all my anger.",
    "I have important ideas and my ideas matter.",
    "I am prepared for new challenges.",
    "I attract the love I desire.",
    "I have the power to create change."
]