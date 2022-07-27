#!/bin/python
from tkinter import *
import base64
from PIL import ImageTk, Image
import requests
from io import BytesIO

from screeninfo import get_monitors
for m in get_monitors():
	print(str(m))

print("Running")

url = "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://tinyurl.com/DLKJFS"

ws = Tk()
#ws.title('PythonGuides')
ws.overrideredirect(True)
def key_pressed(event):
	print("Key Pressed:"+event.char)
	if(event.char == 'c'):
		ws.destroy()
ws.bind("<Key>",key_pressed)
ws.attributes('-topmost',True)
ws.geometry("+1940+20")

#u = requests.get(url)
#img = ImageTk.PhotoImage(Image.open(BytesIO(u.content)))

b64img = '''iVBORw0KGgoAAAANSUhEUgAAAJYAAACWAQMAAAAGz+OhAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABHElEQVRIib2WMQ6DMAxFjRgYc4QcJRdDpNyMo3AExgwI99umVVt1hG9lycsQy/H/jsifqIpY+k2GtWvZNu1yNuKetOhWbJcfIh2JJd3T0qsKQJ5VZyZDLoMefGZlsNoTmdfecD7k6z3uZdFrYEjku//uZe8w9iuoGxly2ZOloyvkNWFxWA9VbcU1jSwmXww2SpGkdoIeF5zURmF1s2q7ptVxx2GI0DQMbDAb0+sZ7kWRIaVmN55vTmCjm4allA8UWb32DIb3lfKSbW3hJQTmPul+pa+RxGARYDZ/pdNVOCx8Est9co5eI7CYC9CvKyhyobBz/kr7fQ8SG+DPOnvTUZnPBcMk5rXfpfgcrPbroLDoNWfmnfrxF7iV/YknYTx+pNyOCMQAAAAASUVORK5CYII='''
img = PhotoImage(data=b64img)

#img = PhotoImage(file='img.png')
Label(
	ws,
	image=img
).pack()

ws.mainloop()