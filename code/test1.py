from pynput.mouse import Button, Controller
import time
import cv2
import os
import sys
from direct_key_inputs import PressKeyPynput, ReleaseKeyPynput, W, A, S, D
mouse=Controller()
cap = cv2.VideoCapture(0)
hex_keys = {"1":0X02,"2":0X03,"3":0X04,"4":0X05,"5":0X06,"6":0X07,"7":0X08,"8":0X09,"9":0X0A,"0":0X0B}
def mouse_paint(x,y,colour):
	global hex_keys
	time.sleep(2)
	#Rectangle 
	#typing rgb values in not done yet then we have to draw at pixels as well
	mouse.position=(245,70)    #(Xposition, Yposition) click pencil
	mouse.press(Button.left)
	mouse.release(Button.left)

	mouse.position=(995,70)    #click edit colour
	mouse.press(Button.left)
	mouse.release(Button.left)

	mouse.position=(887,502)    #click B value
	mouse.press(Button.left)
	mouse.release(Button.left)
	PressKeyPynput(0x0E)
	ReleaseKeyPynput(0x0E)
	PressKeyPynput(0x0E)
	ReleaseKeyPynput(0x0E)
	PressKeyPynput(0x0E)
	ReleaseKeyPynput(0x0E)
	for digits in str(colour[0]):
		PressKeyPynput(hex_keys[digits])
		ReleaseKeyPynput(hex_keys[digits])

	mouse.position=(887,479)    #click G value
	mouse.press(Button.left)
	mouse.release(Button.left)
	PressKeyPynput(0x0E)
	ReleaseKeyPynput(0x0E)
	PressKeyPynput(0x0E)
	ReleaseKeyPynput(0x0E)
	PressKeyPynput(0x0E)
	ReleaseKeyPynput(0x0E)
	for digits in str(colour[1]):
		PressKeyPynput(hex_keys[digits])
		ReleaseKeyPynput(hex_keys[digits])

	mouse.position=(887,457)    #click R value
	mouse.press(Button.left)
	mouse.release(Button.left)
	PressKeyPynput(0x0E)
	ReleaseKeyPynput(0x0E)
	PressKeyPynput(0x0E)
	ReleaseKeyPynput(0x0E)
	PressKeyPynput(0x0E)
	ReleaseKeyPynput(0x0E)
	for digits in str(colour[2]):
		PressKeyPynput(hex_keys[digits])
		ReleaseKeyPynput(hex_keys[digits])

	mouse.position=(500,527)    #click ok button
	mouse.press(Button.left)
	mouse.release(Button.left)

	mouse.position=(x,y)    #Use pencil to draw
	mouse.press(Button.left)
	mouse.release(Button.left)

	# PressKeyPynput(0x24)
	# ReleaseKeyPynput(0x24)

x=325
y=185
while True:
	ret, frame = cap.read()
	if not ret:
		break
	resized_frame = cv2.resize(frame, (50, 50))
	for Yposition in resized_frame:
		for Xposition in Yposition:
			x+=1
			color=Xposition # these are bgr values
			mouse_paint(x,y,color)
		y+=1
		x=325
	print("frame printed")
	break

	k = cv2.waitKey(10)
	if k == ord('q'):
		break

