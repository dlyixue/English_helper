# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\xhc\pycode\English_Learning_Helper\dictation\Dictool0.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(786, 309)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 30, 131, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 100, 151, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(180, 150, 151, 31))
        self.label_3.setObjectName("label_3")
        self.chapter = QtWidgets.QSpinBox(Dialog)
        self.chapter.setGeometry(QtCore.QRect(330, 110, 42, 22))
        self.chapter.setObjectName("chapter")
        self.test = QtWidgets.QSpinBox(Dialog)
        self.test.setGeometry(QtCore.QRect(330, 150, 42, 22))
        self.test.setObjectName("test")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(580, 240, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "听写测试"))
        self.label_2.setText(_translate("Dialog", "输入chapter"))
        self.label_3.setText(_translate("Dialog", "输入test"))
        self.pushButton.setText(_translate("Dialog", "start"))
