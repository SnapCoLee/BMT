# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'storehouse_windows.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_storehouse_window(object):
    def setupUi(self, storehouse_window):
        storehouse_window.setObjectName("storehouse_window")
        storehouse_window.resize(1000, 800)
        storehouse_window.setMaximumSize(QtCore.QSize(1000, 800))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        storehouse_window.setFont(font)
        storehouse_window.setWindowTitle("storehouse_window")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/resource/BMT_64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        storehouse_window.setWindowIcon(icon)
        storehouse_window.setStyleSheet("background-color: rgb(193, 200, 187);")
        self.centralwidget = QtWidgets.QWidget(storehouse_window)
        self.centralwidget.setObjectName("centralwidget")
        self.call_for_help = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.call_for_help.setGeometry(QtCore.QRect(800, 20, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.call_for_help.setFont(font)
        self.call_for_help.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.call_for_help.setToolTipDuration(0)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ico/resource/BMT_32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.call_for_help.setIcon(icon1)
        self.call_for_help.setObjectName("call_for_help")
        self.client_name = QtWidgets.QLabel(self.centralwidget)
        self.client_name.setGeometry(QtCore.QRect(160, 40, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.client_name.setFont(font)
        self.client_name.setAlignment(QtCore.Qt.AlignCenter)
        self.client_name.setObjectName("client_name")
        self.output = QtWidgets.QPushButton(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(640, 70, 100, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.output.setFont(font)
        self.output.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.output.setObjectName("output")
        self.input = QtWidgets.QPushButton(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(520, 70, 100, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.input.setFont(font)
        self.input.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.input.setObjectName("input")
        self.refresh = QtWidgets.QPushButton(self.centralwidget)
        self.refresh.setGeometry(QtCore.QRect(260, 70, 100, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.refresh.setFont(font)
        self.refresh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.refresh.setObjectName("refresh")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(50, 130, 900, 650))
        self.table.setRowCount(0)
        self.table.setColumnCount(5)
        self.table.setObjectName("table")
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        self.table.horizontalHeader().setDefaultSectionSize(180)
        self.table.verticalHeader().setDefaultSectionSize(36)
        self.shop = QtWidgets.QPushButton(self.centralwidget)
        self.shop.setGeometry(QtCore.QRect(380, 70, 121, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.shop.setFont(font)
        self.shop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.shop.setObjectName("shop")
        self.pricechange = QtWidgets.QPushButton(self.centralwidget)
        self.pricechange.setGeometry(QtCore.QRect(760, 70, 101, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.pricechange.setFont(font)
        self.pricechange.setObjectName("pricechange")
        self.client_logo = QtWidgets.QLabel(self.centralwidget)
        self.client_logo.setGeometry(QtCore.QRect(40, 0, 128, 128))
        self.client_logo.setObjectName("client_logo")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(880, 70, 71, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.client_logo.raise_()
        self.call_for_help.raise_()
        self.client_name.raise_()
        self.output.raise_()
        self.input.raise_()
        self.refresh.raise_()
        self.table.raise_()
        self.shop.raise_()
        self.pricechange.raise_()
        self.back.raise_()
        storehouse_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(storehouse_window)
        QtCore.QMetaObject.connectSlotsByName(storehouse_window)
        storehouse_window.setTabOrder(self.call_for_help, self.input)
        storehouse_window.setTabOrder(self.input, self.output)

    def retranslateUi(self, storehouse_window):
        _translate = QtCore.QCoreApplication.translate
        self.call_for_help.setToolTip(_translate("storehouse_window", "<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">huyan35@mail2.sysu.edu.cn</span></p></body></html>"))
        self.call_for_help.setText(_translate("storehouse_window", "联系客服(点我复制)"))
        self.client_name.setText(_translate("storehouse_window", "<html><head/><body><p><span style=\" font-size:28pt; font-style:italic;\">BMT</span></p></body></html>"))
        self.output.setText(_translate("storehouse_window", "出库单"))
        self.input.setText(_translate("storehouse_window", "入库单"))
        self.refresh.setText(_translate("storehouse_window", "更新书目"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("storehouse_window", "书目类别"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("storehouse_window", "书籍名称"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("storehouse_window", "进价"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("storehouse_window", "售价"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("storehouse_window", "库存"))
        self.shop.setText(_translate("storehouse_window", "生成采购单"))
        self.pricechange.setText(_translate("storehouse_window", "更新进价"))
        self.client_logo.setText(_translate("storehouse_window", "<html><head/><body><p><img src=\":/logo/resource/BMT_128.ico\"/></p></body></html>"))
        self.back.setText(_translate("storehouse_window", "返回"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    storehouse_window = QtWidgets.QMainWindow()
    ui = Ui_storehouse_window()
    ui.setupUi(storehouse_window)
    storehouse_window.show()
    sys.exit(app.exec_())
