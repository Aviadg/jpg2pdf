from fpdf import FPDF
import os
import filetype

pdf = FPDF()

imageList = []

for image in os.listdir(os.getcwd()):
	if os.path.isfile(image):
		if bool(filetype.guess(image)):
			if filetype.guess(image).extension in ['jpg','png','gif','jpeg']:
				imageList.append(image)

for image in imageList:
	pdf.add_page()
	pdf.image(image, x = 5, y = 5, w = 200, h = 290, type = '', link = '')

pdf.output("yourfile.pdf", "F")


