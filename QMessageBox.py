from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox 

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(600,400); 
        self.button = QPushButton("Open Dialog")
        self.setCentralWidget(self.button)

        self.button.clicked.connect(self.clickHandler)

    def clickHandler(self): 
        dialog = QMessageBox()
        dialog.setText("This is a dialog")
        dialog.setWindowTitle("Hi!")
        dialog.setIcon(QMessageBox.Icon.Question) # Information, Critical , Warning, Question
        dialog.setMinimumSize(500, 500)

        # set a button 
        dialog.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel) #Cancel, Close , Discard, No, Ok, Open, Retry, Save, SaveAll, Yes

        # dialog.exec()
        clickedButton = dialog.exec() 

        if clickedButton == QMessageBox.StandardButton.Ok:
            print("Click Ok")
        else: 
            print("Dialog Dismissed!")

            

app = QApplication([])
window = Window()

window.show()
app.exec()