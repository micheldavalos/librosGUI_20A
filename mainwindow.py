from PySide2.QtWidgets import QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox
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

        self.ui.mostrar_tabla.\
            clicked.connect(self.click_mostrar_tabla)
        self.ui.buscar.clicked.connect(self.buscar)


    @Slot()
    def buscar(self):
        libros = []

        autor = self.ui.buscar_lineedit.text()

        for libro in self.libros:
            if autor == libro['autor']:
                libros.append(libro)

        if len(libros) == 0:
            QMessageBox.\
                information(self, "Libros", "No se encontraron libros")
        else:
            self.libros_tabla(libros)

    @Slot()
    def click_mostrar_tabla(self):
        self.libros_tabla(self.libros)

    def libros_tabla(self, libros):
        self.ui.tabla.clear()

        self.ui.tabla.setColumnCount(4)
        self.ui.tabla.setRowCount(len(libros))

        labels = ['Título', 'Autor', 'Año', 'Editorial']
        self.ui.tabla.setHorizontalHeaderLabels(labels)

        row = 0
        for libro in libros:
            titulo = QTableWidgetItem(libro['titulo'])
            autor = QTableWidgetItem(libro['autor'])
            year = QTableWidgetItem(str(libro['year']))
            editorial = QTableWidgetItem(libro['editorial'])

            self.ui.tabla.setItem(row, 0, titulo)
            self.ui.tabla.setItem(row, 1, autor)
            self.ui.tabla.setItem(row, 2, year)
            self.ui.tabla.setItem(row, 3, editorial)

            row += 1


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
            print(libro['titulo'], libro['autor'], libro['year'], libro['editorial'])
            for key, value in libro.items():
                if type(value) is int:
                    value = str(value)
                self.ui.salida.insertPlainText(key + ":" + value + '\n')


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
