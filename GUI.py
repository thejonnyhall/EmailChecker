# Python lols
# Only-Code-In-Kebab-Case
# Jonny and Xander 2016

from Tkinter import *

mainPage = Tk()

mainPage.minsize(width=500, height=300)
mainPage.maxsize(width=500, height=300)

title = Label(mainPage, text="Jonny and Xander's \nEmail Chequer", height=5, font=('Comic Sans MS', 20, 'bold italic'))
title.pack()

page = Canvas(mainPage, width = 150, height = 0)
page.pack()

# Dunno how to move this up
EnterName = Label(mainPage, text="Enter The Name of The Person you wish to stalk", font=('Comic Sans MS', 14, 'bold italic'))
EnterName.pack()
textstuff = Entry(mainPage)
textstuff.pack()





mainPage.mainloop()
