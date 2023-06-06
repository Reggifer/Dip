from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создание кнопки в главном окне
        self.button = QPushButton('Открыть дополнительное окно', self)
        self.button.clicked.connect(self.open_dialog)
        self.setCentralWidget(self.button)

    def open_dialog(self):
        # Создание дополнительного окна
        self.dialog = QDialog(self)
        self.dialog.button = QPushButton('Выполнить', self.dialog)
        self.dialog.button.clicked.connect(self.execute_code)
        self.dialog.button.clicked.connect(self.close_dialog)
        self.dialog.setLayout(QVBoxLayout())
        self.dialog.layout().addWidget(self.dialog.button)
        self.dialog.exec_()

    def execute_code(self):
        # Код, который нужно выполнить в главном окне
        print('Выполнение кода в главном окне')

    def close_dialog(self):
        # Закрытие дополнительного окна
        self.dialog.close()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()