from fpdf import FPDF
import os
import filetype
import datetime

pdf = FPDF()

imageList = []

name = input('Output Filename: ')

for image in os.listdir(os.getcwd()):
	if os.path.isfile(image):
		if bool(filetype.guess(image)):
			if filetype.guess(image).extension in ['jpg','png','gif','jpeg']:
				imageList.append(image)

for image in imageList:
	pdf.add_page()
	pdf.image(image, x = 5, y = 5, w = 200, h = 290, type = '', link = '')

if len(name) == 0:
	now_name = "MyPDF-" + str(datetime.datetime.today()).replace(':','_')[0:19] +".pdf"
	pdf.output(now_name, "F")
else:
	pdf.output("%s.pdf" % (name), "F")
