# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RunWidget/runWidget_expand.ui'
#
# Created: Mon Apr 25 20:38:58 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_runWidget(object):
    def setupUi(self, runWidget):
        runWidget.setObjectName("runWidget")
        runWidget.resize(480, 320)
        self.gridLayout = QtGui.QGridLayout(runWidget)
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.StopButton = QtGui.QPushButton(runWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StopButton.sizePolicy().hasHeightForWidth())
        self.StopButton.setSizePolicy(sizePolicy)
        self.StopButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/stop_btn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.StopButton.setIcon(icon)
        self.StopButton.setIconSize(QtCore.QSize(200, 200))
        self.StopButton.setObjectName("StopButton")
        self.gridLayout.addWidget(self.StopButton, 1, 0, 3, 1)
        self.BBOxGroup = QtGui.QGroupBox(runWidget)
        self.BBOxGroup.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BBOxGroup.sizePolicy().hasHeightForWidth())
        self.BBOxGroup.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BBOxGroup.setFont(font)
        self.BBOxGroup.setObjectName("BBOxGroup")
        self.gridLayout_2 = QtGui.QGridLayout(self.BBOxGroup)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.xMinBBoxTxt = QtGui.QLineEdit(self.BBOxGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xMinBBoxTxt.sizePolicy().hasHeightForWidth())
        self.xMinBBoxTxt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.xMinBBoxTxt.setFont(font)
        self.xMinBBoxTxt.setReadOnly(True)
        self.xMinBBoxTxt.setObjectName("xMinBBoxTxt")
        self.gridLayout_2.addWidget(self.xMinBBoxTxt, 0, 0, 1, 1)
        self.yMinBBoxTxt = QtGui.QLineEdit(self.BBOxGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yMinBBoxTxt.sizePolicy().hasHeightForWidth())
        self.yMinBBoxTxt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.yMinBBoxTxt.setFont(font)
        self.yMinBBoxTxt.setReadOnly(True)
        self.yMinBBoxTxt.setObjectName("yMinBBoxTxt")
        self.gridLayout_2.addWidget(self.yMinBBoxTxt, 0, 1, 1, 1)
        self.zMinBBoxTxt = QtGui.QLineEdit(self.BBOxGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zMinBBoxTxt.sizePolicy().hasHeightForWidth())
        self.zMinBBoxTxt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.zMinBBoxTxt.setFont(font)
        self.zMinBBoxTxt.setReadOnly(True)
        self.zMinBBoxTxt.setObjectName("zMinBBoxTxt")
        self.gridLayout_2.addWidget(self.zMinBBoxTxt, 0, 2, 1, 1)
        self.xMaxBBoxTxt = QtGui.QLineEdit(self.BBOxGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xMaxBBoxTxt.sizePolicy().hasHeightForWidth())
        self.xMaxBBoxTxt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.xMaxBBoxTxt.setFont(font)
        self.xMaxBBoxTxt.setReadOnly(True)
        self.xMaxBBoxTxt.setObjectName("xMaxBBoxTxt")
        self.gridLayout_2.addWidget(self.xMaxBBoxTxt, 1, 0, 1, 1)
        self.yMaxBBoxTxt = QtGui.QLineEdit(self.BBOxGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yMaxBBoxTxt.sizePolicy().hasHeightForWidth())
        self.yMaxBBoxTxt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.yMaxBBoxTxt.setFont(font)
        self.yMaxBBoxTxt.setReadOnly(True)
        self.yMaxBBoxTxt.setObjectName("yMaxBBoxTxt")
        self.gridLayout_2.addWidget(self.yMaxBBoxTxt, 1, 1, 1, 1)
        self.zMaxBBoxTxt = QtGui.QLineEdit(self.BBOxGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zMaxBBoxTxt.sizePolicy().hasHeightForWidth())
        self.zMaxBBoxTxt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.zMaxBBoxTxt.setFont(font)
        self.zMaxBBoxTxt.setReadOnly(True)
        self.zMaxBBoxTxt.setObjectName("zMaxBBoxTxt")
        self.gridLayout_2.addWidget(self.zMaxBBoxTxt, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.BBOxGroup, 1, 1, 1, 1)
        self.estTimeGroup = QtGui.QGroupBox(runWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.estTimeGroup.setFont(font)
        self.estTimeGroup.setObjectName("estTimeGroup")
        self.gridLayout_3 = QtGui.QGridLayout(self.estTimeGroup)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.estTimeProgress = QtGui.QProgressBar(self.estTimeGroup)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.estTimeProgress.setFont(font)
        self.estTimeProgress.setProperty("value", 24)
        self.estTimeProgress.setObjectName("estTimeProgress")
        self.gridLayout_3.addWidget(self.estTimeProgress, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.estTimeGroup, 2, 1, 1, 1)
        self.PauseButton = QtGui.QPushButton(runWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PauseButton.sizePolicy().hasHeightForWidth())
        self.PauseButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(27)
        font.setWeight(75)
        font.setBold(True)
        self.PauseButton.setFont(font)
        self.PauseButton.setObjectName("PauseButton")
        self.gridLayout.addWidget(self.PauseButton, 3, 1, 1, 1)
        self.fileLabel = QtGui.QLabel(runWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileLabel.sizePolicy().hasHeightForWidth())
        self.fileLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.fileLabel.setFont(font)
        self.fileLabel.setCursor(QtCore.Qt.UpArrowCursor)
        self.fileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fileLabel.setObjectName("fileLabel")
        self.gridLayout.addWidget(self.fileLabel, 0, 0, 1, 2)

        self.retranslateUi(runWidget)
        QtCore.QMetaObject.connectSlotsByName(runWidget)

    def retranslateUi(self, runWidget):
        runWidget.setWindowTitle(QtGui.QApplication.translate("runWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.BBOxGroup.setTitle(QtGui.QApplication.translate("runWidget", "Bounding box", None, QtGui.QApplication.UnicodeUTF8))
        self.xMinBBoxTxt.setText(QtGui.QApplication.translate("runWidget", "1234", None, QtGui.QApplication.UnicodeUTF8))
        self.yMinBBoxTxt.setText(QtGui.QApplication.translate("runWidget", "1234", None, QtGui.QApplication.UnicodeUTF8))
        self.zMinBBoxTxt.setText(QtGui.QApplication.translate("runWidget", "1234", None, QtGui.QApplication.UnicodeUTF8))
        self.xMaxBBoxTxt.setText(QtGui.QApplication.translate("runWidget", "1234", None, QtGui.QApplication.UnicodeUTF8))
        self.yMaxBBoxTxt.setText(QtGui.QApplication.translate("runWidget", "1234", None, QtGui.QApplication.UnicodeUTF8))
        self.zMaxBBoxTxt.setText(QtGui.QApplication.translate("runWidget", "1234", None, QtGui.QApplication.UnicodeUTF8))
        self.estTimeGroup.setTitle(QtGui.QApplication.translate("runWidget", "Estimated time", None, QtGui.QApplication.UnicodeUTF8))
        self.estTimeProgress.setFormat(QtGui.QApplication.translate("runWidget", "00:00:00", None, QtGui.QApplication.UnicodeUTF8))
        self.PauseButton.setText(QtGui.QApplication.translate("runWidget", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.fileLabel.setText(QtGui.QApplication.translate("runWidget", "None", None, QtGui.QApplication.UnicodeUTF8))

