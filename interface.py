# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceXiFPlM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(338, 424)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.addon_edit = QLineEdit(self.centralwidget)
        self.addon_edit.setObjectName(u"addon_edit")

        self.gridLayout.addWidget(self.addon_edit, 6, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.csgo_button = QPushButton(self.centralwidget)
        self.csgo_button.setObjectName(u"csgo_button")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.csgo_button.sizePolicy().hasHeightForWidth())
        self.csgo_button.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.csgo_button)

        self.csgo_label = QLabel(self.centralwidget)
        self.csgo_label.setObjectName(u"csgo_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.csgo_label.sizePolicy().hasHeightForWidth())
        self.csgo_label.setSizePolicy(sizePolicy1)
        self.csgo_label.setFrameShape(QFrame.Box)
        self.csgo_label.setFrameShadow(QFrame.Raised)
        self.csgo_label.setAlignment(Qt.AlignCenter)
        self.csgo_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.csgo_label)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.launch_options_edit = QLineEdit(self.centralwidget)
        self.launch_options_edit.setObjectName(u"launch_options_edit")

        self.gridLayout.addWidget(self.launch_options_edit, 7, 1, 1, 2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.vmf_button = QPushButton(self.centralwidget)
        self.vmf_button.setObjectName(u"vmf_button")
        sizePolicy.setHeightForWidth(self.vmf_button.sizePolicy().hasHeightForWidth())
        self.vmf_button.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.vmf_button)

        self.vmf_label = QLabel(self.centralwidget)
        self.vmf_label.setObjectName(u"vmf_label")
        sizePolicy1.setHeightForWidth(self.vmf_label.sizePolicy().hasHeightForWidth())
        self.vmf_label.setSizePolicy(sizePolicy1)
        self.vmf_label.setFrameShape(QFrame.Box)
        self.vmf_label.setFrameShadow(QFrame.Raised)
        self.vmf_label.setAlignment(Qt.AlignCenter)
        self.vmf_label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.vmf_label)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 2, 1, 2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line, 4, 1, 1, 3)

        self.go_button = QPushButton(self.centralwidget)
        self.go_button.setObjectName(u"go_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.go_button.sizePolicy().hasHeightForWidth())
        self.go_button.setSizePolicy(sizePolicy2)
        self.go_button.setAutoFillBackground(False)
        self.go_button.setStyleSheet(u"background-color:rgb(0, 255, 0)")

        self.gridLayout.addWidget(self.go_button, 6, 3, 2, 1)

        self.config_checkbox = QCheckBox(self.centralwidget)
        self.config_checkbox.setObjectName(u"config_checkbox")

        self.gridLayout.addWidget(self.config_checkbox, 5, 1, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.addon_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter addon name:", None))
#if QT_CONFIG(tooltip)
        self.csgo_button.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.csgo_button.setText(QCoreApplication.translate("MainWindow", u"Select \"Counter-Strike Global Offensive\" folder", None))
        self.csgo_label.setText(QCoreApplication.translate("MainWindow", u"None selected", None))
        self.launch_options_edit.setText(QCoreApplication.translate("MainWindow", u"-usebsp", None))
        self.launch_options_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter launch options:", None))
#if QT_CONFIG(tooltip)
        self.vmf_button.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.vmf_button.setText(QCoreApplication.translate("MainWindow", u"Select .VMF", None))
        self.vmf_label.setText(QCoreApplication.translate("MainWindow", u"None selected", None))
        self.go_button.setText(QCoreApplication.translate("MainWindow", u"GO!", None))
        self.config_checkbox.setText(QCoreApplication.translate("MainWindow", u"Save to config?", None))
    # retranslateUi

