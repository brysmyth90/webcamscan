import cv2, cv
import Image
import serial
import colorsys

def doCapImage (imgNum):
	capture = cv2.VideoCapture(0)
	
	#need to waste some images to get the webcam warmed up
	for i in xrange(15):
		temp = capture.read()  
	
	flag, im_array = capture.read()
	image = cv.fromarray(im_array)
	cv.SaveImage('output_%d.jpeg'%imgNum, image)
	capture.release() 
	

numFrames=1

for imgNum in range(0,numFrames):
	doCapImage (imgNum)


for imgNum in range(0,numFrames):
	im=Image.open("output_%d.jpeg"%imgNum)
	#print im.size
	for y in range(0,im.size[1]):
		row = [colorsys.rgb_to_hsv(im.getpixel((x,y))[0],im.getpixel((x,y))[1],im.getpixel((x,y))[2])[2] for x in range(0,im.size[0])]
		print "Row is %d pixels"%(len(row))
		bright=row.index(max(row))
		print "Brightest pixel on this row is at %d."%bright
		im.putpixel((bright, y), (255,0,0))
	im.save("output_%d.jpeg"%imgNum)
