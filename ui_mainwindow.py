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
        MainWindow.resize(615, 688)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.year = QSpinBox(self.tab)
        self.year.setObjectName(u"year")
        self.year.setMinimum(1940)
        self.year.setMaximum(2020)
        self.year.setValue(2020)

        self.gridLayout.addWidget(self.year, 2, 1, 1, 1)

        self.autor = QLineEdit(self.tab)
        self.autor.setObjectName(u"autor")

        self.gridLayout.addWidget(self.autor, 1, 1, 1, 1)

        self.titulo = QLineEdit(self.tab)
        self.titulo.setObjectName(u"titulo")

        self.gridLayout.addWidget(self.titulo, 0, 1, 1, 1)

        self.agregar = QPushButton(self.tab)
        self.agregar.setObjectName(u"agregar")

        self.gridLayout.addWidget(self.agregar, 4, 0, 1, 2)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.mostrar = QPushButton(self.tab)
        self.mostrar.setObjectName(u"mostrar")

        self.gridLayout.addWidget(self.mostrar, 5, 0, 1, 2)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.editorial = QLineEdit(self.tab)
        self.editorial.setObjectName(u"editorial")

        self.gridLayout.addWidget(self.editorial, 3, 1, 1, 1)

        self.salida = QPlainTextEdit(self.tab)
        self.salida.setObjectName(u"salida")

        self.gridLayout.addWidget(self.salida, 0, 2, 6, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout = QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buscar_lineedit = QLineEdit(self.tab_2)
        self.buscar_lineedit.setObjectName(u"buscar_lineedit")

        self.horizontalLayout.addWidget(self.buscar_lineedit)

        self.buscar = QPushButton(self.tab_2)
        self.buscar.setObjectName(u"buscar")

        self.horizontalLayout.addWidget(self.buscar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")

        self.verticalLayout.addWidget(self.tabla)

        self.mostrar_tabla = QPushButton(self.tab_2)
        self.mostrar_tabla.setObjectName(u"mostrar_tabla")

        self.verticalLayout.addWidget(self.mostrar_tabla)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 615, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Libros", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Meta+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Meta+S", None))
#endif // QT_CONFIG(shortcut)
        self.agregar.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Editorial", None))
        self.mostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Autor", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrar_tabla.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

