from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QColorDialog 

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(600,400); 
        self.button = QPushButton("Open Dialog")
        self.setCentralWidget(self.button)

        self.button.clicked.connect(self.clickHandler)

    def clickHandler(self): 
        dialog = QColorDialog()
        
        clickedButton = dialog.exec()  

        if clickedButton:
            # print(dialog.textValue())
            print(dialog.currentColor().name()) #to print Integer value
        else: 
            print("Dialog Cancelled!")
        

            

app = QApplication([])
window = Window()

window.show()
app.exec()