from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel,QPushButton
from PyQt6.QtGui import QIcon,QPixmap
from PyQt6.QtCore import Qt

app = QApplication([])

window = QMainWindow() 

# setMinimumHeight(), setMinimumWidth() , SetFixedSize()
window.setMinimumSize(600,400)

# set a title 
window.setWindowTitle("Educxy")

#set window icon
window.setWindowIcon(QIcon("favicon.ico"))


#Adding Widgets 

# ===========text widget============
# label = QLabel("Educxy is a social study platform", alignment=Qt.AlignmentFlag.AlignCenter)
# font = window.font() #creating a font object to customize it
# font.setPointSize(20) # font size
# font.setBold(True) # font weight
# label.setFont(font) # Attaching our customized font to label
# window.setCentralWidget(label)


# ===========image widget============
# label = QLabel()
# label.setPixmap(QPixmap("logo.png").scaled(300,100))   # scaledToHeight(250)
# window.setCentralWidget(label)

# ===========Push Button===========
button = QPushButton("Login")
button.setFixedSize(100,60)
font = window.font() 
font.setBold(True)
font.setPointSize(18)
button.setFont(font)

window.setCentralWidget(button)

window.show() 

app.exec()