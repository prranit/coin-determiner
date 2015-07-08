#Coin Determiner App - Prranit Vaswani - July 2015
#Python, Flask

#imports
import os
from flask import *
from werkzeug import secure_filename
import coinapp
import filehandle

#Initiate app
app = Flask(__name__)

#Set Debugging
app.debug = True

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'upload/'

# We will accept only the ".txt" extension
app.config['ALLOWED_EXTENSIONS'] = set(['txt'])

#Display Home Page
@app.route('/')
def home():
    return render_template("hello.html", a = 0)

#Coin Determiner - This function calls the coin method to solve the problem. 
#Uses error handling for any invalid input
@app.route('/', methods=['GET', 'POST'])
def runcoin():
    try:
        a = coinapp.coin(request.form['numb'])
        return render_template("hello.html", a=a)
    except:
        return render_template("hello.html", a=0)

#This function uploads the test file and processes the test values
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        try:

        #This block uploads the file and saves it to our local directory
            file = request.files['file']
            if file and filehandle.allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        

        #Retrieve and display results from file processing
            reslist = filehandle.fileprocess(filename)
            if len(reslist) > 3:
                resval = 0
            else:
                resval = 1
            return render_template("upload.html", resval = resval, reslist = reslist)

    #If no file has been uploaded, send user an error
        except:
            suberr = "Please upload a .txt file before submitting."
            return render_template("upload.html", suberr=suberr)

    return render_template("upload.html")

#run the app from the python shell
if __name__=='__main__':
    app.run()
