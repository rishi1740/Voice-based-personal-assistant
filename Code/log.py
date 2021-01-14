import time
def log(data):
    logfile = open("logfile.log",'a')
    logfile.write("Time: {}  \t\tCommand: {}\n".format(time.ctime(),data))
    logfile.close()

def display():
    logfile = open("logfile.log",'r')
    gui.printf(logfile.read())
    logfile.close()
