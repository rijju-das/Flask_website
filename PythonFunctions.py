# from pdf2image import convert_from_path,pdfinfo_from_path
# import os
# import pdf2image
# import shutil
# # pathFile="b.pdf"
from pydub import AudioSegment
from pdf2image import convert_from_path,pdfinfo_from_path
import os
import pdf2image
import shutil
from PyPDF2 import PdfFileWriter, PdfFileReader
import os 
import img2pdf
from os import path
from pdf2docx import Converter
from PyPDF2 import PdfFileMerger

class PythonFunctions:
	

	def pdfToImage(pathFile):
		info = pdfinfo_from_path(pathFile, userpw=None, poppler_path=r'C:\\Users\\sutir\\Documents\\GitHub\\Flask_website\\poppler-0.68.0_x86\\bin')
		maxPages =int( info["Pages"])
		
		try:
			output=pathFile[pathFile.rindex('/'):pathFile.rindex('.')]
		except:
			output=pathFile[0:pathFile.rindex('.')]
		folder=pathFile[:pathFile.rindex('/')]+output
		print('Myath ==== '+folder)
		print()
		if(maxPages==1):
			
			images = convert_from_path(pathFile,500,poppler_path=r'C:\\Users\\sutir\\Documents\\GitHub\\Flask_website\\poppler-0.68.0_x86\\bin')
			for i, image in enumerate(images):
				fname = folder+'.png'
				image.save(fname, "PNG")
			return fname
		else:
			os.mkdir(folder)
			print(folder)
			i=1
			for page in range(1, maxPages+1, 1) : 
				images=convert_from_path(pathFile, dpi=200, first_page=page, last_page = page,poppler_path=r'C:\Users\sutir\Documents\GitHub\Flask_website\poppler-0.68.0_x86\bin')
				for image in images:
					fname = folder+'/'+output+'_page_'+str(i)+'.png'
					i=i+1
					image.save(fname, "PNG")
			zipname=folder+'.zip'
			shutil.make_archive(zipname, 'zip', folder)
			return zipname



	def imageToPDF(dirname,extension):
		# dirname = "xxxx/"
		extension="."+extension
		outputFile=dirname[:dirname.rindex('/')]+'.pdf'
		imgs = []
		for r, _, f in os.walk(dirname):
			for fname in f:
				if not fname.endswith(extension):
						continue
				imgs.append(os.path.join(r, fname))
		with open(outputFile,"wb") as f:
			f.write(img2pdf.convert(imgs))
		return outputFile





	def PDFtoDOCX(pdf_file):
		
		# pdf_file = 'a.pdf'
		docx_file = pdf_file[:pdf_file.rindex('.')]+'.docx'

		# convert pdf to docx
		cv = Converter(pdf_file)
		cv.convert(docx_file)      # all pages by default
		cv.close()
		return docx_file


	
	def ALLtoMP3(src):                                                                    
		dst = src[:src.rindex('.')]+".mp3"
		AudioSegment.from_file(src).export(dst, format="mp3")
		return dst

	                                                   
	def ALLtoWAV(src):                                                                    
		dst = src[:src.rindex('.')]+".wav"
		AudioSegment.from_file(src).export(dst, format="wav")
		return dst

	
	def ALLtoFLV(src):                                                                    
		dst = src[:src.rindex('.')]+".flv"
		AudioSegment.from_file(src).export(dst, format="flv")
		return dst

	# import pandas as pd
	# import librosa
	# def getbeats(filepath):
	#     outpath=filepath[:filepath.rindex('.')]+'.csv'
	#     y,sr=librosa.load(filepath)
	#     tempo,beats=librosa.beat.beat_track(y=y,sr=sr,units='time')
	#     pd.DataFrame(beats).to_csv(outpath,index=False)
		

	
	def mergePDF(pdfs):
		# pdfs = ['/content/name.pdf','/content/name.pdf']
		merger = PdfFileMerger()
		for pdf in pdfs:
			merger.append(pdf)
		outfile="MergedPDF.pdf"
		merger.write(outfile)
		merger.close()
		return outfile


	def PDFsplitter(filepath):
		inputpdf = PdfFileReader(open(filepath, "rb"))
		outputfolder=filepath[:filepath.rindex('.')]+'/'
		for i in range(inputpdf.numPages):
			output = PdfFileWriter()
			output.addPage(inputpdf.getPage(i))
			with open(outputfolder+"document-page%s.pdf" % i, "wb") as outputStream:
				output.write(outputStream)
		zipname=output+'.zip'
		shutil.make_archive(zipname, 'zip', outputfolder)	
		return zipname
	
