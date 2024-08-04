from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QGridLayout, QWidget,QFontDialog

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(600,400)
        self.label = QLabel("HELLOOOOO")
        self.button = QPushButton("Open Dialog")
        
        parentLayout = QGridLayout()
        parentLayout.addWidget(self.label, 0,0)
        parentLayout.addWidget(self.button, 0,1)

        centerWidget = QWidget()
        centerWidget.setLayout(parentLayout)

        self.setCentralWidget (centerWidget)


        self.button.clicked.connect(self.clickHandler)

    def clickHandler(self): 
        dialog = QFontDialog()
        
        clickedButton = dialog.exec()  

        if clickedButton:
            self.label.setFont(dialog.currentFont())

            # print(dialog.currentFont().family())
            # others methods : italic(), letterSpacing(), underline(), wordspacing(), bold(), family()
        else: 
            print("Dialog Cancelled!")
        

            

app = QApplication([])
window = Window()

window.show()
app.exec()