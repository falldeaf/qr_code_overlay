#!/bin/python
from email.policy import default
from tkinter import *
import base64
from PIL import ImageTk, Image
import requests
from io import BytesIO
import argparse
from screeninfo import get_monitors

parser = argparse.ArgumentParser()

parser.add_argument("-u", "--Url", help = "Custom URL for the QR Code")
parser.add_argument("-w", "--Width", help = "Custom URL for the QR Code (default: 150x150)", default="150")
parser.add_argument("-f", "--File", help = "Get QR image from file path")
parser.add_argument("-p", "--Padding", help = "Set custom padding value (default: 20)", default=20, type=int)
args = parser.parse_args()

monitors = get_monitors()
monitor_index = 0
padding = args.Padding
img_width = args.Width

print(5 - padding)


print(str(monitors[monitor_index]))
url = "https://api.qrserver.com/v1/create-qr-code/?size={}x{}&data={}".format(args.Width, args.Width, args.Url)
print(url)

ws = Tk()
#ws.title('PythonGuides')
ws.overrideredirect(True)

def setPosition(mon):
	x = mon.x + mon.width - int(img_width) - padding
	y = mon.y + mon.height - int(img_width) - padding
	geo = "+{}+{}".format(x, y)
	ws.geometry(geo)

def key_pressed(event):
	global monitor_index

	if(event.char == 'c' or event.char == chr(27)):
		ws.destroy()
	if(event.char == 'm'):
		monitor_index += 1
		if(monitor_index >= len(monitors)):
			monitor_index = 0

		setPosition(monitors[monitor_index])
		
ws.bind("<Key>",key_pressed)
ws.attributes('-topmost',True)
setPosition(monitors[monitor_index])

#Default image is hardcoded here
b64img = '''iVBORw0KGgoAAAANSUhEUgAAAJYAAACWAQMAAAAGz+OhAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABHElEQVRIib2WMQ6DMAxFjRgYc4QcJRdDpNyMo3AExgwI99umVVt1hG9lycsQy/H/jsifqIpY+k2GtWvZNu1yNuKetOhWbJcfIh2JJd3T0qsKQJ5VZyZDLoMefGZlsNoTmdfecD7k6z3uZdFrYEjku//uZe8w9iuoGxly2ZOloyvkNWFxWA9VbcU1jSwmXww2SpGkdoIeF5zURmF1s2q7ptVxx2GI0DQMbDAb0+sZ7kWRIaVmN55vTmCjm4allA8UWb32DIb3lfKSbW3hJQTmPul+pa+RxGARYDZ/pdNVOCx8Est9co5eI7CYC9CvKyhyobBz/kr7fQ8SG+DPOnvTUZnPBcMk5rXfpfgcrPbroLDoNWfmnfrxF7iV/YknYTx+pNyOCMQAAAAASUVORK5CYII='''
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