import Functions.ui

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 340)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.code_btn = QtWidgets.QPushButton(self.centralwidget)
        self.code_btn.setGeometry(QtCore.QRect(10, 20, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.code_btn.setFont(font)
        self.code_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.code_btn.setObjectName("code_btn")
        self.input_box = QtWidgets.QLineEdit(self.centralwidget)
        self.input_box.setGeometry(QtCore.QRect(140, 20, 641, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.input_box.setFont(font)
        self.input_box.setObjectName("input_box")
        self.return_label = QtWidgets.QLabel(self.centralwidget)
        self.return_label.setGeometry(QtCore.QRect(10, 70, 771, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.return_label.setFont(font)
        self.return_label.setText("")
        self.return_label.setObjectName("return_label")
        self.decode_btn = QtWidgets.QPushButton(self.centralwidget)
        self.decode_btn.setGeometry(QtCore.QRect(10, 130, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.decode_btn.setFont(font)
        self.decode_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.decode_btn.setObjectName("decode_btn")
        self.img_input_box = QtWidgets.QLineEdit(self.centralwidget)
        self.img_input_box.setGeometry(QtCore.QRect(140, 130, 641, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.img_input_box.setFont(font)
        self.img_input_box.setObjectName("img_input_box")
        self.decoded_text_box = QtWidgets.QTextEdit(self.centralwidget)
        self.decoded_text_box.setGeometry(QtCore.QRect(140, 180, 641, 151))
        self.decoded_text_box.setReadOnly(True)
        self.decoded_text_box.setFont(font)
        self.decoded_text_box.setObjectName("decoded_text_box")
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(10, 180, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.clear_btn.setFont(font)
        self.clear_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_btn.setObjectName("clear_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.code_btn.clicked.connect(lambda: Functions.ui.coding(self.input_box.text(), self.return_label))
        self.decode_btn.clicked.connect(lambda: Functions.ui.decoding(self.img_input_box.text(), self.decoded_text_box))
        self.clear_btn.clicked.connect(lambda: Functions.ui.clear(self.input_box, self.decoded_text_box, self.img_input_box, self.return_label))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cowberry"))
        MainWindow.setWindowIcon(QtGui.QIcon('CowBerry.png'))
        self.code_btn.setText(_translate("MainWindow", "Кодировать"))
        self.decode_btn.setText(_translate("MainWindow", "Декодировать"))
        self.clear_btn.setText(_translate("MainWindow", "Очистить"))


if __name__ == "__main__":
    try:
        # Включите в блок try/except, если вы также нацелены на Mac/Linux
        from PyQt5.QtWinExtras import QtWin  # !!!

        myappid = 'mycompany.myproduct.subproduct.version'  # !!!
        QtWin.setCurrentProcessExplicitAppUserModelID(myappid)  # !!!
    except ImportError:
        pass
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('CowBerry.png'))
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowIcon(QtGui.QIcon('CowBerry.png'))
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
