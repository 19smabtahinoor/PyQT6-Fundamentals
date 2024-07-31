from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QLabel, QWidget, QLineEdit,QPushButton

from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt

app = QApplication([])
window = QMainWindow() 

window.setWindowTitle("Educxy's Login Page")
window.setWindowIcon(QIcon('favicon.ico'))
window.setFixedSize(400,400)

#image -> label , input -> button

parentLayout = QGridLayout()

# image 
ImageLabel = QLabel()
ImageLabel.setPixmap(QPixmap('logo.png').scaled(200,50))
ImageLabel.setMaximumHeight(100)
parentLayout.addWidget(ImageLabel,0,1,1,2)

#Email Label 
EmailLabel = QLabel("Email :")
EmailInput = QLineEdit()
parentLayout.addWidget(EmailLabel,1,0)
parentLayout.addWidget(EmailInput,1,1)

#Password Label 
PassWordLabel = QLabel("Password: ")
PasswordInput = QLineEdit()
PasswordInput.setEchoMode(QLineEdit.EchoMode.Password) #to make password hidden
parentLayout.addWidget(PassWordLabel,2,0)
parentLayout.addWidget(PasswordInput,2,1)



# Submit Button 
SumbitButton = QPushButton("Login") 
parentLayout.addWidget(SumbitButton,3,0, 1, 2 )


centerWidget = QWidget() 
centerWidget.setLayout(parentLayout)
window.setCentralWidget(centerWidget)

window.show() 
app.exec() 