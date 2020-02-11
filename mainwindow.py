from PySide2.QtWidgets import QMainWindow, QFileDialog
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import Slot
import json

class MainWindow(QMainWindow):
    libros = []

    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.agregar.clicked.connect(self.agregar)
        self.ui.mostrar.clicked.connect(self.mostrar)

        self.ui.actionAbrir.triggered.connect(self.abrir)
        self.ui.actionGuardar.triggered.connect(self.guardar)


    @Slot()
    def agregar(self):
        titulo = self.ui.titulo.text()
        autor = self.ui.autor.text()
        year = self.ui.year.value()
        editorial = self.ui.editorial.text()

        libro = {
            'titulo': titulo,
            'autor': autor,
            'year': year,
            'editorial': editorial
        }
        self.libros.append(libro)
        print(libro)

        self.ui.titulo.clear()
        self.ui.autor.clear()
        self.ui.year.setValue(2020)
        self.ui.editorial.clear()

    @Slot()
    def mostrar(self):
        for libro in self.libros:
            print(libro)

    @Slot()
    def abrir(self):
        ubicacion = QFileDialog.getOpenFileName(self,
                                                "Abrir archivo",
                                                ".",
                                                "JSON (*.json)")
        #print(ubicacion)
        with open(ubicacion[0], 'r') as archivo:
            self.libros = json.load(archivo)

    @Slot()
    def guardar(self):
        ubicacion = \
            QFileDialog.getSaveFileName(self,
                                        "Guardar libros",
                                        ".",
                                        "JSON (*.json)"
                                                )
        #print(ubicacion)
        with open(ubicacion[0], 'w') as archivo:
            json.dump(self.libros, archivo, indent=5)
