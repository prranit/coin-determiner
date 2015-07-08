#This script processes the test file

#imports
import os
from werkzeug import secure_filename
from flask import *
import coinapp
import routes



# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in routes.app.config['ALLOWED_EXTENSIONS']



#This function generates two lists, "tstnum" with test values and "resnum" with the results
def fileprocess(filename):

    filepath = "upload/" + filename
    tst = open(filepath)
    tstnum = []
    resnum = []
    i = 0

    try:

        for line in tst:
            num = int(line)
            tstnum.append(num)

        for i in range(len(tstnum)):
            resnum.append(coinapp.coin(tstnum[i]))

        #calls retres to combine lists
        finallist = retres(tstnum, resnum)
        
        return finallist

    #return empty list if test fails
    except:
        emtlist = []
        return emtlist



#Combines both lists into one
def retres(tstnum, resnum):

    a = tstnum
    b = resnum
    c = []
    for i in range(len(a)):

        #Ensure proper grammar
        if b[i] == 1:
            grammar = " coin."
        else:
            grammar = " coins."

        a[i] = "For " + str(a[i]) + ", you will need " + str(b[i]) + grammar

    for i in range(len(a)):
        c.append(a[i])

    return c

