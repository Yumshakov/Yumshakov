import sys

from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QIcon, QRegExpValidator
from PyQt5.QtWidgets import *

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
        btn_filter.setEnabled(False)

        btn_save = QPushButton('Сохранить')
        btn_company = QPushButton('Справочник компаний')
        btn_company.clicked.connect(self.create_enterprise)

        btn_layout.addWidget(btn_save)
        btn_layout.addWidget(btn_company)

        table_base = QTableWidget(15, 4)
        table_base.setHorizontalHeaderLabels(['Компании', 'Телефон', 'Вид', 'Цена'])

        # Stretched the table over the entire cell space
        table_base.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # Create table for add data in the base
        for i in range(15):
            combo_box_in_table = QComboBox()
            combo_box_in_table.addItems(['','Картон', 'Бумага', 'Пленка', 'Архив', 'Другое'])
            table_base.setCellWidget(i, 2, combo_box_in_table)
            combo_box_in_table.setEditable(True)
            combo_box_in_table.setFrame(False)


        main_layout = QGridLayout()

        main_layout.addWidget(btn_filter, 0, 1, alignment=Qt.AlignRight)
        main_layout.addLayout(btn_layout, 2, 0, alignment=Qt.AlignTop)
        main_layout.addWidget(table_base, 2, 1)



        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def create_enterprise(self):
        enterprise_window = QDialog(self)
        enterprise_window.setFixedSize(270, 160)
        enterprise_window.setWindowTitle('Создание компании')

        name_label_enterprice = QLabel('Название:', enterprise_window)
        name_label_enterprice.move(20, 20)


        name_enterprice = QLineEdit(enterprise_window)
        name_enterprice.move(100, 15)
        validator = QRegExpValidator(QRegExp('[А-Яа-я]*'))
        name_enterprice.setValidator(validator)

        tel_label_enterprice = QLabel('Телефон:', enterprise_window)
        tel_label_enterprice.move(20, 50)
        tel_enterprise = QLineEdit(enterprise_window)
        tel_enterprise.move(100, 45)
        tel_enterprise.setInputMask('+7 (999)-999-99-99; ')

        people_lable_enterprice = QLabel('ЛПР:', enterprise_window)
        people_lable_enterprice.move(20, 80)
        people_enterprice = QLineEdit(enterprise_window)
        people_enterprice.move(100, 75)
        people_enterprice.setValidator(validator)


        def event_cliked_btn_save():
            enterprise_window.close()

        save_btn = QPushButton('Сохранить', enterprise_window)
        cancel_btn = QPushButton('Отмена', enterprise_window)
        save_btn.clicked.connect(event_cliked_btn_save)
        cancel_btn.clicked.connect(event_cliked_btn_save)
        save_btn.move(60, 120)
        cancel_btn.move(160, 120)

        enterprise_window.show()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MainWindow()
   window.show()
   sys.exit(app.exec_())