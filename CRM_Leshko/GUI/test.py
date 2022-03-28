from PyQt5.QtWidgets import QApplication,QPushButton, QLabel, QComboBox, QTableWidget, QMainWindow, QGridLayout, QVBoxLayout
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)

        # Также меняем заголовок окна.
        self.setWindowTitle("My Oneshot App")

if __name__ == '__main__':
   app = QApplication([])
   window = MainWindow()
   window.show()
   app.exec_()