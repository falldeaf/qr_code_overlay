#!/bin/python
from email.policy import default
from tkinter import *
import base64
from PIL import ImageTk, Image
from numpy import pad
import requests
from io import BytesIO
import argparse
from screeninfo import get_monitors

parser = argparse.ArgumentParser()

parser.add_argument("-u", "--Url", help = "Custom URL for the QR Code")
parser.add_argument("-w", "--Width", help = "Custom URL for the QR Code (default: 150x150)", default="150")
parser.add_argument("-f", "--File", help = "Get QR image from file path")
parser.add_argument("-p", "--Padding", help = "Set custom padding value (default: 20)", default=20, type=int)
parser.add_argument("-t", "--Text", help = "Set custom label text (default: Scan for more info)", default="Scan for more info")
parser.add_argument("-m", "--Monitors", help = "show monitors on command-line and exit", action="store_true", default=False)
parser.add_argument("-s", "--Setmonitor", help = "pick a monitor", default=0, type=int)
args = parser.parse_args()

monitors = get_monitors()
monitor_index = args.Setmonitor if args.Setmonitor <= len(monitors) else 0
padding = args.Padding
img_width = args.Width
label_text = args.Text

if(args.Monitors):
	for m in monitors:
		print(str(m))
		exit()

url = "https://api.qrserver.com/v1/create-qr-code/?size={}x{}&data={}".format(args.Width, args.Width, args.Url)

ws = Tk()
#ws.title('PythonGuides')
ws.overrideredirect(True)

def setPosition(mon):
	x = mon.x + mon.width - int(img_width) - padding
	y = mon.y + mon.height - int(img_width) - ( padding + 20)
	geo = "+{}+{}".format(x, y)
	ws.geometry(geo)

def key_pressed(event):
	global monitor_index
	global padding

	if event.char == 'c' or event.char == chr(27):
		ws.destroy()
	if event.keysym=='Up':
		padding += 5
		setPosition(monitors[monitor_index])
	if event.keysym=='Down':
		padding -= 5
		setPosition(monitors[monitor_index])
	if(event.char == 'm' or event.keysym=='Right'):
		monitor_index += 1
		if(monitor_index >= len(monitors)):
			monitor_index = 0

		setPosition(monitors[monitor_index])
		
ws.bind("<Key>",key_pressed)
ws.attributes('-topmost',True)

label = Label(ws, text=label_text)
label.pack(ipadx=1, ipady=1)

setPosition(monitors[monitor_index])

#Default image is hardcoded here
b64img = '''

iVBORw0KGgoAAAANSUhEUgAAAJYAAACWAQMAAAAGz+OhAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABsUlEQVRIibWWMY6DMBBFB7lw6RvARdD6WhSRjJSCaxFxEecGLl0gZv832dWulCo2rvAjyjB//ngs8mYFVZVJxOWgMVnschXDdnDZR5GbV7GrSCULxyBh71IWr8lumq5hLo8iekfMNoyPKmGVdBGjVss6qO7/9fuQsZZu2Z4p377w8re+Ldm5zOFKff+uz1jQAzlsT7WzDJrH3rVnEyR3+HSHDKIua0eP1zBoLxM8budO3StGa2YOxKTHzSPiF12qY4ISykSPz3hAEeQCZjQ6pcexTfYUroKhxRWfjjIKYoQtsr6NGcPpssGThmbfi1YVDGojhoH/7szBR3cBg1ZsRZdPrXpoVcOQx0B7IyP0uTKh9uwGf08jPIneL+asYxa1dDP8ZxWHYDbUpTWbEBc6qVqFVuHUr4YV2/HvheefP0p9WzPPPjowDnwsc6aSoc9TwAyA/1BL5cvWjMvpSuM8os6Gs7GGlbk1MxcU9WzQ5uw8s0eMA9T4FbeK8Q6iu7gfXcrcuoCVcLzrTb7c9WoZ2wXNA7/svUh7xnsOjxDMMuXplepYqSXvB5xbCNa79uzN+gY2sTf6lrwyWAAAAABJRU5ErkJggg=='''
img = PhotoImage(data=b64img)

#If the command line specifies a filepath or URL then load that instead
if(args.Url):
	u = requests.get(url)
	img = ImageTk.PhotoImage(Image.open(BytesIO(u.content)))
elif(args.File):
	img = PhotoImage(file=args.File)

Label(
	ws,
	image=img
).pack()

ws.mainloop()