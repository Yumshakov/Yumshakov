from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, \
    QLabel, QComboBox, QPushButton, QMainWindow, QGridLayout, QVBoxLayout, QTableWidget, QHeaderView


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Сбор Втор')
        self.setGeometry(200, 100, 1000, 600)
        self.setMinimumSize(1000, 600)
        self.style()
        btn_layout = QVBoxLayout()

        btn_filter = QPushButton()
        btn_filter.setIcon(QIcon('//home/vyzcheslav/Yumshakov/CRM_Leshko/pictures/icon/filter_icon.png'))
        btn_filter.setFixedSize(20, 20)
        btn_save = QPushButton('Сохранить')
        btn_company = QPushButton('Справочник компаний')

        btn_layout.addWidget(btn_save)
        btn_layout.addWidget(btn_company)


        table_base = QTableWidget(15, 4)
        table_base.setHorizontalHeaderLabels(['Компании', 'Телефон', 'Вид', 'Цена'])
        table_base.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for i in range(15):
            combo_box_in_table = QComboBox()
            combo_box_in_table.addItems(['','Картон', 'Бумага', 'Пленка', 'Архив', 'Другое'])
            table_base.setCellWidget(i, 2, combo_box_in_table)
            combo_box_in_table.setEditable(True)

        main_layout = QGridLayout()

        main_layout.addWidget(btn_filter, 0, 1, alignment=Qt.AlignRight)
        main_layout.addLayout(btn_layout, 2, 0, alignment=Qt.AlignTop)
        main_layout.addWidget(table_base, 2, 1)



        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)


if __name__ == '__main__':
   app = QApplication([])
   window = MainWindow()
   window.show()
   app.exec_()