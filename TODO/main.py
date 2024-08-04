from todo_design import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow

class Window(QMainWindow, Ui_MainWindow): 
    def __init__(self): 
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.clickedAdd)

    def clickedAdd(self):
        print('Hi')
        entered_Task = self.lineEdit.text() 
        if entered_Task.strip() != "":
            self.listWidget.addItem(entered_Task)
            self.lineEdit.setText("")

app = QApplication([])
window = Window() 

window.show() 
app.exec() 
