import os
import sys
import math
import time
from PyQt4.QtGui import *
px=[]
py=[]
c=1
app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle("PyQT4 Pixmap @ pythonspot.com ")
label = QLabel(w)
files=os.listdir("/home/anusha/Documents/hobby_projs/navya_proj/")
def changepic(filen):

    pixmap = QPixmap("/home/anusha/Documents/hobby_projs/navya_proj/"+filen)
    label.setPixmap(pixmap)
    w.resize(pixmap.width(),pixmap.height())
    #w.resize(200,200)
    label.mousePressEvent = getPos
        # Draw window
    w.show()
    app.exec_()



def getPos(event):
    global px,py
    global c
    x = event.pos().x()
    y = event.pos().y()
    if(len(px)==0):
        px.append(x)
        py.append(y)
        print("******")
        print (px[-1],py[-1])
    else:
        hd=abs(px.pop()-x)
        vd=abs(py.pop()-y)
        print(x,y)
        td=math.sqrt((hd**2+vd**2))
        print("horizontal distance:"+str(hd)+"\nvertical distance:"+str(vd)+"\ntd:"+str(td))

        #app.exec_()

        if c<len(files):
            filen=files[c]
            c+=1
            print c
            changepic(filen)
        else:
            sys.exit(app.exec_)




if __name__=="__main__":
    changepic(files[0])


# Create window
