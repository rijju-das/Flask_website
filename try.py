from flask import Flask, redirect, url_for, render_template, request, send_file
from flask import *
from flask_ngrok import run_with_ngrok
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage



app = Flask(__name__,template_folder='/content/Flask_website/sutiHTML/')
run_with_ngrok(app)  # Start ngrok when app is run

@app.route('/')
def index():
    return render_template('sample.html')

# @app.route('/converted',methods = ['GET', 'POST'])
# def convert():
#     global f1
#     fi = request.files['img']
#     f1 = fi.filename
#     fi.save(f1)
#     return render_template('sample.html')

# @app.route('/download')
# def download():
#     filename = f1.split('.')[0]+'converted.pdf'
#     return send_file(filename,as_attachment=True)


@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'



app.run() 