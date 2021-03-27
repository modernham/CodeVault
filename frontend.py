"""
Program that uses sqlLite to store code snippets from a user.
UI design by QT designer
@author aspect
"""

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import backend



class Ui_MainWindow(object):
    CurrentCat = ""
    CurrentSnip = ""


    #Setup Basic Layout and create the Widgets.
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1229, 791)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CategoriesBox = QtWidgets.QGroupBox(self.centralwidget)
        self.CategoriesBox.setGeometry(QtCore.QRect(10, 10, 161, 761))
        self.CategoriesBox.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.CategoriesBox.setFont(font)
        self.CategoriesBox.setObjectName("CategoriesBox")

        #change Window icon.
        MainWindow.setWindowIcon(QtGui.QIcon('icon.ico'))

        #CategoryListBox
        self.CatListBox = QtWidgets.QListWidget(self.CategoriesBox)
        self.CatListBox.setGeometry(QtCore.QRect(10, 150, 141, 571))
        self.CatListBox.setObjectName("CatListBox")
        # Populate the Categories (tables) List
        #Bind function that gets rows from categories table when changed.
        self.CatListBox.itemClicked.connect(self.UpdateSnipets)

        #Catagory Edit (add) Box
        self.CatAddEdit = QtWidgets.QLineEdit(self.CategoriesBox)
        self.CatAddEdit.setGeometry(QtCore.QRect(10, 100, 141, 20))
        self.CatAddEdit.setObjectName("CatAddEdit")

        #Create the Add category Button, and bind AddCategory to it.
        self.CatAddBtn = QtWidgets.QPushButton(self.CategoriesBox)
        self.CatAddBtn.setGeometry(QtCore.QRect(10, 120, 141, 23))
        self.CatAddBtn.setObjectName("CatAddBtn")
        self.CatAddBtn.clicked.connect(self.AddCategory)

        #Remove a Category
        self.CatRemoveBtn = QtWidgets.QPushButton(self.CategoriesBox)
        self.CatRemoveBtn.setGeometry(QtCore.QRect(10, 730, 141, 23))
        self.CatRemoveBtn.setObjectName("CatRemoveBtn")
        self.CatRemoveBtn.clicked.connect(self.RemoveCategory)

        #When user types in filter, we filter the ctegory list.
        self.CatFilterEdit = QtWidgets.QLineEdit(self.CategoriesBox)
        self.CatFilterEdit.setGeometry(QtCore.QRect(10, 60, 141, 20))
        self.CatFilterEdit.setObjectName("CatFilterEdit")
        self.CatFilterEdit.textChanged.connect(self.UpdateCatList)


        self.label = QtWidgets.QLabel(self.CategoriesBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.SnipetsBox = QtWidgets.QGroupBox(self.centralwidget)
        self.SnipetsBox.setGeometry(QtCore.QRect(180, 10, 161, 761))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SnipetsBox.setFont(font)
        self.SnipetsBox.setObjectName("SnipetsBox")

        #Our Snipet List. When user clicks, we update the code window.
        self.SnipListBox = QtWidgets.QListWidget(self.SnipetsBox)
        self.SnipListBox.setGeometry(QtCore.QRect(10, 150, 141, 571))
        self.SnipListBox.setObjectName("SnipListBox")
        self.SnipListBox.itemClicked.connect(self.SetCode)


        self.SnipAddEdit = QtWidgets.QLineEdit(self.SnipetsBox)
        self.SnipAddEdit.setGeometry(QtCore.QRect(10, 100, 141, 20))
        self.SnipAddEdit.setObjectName("SnipAddEdit")

        #Button for Adding Codes to the currently selected Category(Table)
        self.SnipAddBtn = QtWidgets.QPushButton(self.SnipetsBox)
        self.SnipAddBtn.setGeometry(QtCore.QRect(10, 120, 141, 23))
        self.SnipAddBtn.setObjectName("SnipAddBtn")
        self.SnipAddBtn.clicked.connect(self.AddSnipet)

        #Button for removing Snipets
        self.SnipRemoveBtn = QtWidgets.QPushButton(self.SnipetsBox)
        self.SnipRemoveBtn.setGeometry(QtCore.QRect(10, 730, 141, 23))
        self.SnipRemoveBtn.setObjectName("SnipRemoveBtn")
        self.SnipRemoveBtn.clicked.connect(self.RemoveSnip)

        #When user types in filter, we filter the snip list.
        self.SnipFilterEdit = QtWidgets.QLineEdit(self.SnipetsBox)
        self.SnipFilterEdit.setGeometry(QtCore.QRect(10, 60, 141, 20))
        self.SnipFilterEdit.setObjectName("SnipFilterEdit")
        self.SnipFilterEdit.textChanged.connect(self.UpdateSnipets)


        self.label_2 = QtWidgets.QLabel(self.SnipetsBox)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setWeight(25)
        self.label.setFont(font)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.CodeBox = QtWidgets.QGroupBox(self.centralwidget)
        self.CodeBox.setGeometry(QtCore.QRect(370, 10, 821, 761))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.CodeBox.setFont(font)
        self.CodeBox.setObjectName("CodeBox")

        #Code for our Code Window
        self.CodeWindow = QtWidgets.QPlainTextEdit(self.CodeBox)
        self.CodeWindow.setGeometry(QtCore.QRect(10, 30, 801, 691))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.CodeWindow.setFont(font)
        self.CodeWindow.setObjectName("CodeWindow")

        #Code to Save Code Changes to The Currently selected Code
        self.CodeUpdateSaveBtn = QtWidgets.QPushButton(self.CodeBox)
        self.CodeUpdateSaveBtn.setGeometry(QtCore.QRect(20, 730, 791, 23))
        self.CodeUpdateSaveBtn.setObjectName("CodeUpdateSaveBtn")
        self.CodeUpdateSaveBtn.clicked.connect(self.UpdateCode)

        #update our Category List When Program finishes loading widgets,
        self.UpdateCatList()

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CodeVault"))
        self.CategoriesBox.setTitle(_translate("MainWindow", "Categories"))
        self.CatAddBtn.setText(_translate("MainWindow", "Add"))
        self.CatRemoveBtn.setText(_translate("MainWindow", "Remove"))
        self.label.setText(_translate("MainWindow", "Filter"))
        self.SnipetsBox.setTitle(_translate("MainWindow", "Snippets"))
        self.SnipAddBtn.setText(_translate("MainWindow", "Add"))
        self.SnipRemoveBtn.setText(_translate("MainWindow", "Remove"))
        self.label_2.setText(_translate("MainWindow", "Filter"))
        self.CodeBox.setTitle(_translate("MainWindow", "Code"))
        self.CodeUpdateSaveBtn.setText(_translate("MainWindow", "Update/Save"))

    # Button Event Handling
    def AddCategory(self):
        catExists = False
        catValid = True
        catList = [self.CatListBox.item(i).text() for i in range(self.CatListBox.count())]
        if(self.CatAddEdit.text()):
            for chars in self.CatAddEdit.text():
                if not chars.isalpha():
                    catValid = False
            if (catValid):
                for items in catList:
                    if(items == self.CatAddEdit.text()):
                        MessageBox("Error", "Category already exists.")
                        catExists = True
                if not (catExists):
                    backend.addCategory(str(self.CatAddEdit.text()))
                    self.UpdateCatList()
            else:
                MessageBox("Error", "Category can only contain letters")
        else:
            MessageBox("Error", "No Category Entered")

    #Update CategoryList When we Start the program or add/remove Categories or change the filter
    def UpdateCatList(self):
        self.CatListBox.clear()
        for items in backend.getCategories():
            if(self.CatFilterEdit.text()):
                if (self.CatFilterEdit.text() in items[0]):
                    self.CatListBox.addItem(items[0])
            else:
                self.CatListBox.addItem(items[0])

    #Update Code Snipets List when new Categories are selected
    def UpdateSnipets(self):
        self.CurrentCat = [item.text() for item in self.CatListBox.selectedItems()][0]
        self.SnipListBox.clear()
        for items in backend.getSnipets(self.CurrentCat):
            if(self.SnipFilterEdit.text()):
                if (self.SnipFilterEdit.text() in items[0]):
                    self.SnipListBox.addItem(items[0])
            else:
                self.SnipListBox.addItem(items[0])

    #Add Code Sniplet to current selected Category Table.
    def AddSnipet(self):
        snipExists = False
        snipList = [self.SnipListBox.item(i).text() for i in range(self.SnipListBox.count())]
        if(self.SnipAddEdit.text()):
            for items in snipList:
                if(items == self.SnipAddEdit.text()):
                    MessageBox("Error", "Snippet already exists.")
                    snipExists = True
            if(self.CurrentCat):
                if not (snipExists):
                    backend.addSnipet(self.CurrentCat, str(self.SnipAddEdit.text()))
                    self.UpdateSnipets()
            else:
                MessageBox("Error", "No Category Selected.")
        else:
            MessageBox("Error", "No Snippet Name Entered.")

    def UpdateCode(self):
        if(self.CodeWindow.toPlainText()):
                if(self.CurrentSnip):
                    backend.updateCode(self.CurrentCat,self.CurrentSnip,  str(self.CodeWindow.toPlainText()))
                    MessageBox("Saved", "Code was saved successfully")
                else:
                    MessageBox("Error", "No Code Snippet Selected")
        else:
            MessageBox("Error", "No Snippet Name Entered.")

    def SetCode(self):
        self.CurrentSnip = [item.text() for item in self.SnipListBox.selectedItems()][0]
        self.CodeWindow.clear()
        self.CodeWindow.appendPlainText(backend.getCode(self.CurrentCat, self.CurrentSnip))
        self.CodeWindow.verticalScrollBar().setValue(0)

    def RemoveCategory(self):
        if ([item.text() for item in self.CatListBox.selectedItems()]):
            self.CatListBox.clear()
            self.SnipListBox.clear()
            backend.removeCat(self.CurrentCat)
            self.CurrentCat = ""
            self.UpdateCatList()
        else:
            MessageBox("Error", "No Category Selected.")

    def RemoveSnip(self):
        if ([item.text() for item in self.SnipListBox.selectedItems()]):
            self.SnipListBox.clear()
            self.CodeWindow.clear()
            backend.removeSnip(self.CurrentCat, self.CurrentSnip)
            self.CurrentSnip = ""
            self.UpdateSnipets()
        else:
            MessageBox("Error", "No Snippets Selected.")




def MessageBox(Title, Message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(Message)
    msg.setWindowTitle(Title)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()

if __name__ == "__main__":
    #Setup the QT window and handle themes.
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    app.setStyle('Fusion')
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(15, 15, 15))
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(142, 45, 197).lighter())
    palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    app.setPalette(palette)

    #Create the database if one doesn't exist.
    backend.connect()

    #Show the window
    MainWindow.show()
    sys.exit(app.exec_())
