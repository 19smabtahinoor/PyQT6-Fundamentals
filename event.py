from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel , QPushButton,QGridLayout,QLineEdit, QComboBox, QSpinBox, QDoubleSpinBox, QButtonGroup, QRadioButton
from PyQt6.QtGui import QIcon

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('img/favicon.ico'))
        self.setWindowTitle("Educxy is awesomes")
        self.setMinimumSize(500,400)

        parentLayout = QGridLayout()
 
        # initialization
        self.label = QLabel("This is app")
        self.button = QPushButton("Click me")
        self.lineEdit = QLineEdit()
        self.comboBox = QComboBox() 
        # self.spinBox = QSpinBox()
        self.spinBox = QDoubleSpinBox() #QSpinBox() and QDoubleSpinBox works similarly

        # comboBox
        self.comboBox.addItem(QIcon("img/py.png"),"Python") 
        self.comboBox.addItem(QIcon("img/js.png"),"Javascript")
        self.comboBox.addItem(QIcon("img/php.png"),"Php")

        #spinbox 
        self.spinBox.setMaximum(10)
        self.spinBox.setMinimum(5)
        self.spinBox.setSingleStep(2)

        #Radio Button 
        self.buttonGroup = QButtonGroup() 

        self.radiobtn1 = QRadioButton("1")
        self.radiobtn2 = QRadioButton("2")
        self.radiobtn3 = QRadioButton("3")

        # add radio button in grp 
        self.buttonGroup.addButton(self.radiobtn1)
        self.buttonGroup.addButton(self.radiobtn2)
        self.buttonGroup.addButton(self.radiobtn3)

        # lineedit placeholder set
        self.lineEdit.setPlaceholderText("Enter your name..........")


        # event( clicked, textChanged)
        self.button.clicked.connect(self.clickHandler) # widget.signal.connect(method)
        # self.lineEdit.textChanged.connect(self.lineTextChange)
        #self.comboBox.currentTextChanged.conect(method)

        # add to layout 
        parentLayout.addWidget(self.label)
        parentLayout.addWidget(self.lineEdit)
        parentLayout.addWidget(self.comboBox)
        parentLayout.addWidget(self.spinBox)
        parentLayout.addWidget(self.radiobtn1)
        parentLayout.addWidget(self.radiobtn2)
        parentLayout.addWidget(self.radiobtn3)
        parentLayout.addWidget(self.button)

        centerWidget = QWidget()
        centerWidget.setLayout(parentLayout)
        self.setCentralWidget(centerWidget)

    #creating a click handler 
    def clickHandler(self):
        print("Button is clicked!")
        print(self.lineEdit.text())
        print(self.comboBox.currentText())
        print(self.spinBox.value())
        print(self.buttonGroup.checkedButton().text())

    #creating a textChanged handler 
    # def lineTextChange(self):
    #     print(self.lineEdit.text())

app = QApplication([])
window = Window() 

window.show() 
app.exec() 