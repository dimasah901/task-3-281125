# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addEditCoffeeForm.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridWidget = QWidget(Dialog)
        self.gridWidget.setObjectName(u"gridWidget")
        self.gridLayout = QGridLayout(self.gridWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.rare = QLineEdit(self.gridWidget)
        self.rare.setObjectName(u"rare")

        self.gridLayout.addWidget(self.rare, 1, 1, 1, 1)

        self.label_2 = QLabel(self.gridWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_4 = QLabel(self.gridWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.sort = QLineEdit(self.gridWidget)
        self.sort.setObjectName(u"sort")

        self.gridLayout.addWidget(self.sort, 0, 1, 1, 1)

        self.taste = QLineEdit(self.gridWidget)
        self.taste.setObjectName(u"taste")

        self.gridLayout.addWidget(self.taste, 3, 1, 1, 1)

        self.state = QLineEdit(self.gridWidget)
        self.state.setObjectName(u"state")

        self.gridLayout.addWidget(self.state, 2, 1, 1, 1)

        self.label_3 = QLabel(self.gridWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label = QLabel(self.gridWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_5 = QLabel(self.gridWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.price = QLineEdit(self.gridWidget)
        self.price.setObjectName(u"price")

        self.gridLayout.addWidget(self.price, 4, 1, 1, 1)

        self.label_6 = QLabel(self.gridWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.volume = QLineEdit(self.gridWidget)
        self.volume.setObjectName(u"volume")

        self.gridLayout.addWidget(self.volume, 5, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.gridWidget)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0435\u043f\u0435\u043d\u044c \u043f\u0440\u043e\u0436\u0430\u0440\u043a\u0438", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0432\u043a\u0443\u0441\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u041c\u043e\u043b\u043e\u0442\u044b\u0439/\u0432 \u0437\u0435\u0440\u043d\u0430\u0445", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u043e\u0440\u0442\u0430", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u0426\u0435\u043d\u0430", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u044a\u0435\u043c \u0443\u043f\u0430\u043a\u043e\u0432\u043a\u0438", None))
    # retranslateUi

