from glob import glob
from PyPDF2 import PdfFileMerger
import datetime

INPUT_PATH = "input/"

def pdf_merger():
	merger = PdfFileMerger()
	for file_name in glob(f"{INPUT_PATH}*.pdf"):
		print(f"Merging file {file_name} to pdf")
		merger.append(file_name)
	timestamp = datetime.datetime.now()
	filename = timestamp.strftime("%d-%b-%Y_(%H-%M-%S)")
	op = open(f"output/{filename}","wb")
	merger.write(op)
	merger.close()

pdf_merger()
