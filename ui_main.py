# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cliente.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(624, 378)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -10, 791, 531))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 30, 181, 20))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 110, 49, 16))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(260, 110, 49, 16))
        self.label_3.setFont(font1)
        self.btn_cadastrar = QPushButton(self.frame)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(430, 100, 131, 31))
        font2 = QFont()
        font2.setBold(True)
        self.btn_cadastrar.setFont(font2)
        icon = QIcon()
        icon.addFile(u":/icons/icons/cadastro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastrar.setIcon(icon)
        self.nome_txt = QLineEdit(self.frame)
        self.nome_txt.setObjectName(u"nome_txt")
        self.nome_txt.setGeometry(QRect(130, 110, 113, 21))
        self.cpf_txt = QLineEdit(self.frame)
        self.cpf_txt.setObjectName(u"cpf_txt")
        self.cpf_txt.setGeometry(QRect(290, 110, 113, 21))
        self.btn_pesquisar = QPushButton(self.frame)
        self.btn_pesquisar.setObjectName(u"btn_pesquisar")
        self.btn_pesquisar.setGeometry(QRect(440, 180, 111, 31))
        self.btn_pesquisar.setFont(font2)
        icon1 = QIcon()
        icon1.addFile(u"icons/pesquisar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pesquisar.setIcon(icon1)
        self.btn_alterar = QPushButton(self.frame)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setGeometry(QRect(440, 230, 111, 31))
        self.btn_alterar.setFont(font2)
        icon2 = QIcon()
        icon2.addFile(u"icons/alter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_alterar.setIcon(icon2)
        self.btn_excluir = QPushButton(self.frame)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setGeometry(QRect(440, 280, 111, 31))
        self.btn_excluir.setFont(font2)
        icon3 = QIcon()
        icon3.addFile(u"icons/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_excluir.setIcon(icon3)
        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(70, 180, 351, 141))
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.btn_limpar = QPushButton(self.frame)
        self.btn_limpar.setObjectName(u"btn_limpar")
        self.btn_limpar.setGeometry(QRect(440, 330, 111, 24))
        self.btn_limpar.setFont(font3)
        icon4 = QIcon()
        icon4.addFile(u"icons/limpar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_limpar.setIcon(icon4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cadastro de Cliente", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.btn_pesquisar.setText(QCoreApplication.translate("MainWindow", u"PESQUISAR", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"ALTERAR", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
#if QT_CONFIG(tooltip)
        self.tableWidget.setToolTip(QCoreApplication.translate("MainWindow", u"tabela de Cliente", None))
#endif // QT_CONFIG(tooltip)
        self.btn_limpar.setText(QCoreApplication.translate("MainWindow", u"LIMPAR", None))
    # retranslateUi

