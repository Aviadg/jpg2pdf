from fpdf import FPDF
import os
import filetype
from PIL import Image




pdf = FPDF()

# imagelist is the list with all image filenames
margin = 10

for image in os.listdir(os.getcwd()):
	print(type(filetype.guess(image)))
	if bool(filetype.guess(image)):
		if filetype.guess(image).extension in ['jpg','png','gif','jpeg']:
			cover = Image.open(image)
			width, height = cover.size
			print(filetype.guess(image).extension)
			pdf.add_page()

			pdf.image(image, x = 5, y = 5, w = 200, h = 290, type = '', link = '')

pdf.output("yourfile.pdf", "F")


