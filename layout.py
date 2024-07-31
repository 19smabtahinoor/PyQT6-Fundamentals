from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout,QWidget, QLabel
from PyQt6.QtGui import QIcon

app = QApplication([])
window = QMainWindow() 

window.setMinimumSize(600,400)
window.setWindowTitle("Educxy")
window.setWindowIcon(QIcon("favicon.ico"))

# ====================created a horizontal and vertical layout=====================
# parentLayout = QVBoxLayout()
# buttonLayout = QHBoxLayout() 


# button1 = QPushButton("Button1")  
# button2 =QPushButton("Button2")
# button3 =QPushButton("Button3")
# label = QLabel("This is Educxy")

# buttonLayout.addWidget(button1)
# buttonLayout.addWidget(button2)
# buttonLayout.addWidget(button3)
# buttonLayout.addSpacing(100)

# parentLayout.addLayout(buttonLayout)
# parentLayout.addWidget(label)


# centerWidget = QWidget()
# centerWidget.setLayout(parentLayout)

# window.setCentralWidget(centerWidget)




# ====================QGridLayout=====================
parentLayout = QGridLayout() 

label = QLabel("This is crazy")
parentLayout.addWidget(label, 0,0,1,3)
# here 0 = row , 0= col , 1= rowspan , 3 = colspan

button1 = QPushButton('Button1')
button2 = QPushButton("Button2")
parentLayout.addWidget(button1,0,1)
parentLayout.addWidget(button2,1,2)

parentLayout.setRowMinimumHeight(1,200)

parentLayout.setHorizontalSpacing(50)

centerWidget = QWidget() 
centerWidget.setLayout(parentLayout)

window.setCentralWidget(centerWidget)

window.show() 
app.exec() 
