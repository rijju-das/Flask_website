import os
from flask import Flask, redirect, url_for, render_template, request, send_file, url_for, flash, sessions
from flask import *
# from flask_ngrok import run_with_ngrok
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask import send_from_directory
from PythonFunctions import PythonFunctions


UPLOAD_FOLDER = 'uploaded_file/'

# app = Flask(__name__,template_folder='C:/Users/rijju/Documents/GitHub/Flask/sutiHTML/')
app = Flask(__name__,template_folder='C:/Users/sutir/Documents/GitHub/Flask_website/sutiHTML/')
# run_with_ngrok(app)  # Start ngrok when app is run
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "super secret key"



 

@app.route('/', methods=['POST','GET'])
def upload():
    if request.method == 'POST':
      f = request.files['file']
      filename=secure_filename(f.filename)
      if filename== '':
          flash('No file selected')
      if filename:
          f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
          filepath=os.path.join(app.config['UPLOAD_FOLDER'], filename)
          print('filepath '+ filepath)
          outputfilepath= PythonFunctions.pdfToImage(filepath)
        #   outputfilepath=outputfilepath.replace('uploaded_file/', '')
          print('output filepath '+ outputfilepath)
          return redirect(url_for('download',filename=outputfilepath))

    return render_template('upload_page.html')



@app.route("/download/<filename>", methods = ['GET'])
def download(filename):
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    # return send_from_directory(app.config["UPLOAD_FOLDER"], filename)
    return render_template('download.html',value=filename,f_list=files)


@app.route("/download_file/<filename>", methods= ['GET'])
def download_file(filename):
    # return "<h1>Successfully uploaded</h1>"
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename,as_attachment=True)




if __name__ == '__main__':
   app.run(debug = True)


app.run() 