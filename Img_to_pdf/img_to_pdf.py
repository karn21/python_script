import os
from PIL import Image
from fpdf import FPDF
import datetime

# Page Size
A4_HEIGHT = 842
A4_WIDTH = 595

INPUT_PATH = "input/"

def img_to_pdf():
	# initialise fpdf object
	pdf = FPDF(unit="pt",format=[A4_WIDTH,A4_HEIGHT])

	for file_name in os.listdir(INPUT_PATH):

		file_path = INPUT_PATH+file_name
		print("Merging",file_name,"to pdf...")
		img = Image.open(file_path)
		width,height = img.size

		# convert px to pt
		width = width/1.36
		height = height/1.36

		# resize if bigger than page size
		while(height>A4_HEIGHT or width>A4_WIDTH):
			width = width/1.2
			height = height/1.2

		# calculate offset for centering image
		x_offset = (A4_WIDTH - width)/2
		y_offset =  (A4_HEIGHT - height)/2

		pdf.add_page()
		pdf.image(file_path,x=x_offset,y=y_offset,w=width,h=height)
		img.close()

	# use timestamp for unique filename
	timestamp = datetime.datetime.now()
	filename = timestamp.strftime("%d-%b-%Y_(%H-%M-%S)")
	pdf.output(f"output/{filename}.pdf","F")

img_to_pdf()