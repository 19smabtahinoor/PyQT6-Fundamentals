from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QInputDialog 

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(600,400); 
        self.button = QPushButton("Open Dialog")
        self.setCentralWidget(self.button)

        self.button.clicked.connect(self.clickHandler)

    def clickHandler(self): 
        dialog = QInputDialog() 
        dialog.setLabelText("Enter your name : ")

        # to get interger input
        dialog.setInputMode(QInputDialog.InputMode.IntInput)  
        
        clickedButton = dialog.exec()  

        if clickedButton:
            # print(dialog.textValue())
            print(dialog.intValue()) #to print Integer value
        else: 
            print("Dialog Cancelled!")
        

            

app = QApplication([])
window = Window()

window.show()
app.exec()