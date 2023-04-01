# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\designer\preferencesdialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PreferencesDialog(object):
    def setupUi(self, PreferencesDialog):
        PreferencesDialog.setObjectName("PreferencesDialog")
        PreferencesDialog.resize(406, 345)
        self.verticalLayout = QtWidgets.QVBoxLayout(PreferencesDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(PreferencesDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gb_websocket_server = QtWidgets.QGroupBox(self.tab)
        self.gb_websocket_server.setCheckable(True)
        self.gb_websocket_server.setObjectName("gb_websocket_server")
        self.formLayout_4 = QtWidgets.QFormLayout(self.gb_websocket_server)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label = QtWidgets.QLabel(self.gb_websocket_server)
        self.label.setObjectName("label")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_6 = QtWidgets.QLabel(self.gb_websocket_server)
        self.label_6.setObjectName("label_6")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.websocket_localhost_only = QtWidgets.QCheckBox(self.gb_websocket_server)
        self.websocket_localhost_only.setText("")
        self.websocket_localhost_only.setObjectName("websocket_localhost_only")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.websocket_localhost_only)
        self.websocket_port = QtWidgets.QSpinBox(self.gb_websocket_server)
        self.websocket_port.setMaximum(65535)
        self.websocket_port.setObjectName("websocket_port")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.websocket_port)
        self.verticalLayout_2.addWidget(self.gb_websocket_server)
        self.gb_tcp_server = QtWidgets.QGroupBox(self.tab)
        self.gb_tcp_server.setCheckable(True)
        self.gb_tcp_server.setObjectName("gb_tcp_server")
        self.formLayout_2 = QtWidgets.QFormLayout(self.gb_tcp_server)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.gb_tcp_server)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_10 = QtWidgets.QLabel(self.gb_tcp_server)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.tcp_localhost_only = QtWidgets.QCheckBox(self.gb_tcp_server)
        self.tcp_localhost_only.setText("")
        self.tcp_localhost_only.setObjectName("tcp_localhost_only")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.tcp_localhost_only)
        self.tcp_port = QtWidgets.QSpinBox(self.gb_tcp_server)
        self.tcp_port.setMaximum(65535)
        self.tcp_port.setObjectName("tcp_port")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tcp_port)
        self.verticalLayout_2.addWidget(self.gb_tcp_server)
        self.gb_udp_server = QtWidgets.QGroupBox(self.tab)
        self.gb_udp_server.setFlat(False)
        self.gb_udp_server.setCheckable(True)
        self.gb_udp_server.setObjectName("gb_udp_server")
        self.formLayout = QtWidgets.QFormLayout(self.gb_udp_server)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.gb_udp_server)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_11 = QtWidgets.QLabel(self.gb_udp_server)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.udp_localhost_only = QtWidgets.QCheckBox(self.gb_udp_server)
        self.udp_localhost_only.setText("")
        self.udp_localhost_only.setObjectName("udp_localhost_only")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.udp_localhost_only)
        self.udp_port = QtWidgets.QSpinBox(self.gb_udp_server)
        self.udp_port.setMaximum(65535)
        self.udp_port.setObjectName("udp_port")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.udp_port)
        self.verticalLayout_2.addWidget(self.gb_udp_server)
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.audio_api = QtWidgets.QComboBox(self.groupBox)
        self.audio_api.setObjectName("audio_api")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.audio_api)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.audio_device = QtWidgets.QComboBox(self.groupBox)
        self.audio_device.setObjectName("audio_device")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.audio_device)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.audio_latency = QtWidgets.QComboBox(self.groupBox)
        self.audio_latency.setObjectName("audio_latency")
        self.audio_latency.addItem("")
        self.audio_latency.addItem("")
        self.audio_latency.addItem("")
        self.audio_latency.addItem("")
        self.audio_latency.addItem("")
        self.audio_latency.addItem("")
        self.audio_latency.addItem("")
        self.audio_latency.addItem("")
        self.audio_latency.addItem("")
        self.audio_latency.addItem("")
        self.audio_latency.addItem("")
        self.audio_latency.addItem("")
        self.audio_latency.addItem("")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.audio_latency)
        self.verticalLayout_3.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_5.setEnabled(False)
        self.groupBox_5.setObjectName("groupBox_5")
        self.formLayout_5 = QtWidgets.QFormLayout(self.groupBox_5)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setObjectName("label_2")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setObjectName("label_5")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinBox.setMaximum(1000)
        self.spinBox.setObjectName("spinBox")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox.setSuffix("")
        self.doubleSpinBox.setMaximum(1000.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox)
        self.verticalLayout_4.addWidget(self.groupBox_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.buttonBox = QtWidgets.QDialogButtonBox(PreferencesDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(PreferencesDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PreferencesDialog)
        PreferencesDialog.setTabOrder(self.udp_localhost_only, self.audio_latency)
        PreferencesDialog.setTabOrder(self.audio_latency, self.spinBox)
        PreferencesDialog.setTabOrder(self.spinBox, self.doubleSpinBox)
        PreferencesDialog.setTabOrder(self.doubleSpinBox, self.audio_api)
        PreferencesDialog.setTabOrder(self.audio_api, self.audio_device)
        PreferencesDialog.setTabOrder(self.audio_device, self.tabWidget)
        PreferencesDialog.setTabOrder(self.tabWidget, self.gb_websocket_server)
        PreferencesDialog.setTabOrder(self.gb_websocket_server, self.websocket_localhost_only)
        PreferencesDialog.setTabOrder(self.websocket_localhost_only, self.gb_tcp_server)
        PreferencesDialog.setTabOrder(self.gb_tcp_server, self.tcp_localhost_only)
        PreferencesDialog.setTabOrder(self.tcp_localhost_only, self.gb_udp_server)

    def retranslateUi(self, PreferencesDialog):
        _translate = QtCore.QCoreApplication.translate
        PreferencesDialog.setWindowTitle(_translate("PreferencesDialog", "Preferences"))
        self.gb_websocket_server.setTitle(_translate("PreferencesDialog", "Websocket server"))
        self.label.setText(_translate("PreferencesDialog", "Port"))
        self.label_6.setText(_translate("PreferencesDialog", "Localhost only"))
        self.gb_tcp_server.setTitle(_translate("PreferencesDialog", "TCP server"))
        self.label_3.setText(_translate("PreferencesDialog", "Port"))
        self.label_10.setText(_translate("PreferencesDialog", "Localhost only"))
        self.gb_udp_server.setTitle(_translate("PreferencesDialog", "UDP server"))
        self.label_4.setText(_translate("PreferencesDialog", "Port"))
        self.label_11.setText(_translate("PreferencesDialog", "Localhost only"))
        self.label_12.setText(_translate("PreferencesDialog", "Changes require restart"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("PreferencesDialog", "Network"))
        self.groupBox.setTitle(_translate("PreferencesDialog", "Audio"))
        self.label_7.setText(_translate("PreferencesDialog", "Audio API"))
        self.label_8.setText(_translate("PreferencesDialog", "Device"))
        self.label_9.setText(_translate("PreferencesDialog", "Latency"))
        self.audio_latency.setItemText(0, _translate("PreferencesDialog", "high"))
        self.audio_latency.setItemText(1, _translate("PreferencesDialog", "low"))
        self.audio_latency.setItemText(2, _translate("PreferencesDialog", "0.00"))
        self.audio_latency.setItemText(3, _translate("PreferencesDialog", "0.02"))
        self.audio_latency.setItemText(4, _translate("PreferencesDialog", "0.04"))
        self.audio_latency.setItemText(5, _translate("PreferencesDialog", "0.06"))
        self.audio_latency.setItemText(6, _translate("PreferencesDialog", "0.08"))
        self.audio_latency.setItemText(7, _translate("PreferencesDialog", "0.10"))
        self.audio_latency.setItemText(8, _translate("PreferencesDialog", "0.12"))
        self.audio_latency.setItemText(9, _translate("PreferencesDialog", "0.14"))
        self.audio_latency.setItemText(10, _translate("PreferencesDialog", "0.16"))
        self.audio_latency.setItemText(11, _translate("PreferencesDialog", "0.18"))
        self.audio_latency.setItemText(12, _translate("PreferencesDialog", "0.20"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("PreferencesDialog", "Audio"))
        self.groupBox_5.setTitle(_translate("PreferencesDialog", "Phase"))
        self.label_2.setText(_translate("PreferencesDialog", "max fps"))
        self.label_5.setText(_translate("PreferencesDialog", "display latency [ms]"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("PreferencesDialog", "Display"))
