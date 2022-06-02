#Importing file
import datetime

#Defining getDate function
def getDate():
    now=datetime.datetime.now()
    return str(now.strftime("%Y-%m-%d"))

#Defining getTime function
def getTime():
    now=datetime.datetime.now()
    return str(now.strftime("%H:%M"))
