# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './signalum_desktop.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(756, 630)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.adapterTab = QtWidgets.QWidget()
        self.adapterTab.setObjectName("adapterTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.adapterTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.adapterTab)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.bluetoothAdapterTable = QtWidgets.QTableWidget(self.adapterTab)
        self.bluetoothAdapterTable.setObjectName("bluetoothAdapterTable")
        self.bluetoothAdapterTable.setColumnCount(2)
        self.bluetoothAdapterTable.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothAdapterTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothAdapterTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothAdapterTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothAdapterTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothAdapterTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothAdapterTable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothAdapterTable.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothAdapterTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothAdapterTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.bluetoothAdapterTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.bluetoothAdapterTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.bluetoothAdapterTable.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.bluetoothAdapterTable.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.bluetoothAdapterTable.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.bluetoothAdapterTable.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothAdapterTable.setItem(6, 0, item)
        self.bluetoothAdapterTable.horizontalHeader().setDefaultSectionSize(200)
        self.bluetoothAdapterTable.horizontalHeader().setStretchLastSection(False)
        self.bluetoothAdapterTable.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.bluetoothAdapterTable)
        self.label = QtWidgets.QLabel(self.adapterTab)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.wifiAdapterTable = QtWidgets.QTableWidget(self.adapterTab)
        self.wifiAdapterTable.setObjectName("wifiAdapterTable")
        self.wifiAdapterTable.setColumnCount(2)
        self.wifiAdapterTable.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.wifiAdapterTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiAdapterTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiAdapterTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiAdapterTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiAdapterTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiAdapterTable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiAdapterTable.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiAdapterTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiAdapterTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.wifiAdapterTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.wifiAdapterTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.wifiAdapterTable.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.wifiAdapterTable.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.wifiAdapterTable.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.wifiAdapterTable.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiAdapterTable.setItem(6, 0, item)
        self.wifiAdapterTable.horizontalHeader().setDefaultSectionSize(200)
        self.wifiAdapterTable.horizontalHeader().setStretchLastSection(False)
        self.wifiAdapterTable.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.wifiAdapterTable)
        self.tabWidget.addTab(self.adapterTab, "")
        self.bluetoothTab = QtWidgets.QWidget()
        self.bluetoothTab.setObjectName("bluetoothTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.bluetoothTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.bluetoothTab)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.btGraphTab = QtWidgets.QWidget()
        self.btGraphTab.setObjectName("btGraphTab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.btGraphTab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.bluetoothGraphLayout = QtWidgets.QVBoxLayout()
        self.bluetoothGraphLayout.setObjectName("bluetoothGraphLayout")
        self.verticalLayout_5.addLayout(self.bluetoothGraphLayout)
        self.bluetoothGraphToolbar = QtWidgets.QVBoxLayout()
        self.bluetoothGraphToolbar.setObjectName("bluetoothGraphToolbar")
        self.verticalLayout_5.addLayout(self.bluetoothGraphToolbar)
        self.tabWidget_2.addTab(self.btGraphTab, "")
        self.btDevicesTab = QtWidgets.QWidget()
        self.btDevicesTab.setObjectName("btDevicesTab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.btDevicesTab)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.bluetoothTable = QtWidgets.QTableWidget(self.btDevicesTab)
        self.bluetoothTable.setObjectName("bluetoothTable")
        self.bluetoothTable.setColumnCount(6)
        self.bluetoothTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothTable.setHorizontalHeaderItem(5, item)
        self.bluetoothTable.horizontalHeader().setCascadingSectionResizes(False)
        self.bluetoothTable.horizontalHeader().setDefaultSectionSize(110)
        self.bluetoothTable.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_9.addWidget(self.bluetoothTable)
        self.tabWidget_2.addTab(self.btDevicesTab, "")
        self.verticalLayout_4.addWidget(self.tabWidget_2)
        self.tabWidget.addTab(self.bluetoothTab, "")
        self.wifiTab = QtWidgets.QWidget()
        self.wifiTab.setObjectName("wifiTab")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.wifiTab)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.wifiTab)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.wifiDevicesTab = QtWidgets.QWidget()
        self.wifiDevicesTab.setObjectName("wifiDevicesTab")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.wifiDevicesTab)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.wifiTable = QtWidgets.QTableWidget(self.wifiDevicesTab)
        self.wifiTable.setObjectName("wifiTable")
        self.wifiTable.setColumnCount(8)
        self.wifiTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.wifiTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiTable.setHorizontalHeaderItem(7, item)
        self.wifiTable.horizontalHeader().setCascadingSectionResizes(True)
        self.wifiTable.horizontalHeader().setDefaultSectionSize(110)
        self.wifiTable.horizontalHeader().setStretchLastSection(True)
        self.wifiTable.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_11.addWidget(self.wifiTable)
        self.tabWidget_3.addTab(self.wifiDevicesTab, "")
        self.wifiGraphTab = QtWidgets.QWidget()
        self.wifiGraphTab.setObjectName("wifiGraphTab")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.wifiGraphTab)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.wifiGraphLayout = QtWidgets.QVBoxLayout()
        self.wifiGraphLayout.setObjectName("wifiGraphLayout")
        self.verticalLayout_12.addLayout(self.wifiGraphLayout)
        self.wifiGraphToolbar = QtWidgets.QVBoxLayout()
        self.wifiGraphToolbar.setObjectName("wifiGraphToolbar")
        self.verticalLayout_12.addLayout(self.wifiGraphToolbar)
        self.tabWidget_3.addTab(self.wifiGraphTab, "")
        self.verticalLayout_10.addWidget(self.tabWidget_3)
        self.tabWidget.addTab(self.wifiTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 756, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExport = QtWidgets.QMenu(self.menuFile)
        self.menuExport.setObjectName("menuExport")
        self.menuPreferences = QtWidgets.QMenu(self.menubar)
        self.menuPreferences.setObjectName("menuPreferences")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setShortcutContext(QtCore.Qt.WidgetWithChildrenShortcut)
        self.actionSave.setObjectName("actionSave")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionExportWifi = QtWidgets.QAction(MainWindow)
        self.actionExportWifi.setObjectName("actionExportWifi")
        self.actionExportBluetooth = QtWidgets.QAction(MainWindow)
        self.actionExportBluetooth.setObjectName("actionExportBluetooth")
        self.menuExport.addAction(self.actionExportWifi)
        self.menuExport.addAction(self.actionExportBluetooth)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.menuExport.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuPreferences.addAction(self.actionPreferences)
        self.menuAbout.addAction(self.actionDocumentation)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPreferences.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Wifi Adapter"))
        item = self.bluetoothAdapterTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Property"))
        item = self.bluetoothAdapterTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        __sortingEnabled = self.bluetoothAdapterTable.isSortingEnabled()
        self.bluetoothAdapterTable.setSortingEnabled(False)
        item = self.bluetoothAdapterTable.item(0, 0)
        item.setText(_translate("MainWindow", "Vendor"))
        item = self.bluetoothAdapterTable.item(1, 0)
        item.setText(_translate("MainWindow", "MAC Address"))
        item = self.bluetoothAdapterTable.item(2, 0)
        item.setText(_translate("MainWindow", "API"))
        item = self.bluetoothAdapterTable.item(3, 0)
        item.setText(_translate("MainWindow", "Revision"))
        item = self.bluetoothAdapterTable.item(4, 0)
        item.setText(_translate("MainWindow", "Services"))
        item = self.bluetoothAdapterTable.item(5, 0)
        item.setText(_translate("MainWindow", "Class"))
        item = self.bluetoothAdapterTable.item(6, 0)
        item.setText(_translate("MainWindow", "Manufacturer"))
        self.bluetoothAdapterTable.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Bluetooth Adapter"))
        item = self.wifiAdapterTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Property"))
        item = self.wifiAdapterTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        __sortingEnabled = self.wifiAdapterTable.isSortingEnabled()
        self.wifiAdapterTable.setSortingEnabled(False)
        item = self.wifiAdapterTable.item(0, 0)
        item.setText(_translate("MainWindow", "Vendor"))
        item = self.wifiAdapterTable.item(1, 0)
        item.setText(_translate("MainWindow", "MAC Address"))
        item = self.wifiAdapterTable.item(2, 0)
        item.setText(_translate("MainWindow", "API"))
        item = self.wifiAdapterTable.item(3, 0)
        item.setText(_translate("MainWindow", "Revision"))
        item = self.wifiAdapterTable.item(4, 0)
        item.setText(_translate("MainWindow", "Services"))
        item = self.wifiAdapterTable.item(5, 0)
        item.setText(_translate("MainWindow", "Class"))
        item = self.wifiAdapterTable.item(6, 0)
        item.setText(_translate("MainWindow", "Manufacturer"))
        self.wifiAdapterTable.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.adapterTab), _translate("MainWindow", "Adapter Overview"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.btGraphTab), _translate("MainWindow", "Graph"))
        self.bluetoothTable.setSortingEnabled(True)
        item = self.bluetoothTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Device"))
        item = self.bluetoothTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "MAC Address"))
        item = self.bluetoothTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Signal Strength"))
        item = self.bluetoothTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Major Class"))
        item = self.bluetoothTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Minor Class"))
        item = self.bluetoothTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Services"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.btDevicesTab), _translate("MainWindow", "Devices"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.bluetoothTab), _translate("MainWindow", "Bluetooth"))
        self.wifiTable.setSortingEnabled(True)
        item = self.wifiTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.wifiTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "MAC Address"))
        item = self.wifiTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "RSSI"))
        item = self.wifiTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Frequency"))
        item = self.wifiTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Quality"))
        item = self.wifiTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Encryption Type"))
        item = self.wifiTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Mode of Device"))
        item = self.wifiTable.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Channel"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.wifiDevicesTab), _translate("MainWindow", "Devices"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.wifiGraphTab), _translate("MainWindow", "Graph"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.wifiTab), _translate("MainWindow", "WiFi"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuExport.setTitle(_translate("MainWindow", "Export"))
        self.menuPreferences.setTitle(_translate("MainWindow", "Settings"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionAbout.setText(_translate("MainWindow", "About Signalum"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionExportWifi.setText(_translate("MainWindow", "WiFi"))
        self.actionExportBluetooth.setText(_translate("MainWindow", "Bluetooth"))


