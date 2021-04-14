import os
from PIL import Image
from fpdf import FPDF

A4_HEIGHT = 842
A4_WIDTH = 595

INPUT_PATH = "input/"

def img_to_pdf():
	pdf = FPDF(unit="pt",format=[A4_WIDTH,A4_HEIGHT])
	for file_name in os.listdir(INPUT_PATH):
		file_path = INPUT_PATH+file_name
		print("Merging",file_name,"to pdf...")
		img = Image.open(file_path)
		width,height = img.size
		width = width/1.36
		height = height/1.36
		while(height>A4_HEIGHT or width>A4_WIDTH):
			width = width/1.2
			height = height/1.2
		x_offset = (A4_WIDTH - width)/2
		y_offset =  (A4_HEIGHT - height)/2
		pdf.add_page()
		pdf.image(file_path,x=x_offset,y=y_offset,w=width,h=height)
		img.close()
	pdf.output("output/op.pdf","F")

img_to_pdf()