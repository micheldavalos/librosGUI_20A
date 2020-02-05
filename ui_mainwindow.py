# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(305, 462)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.titulo = QLineEdit(self.centralwidget)
        self.titulo.setObjectName(u"titulo")

        self.gridLayout.addWidget(self.titulo, 0, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.autor = QLineEdit(self.centralwidget)
        self.autor.setObjectName(u"autor")

        self.gridLayout.addWidget(self.autor, 1, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.year = QSpinBox(self.centralwidget)
        self.year.setObjectName(u"year")
        self.year.setMinimum(1940)
        self.year.setMaximum(2020)
        self.year.setValue(2020)

        self.gridLayout.addWidget(self.year, 2, 1, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.editorial = QLineEdit(self.centralwidget)
        self.editorial.setObjectName(u"editorial")

        self.gridLayout.addWidget(self.editorial, 3, 1, 1, 1)

        self.agregar = QPushButton(self.centralwidget)
        self.agregar.setObjectName(u"agregar")

        self.gridLayout.addWidget(self.agregar, 4, 0, 1, 2)

        self.mostrar = QPushButton(self.centralwidget)
        self.mostrar.setObjectName(u"mostrar")

        self.gridLayout.addWidget(self.mostrar, 5, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 305, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Libros", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Autor", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Editorial", None))
        self.agregar.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.mostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
    # retranslateUi

