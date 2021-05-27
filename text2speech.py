# importing required module
from tkinter import *
from gtts import gTTS

# this module helps to
# play the converted audio
import os

# create tkinter window
root = Tk()
root.minsize(700, 700)
# styling the frame which helps to
# make our background stylish
frame1 = Frame(root,
			bg = "lightBlue",
			height = "150")

# plcae the widget in gui window
frame1.pack(fill = X)


frame2 = Frame(root,
			bg = "lightgreen",
			height = "750")
frame2.pack(fill=X)


label = Label(frame1, text = "Text to Speech \n by saksham garg",
			font = "impact, 30")
label.pack()



# entry is used to enter the text
entry = Entry(frame2, width = 45,
			bd = 4, font = 14)

entry.place(x = 130, y = 52)
entry.insert(0, "")

# define a function which can
# get text and convert into audio
def play():

	# Language in which you want to convert
	language = "en"



# Passing the text and language,
# here we have slow=False. Which tells
# the module that the converted audio should
# have a high speed

	myobj = gTTS(text = entry.get(),
				lang = language,
				slow = False)



	# give the name as you want to
	# save the audio
	myobj.save("convert.mp4")
	os.system("convert.mp4")

# cereate a button which holds
# our play function using command = play
btn = Button(frame2, text = "SUBMIT",
			width = "15", pady = 10,
			font = "bold, 15",
			command = play, bg='yellow')

btn.place(x = 250,
		y = 130)

# give a title
root.title("text_to_speech_convertor")

root.geometry("650x550+350+200")

# start the gui
root.mainloop()
