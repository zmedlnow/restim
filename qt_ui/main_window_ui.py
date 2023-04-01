# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\designer\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(716, 528)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(230, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = PhaseWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(200, 200))
        self.graphicsView.setMaximumSize(QtCore.QSize(200, 200))
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setSingleStep(0.1)
        self.doubleSpinBox.setProperty("value", 1.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.verticalLayout_2.addWidget(self.doubleSpinBox)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.startStopAudioButton = QtWidgets.QCommandLinkButton(self.groupBox_2)
        self.startStopAudioButton.setObjectName("startStopAudioButton")
        self.verticalLayout_4.addWidget(self.startStopAudioButton)
        self.verticalLayout.addWidget(self.groupBox_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.frame)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_transform_calibration = TransformCalibrationSettingsWidget()
        self.tab_transform_calibration.setObjectName("tab_transform_calibration")
        self.tabWidget.addTab(self.tab_transform_calibration, "")
        self.tab_carrier = ModulationSettingsWidget()
        self.tab_carrier.setObjectName("tab_carrier")
        self.tabWidget.addTab(self.tab_carrier, "")
        self.tab_volume = QtWidgets.QWidget()
        self.tab_volume.setObjectName("tab_volume")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_volume)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 6)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.volumeWidget = VolumeControlWidget(self.tab_volume)
        self.volumeWidget.setObjectName("volumeWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.volumeWidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_6.addWidget(self.volumeWidget)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab_volume, "")
        self.tab_calibration = CalibrationSettingsWidget()
        self.tab_calibration.setObjectName("tab_calibration")
        self.tabWidget.addTab(self.tab_calibration, "")
        self.tab_details = WaveformDetailsWidget()
        self.tab_details.setObjectName("tab_details")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_details)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget.addTab(self.tab_details, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 716, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuTools = QtWidgets.QMenu(self.menuBar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menuBar)
        self.actionFunscript_conversion_2 = QtWidgets.QAction(MainWindow)
        self.actionFunscript_conversion_2.setObjectName("actionFunscript_conversion_2")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.menuTools.addAction(self.actionFunscript_conversion_2)
        self.menuTools.addAction(self.actionPreferences)
        self.menuBar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "restim"))
        self.groupBox.setTitle(_translate("MainWindow", "Pattern generator"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Mouse"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Circle"))
        self.comboBox.setItemText(2, _translate("MainWindow", "A"))
        self.comboBox.setItemText(3, _translate("MainWindow", "B"))
        self.comboBox.setItemText(4, _translate("MainWindow", "C"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Audio"))
        self.startStopAudioButton.setText(_translate("MainWindow", "Start audio"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_transform_calibration), _translate("MainWindow", "Calibration"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_carrier), _translate("MainWindow", "Carrier and modulation"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_volume), _translate("MainWindow", "Volume"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_calibration), _translate("MainWindow", "Fine tuning"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_details), _translate("MainWindow", "Details"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionFunscript_conversion_2.setText(_translate("MainWindow", "Funscript conversion"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
from qt_ui.calibrationsettingswidget import CalibrationSettingsWidget
from qt_ui.modulationsettingswidget import ModulationSettingsWidget
from qt_ui.phasewidget import PhaseWidget
from qt_ui.transformcalibrationsettingswidget import TransformCalibrationSettingsWidget
from qt_ui.volumecontrolwidget import VolumeControlWidget
from qt_ui.waveformdetailswidget import WaveformDetailsWidget
