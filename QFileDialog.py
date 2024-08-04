from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog 

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(600,400); 
        self.button = QPushButton("Open Dialog")
        self.setCentralWidget(self.button)

        self.button.clicked.connect(self.clickHandler)

    def clickHandler(self): 
        dialog = QFileDialog()
        dialog.setNameFilter("All images (*.png *.jpg)")
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        # dialog.setFileMode(QFileDialog.FileMode.Directory) # to select folder  
        dialogSuccessful = dialog.exec()  

        if dialogSuccessful ==1 :
            selectedFiles = dialog.selectedFiles()
            print(selectedFiles)
        else: 
            print("Dialog Cancelled!")
        

            

app = QApplication([])
window = Window()

window.show()
app.exec()