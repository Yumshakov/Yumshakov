from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QLabel, QComboBox, QTableWidget, QWidget, QGridLayout, QVBoxLayout

def main_window():
    app = QApplication([])
    window = QWidget()
    window.show()
    window.setGeometry(200, 100, 1000, 600)
    window.setMinimumSize(1000, 600)
    window.setWindowTitle('Сбор Втор')

    layout = QVBoxLayout()
    layout.addWidget(QTableWidget(10,5))
    layout.setGeometry(QRect(100, 50, 500, 500))
    #main_layout = QGridLayout()
    #main_layout.addLayout()
    window.setLayout(layout)
    app.exec_()

if __name__ == '__main__':
   main_window()
