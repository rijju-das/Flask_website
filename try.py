from flask import Flask, redirect, url_for, render_template, request, send_file
from flask import *
from pdf_image import pdf2img
# from pdf_image import pdf2img
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/converted',methods = ['GET', 'POST'])
def convert():
    global f1
    fi = request.files['img']
    f1 = fi.filename
    fi.save(f1)
    pdf2img(f1)
    return render_template('converted.html')

@app.route('/download')
def download():
    filename = f1.split('.')[0]+'converted.pdf'
    return send_file(filename,as_attachment=True)

app.run(debug=True)