# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'g:\FracktalWorks\Volterra400TouchUI\octoprint_Volterra400TouchUI\mainGUI_volterra400.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(480, 800)
        MainWindow.setMinimumSize(QtCore.QSize(480, 800))
        MainWindow.setMaximumSize(QtCore.QSize(480, 800))
        MainWindow.setStyleSheet(_fromUtf8("QStatusBar {\n"
"    background-color: rgb(49, 49, 49);\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"}"))
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.mainApplication = QtGui.QWidget(MainWindow)
        self.mainApplication.setObjectName(_fromUtf8("mainApplication"))
        self.stackedWidget = QtGui.QStackedWidget(self.mainApplication)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 480, 800))
        self.stackedWidget.setMinimumSize(QtCore.QSize(480, 800))
        self.stackedWidget.setMaximumSize(QtCore.QSize(480, 800))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.stackedWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(_fromUtf8("\n"
"background-color: rgb(40, 40, 40);"))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.loadingPage = QtGui.QWidget()
        self.loadingPage.setObjectName(_fromUtf8("loadingPage"))
        self.LoadingLabel = QtGui.QLabel(self.loadingPage)
        self.LoadingLabel.setGeometry(QtCore.QRect(0, 0, 481, 800))
        self.LoadingLabel.setStyleSheet(_fromUtf8("background:rgb(255, 255, 255)"))
        self.LoadingLabel.setText(_fromUtf8(""))
        self.LoadingLabel.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/splash.png")))
        self.LoadingLabel.setObjectName(_fromUtf8("LoadingLabel"))
        self.loadingGif = QtGui.QLabel(self.loadingPage)
        self.loadingGif.setGeometry(QtCore.QRect(190, 436, 100, 97))
        self.loadingGif.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255,0);"))
        self.loadingGif.setText(_fromUtf8(""))
        self.loadingGif.setScaledContents(True)
        self.loadingGif.setObjectName(_fromUtf8("loadingGif"))
        self.stackedWidget.addWidget(self.loadingPage)
        self.homePage = QtGui.QWidget()
        self.homePage.setObjectName(_fromUtf8("homePage"))
        self.playPauseButton = QtGui.QPushButton(self.homePage)
        self.playPauseButton.setGeometry(QtCore.QRect(220, 650, 131, 111))
        self.playPauseButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        self.playPauseButton.setFont(font)
        self.playPauseButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.playPauseButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/play-button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/pause-button.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.playPauseButton.setIcon(icon)
        self.playPauseButton.setIconSize(QtCore.QSize(40, 40))
        self.playPauseButton.setCheckable(True)
        self.playPauseButton.setChecked(False)
        self.playPauseButton.setAutoDefault(False)
        self.playPauseButton.setDefault(False)
        self.playPauseButton.setFlat(False)
        self.playPauseButton.setObjectName(_fromUtf8("playPauseButton"))
        self.stopButton = QtGui.QPushButton(self.homePage)
        self.stopButton.setGeometry(QtCore.QRect(350, 650, 131, 111))
        self.stopButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        self.stopButton.setFont(font)
        self.stopButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.stopButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/video-player-stop-button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon1)
        self.stopButton.setIconSize(QtCore.QSize(30, 30))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.tool0Label = QtGui.QLabel(self.homePage)
        self.tool0Label.setGeometry(QtCore.QRect(10, 434, 35, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tool0Label.setFont(font)
        self.tool0Label.setStyleSheet(_fromUtf8("\n"
"   color:  white;"))
        self.tool0Label.setText(_fromUtf8(""))
        self.tool0Label.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/Nozzle.png")))
        self.tool0Label.setScaledContents(True)
        self.tool0Label.setObjectName(_fromUtf8("tool0Label"))
        self.FileNameLabel = QtGui.QLabel(self.homePage)
        self.FileNameLabel.setGeometry(QtCore.QRect(10, 560, 61, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.FileNameLabel.setFont(font)
        self.FileNameLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.FileNameLabel.setObjectName(_fromUtf8("FileNameLabel"))
        self.printTimeLabel = QtGui.QLabel(self.homePage)
        self.printTimeLabel.setGeometry(QtCore.QRect(10, 590, 171, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.printTimeLabel.setFont(font)
        self.printTimeLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.printTimeLabel.setObjectName(_fromUtf8("printTimeLabel"))
        self.fileName = QtGui.QLabel(self.homePage)
        self.fileName.setGeometry(QtCore.QRect(75, 560, 401, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(18)
        self.fileName.setFont(font)
        self.fileName.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.fileName.setScaledContents(True)
        self.fileName.setWordWrap(False)
        self.fileName.setObjectName(_fromUtf8("fileName"))
        self.printTime = QtGui.QLabel(self.homePage)
        self.printTime.setGeometry(QtCore.QRect(185, 580, 281, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(18)
        self.printTime.setFont(font)
        self.printTime.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.printTime.setObjectName(_fromUtf8("printTime"))
        self.timeLeftLabel = QtGui.QLabel(self.homePage)
        self.timeLeftLabel.setGeometry(QtCore.QRect(10, 620, 161, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.timeLeftLabel.setFont(font)
        self.timeLeftLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.timeLeftLabel.setObjectName(_fromUtf8("timeLeftLabel"))
        self.bedTempBar = QtGui.QProgressBar(self.homePage)
        self.bedTempBar.setGeometry(QtCore.QRect(243, 401, 20, 100))
        self.bedTempBar.setStyleSheet(_fromUtf8("QProgressBar::chunk {\n"
"    border-radius: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.517, y1:0, x2:0.522, y2:0, stop:0.0336134 rgba(74, 183, 255, 255), stop:1 rgba(53, 173, 242, 255));\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid white;\n"
"    border-radius: 5px;\n"
"}\n"
""))
        self.bedTempBar.setMaximum(300)
        self.bedTempBar.setProperty("value", 200)
        self.bedTempBar.setAlignment(QtCore.Qt.AlignCenter)
        self.bedTempBar.setTextVisible(False)
        self.bedTempBar.setOrientation(QtCore.Qt.Vertical)
        self.bedTempBar.setObjectName(_fromUtf8("bedTempBar"))
        self.bedLabel = QtGui.QLabel(self.homePage)
        self.bedLabel.setGeometry(QtCore.QRect(187, 420, 55, 55))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.bedLabel.setFont(font)
        self.bedLabel.setStyleSheet(_fromUtf8("\n"
"   color:  white;\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.bedLabel.setText(_fromUtf8(""))
        self.bedLabel.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/bed.png")))
        self.bedLabel.setScaledContents(True)
        self.bedLabel.setObjectName(_fromUtf8("bedLabel"))
        self.tool0TargetTemperature = QtGui.QLabel(self.homePage)
        self.tool0TargetTemperature.setGeometry(QtCore.QRect(20, 380, 41, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tool0TargetTemperature.setFont(font)
        self.tool0TargetTemperature.setStyleSheet(_fromUtf8("\n"
"   color:  white;\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.tool0TargetTemperature.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tool0TargetTemperature.setObjectName(_fromUtf8("tool0TargetTemperature"))
        self.tool0TempBar = QtGui.QProgressBar(self.homePage)
        self.tool0TempBar.setGeometry(QtCore.QRect(56, 400, 20, 100))
        self.tool0TempBar.setStyleSheet(_fromUtf8("QProgressBar::chunk {\n"
"    border-radius: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.517, y1:0, x2:0.522, y2:0, stop:0.0336134 rgba(74, 183, 255, 255), stop:1 rgba(53, 173, 242, 255));\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid white;\n"
"    border-radius: 5px;\n"
"}\n"
""))
        self.tool0TempBar.setMaximum(300)
        self.tool0TempBar.setProperty("value", 200)
        self.tool0TempBar.setAlignment(QtCore.Qt.AlignCenter)
        self.tool0TempBar.setTextVisible(False)
        self.tool0TempBar.setOrientation(QtCore.Qt.Vertical)
        self.tool0TempBar.setObjectName(_fromUtf8("tool0TempBar"))
        self.tool0ActualTemperature = QtGui.QLabel(self.homePage)
        self.tool0ActualTemperature.setGeometry(QtCore.QRect(12, 500, 49, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tool0ActualTemperature.setFont(font)
        self.tool0ActualTemperature.setStyleSheet(_fromUtf8("\n"
"   color:  white;\n"
"background-color: rgba(0, 0, 0, 0);"))
        self.tool0ActualTemperature.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tool0ActualTemperature.setObjectName(_fromUtf8("tool0ActualTemperature"))
        self.bedActualTemperatute = QtGui.QLabel(self.homePage)
        self.bedActualTemperatute.setGeometry(QtCore.QRect(200, 500, 47, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.bedActualTemperatute.setFont(font)
        self.bedActualTemperatute.setStyleSheet(_fromUtf8("\n"
"   color:  white;\n"
"background-color: rgba(0, 0, 0, 0);"))
        self.bedActualTemperatute.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bedActualTemperatute.setObjectName(_fromUtf8("bedActualTemperatute"))
        self.bedTargetTemperature = QtGui.QLabel(self.homePage)
        self.bedTargetTemperature.setGeometry(QtCore.QRect(206, 380, 41, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.bedTargetTemperature.setFont(font)
        self.bedTargetTemperature.setStyleSheet(_fromUtf8("\n"
"   color:  white;\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.bedTargetTemperature.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bedTargetTemperature.setObjectName(_fromUtf8("bedTargetTemperature"))
        self.menuButton = QtGui.QPushButton(self.homePage)
        self.menuButton.setGeometry(QtCore.QRect(0, 650, 111, 111))
        self.menuButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(13)
        self.menuButton.setFont(font)
        self.menuButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.menuButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/menu.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuButton.setIcon(icon2)
        self.menuButton.setIconSize(QtCore.QSize(60, 60))
        self.menuButton.setCheckable(False)
        self.menuButton.setAutoDefault(False)
        self.menuButton.setDefault(False)
        self.menuButton.setFlat(False)
        self.menuButton.setObjectName(_fromUtf8("menuButton"))
        self.printProgressBar = QtGui.QProgressBar(self.homePage)
        self.printProgressBar.setGeometry(QtCore.QRect(0, 760, 481, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.printProgressBar.setFont(font)
        self.printProgressBar.setStyleSheet(_fromUtf8("QProgressBar::chunk {\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.523, x2:0, y2:0.534, stop:0 rgba(130, 203, 117, 255), stop:1 rgba(66, 191, 85, 255));\n"
"border: 1px solid green;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
" /*  border-bottom-left-radius: 10px;\n"
" border-bottom-right-radius: 10px;*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(180, 180, 180, 255));\n"
"}\n"
""))
        self.printProgressBar.setMaximum(100)
        self.printProgressBar.setProperty("value", 0)
        self.printProgressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.printProgressBar.setTextVisible(True)
        self.printProgressBar.setOrientation(QtCore.Qt.Horizontal)
        self.printProgressBar.setObjectName(_fromUtf8("printProgressBar"))
        self.timeLeft = QtGui.QLabel(self.homePage)
        self.timeLeft.setGeometry(QtCore.QRect(175, 620, 281, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(18)
        self.timeLeft.setFont(font)
        self.timeLeft.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.timeLeft.setWordWrap(False)
        self.timeLeft.setObjectName(_fromUtf8("timeLeft"))
        self.printerStatus = QtGui.QLabel(self.homePage)
        self.printerStatus.setGeometry(QtCore.QRect(64, 4, 376, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.printerStatus.setFont(font)
        self.printerStatus.setStyleSheet(_fromUtf8("\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.printerStatus.setScaledContents(True)
        self.printerStatus.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.printerStatus.setWordWrap(True)
        self.printerStatus.setObjectName(_fromUtf8("printerStatus"))
        self.controlButton = QtGui.QPushButton(self.homePage)
        self.controlButton.setGeometry(QtCore.QRect(110, 650, 111, 111))
        self.controlButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(13)
        self.controlButton.setFont(font)
        self.controlButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.controlButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/settings-1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.controlButton.setIcon(icon3)
        self.controlButton.setIconSize(QtCore.QSize(60, 60))
        self.controlButton.setCheckable(False)
        self.controlButton.setAutoDefault(False)
        self.controlButton.setDefault(False)
        self.controlButton.setFlat(False)
        self.controlButton.setObjectName(_fromUtf8("controlButton"))
        self.printerStatusColour = QtGui.QLabel(self.homePage)
        self.printerStatusColour.setGeometry(QtCore.QRect(20, 20, 31, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.printerStatusColour.setFont(font)
        self.printerStatusColour.setStyleSheet(_fromUtf8("     border: 1px solid rgb(87, 87, 87);\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.523, x2:0, y2:0.534, stop:0 rgba(130, 203, 117, 255), stop:1 rgba(66, 191, 85, 255));"))
        self.printerStatusColour.setText(_fromUtf8(""))
        self.printerStatusColour.setAlignment(QtCore.Qt.AlignCenter)
        self.printerStatusColour.setObjectName(_fromUtf8("printerStatusColour"))
        self.celciusLabel = QtGui.QLabel(self.homePage)
        self.celciusLabel.setGeometry(QtCore.QRect(253, 380, 19, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.celciusLabel.setFont(font)
        self.celciusLabel.setStyleSheet(_fromUtf8("\n"
"   color:  white;\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.celciusLabel.setObjectName(_fromUtf8("celciusLabel"))
        self.tool1TargetTemperature = QtGui.QLabel(self.homePage)
        self.tool1TargetTemperature.setGeometry(QtCore.QRect(110, 380, 41, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tool1TargetTemperature.setFont(font)
        self.tool1TargetTemperature.setStyleSheet(_fromUtf8("\n"
"   color:  white;\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.tool1TargetTemperature.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tool1TargetTemperature.setObjectName(_fromUtf8("tool1TargetTemperature"))
        self.tool1Label = QtGui.QLabel(self.homePage)
        self.tool1Label.setGeometry(QtCore.QRect(100, 434, 35, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tool1Label.setFont(font)
        self.tool1Label.setStyleSheet(_fromUtf8("\n"
"   color:  white;"))
        self.tool1Label.setText(_fromUtf8(""))
        self.tool1Label.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/Nozzle.png")))
        self.tool1Label.setScaledContents(True)
        self.tool1Label.setObjectName(_fromUtf8("tool1Label"))
        self.tool1TempBar = QtGui.QProgressBar(self.homePage)
        self.tool1TempBar.setGeometry(QtCore.QRect(150, 401, 20, 100))
        self.tool1TempBar.setStyleSheet(_fromUtf8("QProgressBar::chunk {\n"
"    border-radius: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.517, y1:0, x2:0.522, y2:0, stop:0.0336134 rgba(74, 183, 255, 255), stop:1 rgba(53, 173, 242, 255));\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid white;\n"
"    border-radius: 5px;\n"
"}\n"
""))
        self.tool1TempBar.setMaximum(300)
        self.tool1TempBar.setProperty("value", 200)
        self.tool1TempBar.setAlignment(QtCore.Qt.AlignCenter)
        self.tool1TempBar.setTextVisible(False)
        self.tool1TempBar.setOrientation(QtCore.Qt.Vertical)
        self.tool1TempBar.setObjectName(_fromUtf8("tool1TempBar"))
        self.tool1ActualTemperature = QtGui.QLabel(self.homePage)
        self.tool1ActualTemperature.setGeometry(QtCore.QRect(100, 500, 58, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tool1ActualTemperature.setFont(font)
        self.tool1ActualTemperature.setStyleSheet(_fromUtf8("\n"
"   color:  white;\n"
"background-color: rgba(0, 0, 0, 0);"))
        self.tool1ActualTemperature.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tool1ActualTemperature.setObjectName(_fromUtf8("tool1ActualTemperature"))
        self.statusBar = QtGui.QLabel(self.homePage)
        self.statusBar.setGeometry(QtCore.QRect(0, 0, 481, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        self.statusBar.setFont(font)
        self.statusBar.setStyleSheet(_fromUtf8("     border-bottom: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.statusBar.setFrameShape(QtGui.QFrame.NoFrame)
        self.statusBar.setFrameShadow(QtGui.QFrame.Raised)
        self.statusBar.setText(_fromUtf8(""))
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        self.printPreviewMain = QtGui.QLabel(self.homePage)
        self.printPreviewMain.setGeometry(QtCore.QRect(100, 70, 281, 271))
        self.printPreviewMain.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.printPreviewMain.setText(_fromUtf8(""))
        self.printPreviewMain.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/thumbnail.png")))
        self.printPreviewMain.setScaledContents(True)
        self.printPreviewMain.setObjectName(_fromUtf8("printPreviewMain"))
        self.celciusLabel_2 = QtGui.QLabel(self.homePage)
        self.celciusLabel_2.setGeometry(QtCore.QRect(160, 380, 22, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.celciusLabel_2.setFont(font)
        self.celciusLabel_2.setStyleSheet(_fromUtf8("\n"
"   color:  white;\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.celciusLabel_2.setObjectName(_fromUtf8("celciusLabel_2"))
        self.celciusLabel_3 = QtGui.QLabel(self.homePage)
        self.celciusLabel_3.setGeometry(QtCore.QRect(70, 380, 23, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.celciusLabel_3.setFont(font)
        self.celciusLabel_3.setStyleSheet(_fromUtf8("\n"
"   color:  white;\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.celciusLabel_3.setObjectName(_fromUtf8("celciusLabel_3"))
        self.chamberLabel = QtGui.QLabel(self.homePage)
        self.chamberLabel.setGeometry(QtCore.QRect(280, 430, 45, 45))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.chamberLabel.setFont(font)
        self.chamberLabel.setStyleSheet(_fromUtf8("\n"
"   color:  white;\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.chamberLabel.setText(_fromUtf8(""))
        self.chamberLabel.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/chamberHeatIcon.png")))
        self.chamberLabel.setScaledContents(True)
        self.chamberLabel.setObjectName(_fromUtf8("chamberLabel"))
        self.chamberTempBar = QtGui.QProgressBar(self.homePage)
        self.chamberTempBar.setGeometry(QtCore.QRect(340, 401, 20, 100))
        self.chamberTempBar.setStyleSheet(_fromUtf8("QProgressBar::chunk {\n"
"    border-radius: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.517, y1:0, x2:0.522, y2:0, stop:0.0336134 rgba(74, 183, 255, 255), stop:1 rgba(53, 173, 242, 255));\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid white;\n"
"    border-radius: 5px;\n"
"}\n"
""))
        self.chamberTempBar.setMaximum(300)
        self.chamberTempBar.setProperty("value", 150)
        self.chamberTempBar.setAlignment(QtCore.Qt.AlignCenter)
        self.chamberTempBar.setTextVisible(False)
        self.chamberTempBar.setOrientation(QtCore.Qt.Vertical)
        self.chamberTempBar.setObjectName(_fromUtf8("chamberTempBar"))
        self.chamberActualTemperatute = QtGui.QLabel(self.homePage)
        self.chamberActualTemperatute.setGeometry(QtCore.QRect(300, 500, 41, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.chamberActualTemperatute.setFont(font)
        self.chamberActualTemperatute.setStyleSheet(_fromUtf8("\n"
"   color:  white;\n"
"background-color: rgba(0, 0, 0, 0);"))
        self.chamberActualTemperatute.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.chamberActualTemperatute.setObjectName(_fromUtf8("chamberActualTemperatute"))
        self.celciusLabel_4 = QtGui.QLabel(self.homePage)
        self.celciusLabel_4.setGeometry(QtCore.QRect(356, 380, 23, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.celciusLabel_4.setFont(font)
        self.celciusLabel_4.setStyleSheet(_fromUtf8("\n"
"   color:  white;\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.celciusLabel_4.setObjectName(_fromUtf8("celciusLabel_4"))
        self.chamberTargetTemperature = QtGui.QLabel(self.homePage)
        self.chamberTargetTemperature.setGeometry(QtCore.QRect(297, 380, 41, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.chamberTargetTemperature.setFont(font)
        self.chamberTargetTemperature.setStyleSheet(_fromUtf8("\n"
"   color:  white;\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.chamberTargetTemperature.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.chamberTargetTemperature.setObjectName(_fromUtf8("chamberTargetTemperature"))
        self.filboxTempBar = QtGui.QProgressBar(self.homePage)
        self.filboxTempBar.setGeometry(QtCore.QRect(439, 401, 20, 100))
        self.filboxTempBar.setStyleSheet(_fromUtf8("QProgressBar::chunk {\n"
"    border-radius: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.517, y1:0, x2:0.522, y2:0, stop:0.0336134 rgba(74, 183, 255, 255), stop:1 rgba(53, 173, 242, 255));\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid white;\n"
"    border-radius: 5px;\n"
"}\n"
""))
        self.filboxTempBar.setMaximum(110)
        self.filboxTempBar.setProperty("value", 90)
        self.filboxTempBar.setAlignment(QtCore.Qt.AlignCenter)
        self.filboxTempBar.setTextVisible(False)
        self.filboxTempBar.setOrientation(QtCore.Qt.Vertical)
        self.filboxTempBar.setObjectName(_fromUtf8("filboxTempBar"))
        self.spoolHeatLabel = QtGui.QLabel(self.homePage)
        self.spoolHeatLabel.setGeometry(QtCore.QRect(389, 430, 45, 45))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.spoolHeatLabel.setFont(font)
        self.spoolHeatLabel.setStyleSheet(_fromUtf8("\n"
"   color:  white;\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.spoolHeatLabel.setText(_fromUtf8(""))
        self.spoolHeatLabel.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/spoolHeating.png")))
        self.spoolHeatLabel.setScaledContents(True)
        self.spoolHeatLabel.setObjectName(_fromUtf8("spoolHeatLabel"))
        self.filboxActualTemperatute = QtGui.QLabel(self.homePage)
        self.filboxActualTemperatute.setGeometry(QtCore.QRect(399, 500, 41, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.filboxActualTemperatute.setFont(font)
        self.filboxActualTemperatute.setStyleSheet(_fromUtf8("\n"
"   color:  white;\n"
"background-color: rgba(0, 0, 0, 0);"))
        self.filboxActualTemperatute.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.filboxActualTemperatute.setObjectName(_fromUtf8("filboxActualTemperatute"))
        self.filboxTargetTemperature = QtGui.QLabel(self.homePage)
        self.filboxTargetTemperature.setGeometry(QtCore.QRect(396, 380, 41, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.filboxTargetTemperature.setFont(font)
        self.filboxTargetTemperature.setStyleSheet(_fromUtf8("\n"
"   color:  white;\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.filboxTargetTemperature.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.filboxTargetTemperature.setObjectName(_fromUtf8("filboxTargetTemperature"))
        self.celciusLabel_5 = QtGui.QLabel(self.homePage)
        self.celciusLabel_5.setGeometry(QtCore.QRect(455, 378, 23, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.celciusLabel_5.setFont(font)
        self.celciusLabel_5.setStyleSheet(_fromUtf8("\n"
"   color:  white;\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.celciusLabel_5.setObjectName(_fromUtf8("celciusLabel_5"))
        self.tool0TargetTemperature_2 = QtGui.QLabel(self.homePage)
        self.tool0TargetTemperature_2.setGeometry(QtCore.QRect(-15, 440, 41, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tool0TargetTemperature_2.setFont(font)
        self.tool0TargetTemperature_2.setStyleSheet(_fromUtf8("\n"
"   color:  black;\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.tool0TargetTemperature_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tool0TargetTemperature_2.setObjectName(_fromUtf8("tool0TargetTemperature_2"))
        self.tool0TargetTemperature_3 = QtGui.QLabel(self.homePage)
        self.tool0TargetTemperature_3.setGeometry(QtCore.QRect(72, 440, 41, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tool0TargetTemperature_3.setFont(font)
        self.tool0TargetTemperature_3.setStyleSheet(_fromUtf8("\n"
"   color:  black;\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.tool0TargetTemperature_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tool0TargetTemperature_3.setObjectName(_fromUtf8("tool0TargetTemperature_3"))
        self.doorLockButton = QtGui.QToolButton(self.homePage)
        self.doorLockButton.setEnabled(False)
        self.doorLockButton.setGeometry(QtCore.QRect(390, 111, 90, 100))
        self.doorLockButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(8)
        self.doorLockButton.setFont(font)
        self.doorLockButton.setStyleSheet(_fromUtf8("QToolButton {\n"
"    padding-top: 20px;\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"border-top-left-radius: 10px;\n"
"\n"
"border-bottom-left-radius: 10px;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/doorUnlock.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/doorLock.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.doorLockButton.setIcon(icon4)
        self.doorLockButton.setIconSize(QtCore.QSize(50, 50))
        self.doorLockButton.setCheckable(False)
        self.doorLockButton.setChecked(False)
        self.doorLockButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.doorLockButton.setAutoRaise(False)
        self.doorLockButton.setObjectName(_fromUtf8("doorLockButton"))
        self.line_8 = QtGui.QFrame(self.homePage)
        self.line_8.setGeometry(QtCore.QRect(28, 350, 416, 20))
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.line_9 = QtGui.QFrame(self.homePage)
        self.line_9.setGeometry(QtCore.QRect(31, 530, 415, 20))
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.virtualPrinterMode = QtGui.QLabel(self.homePage)
        self.virtualPrinterMode.setEnabled(False)
        self.virtualPrinterMode.setGeometry(QtCore.QRect(440, 4, 41, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.virtualPrinterMode.setFont(font)
        self.virtualPrinterMode.setStyleSheet(_fromUtf8("\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 40, 10);\n"
"font-size: 18pt;\n"
"font-weight: bold;"))
        self.virtualPrinterMode.setScaledContents(True)
        self.virtualPrinterMode.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.virtualPrinterMode.setWordWrap(True)
        self.virtualPrinterMode.setObjectName(_fromUtf8("virtualPrinterMode"))
        self.timeLeftLabel.raise_()
        self.printPreviewMain.raise_()
        self.statusBar.raise_()
        self.playPauseButton.raise_()
        self.stopButton.raise_()
        self.tool0Label.raise_()
        self.FileNameLabel.raise_()
        self.printTimeLabel.raise_()
        self.printTime.raise_()
        self.bedTempBar.raise_()
        self.bedLabel.raise_()
        self.tool0TempBar.raise_()
        self.tool0ActualTemperature.raise_()
        self.tool0TargetTemperature.raise_()
        self.bedActualTemperatute.raise_()
        self.bedTargetTemperature.raise_()
        self.menuButton.raise_()
        self.timeLeft.raise_()
        self.controlButton.raise_()
        self.printProgressBar.raise_()
        self.printerStatus.raise_()
        self.printerStatusColour.raise_()
        self.celciusLabel.raise_()
        self.tool1TargetTemperature.raise_()
        self.tool1Label.raise_()
        self.tool1TempBar.raise_()
        self.tool1ActualTemperature.raise_()
        self.fileName.raise_()
        self.celciusLabel_2.raise_()
        self.celciusLabel_3.raise_()
        self.chamberLabel.raise_()
        self.chamberTempBar.raise_()
        self.chamberActualTemperatute.raise_()
        self.celciusLabel_4.raise_()
        self.chamberTargetTemperature.raise_()
        self.filboxTempBar.raise_()
        self.spoolHeatLabel.raise_()
        self.filboxActualTemperatute.raise_()
        self.filboxTargetTemperature.raise_()
        self.celciusLabel_5.raise_()
        self.tool0TargetTemperature_2.raise_()
        self.tool0TargetTemperature_3.raise_()
        self.doorLockButton.raise_()
        self.line_8.raise_()
        self.line_9.raise_()
        self.virtualPrinterMode.raise_()
        self.stackedWidget.addWidget(self.homePage)
        self.MenuPage = QtGui.QWidget()
        self.MenuPage.setObjectName(_fromUtf8("MenuPage"))
        self.menuBackButton = QtGui.QPushButton(self.MenuPage)
        self.menuBackButton.setGeometry(QtCore.QRect(240, 531, 245, 269))
        self.menuBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.menuBackButton.setFont(font)
        self.menuBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        self.menuBackButton.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/arrows-4.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuBackButton.setIcon(icon5)
        self.menuBackButton.setIconSize(QtCore.QSize(120, 120))
        self.menuBackButton.setCheckable(False)
        self.menuBackButton.setObjectName(_fromUtf8("menuBackButton"))
        self.menuControlButton = QtGui.QToolButton(self.MenuPage)
        self.menuControlButton.setGeometry(QtCore.QRect(240, 0, 245, 269))
        self.menuControlButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(18)
        self.menuControlButton.setFont(font)
        self.menuControlButton.setStyleSheet(_fromUtf8("QToolButton {\n"
"padding-top: 20px;\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        self.menuControlButton.setIcon(icon3)
        self.menuControlButton.setIconSize(QtCore.QSize(120, 120))
        self.menuControlButton.setCheckable(False)
        self.menuControlButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.menuControlButton.setObjectName(_fromUtf8("menuControlButton"))
        self.menuPrintButton = QtGui.QToolButton(self.MenuPage)
        self.menuPrintButton.setGeometry(QtCore.QRect(0, 0, 245, 269))
        self.menuPrintButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(18)
        self.menuPrintButton.setFont(font)
        self.menuPrintButton.setStyleSheet(_fromUtf8("QToolButton {\n"
"    padding-top: 20px;\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/printer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuPrintButton.setIcon(icon6)
        self.menuPrintButton.setIconSize(QtCore.QSize(120, 120))
        self.menuPrintButton.setCheckable(False)
        self.menuPrintButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.menuPrintButton.setObjectName(_fromUtf8("menuPrintButton"))
        self.menuSettingsButton = QtGui.QToolButton(self.MenuPage)
        self.menuSettingsButton.setGeometry(QtCore.QRect(240, 268, 245, 268))
        self.menuSettingsButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(18)
        self.menuSettingsButton.setFont(font)
        self.menuSettingsButton.setStyleSheet(_fromUtf8("QToolButton {\n"
"padding-top: 20px;\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuSettingsButton.setIcon(icon7)
        self.menuSettingsButton.setIconSize(QtCore.QSize(120, 120))
        self.menuSettingsButton.setCheckable(False)
        self.menuSettingsButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.menuSettingsButton.setObjectName(_fromUtf8("menuSettingsButton"))
        self.menuCartButton = QtGui.QToolButton(self.MenuPage)
        self.menuCartButton.setGeometry(QtCore.QRect(0, 531, 245, 269))
        self.menuCartButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(18)
        self.menuCartButton.setFont(font)
        self.menuCartButton.setStyleSheet(_fromUtf8("QToolButton {\n"
"padding-top: 20px;\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/cart.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuCartButton.setIcon(icon8)
        self.menuCartButton.setIconSize(QtCore.QSize(120, 120))
        self.menuCartButton.setCheckable(False)
        self.menuCartButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.menuCartButton.setAutoRaise(False)
        self.menuCartButton.setObjectName(_fromUtf8("menuCartButton"))
        self.menuCalibrateButton = QtGui.QToolButton(self.MenuPage)
        self.menuCalibrateButton.setGeometry(QtCore.QRect(0, 268, 245, 269))
        self.menuCalibrateButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(18)
        self.menuCalibrateButton.setFont(font)
        self.menuCalibrateButton.setStyleSheet(_fromUtf8("QToolButton {\n"
"padding-top: 20px;\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/reload.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuCalibrateButton.setIcon(icon9)
        self.menuCalibrateButton.setIconSize(QtCore.QSize(120, 120))
        self.menuCalibrateButton.setCheckable(False)
        self.menuCalibrateButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.menuCalibrateButton.setObjectName(_fromUtf8("menuCalibrateButton"))
        self.menuSettingsButton.raise_()
        self.menuControlButton.raise_()
        self.menuCalibrateButton.raise_()
        self.menuBackButton.raise_()
        self.menuPrintButton.raise_()
        self.menuCartButton.raise_()
        self.stackedWidget.addWidget(self.MenuPage)
        self.settingsPage = QtGui.QWidget()
        self.settingsPage.setObjectName(_fromUtf8("settingsPage"))
        self.scrollArea = QtGui.QScrollArea(self.settingsPage)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 480, 801))
        self.scrollArea.setStyleSheet(_fromUtf8(" QScrollBar:vertical {\n"
"     border: 1px solid black;\n"
"border-radius: 5px;\n"
"    background-color: rgb(40,40,40);\n"
"     width: 80px;\n"
"     margin: 70px 0 70px 0;\n"
" }\n"
" QScrollBar::handle:vertical {\n"
"border-radius: 5px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"min-height: 20px;\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: 1px solid black;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     height:65px;\n"
"border-radius: 5px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"     border: 1px solid black;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     height: 65px;\n"
"border-radius: 5px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
" image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
" padding: 5px;\n"
" }\n"
"QScrollBar::down-arrow:vertical {\n"
" image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
" padding: 5px;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }"))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 478, 799))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 3, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.settingsBackButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.settingsBackButton.setMinimumSize(QtCore.QSize(0, 85))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.settingsBackButton.setFont(font)
        self.settingsBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        self.settingsBackButton.setText(_fromUtf8(""))
        self.settingsBackButton.setIcon(icon5)
        self.settingsBackButton.setIconSize(QtCore.QSize(50, 50))
        self.settingsBackButton.setCheckable(False)
        self.settingsBackButton.setAutoDefault(False)
        self.settingsBackButton.setDefault(False)
        self.settingsBackButton.setFlat(False)
        self.settingsBackButton.setObjectName(_fromUtf8("settingsBackButton"))
        self.verticalLayout.addWidget(self.settingsBackButton)
        self.networkSettingsButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.networkSettingsButton.setMinimumSize(QtCore.QSize(0, 88))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.networkSettingsButton.setFont(font)
        self.networkSettingsButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.networkSettingsButton.setIconSize(QtCore.QSize(40, 40))
        self.networkSettingsButton.setObjectName(_fromUtf8("networkSettingsButton"))
        self.verticalLayout.addWidget(self.networkSettingsButton)
        self.displaySettingsButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.displaySettingsButton.setMinimumSize(QtCore.QSize(0, 85))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.displaySettingsButton.setFont(font)
        self.displaySettingsButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.displaySettingsButton.setIconSize(QtCore.QSize(40, 40))
        self.displaySettingsButton.setObjectName(_fromUtf8("displaySettingsButton"))
        self.verticalLayout.addWidget(self.displaySettingsButton)
        self.pairPhoneButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pairPhoneButton.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.pairPhoneButton.setFont(font)
        self.pairPhoneButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.pairPhoneButton.setIconSize(QtCore.QSize(40, 40))
        self.pairPhoneButton.setObjectName(_fromUtf8("pairPhoneButton"))
        self.verticalLayout.addWidget(self.pairPhoneButton)
        self.OTAButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.OTAButton.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.OTAButton.setFont(font)
        self.OTAButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.OTAButton.setIconSize(QtCore.QSize(40, 40))
        self.OTAButton.setObjectName(_fromUtf8("OTAButton"))
        self.verticalLayout.addWidget(self.OTAButton)
        self.versionButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.versionButton.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.versionButton.setFont(font)
        self.versionButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.versionButton.setIconSize(QtCore.QSize(40, 40))
        self.versionButton.setObjectName(_fromUtf8("versionButton"))
        self.verticalLayout.addWidget(self.versionButton)
        self.restorePrintSettingsButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.restorePrintSettingsButton.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.restorePrintSettingsButton.setFont(font)
        self.restorePrintSettingsButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.restorePrintSettingsButton.setIconSize(QtCore.QSize(40, 40))
        self.restorePrintSettingsButton.setObjectName(_fromUtf8("restorePrintSettingsButton"))
        self.verticalLayout.addWidget(self.restorePrintSettingsButton)
        self.restoreFactoryDefaultsButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.restoreFactoryDefaultsButton.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.restoreFactoryDefaultsButton.setFont(font)
        self.restoreFactoryDefaultsButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.restoreFactoryDefaultsButton.setIconSize(QtCore.QSize(40, 40))
        self.restoreFactoryDefaultsButton.setObjectName(_fromUtf8("restoreFactoryDefaultsButton"))
        self.verticalLayout.addWidget(self.restoreFactoryDefaultsButton)
        self.restartButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.restartButton.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.restartButton.setFont(font)
        self.restartButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.restartButton.setIconSize(QtCore.QSize(40, 40))
        self.restartButton.setObjectName(_fromUtf8("restartButton"))
        self.verticalLayout.addWidget(self.restartButton)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.addWidget(self.settingsPage)
        self.QRCodePage = QtGui.QWidget()
        self.QRCodePage.setObjectName(_fromUtf8("QRCodePage"))
        self.QRCodeBackButton = QtGui.QPushButton(self.QRCodePage)
        self.QRCodeBackButton.setGeometry(QtCore.QRect(0, 690, 481, 111))
        self.QRCodeBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.QRCodeBackButton.setFont(font)
        self.QRCodeBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        self.QRCodeBackButton.setText(_fromUtf8(""))
        self.QRCodeBackButton.setIcon(icon5)
        self.QRCodeBackButton.setIconSize(QtCore.QSize(50, 50))
        self.QRCodeBackButton.setCheckable(False)
        self.QRCodeBackButton.setAutoDefault(False)
        self.QRCodeBackButton.setDefault(False)
        self.QRCodeBackButton.setFlat(False)
        self.QRCodeBackButton.setObjectName(_fromUtf8("QRCodeBackButton"))
        self.QRCodeBackground = QtGui.QLabel(self.QRCodePage)
        self.QRCodeBackground.setGeometry(QtCore.QRect(130, 230, 251, 251))
        self.QRCodeBackground.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.QRCodeBackground.setText(_fromUtf8(""))
        self.QRCodeBackground.setObjectName(_fromUtf8("QRCodeBackground"))
        self.QRCodeLabel = QtGui.QLabel(self.QRCodePage)
        self.QRCodeLabel.setGeometry(QtCore.QRect(130, 230, 251, 251))
        self.QRCodeLabel.setStyleSheet(_fromUtf8(""))
        self.QRCodeLabel.setText(_fromUtf8(""))
        self.QRCodeLabel.setScaledContents(True)
        self.QRCodeLabel.setObjectName(_fromUtf8("QRCodeLabel"))
        self.QRCodeBackground.raise_()
        self.QRCodeLabel.raise_()
        self.QRCodeBackButton.raise_()
        self.stackedWidget.addWidget(self.QRCodePage)
        self.wifiSettingsPage = QtGui.QWidget()
        self.wifiSettingsPage.setObjectName(_fromUtf8("wifiSettingsPage"))
        self.wifiSettingsComboBox = QtGui.QComboBox(self.wifiSettingsPage)
        self.wifiSettingsComboBox.setGeometry(QtCore.QRect(0, 40, 421, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(20)
        self.wifiSettingsComboBox.setFont(font)
        self.wifiSettingsComboBox.setStyleSheet(_fromUtf8(" QScrollBar:vertical {\n"
"     border: 1px solid black;\n"
"border-radius: 5px;\n"
"    background-color: rgb(40,40,40);\n"
"     width: 60px;\n"
"     margin: 67px 0 67px 0;\n"
" }\n"
"\n"
"/* Sets up the color and height of handle */\n"
"QScrollBar::handle:vertical {\n"
"border-radius: 5px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"min-height: 7px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"     border: 1px solid black;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     height:65px;\n"
"border-radius: 5px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"     border: 1px solid black;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     height: 65px;\n"
"border-radius: 5px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
" image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
" padding: 5px;\n"
" }\n"
"QScrollBar::down-arrow:vertical {\n"
" image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
" padding: 5px;\n"
" }\n"
"\n"
"/* need this to get rid of crosshatching on scrollbar background */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"background: none;\n"
"}\n"
"\n"
"QComboBox {\n"
"border: 1px solid black;\n"
"    padding: 0px 18px 0px 3px;\n"
"    min-width: 6em;\n"
"\n"
"}\n"
"\n"
"QComboBox::item {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"background: white;\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"background: white;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"border-left: 1px solid black;\n"
"border-right: 1px solid black;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 50px;\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"\n"
"image: url(./templates/img/arrows-5.png);\n"
"width: 30px;\n"
"height: 30px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(40, 40, 40);\n"
"    background: white;\n"
"}"))
        self.wifiSettingsComboBox.setEditable(False)
        self.wifiSettingsComboBox.setMaxVisibleItems(8)
        self.wifiSettingsComboBox.setIconSize(QtCore.QSize(30, 30))
        self.wifiSettingsComboBox.setObjectName(_fromUtf8("wifiSettingsComboBox"))
        self.ssidlabel = QtGui.QLabel(self.wifiSettingsPage)
        self.ssidlabel.setGeometry(QtCore.QRect(0, 0, 461, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ssidlabel.setFont(font)
        self.ssidlabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.ssidlabel.setObjectName(_fromUtf8("ssidlabel"))
        self.passwordlabel = QtGui.QLabel(self.wifiSettingsPage)
        self.passwordlabel.setGeometry(QtCore.QRect(0, 130, 461, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.passwordlabel.setFont(font)
        self.passwordlabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.passwordlabel.setObjectName(_fromUtf8("passwordlabel"))
        self.wifiSettingsDoneButton = QtGui.QPushButton(self.wifiSettingsPage)
        self.wifiSettingsDoneButton.setGeometry(QtCore.QRect(0, 710, 251, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.wifiSettingsDoneButton.setFont(font)
        self.wifiSettingsDoneButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.wifiSettingsDoneButton.setIconSize(QtCore.QSize(40, 40))
        self.wifiSettingsDoneButton.setObjectName(_fromUtf8("wifiSettingsDoneButton"))
        self.wifiSettingsCancelButton = QtGui.QPushButton(self.wifiSettingsPage)
        self.wifiSettingsCancelButton.setGeometry(QtCore.QRect(250, 710, 231, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.wifiSettingsCancelButton.setFont(font)
        self.wifiSettingsCancelButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.wifiSettingsCancelButton.setIconSize(QtCore.QSize(40, 40))
        self.wifiSettingsCancelButton.setObjectName(_fromUtf8("wifiSettingsCancelButton"))
        self.wifiSettingsSSIDKeyboardButton = QtGui.QPushButton(self.wifiSettingsPage)
        self.wifiSettingsSSIDKeyboardButton.setGeometry(QtCore.QRect(419, 40, 62, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(19)
        self.wifiSettingsSSIDKeyboardButton.setFont(font)
        self.wifiSettingsSSIDKeyboardButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.wifiSettingsSSIDKeyboardButton.setIconSize(QtCore.QSize(40, 40))
        self.wifiSettingsSSIDKeyboardButton.setObjectName(_fromUtf8("wifiSettingsSSIDKeyboardButton"))
        self.hiddenCheckBox = QtGui.QCheckBox(self.wifiSettingsPage)
        self.hiddenCheckBox.setGeometry(QtCore.QRect(0, 90, 161, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        self.hiddenCheckBox.setFont(font)
        self.hiddenCheckBox.setStyleSheet(_fromUtf8("QCheckBox {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(./templates/img/check-box.png);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(./templates/img/blank-check-box.png);\n"
"}\n"
"\n"
"\n"
"\n"
""))
        self.hiddenCheckBox.setIconSize(QtCore.QSize(40, 40))
        self.hiddenCheckBox.setChecked(False)
        self.hiddenCheckBox.setObjectName(_fromUtf8("hiddenCheckBox"))
        self.wifiSettingsComboBox.raise_()
        self.ssidlabel.raise_()
        self.passwordlabel.raise_()
        self.wifiSettingsSSIDKeyboardButton.raise_()
        self.wifiSettingsCancelButton.raise_()
        self.wifiSettingsDoneButton.raise_()
        self.hiddenCheckBox.raise_()
        self.stackedWidget.addWidget(self.wifiSettingsPage)
        self.ethSettingsPage = QtGui.QWidget()
        self.ethSettingsPage.setObjectName(_fromUtf8("ethSettingsPage"))
        self.ethSettingsDoneButton = QtGui.QPushButton(self.ethSettingsPage)
        self.ethSettingsDoneButton.setGeometry(QtCore.QRect(0, 710, 251, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.ethSettingsDoneButton.setFont(font)
        self.ethSettingsDoneButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ethSettingsDoneButton.setIconSize(QtCore.QSize(40, 40))
        self.ethSettingsDoneButton.setObjectName(_fromUtf8("ethSettingsDoneButton"))
        self.ethSettingsCancelButton = QtGui.QPushButton(self.ethSettingsPage)
        self.ethSettingsCancelButton.setGeometry(QtCore.QRect(250, 710, 231, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.ethSettingsCancelButton.setFont(font)
        self.ethSettingsCancelButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ethSettingsCancelButton.setIconSize(QtCore.QSize(40, 40))
        self.ethSettingsCancelButton.setObjectName(_fromUtf8("ethSettingsCancelButton"))
        self.ethStaticCheckBox = QtGui.QCheckBox(self.ethSettingsPage)
        self.ethStaticCheckBox.setGeometry(QtCore.QRect(10, 20, 161, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        self.ethStaticCheckBox.setFont(font)
        self.ethStaticCheckBox.setStyleSheet(_fromUtf8("QCheckBox {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(./templates/img/check-box.png);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(./templates/img/blank-check-box.png);\n"
"}\n"
"\n"
"\n"
"\n"
""))
        self.ethStaticCheckBox.setIconSize(QtCore.QSize(40, 40))
        self.ethStaticCheckBox.setChecked(False)
        self.ethStaticCheckBox.setObjectName(_fromUtf8("ethStaticCheckBox"))
        self.ethStaticSettings = QtGui.QWidget(self.ethSettingsPage)
        self.ethStaticSettings.setEnabled(True)
        self.ethStaticSettings.setGeometry(QtCore.QRect(0, 70, 481, 151))
        self.ethStaticSettings.setObjectName(_fromUtf8("ethStaticSettings"))
        self.ethStaticIpLabel = QtGui.QLabel(self.ethStaticSettings)
        self.ethStaticIpLabel.setGeometry(QtCore.QRect(10, 10, 110, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.ethStaticIpLabel.setFont(font)
        self.ethStaticIpLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.ethStaticIpLabel.setObjectName(_fromUtf8("ethStaticIpLabel"))
        self.ethStaticGatewayLabel = QtGui.QLabel(self.ethStaticSettings)
        self.ethStaticGatewayLabel.setGeometry(QtCore.QRect(10, 60, 110, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.ethStaticGatewayLabel.setFont(font)
        self.ethStaticGatewayLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.ethStaticGatewayLabel.setObjectName(_fromUtf8("ethStaticGatewayLabel"))
        self.ethStaticGatewayKeyboardButton = QtGui.QPushButton(self.ethStaticSettings)
        self.ethStaticGatewayKeyboardButton.setGeometry(QtCore.QRect(420, 60, 60, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ethStaticGatewayKeyboardButton.setFont(font)
        self.ethStaticGatewayKeyboardButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ethStaticGatewayKeyboardButton.setIconSize(QtCore.QSize(40, 40))
        self.ethStaticGatewayKeyboardButton.setObjectName(_fromUtf8("ethStaticGatewayKeyboardButton"))
        self.ethStaticIpKeyboardButton = QtGui.QPushButton(self.ethStaticSettings)
        self.ethStaticIpKeyboardButton.setEnabled(True)
        self.ethStaticIpKeyboardButton.setGeometry(QtCore.QRect(420, 10, 60, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ethStaticIpKeyboardButton.setFont(font)
        self.ethStaticIpKeyboardButton.setAutoFillBackground(False)
        self.ethStaticIpKeyboardButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ethStaticIpKeyboardButton.setIconSize(QtCore.QSize(40, 40))
        self.ethStaticIpKeyboardButton.setObjectName(_fromUtf8("ethStaticIpKeyboardButton"))
        self.stackedWidget.addWidget(self.ethSettingsPage)
        self.networkSettingsPage = QtGui.QWidget()
        self.networkSettingsPage.setObjectName(_fromUtf8("networkSettingsPage"))
        self.networkInfoButton = QtGui.QPushButton(self.networkSettingsPage)
        self.networkInfoButton.setGeometry(QtCore.QRect(0, 0, 480, 70))
        self.networkInfoButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.networkInfoButton.setFont(font)
        self.networkInfoButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.networkInfoButton.setIconSize(QtCore.QSize(40, 40))
        self.networkInfoButton.setObjectName(_fromUtf8("networkInfoButton"))
        self.configureWifiButton = QtGui.QPushButton(self.networkSettingsPage)
        self.configureWifiButton.setGeometry(QtCore.QRect(0, 70, 480, 70))
        self.configureWifiButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.configureWifiButton.setFont(font)
        self.configureWifiButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.configureWifiButton.setIconSize(QtCore.QSize(40, 40))
        self.configureWifiButton.setObjectName(_fromUtf8("configureWifiButton"))
        self.configureEthButton = QtGui.QPushButton(self.networkSettingsPage)
        self.configureEthButton.setGeometry(QtCore.QRect(0, 140, 480, 70))
        self.configureEthButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.configureEthButton.setFont(font)
        self.configureEthButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.configureEthButton.setIconSize(QtCore.QSize(40, 40))
        self.configureEthButton.setObjectName(_fromUtf8("configureEthButton"))
        self.networkSettingsBackButton = QtGui.QPushButton(self.networkSettingsPage)
        self.networkSettingsBackButton.setGeometry(QtCore.QRect(0, 730, 481, 71))
        self.networkSettingsBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.networkSettingsBackButton.setFont(font)
        self.networkSettingsBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        self.networkSettingsBackButton.setText(_fromUtf8(""))
        self.networkSettingsBackButton.setIcon(icon5)
        self.networkSettingsBackButton.setIconSize(QtCore.QSize(50, 50))
        self.networkSettingsBackButton.setCheckable(False)
        self.networkSettingsBackButton.setAutoDefault(False)
        self.networkSettingsBackButton.setDefault(False)
        self.networkSettingsBackButton.setFlat(False)
        self.networkSettingsBackButton.setObjectName(_fromUtf8("networkSettingsBackButton"))
        self.stackedWidget.addWidget(self.networkSettingsPage)
        self.displaySettingsPage = QtGui.QWidget()
        self.displaySettingsPage.setObjectName(_fromUtf8("displaySettingsPage"))
        self.displaySettingsBackButton = QtGui.QPushButton(self.displaySettingsPage)
        self.displaySettingsBackButton.setGeometry(QtCore.QRect(0, 730, 481, 71))
        self.displaySettingsBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.displaySettingsBackButton.setFont(font)
        self.displaySettingsBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        self.displaySettingsBackButton.setText(_fromUtf8(""))
        self.displaySettingsBackButton.setIcon(icon5)
        self.displaySettingsBackButton.setIconSize(QtCore.QSize(50, 50))
        self.displaySettingsBackButton.setCheckable(False)
        self.displaySettingsBackButton.setAutoDefault(False)
        self.displaySettingsBackButton.setDefault(False)
        self.displaySettingsBackButton.setFlat(False)
        self.displaySettingsBackButton.setObjectName(_fromUtf8("displaySettingsBackButton"))
        self.calibrateTouch = QtGui.QPushButton(self.displaySettingsPage)
        self.calibrateTouch.setGeometry(QtCore.QRect(0, 70, 480, 70))
        self.calibrateTouch.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.calibrateTouch.setFont(font)
        self.calibrateTouch.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.calibrateTouch.setIconSize(QtCore.QSize(40, 40))
        self.calibrateTouch.setObjectName(_fromUtf8("calibrateTouch"))
        self.rotateDisplay = QtGui.QPushButton(self.displaySettingsPage)
        self.rotateDisplay.setGeometry(QtCore.QRect(0, 0, 480, 70))
        self.rotateDisplay.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.rotateDisplay.setFont(font)
        self.rotateDisplay.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.rotateDisplay.setIconSize(QtCore.QSize(40, 40))
        self.rotateDisplay.setObjectName(_fromUtf8("rotateDisplay"))
        self.stackedWidget.addWidget(self.displaySettingsPage)
        self.rotateDisplaySettingsPage = QtGui.QWidget()
        self.rotateDisplaySettingsPage.setObjectName(_fromUtf8("rotateDisplaySettingsPage"))
        self.rotateDisplaySettingsDoneButton = QtGui.QPushButton(self.rotateDisplaySettingsPage)
        self.rotateDisplaySettingsDoneButton.setGeometry(QtCore.QRect(0, 710, 251, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.rotateDisplaySettingsDoneButton.setFont(font)
        self.rotateDisplaySettingsDoneButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.rotateDisplaySettingsDoneButton.setIconSize(QtCore.QSize(40, 40))
        self.rotateDisplaySettingsDoneButton.setObjectName(_fromUtf8("rotateDisplaySettingsDoneButton"))
        self.rotateDisplaySettingsCancelButton = QtGui.QPushButton(self.rotateDisplaySettingsPage)
        self.rotateDisplaySettingsCancelButton.setGeometry(QtCore.QRect(250, 710, 231, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.rotateDisplaySettingsCancelButton.setFont(font)
        self.rotateDisplaySettingsCancelButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.rotateDisplaySettingsCancelButton.setIconSize(QtCore.QSize(40, 40))
        self.rotateDisplaySettingsCancelButton.setObjectName(_fromUtf8("rotateDisplaySettingsCancelButton"))
        self.rotateDisplaySettingsComboBox = QtGui.QComboBox(self.rotateDisplaySettingsPage)
        self.rotateDisplaySettingsComboBox.setGeometry(QtCore.QRect(10, 50, 461, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(20)
        self.rotateDisplaySettingsComboBox.setFont(font)
        self.rotateDisplaySettingsComboBox.setStyleSheet(_fromUtf8(" QScrollBar:vertical {\n"
"     border: 1px solid black;\n"
"border-radius: 5px;\n"
"    background-color: rgb(40,40,40);\n"
"     width: 60px;\n"
"     margin: 67px 0 67px 0;\n"
" }\n"
"\n"
"/* Sets up the color and height of handle */\n"
"QScrollBar::handle:vertical {\n"
"border-radius: 5px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"min-height: 7px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"     border: 1px solid black;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     height:65px;\n"
"border-radius: 5px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"     border: 1px solid black;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     height: 65px;\n"
"border-radius: 5px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
" image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
" padding: 5px;\n"
" }\n"
"QScrollBar::down-arrow:vertical {\n"
" image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
" padding: 5px;\n"
" }\n"
"\n"
"/* need this to get rid of crosshatching on scrollbar background */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"background: none;\n"
"}\n"
"\n"
"QComboBox {\n"
"border: 1px solid black;\n"
"    padding: 0px 18px 0px 3px;\n"
"    min-width: 6em;\n"
"\n"
"}\n"
"\n"
"QComboBox::item {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"background: white;\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"background: white;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"border-left: 1px solid black;\n"
"border-right: 1px solid black;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 50px;\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"\n"
"image: url(./templates/img/arrows-5.png);\n"
"width: 30px;\n"
"height: 30px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(40, 40, 40);\n"
"    background: white;\n"
"}"))
        self.rotateDisplaySettingsComboBox.setEditable(False)
        self.rotateDisplaySettingsComboBox.setMaxVisibleItems(8)
        self.rotateDisplaySettingsComboBox.setIconSize(QtCore.QSize(30, 30))
        self.rotateDisplaySettingsComboBox.setObjectName(_fromUtf8("rotateDisplaySettingsComboBox"))
        self.rotateDisplaySettingsComboBox.addItem(_fromUtf8(""))
        self.rotateDisplaySettingsComboBox.addItem(_fromUtf8(""))
        self.rotateDisplaySettingsLabel = QtGui.QLabel(self.rotateDisplaySettingsPage)
        self.rotateDisplaySettingsLabel.setGeometry(QtCore.QRect(10, 10, 461, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.rotateDisplaySettingsLabel.setFont(font)
        self.rotateDisplaySettingsLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.rotateDisplaySettingsLabel.setObjectName(_fromUtf8("rotateDisplaySettingsLabel"))
        self.stackedWidget.addWidget(self.rotateDisplaySettingsPage)
        self.networkInfoPage = QtGui.QWidget()
        self.networkInfoPage.setObjectName(_fromUtf8("networkInfoPage"))
        self.hostnameLabel = QtGui.QLabel(self.networkInfoPage)
        self.hostnameLabel.setGeometry(QtCore.QRect(1, 235, 240, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.hostnameLabel.setFont(font)
        self.hostnameLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.hostnameLabel.setObjectName(_fromUtf8("hostnameLabel"))
        self.hostname = QtGui.QLabel(self.networkInfoPage)
        self.hostname.setGeometry(QtCore.QRect(1, 257, 240, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.hostname.setFont(font)
        self.hostname.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.hostname.setObjectName(_fromUtf8("hostname"))
        self.wifiIpLabel = QtGui.QLabel(self.networkInfoPage)
        self.wifiIpLabel.setGeometry(QtCore.QRect(1, 325, 240, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.wifiIpLabel.setFont(font)
        self.wifiIpLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.wifiIpLabel.setObjectName(_fromUtf8("wifiIpLabel"))
        self.wifiMac = QtGui.QLabel(self.networkInfoPage)
        self.wifiMac.setGeometry(QtCore.QRect(1, 345, 241, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.wifiMac.setFont(font)
        self.wifiMac.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.wifiMac.setObjectName(_fromUtf8("wifiMac"))
        self.lanIpLabel = QtGui.QLabel(self.networkInfoPage)
        self.lanIpLabel.setGeometry(QtCore.QRect(1, 405, 240, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lanIpLabel.setFont(font)
        self.lanIpLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.lanIpLabel.setObjectName(_fromUtf8("lanIpLabel"))
        self.lanMac = QtGui.QLabel(self.networkInfoPage)
        self.lanMac.setGeometry(QtCore.QRect(1, 425, 240, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lanMac.setFont(font)
        self.lanMac.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.lanMac.setObjectName(_fromUtf8("lanMac"))
        self.networkInfoBackButton = QtGui.QPushButton(self.networkInfoPage)
        self.networkInfoBackButton.setGeometry(QtCore.QRect(0, 730, 481, 71))
        self.networkInfoBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.networkInfoBackButton.setFont(font)
        self.networkInfoBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        self.networkInfoBackButton.setText(_fromUtf8(""))
        self.networkInfoBackButton.setIcon(icon5)
        self.networkInfoBackButton.setIconSize(QtCore.QSize(50, 50))
        self.networkInfoBackButton.setCheckable(False)
        self.networkInfoBackButton.setAutoDefault(False)
        self.networkInfoBackButton.setDefault(False)
        self.networkInfoBackButton.setFlat(False)
        self.networkInfoBackButton.setObjectName(_fromUtf8("networkInfoBackButton"))
        self.wifiMacLabel = QtGui.QLabel(self.networkInfoPage)
        self.wifiMacLabel.setGeometry(QtCore.QRect(232, 325, 240, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.wifiMacLabel.setFont(font)
        self.wifiMacLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.wifiMacLabel.setObjectName(_fromUtf8("wifiMacLabel"))
        self.lanMacLabel = QtGui.QLabel(self.networkInfoPage)
        self.lanMacLabel.setGeometry(QtCore.QRect(232, 405, 240, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lanMacLabel.setFont(font)
        self.lanMacLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.lanMacLabel.setObjectName(_fromUtf8("lanMacLabel"))
        self.wifiIp = QtGui.QLabel(self.networkInfoPage)
        self.wifiIp.setGeometry(QtCore.QRect(232, 345, 241, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.wifiIp.setFont(font)
        self.wifiIp.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.wifiIp.setObjectName(_fromUtf8("wifiIp"))
        self.lanIp = QtGui.QLabel(self.networkInfoPage)
        self.lanIp.setGeometry(QtCore.QRect(232, 425, 240, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lanIp.setFont(font)
        self.lanIp.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.lanIp.setObjectName(_fromUtf8("lanIp"))
        self.wifiApLabel = QtGui.QLabel(self.networkInfoPage)
        self.wifiApLabel.setGeometry(QtCore.QRect(232, 235, 240, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.wifiApLabel.setFont(font)
        self.wifiApLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.wifiApLabel.setObjectName(_fromUtf8("wifiApLabel"))
        self.wifiAp = QtGui.QLabel(self.networkInfoPage)
        self.wifiAp.setGeometry(QtCore.QRect(232, 257, 240, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.wifiAp.setFont(font)
        self.wifiAp.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.wifiAp.setObjectName(_fromUtf8("wifiAp"))
        self.line_10 = QtGui.QFrame(self.networkInfoPage)
        self.line_10.setGeometry(QtCore.QRect(210, 249, 20, 212))
        self.line_10.setFrameShape(QtGui.QFrame.VLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.hostnameLabel.raise_()
        self.wifiIpLabel.raise_()
        self.wifiMac.raise_()
        self.lanIpLabel.raise_()
        self.lanMac.raise_()
        self.networkInfoBackButton.raise_()
        self.hostname.raise_()
        self.wifiMacLabel.raise_()
        self.lanMacLabel.raise_()
        self.wifiIp.raise_()
        self.lanIp.raise_()
        self.wifiApLabel.raise_()
        self.wifiAp.raise_()
        self.line_10.raise_()
        self.stackedWidget.addWidget(self.networkInfoPage)
        self.OTAUpdatePage = QtGui.QWidget()
        self.OTAUpdatePage.setObjectName(_fromUtf8("OTAUpdatePage"))
        self.updateListWidget = QtGui.QListWidget(self.OTAUpdatePage)
        self.updateListWidget.setGeometry(QtCore.QRect(0, 0, 481, 731))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.updateListWidget.setFont(font)
        self.updateListWidget.setStyleSheet(_fromUtf8("\n"
"\n"
"QScrollBar:vertical {\n"
" border: 1px solid black; \n"
"border-radius: 5px;\n"
"background: rgb(40,40,40);\n"
"width: 62px;\n"
"}\n"
"\n"
"/* Sets up the color and height of handle */\n"
"QScrollBar::handle:vertical {\n"
"border-radius: 5px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"min-height: 20px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/* This remvoes the bottom button by setting the height to 0px */\n"
"QScrollBar::add-line:vertical {\n"
"height: 0px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"/* This remvoes the top button by setting the height to 0px */\n"
"QScrollBar::sub-line:vertical {\n"
"height: 0px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"/*\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"border: 2px solid grey;\n"
"width: 5px;\n"
"height: 5px;\n"
"background: white;\n"
"}\n"
"\n"
"\n"
"/* need this to get rid of crosshatching on scrollbar background */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"background: none;\n"
"}\n"
"\n"
"QListView::item {\n"
"color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"outline: none;\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:focus {\n"
"    outline: none;\n"
"}\n"
""))
        self.updateListWidget.setObjectName(_fromUtf8("updateListWidget"))
        self.softwareUpdateBackButton = QtGui.QPushButton(self.OTAUpdatePage)
        self.softwareUpdateBackButton.setGeometry(QtCore.QRect(250, 730, 231, 71))
        self.softwareUpdateBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.softwareUpdateBackButton.setFont(font)
        self.softwareUpdateBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        self.softwareUpdateBackButton.setText(_fromUtf8(""))
        self.softwareUpdateBackButton.setIcon(icon5)
        self.softwareUpdateBackButton.setIconSize(QtCore.QSize(50, 50))
        self.softwareUpdateBackButton.setCheckable(False)
        self.softwareUpdateBackButton.setAutoDefault(False)
        self.softwareUpdateBackButton.setDefault(False)
        self.softwareUpdateBackButton.setFlat(False)
        self.softwareUpdateBackButton.setObjectName(_fromUtf8("softwareUpdateBackButton"))
        self.performUpdateButton = QtGui.QPushButton(self.OTAUpdatePage)
        self.performUpdateButton.setGeometry(QtCore.QRect(0, 730, 251, 71))
        self.performUpdateButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(17)
        self.performUpdateButton.setFont(font)
        self.performUpdateButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/update-arrows.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.performUpdateButton.setIcon(icon10)
        self.performUpdateButton.setIconSize(QtCore.QSize(40, 40))
        self.performUpdateButton.setCheckable(False)
        self.performUpdateButton.setAutoDefault(False)
        self.performUpdateButton.setDefault(False)
        self.performUpdateButton.setFlat(False)
        self.performUpdateButton.setObjectName(_fromUtf8("performUpdateButton"))
        self.stackedWidget.addWidget(self.OTAUpdatePage)
        self.softwareUpdateProgressPage = QtGui.QWidget()
        self.softwareUpdateProgressPage.setObjectName(_fromUtf8("softwareUpdateProgressPage"))
        self.logTextEdit = QtGui.QTextEdit(self.softwareUpdateProgressPage)
        self.logTextEdit.setGeometry(QtCore.QRect(0, 0, 481, 801))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(10)
        self.logTextEdit.setFont(font)
        self.logTextEdit.setStyleSheet(_fromUtf8("QTextEdit{\n"
"background-color:  rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
" border: 1px solid black; \n"
"border-radius: 5px;\n"
"background: rgb(40,40,40);\n"
"width: 30px;\n"
"}\n"
"\n"
"/* Sets up the color and height of handle */\n"
"QScrollBar::handle:vertical {\n"
"border-radius: 5px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"min-height: 20px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/* This remvoes the bottom button by setting the height to 0px */\n"
"QScrollBar::add-line:vertical {\n"
"height: 0px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"/* This remvoes the top button by setting the height to 0px */\n"
"QScrollBar::sub-line:vertical {\n"
"height: 0px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"/*\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"border: 2px solid grey;\n"
"width: 5px;\n"
"height: 5px;\n"
"background: white;\n"
"}\n"
"\n"
"\n"
"/* need this to get rid of crosshatching on scrollbar background */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"background: none;\n"
"}\n"
""))
        self.logTextEdit.setReadOnly(True)
        self.logTextEdit.setObjectName(_fromUtf8("logTextEdit"))
        self.stackedWidget.addWidget(self.softwareUpdateProgressPage)
        self.firmwareUpdateProgressPage = QtGui.QWidget()
        self.firmwareUpdateProgressPage.setObjectName(_fromUtf8("firmwareUpdateProgressPage"))
        self.firmwareUpdateLog = QtGui.QTextEdit(self.firmwareUpdateProgressPage)
        self.firmwareUpdateLog.setGeometry(QtCore.QRect(0, 0, 481, 731))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(12)
        self.firmwareUpdateLog.setFont(font)
        self.firmwareUpdateLog.setStyleSheet(_fromUtf8("QTextEdit{\n"
"background-color:  rgb(40, 40, 40);\n"
"/*font-color: white;*/\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
" border: 1px solid black; \n"
"border-radius: 5px;\n"
"background: rgb(40,40,40);\n"
"width: 30px;\n"
"}\n"
"\n"
"/* Sets up the color and height of handle */\n"
"QScrollBar::handle:vertical {\n"
"border-radius: 5px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"min-height: 20px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/* This remvoes the bottom button by setting the height to 0px */\n"
"QScrollBar::add-line:vertical {\n"
"height: 0px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"/* This remvoes the top button by setting the height to 0px */\n"
"QScrollBar::sub-line:vertical {\n"
"height: 0px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"/*\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"border: 2px solid grey;\n"
"width: 5px;\n"
"height: 5px;\n"
"background: white;\n"
"}\n"
"\n"
"\n"
"/* need this to get rid of crosshatching on scrollbar background */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"background: none;\n"
"}\n"
""))
        self.firmwareUpdateLog.setReadOnly(True)
        self.firmwareUpdateLog.setObjectName(_fromUtf8("firmwareUpdateLog"))
        self.firmwareUpdateBackButton = QtGui.QPushButton(self.firmwareUpdateProgressPage)
        self.firmwareUpdateBackButton.setEnabled(False)
        self.firmwareUpdateBackButton.setGeometry(QtCore.QRect(0, 730, 481, 71))
        self.firmwareUpdateBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.firmwareUpdateBackButton.setFont(font)
        self.firmwareUpdateBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        self.firmwareUpdateBackButton.setText(_fromUtf8(""))
        self.firmwareUpdateBackButton.setIcon(icon5)
        self.firmwareUpdateBackButton.setIconSize(QtCore.QSize(50, 50))
        self.firmwareUpdateBackButton.setCheckable(False)
        self.firmwareUpdateBackButton.setAutoDefault(False)
        self.firmwareUpdateBackButton.setDefault(False)
        self.firmwareUpdateBackButton.setFlat(False)
        self.firmwareUpdateBackButton.setObjectName(_fromUtf8("firmwareUpdateBackButton"))
        self.stackedWidget.addWidget(self.firmwareUpdateProgressPage)
        self.calibratePage = QtGui.QWidget()
        self.calibratePage.setObjectName(_fromUtf8("calibratePage"))
        self.calibrateLabel = QtGui.QLabel(self.calibratePage)
        self.calibrateLabel.setGeometry(QtCore.QRect(10, 20, 231, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.calibrateLabel.setFont(font)
        self.calibrateLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.calibrateLabel.setObjectName(_fromUtf8("calibrateLabel"))
        self.calibrateBackButton = QtGui.QPushButton(self.calibratePage)
        self.calibrateBackButton.setGeometry(QtCore.QRect(0, 690, 481, 111))
        self.calibrateBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.calibrateBackButton.setFont(font)
        self.calibrateBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        self.calibrateBackButton.setText(_fromUtf8(""))
        self.calibrateBackButton.setIcon(icon5)
        self.calibrateBackButton.setIconSize(QtCore.QSize(50, 50))
        self.calibrateBackButton.setCheckable(False)
        self.calibrateBackButton.setAutoDefault(False)
        self.calibrateBackButton.setDefault(False)
        self.calibrateBackButton.setFlat(False)
        self.calibrateBackButton.setObjectName(_fromUtf8("calibrateBackButton"))
        self.calibrationWizardButton = QtGui.QToolButton(self.calibratePage)
        self.calibrationWizardButton.setGeometry(QtCore.QRect(-1, 470, 245, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(11)
        self.calibrationWizardButton.setFont(font)
        self.calibrationWizardButton.setStyleSheet(_fromUtf8("QToolButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QToolButton:focus {\n"
"    outline: none;\n"
"}"))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/magic-wand.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calibrationWizardButton.setIcon(icon11)
        self.calibrationWizardButton.setIconSize(QtCore.QSize(60, 60))
        self.calibrationWizardButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.calibrationWizardButton.setObjectName(_fromUtf8("calibrationWizardButton"))
        self.toolOffsetXYButton = QtGui.QToolButton(self.calibratePage)
        self.toolOffsetXYButton.setGeometry(QtCore.QRect(310, 580, 171, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(11)
        self.toolOffsetXYButton.setFont(font)
        self.toolOffsetXYButton.setStyleSheet(_fromUtf8("QToolButton {\n"
"\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QToolButton:focus {\n"
"    outline: none;\n"
"}"))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/Tool Offset Icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolOffsetXYButton.setIcon(icon12)
        self.toolOffsetXYButton.setIconSize(QtCore.QSize(70, 70))
        self.toolOffsetXYButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolOffsetXYButton.setObjectName(_fromUtf8("toolOffsetXYButton"))
        self.nozzleOffsetButton = QtGui.QToolButton(self.calibratePage)
        self.nozzleOffsetButton.setGeometry(QtCore.QRect(-9, 580, 171, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(11)
        self.nozzleOffsetButton.setFont(font)
        self.nozzleOffsetButton.setStyleSheet(_fromUtf8("QToolButton {\n"
"\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QToolButton:focus {\n"
"    outline: none;\n"
"}"))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/Nozzle Offset Icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nozzleOffsetButton.setIcon(icon13)
        self.nozzleOffsetButton.setIconSize(QtCore.QSize(70, 70))
        self.nozzleOffsetButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.nozzleOffsetButton.setObjectName(_fromUtf8("nozzleOffsetButton"))
        self.toolOffsetZButton = QtGui.QToolButton(self.calibratePage)
        self.toolOffsetZButton.setGeometry(QtCore.QRect(161, 580, 151, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(11)
        self.toolOffsetZButton.setFont(font)
        self.toolOffsetZButton.setStyleSheet(_fromUtf8("QToolButton {\n"
"\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QToolButton:focus {\n"
"    outline: none;\n"
"}"))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/Tool Z Offset Icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolOffsetZButton.setIcon(icon14)
        self.toolOffsetZButton.setIconSize(QtCore.QSize(70, 70))
        self.toolOffsetZButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolOffsetZButton.setObjectName(_fromUtf8("toolOffsetZButton"))
        self.testPrintsButton = QtGui.QToolButton(self.calibratePage)
        self.testPrintsButton.setGeometry(QtCore.QRect(240, 470, 243, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(11)
        self.testPrintsButton.setFont(font)
        self.testPrintsButton.setStyleSheet(_fromUtf8("QToolButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QToolButton:focus {\n"
"    outline: none;\n"
"}"))
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/3d-printing.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.testPrintsButton.setIcon(icon15)
        self.testPrintsButton.setIconSize(QtCore.QSize(60, 60))
        self.testPrintsButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.testPrintsButton.setObjectName(_fromUtf8("testPrintsButton"))
        self.line_11 = QtGui.QFrame(self.calibratePage)
        self.line_11.setGeometry(QtCore.QRect(10, 51, 378, 17))
        self.line_11.setFrameShape(QtGui.QFrame.HLine)
        self.line_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_11.setObjectName(_fromUtf8("line_11"))
        self.stackedWidget.addWidget(self.calibratePage)
        self.testPrintsPage1 = QtGui.QWidget()
        self.testPrintsPage1.setObjectName(_fromUtf8("testPrintsPage1"))
        self.calibrateLabel_2 = QtGui.QLabel(self.testPrintsPage1)
        self.calibrateLabel_2.setGeometry(QtCore.QRect(10, 19, 469, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.calibrateLabel_2.setFont(font)
        self.calibrateLabel_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.calibrateLabel_2.setObjectName(_fromUtf8("calibrateLabel_2"))
        self.testPrintsTool0SizeComboBox = QtGui.QComboBox(self.testPrintsPage1)
        self.testPrintsTool0SizeComboBox.setGeometry(QtCore.QRect(100, 287, 370, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(20)
        self.testPrintsTool0SizeComboBox.setFont(font)
        self.testPrintsTool0SizeComboBox.setStyleSheet(_fromUtf8(" QScrollBar:vertical {\n"
"     border: 1px solid black;\n"
"border-radius: 5px;\n"
"    background-color: rgb(40,40,40);\n"
"     width: 60px;\n"
"     margin: 67px 0 67px 0;\n"
" }\n"
"\n"
"/* Sets up the color and height of handle */\n"
"QScrollBar::handle:vertical {\n"
"border-radius: 5px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"min-height: 7px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"     border: 1px solid black;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     height:65px;\n"
"border-radius: 5px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"     border: 1px solid black;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     height: 65px;\n"
"border-radius: 5px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
" image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
" padding: 5px;\n"
" }\n"
"QScrollBar::down-arrow:vertical {\n"
" image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
" padding: 5px;\n"
" }\n"
"\n"
"/* need this to get rid of crosshatching on scrollbar background */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"background: none;\n"
"}\n"
"\n"
"QComboBox {\n"
"border: 1px solid black;\n"
"    padding: 0px 18px 0px 3px;\n"
"    min-width: 6em;\n"
"\n"
"}\n"
"\n"
"QComboBox::item {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"background: white;\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"background: white;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"border-left: 1px solid black;\n"
"border-right: 1px solid black;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 50px;\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"\n"
"image: url(./templates/img/arrows-5.png);\n"
"width: 30px;\n"
"height: 30px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(40, 40, 40);\n"
"    background: white;\n"
"}"))
        self.testPrintsTool0SizeComboBox.setEditable(False)
        self.testPrintsTool0SizeComboBox.setMaxVisibleItems(8)
        self.testPrintsTool0SizeComboBox.setIconSize(QtCore.QSize(30, 30))
        self.testPrintsTool0SizeComboBox.setObjectName(_fromUtf8("testPrintsTool0SizeComboBox"))
        self.testPrintsTool0SizeComboBox.addItem(_fromUtf8(""))
        self.testPrintsTool0SizeComboBox.addItem(_fromUtf8(""))
        self.testPrintsTool0SizeComboBox.addItem(_fromUtf8(""))
        self.testPrintsTool1SizeComboBox = QtGui.QComboBox(self.testPrintsPage1)
        self.testPrintsTool1SizeComboBox.setGeometry(QtCore.QRect(103, 500, 367, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(20)
        self.testPrintsTool1SizeComboBox.setFont(font)
        self.testPrintsTool1SizeComboBox.setStyleSheet(_fromUtf8(" QScrollBar:vertical {\n"
"     border: 1px solid black;\n"
"border-radius: 5px;\n"
"    background-color: rgb(40,40,40);\n"
"     width: 60px;\n"
"     margin: 67px 0 67px 0;\n"
" }\n"
"\n"
"/* Sets up the color and height of handle */\n"
"QScrollBar::handle:vertical {\n"
"border-radius: 5px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"min-height: 7px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"     border: 1px solid black;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     height:65px;\n"
"border-radius: 5px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"     border: 1px solid black;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     height: 65px;\n"
"border-radius: 5px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
" image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
" padding: 5px;\n"
" }\n"
"QScrollBar::down-arrow:vertical {\n"
" image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
" padding: 5px;\n"
" }\n"
"\n"
"/* need this to get rid of crosshatching on scrollbar background */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"background: none;\n"
"}\n"
"\n"
"QComboBox {\n"
"border: 1px solid black;\n"
"    padding: 0px 18px 0px 3px;\n"
"    min-width: 6em;\n"
"\n"
"}\n"
"\n"
"QComboBox::item {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"background: white;\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"background: white;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"border-left: 1px solid black;\n"
"border-right: 1px solid black;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 50px;\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"\n"
"image: url(./templates/img/arrows-5.png);\n"
"width: 30px;\n"
"height: 30px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(40, 40, 40);\n"
"    background: white;\n"
"}"))
        self.testPrintsTool1SizeComboBox.setEditable(False)
        self.testPrintsTool1SizeComboBox.setMaxVisibleItems(8)
        self.testPrintsTool1SizeComboBox.setIconSize(QtCore.QSize(30, 30))
        self.testPrintsTool1SizeComboBox.setObjectName(_fromUtf8("testPrintsTool1SizeComboBox"))
        self.testPrintsTool1SizeComboBox.addItem(_fromUtf8(""))
        self.testPrintsTool1SizeComboBox.addItem(_fromUtf8(""))
        self.testPrintsTool1SizeComboBox.addItem(_fromUtf8(""))
        self.tool0Label_2 = QtGui.QLabel(self.testPrintsPage1)
        self.tool0Label_2.setGeometry(QtCore.QRect(31, 288, 50, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tool0Label_2.setFont(font)
        self.tool0Label_2.setStyleSheet(_fromUtf8("\n"
"   color:  white;"))
        self.tool0Label_2.setText(_fromUtf8(""))
        self.tool0Label_2.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/Nozzle.png")))
        self.tool0Label_2.setScaledContents(True)
        self.tool0Label_2.setObjectName(_fromUtf8("tool0Label_2"))
        self.tool0TargetTemperature_5 = QtGui.QLabel(self.testPrintsPage1)
        self.tool0TargetTemperature_5.setGeometry(QtCore.QRect(10, 300, 41, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tool0TargetTemperature_5.setFont(font)
        self.tool0TargetTemperature_5.setStyleSheet(_fromUtf8("\n"
"   color:  black;\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.tool0TargetTemperature_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tool0TargetTemperature_5.setObjectName(_fromUtf8("tool0TargetTemperature_5"))
        self.tool1Label_2 = QtGui.QLabel(self.testPrintsPage1)
        self.tool1Label_2.setGeometry(QtCore.QRect(30, 506, 50, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tool1Label_2.setFont(font)
        self.tool1Label_2.setStyleSheet(_fromUtf8("\n"
"   color:  white;"))
        self.tool1Label_2.setText(_fromUtf8(""))
        self.tool1Label_2.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/Nozzle.png")))
        self.tool1Label_2.setScaledContents(True)
        self.tool1Label_2.setObjectName(_fromUtf8("tool1Label_2"))
        self.tool0TargetTemperature_6 = QtGui.QLabel(self.testPrintsPage1)
        self.tool0TargetTemperature_6.setGeometry(QtCore.QRect(10, 519, 41, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tool0TargetTemperature_6.setFont(font)
        self.tool0TargetTemperature_6.setStyleSheet(_fromUtf8("\n"
"   color:  black;\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.tool0TargetTemperature_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tool0TargetTemperature_6.setObjectName(_fromUtf8("tool0TargetTemperature_6"))
        self.calibrateLabel_3 = QtGui.QLabel(self.testPrintsPage1)
        self.calibrateLabel_3.setGeometry(QtCore.QRect(9, 192, 465, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calibrateLabel_3.setFont(font)
        self.calibrateLabel_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.calibrateLabel_3.setObjectName(_fromUtf8("calibrateLabel_3"))
        self.testPrintsNextButton = QtGui.QPushButton(self.testPrintsPage1)
        self.testPrintsNextButton.setGeometry(QtCore.QRect(-1, 740, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.testPrintsNextButton.setFont(font)
        self.testPrintsNextButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.testPrintsNextButton.setIconSize(QtCore.QSize(40, 40))
        self.testPrintsNextButton.setObjectName(_fromUtf8("testPrintsNextButton"))
        self.testPrintsBackButton = QtGui.QPushButton(self.testPrintsPage1)
        self.testPrintsBackButton.setGeometry(QtCore.QRect(239, 740, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.testPrintsBackButton.setFont(font)
        self.testPrintsBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.testPrintsBackButton.setText(_fromUtf8(""))
        self.testPrintsBackButton.setIcon(icon5)
        self.testPrintsBackButton.setIconSize(QtCore.QSize(40, 40))
        self.testPrintsBackButton.setObjectName(_fromUtf8("testPrintsBackButton"))
        self.calibrateLabel_4 = QtGui.QLabel(self.testPrintsPage1)
        self.calibrateLabel_4.setGeometry(QtCore.QRect(85, 64, 388, 96))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.calibrateLabel_4.setFont(font)
        self.calibrateLabel_4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.calibrateLabel_4.setScaledContents(False)
        self.calibrateLabel_4.setWordWrap(True)
        self.calibrateLabel_4.setObjectName(_fromUtf8("calibrateLabel_4"))
        self.tool0Label_3 = QtGui.QLabel(self.testPrintsPage1)
        self.tool0Label_3.setGeometry(QtCore.QRect(20, 86, 50, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tool0Label_3.setFont(font)
        self.tool0Label_3.setStyleSheet(_fromUtf8("\n"
"   color:  white;"))
        self.tool0Label_3.setText(_fromUtf8(""))
        self.tool0Label_3.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/exclamation-mark.png")))
        self.tool0Label_3.setScaledContents(True)
        self.tool0Label_3.setObjectName(_fromUtf8("tool0Label_3"))
        self.calibrateLabel_8 = QtGui.QLabel(self.testPrintsPage1)
        self.calibrateLabel_8.setGeometry(QtCore.QRect(90, 376, 388, 96))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.calibrateLabel_8.setFont(font)
        self.calibrateLabel_8.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.calibrateLabel_8.setScaledContents(False)
        self.calibrateLabel_8.setWordWrap(True)
        self.calibrateLabel_8.setObjectName(_fromUtf8("calibrateLabel_8"))
        self.tool0Label_5 = QtGui.QLabel(self.testPrintsPage1)
        self.tool0Label_5.setGeometry(QtCore.QRect(16, 400, 50, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tool0Label_5.setFont(font)
        self.tool0Label_5.setStyleSheet(_fromUtf8("\n"
"   color:  white;"))
        self.tool0Label_5.setText(_fromUtf8(""))
        self.tool0Label_5.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/exclamation-mark.png")))
        self.tool0Label_5.setScaledContents(True)
        self.tool0Label_5.setObjectName(_fromUtf8("tool0Label_5"))
        self.stackedWidget.addWidget(self.testPrintsPage1)
        self.testPrintsPage2 = QtGui.QWidget()
        self.testPrintsPage2.setObjectName(_fromUtf8("testPrintsPage2"))
        self.testPrintsCancelButton = QtGui.QPushButton(self.testPrintsPage2)
        self.testPrintsCancelButton.setGeometry(QtCore.QRect(-1, 691, 481, 111))
        self.testPrintsCancelButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(13)
        self.testPrintsCancelButton.setFont(font)
        self.testPrintsCancelButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        self.testPrintsCancelButton.setIconSize(QtCore.QSize(50, 50))
        self.testPrintsCancelButton.setCheckable(False)
        self.testPrintsCancelButton.setAutoDefault(False)
        self.testPrintsCancelButton.setDefault(False)
        self.testPrintsCancelButton.setFlat(False)
        self.testPrintsCancelButton.setObjectName(_fromUtf8("testPrintsCancelButton"))
        self.dualCaliberationPrintButton = QtGui.QPushButton(self.testPrintsPage2)
        self.dualCaliberationPrintButton.setGeometry(QtCore.QRect(0, 192, 480, 70))
        self.dualCaliberationPrintButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.dualCaliberationPrintButton.setFont(font)
        self.dualCaliberationPrintButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.dualCaliberationPrintButton.setIconSize(QtCore.QSize(40, 40))
        self.dualCaliberationPrintButton.setObjectName(_fromUtf8("dualCaliberationPrintButton"))
        self.bedLevelPrintButton = QtGui.QPushButton(self.testPrintsPage2)
        self.bedLevelPrintButton.setGeometry(QtCore.QRect(0, 260, 480, 70))
        self.bedLevelPrintButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.bedLevelPrintButton.setFont(font)
        self.bedLevelPrintButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.bedLevelPrintButton.setIconSize(QtCore.QSize(40, 40))
        self.bedLevelPrintButton.setObjectName(_fromUtf8("bedLevelPrintButton"))
        self.movementTestPrintButton = QtGui.QPushButton(self.testPrintsPage2)
        self.movementTestPrintButton.setGeometry(QtCore.QRect(0, 329, 480, 70))
        self.movementTestPrintButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.movementTestPrintButton.setFont(font)
        self.movementTestPrintButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.movementTestPrintButton.setIconSize(QtCore.QSize(40, 40))
        self.movementTestPrintButton.setObjectName(_fromUtf8("movementTestPrintButton"))
        self.singleNozzlePrintButton = QtGui.QPushButton(self.testPrintsPage2)
        self.singleNozzlePrintButton.setGeometry(QtCore.QRect(0, 392, 480, 70))
        self.singleNozzlePrintButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.singleNozzlePrintButton.setFont(font)
        self.singleNozzlePrintButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.singleNozzlePrintButton.setIconSize(QtCore.QSize(40, 40))
        self.singleNozzlePrintButton.setObjectName(_fromUtf8("singleNozzlePrintButton"))
        self.dualNozzlePrintButton = QtGui.QPushButton(self.testPrintsPage2)
        self.dualNozzlePrintButton.setGeometry(QtCore.QRect(0, 453, 480, 70))
        self.dualNozzlePrintButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.dualNozzlePrintButton.setFont(font)
        self.dualNozzlePrintButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.dualNozzlePrintButton.setIconSize(QtCore.QSize(40, 40))
        self.dualNozzlePrintButton.setObjectName(_fromUtf8("dualNozzlePrintButton"))
        self.tool0Label_4 = QtGui.QLabel(self.testPrintsPage2)
        self.tool0Label_4.setGeometry(QtCore.QRect(18, 67, 50, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tool0Label_4.setFont(font)
        self.tool0Label_4.setStyleSheet(_fromUtf8("\n"
"   color:  white;"))
        self.tool0Label_4.setText(_fromUtf8(""))
        self.tool0Label_4.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/exclamation-mark.png")))
        self.tool0Label_4.setScaledContents(True)
        self.tool0Label_4.setObjectName(_fromUtf8("tool0Label_4"))
        self.calibrateLabel_5 = QtGui.QLabel(self.testPrintsPage2)
        self.calibrateLabel_5.setGeometry(QtCore.QRect(83, 45, 388, 96))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.calibrateLabel_5.setFont(font)
        self.calibrateLabel_5.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.calibrateLabel_5.setScaledContents(False)
        self.calibrateLabel_5.setWordWrap(True)
        self.calibrateLabel_5.setObjectName(_fromUtf8("calibrateLabel_5"))
        self.stackedWidget.addWidget(self.testPrintsPage2)
        self.toolOffsetXYPage = QtGui.QWidget()
        self.toolOffsetXYPage.setObjectName(_fromUtf8("toolOffsetXYPage"))
        self.tollOffsetXLabel = QtGui.QLabel(self.toolOffsetXYPage)
        self.tollOffsetXLabel.setGeometry(QtCore.QRect(10, 200, 70, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.tollOffsetXLabel.setFont(font)
        self.tollOffsetXLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.tollOffsetXLabel.setObjectName(_fromUtf8("tollOffsetXLabel"))
        self.toolOffsetXYBackButton = QtGui.QPushButton(self.toolOffsetXYPage)
        self.toolOffsetXYBackButton.setGeometry(QtCore.QRect(0, 699, 480, 101))
        self.toolOffsetXYBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.toolOffsetXYBackButton.setFont(font)
        self.toolOffsetXYBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.toolOffsetXYBackButton.setText(_fromUtf8(""))
        self.toolOffsetXYBackButton.setIcon(icon5)
        self.toolOffsetXYBackButton.setIconSize(QtCore.QSize(50, 50))
        self.toolOffsetXYBackButton.setCheckable(False)
        self.toolOffsetXYBackButton.setAutoDefault(False)
        self.toolOffsetXYBackButton.setDefault(False)
        self.toolOffsetXYBackButton.setFlat(False)
        self.toolOffsetXYBackButton.setObjectName(_fromUtf8("toolOffsetXYBackButton"))
        self.toolOffsetLabel = QtGui.QLabel(self.toolOffsetXYPage)
        self.toolOffsetLabel.setGeometry(QtCore.QRect(5, 5, 281, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.toolOffsetLabel.setFont(font)
        self.toolOffsetLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.toolOffsetLabel.setObjectName(_fromUtf8("toolOffsetLabel"))
        self.toolOffsetXDoubleSpinBox = QtGui.QDoubleSpinBox(self.toolOffsetXYPage)
        self.toolOffsetXDoubleSpinBox.setGeometry(QtCore.QRect(90, 120, 281, 171))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(20)
        self.toolOffsetXDoubleSpinBox.setFont(font)
        self.toolOffsetXDoubleSpinBox.setStyleSheet(_fromUtf8("QDoubleSpinBox {\n"
"    padding-right: 5px; /* make room for the arrows */\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"   \n"
"}\n"
"QDoubleSpinBox ::text:selected {\n"
"    background-color: rgb(255, 146, 57);\n"
"   \n"
"}\n"
"QDoubleSpinBox::up-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"border-top-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 80px;\n"
"     height:80px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-arrow { \n"
"image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"QDoubleSpinBox::up-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"border-bottom-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 80px;\n"
"     height:80px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-arrow { \n"
"image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"\n"
"}\n"
"\n"
""))
        self.toolOffsetXDoubleSpinBox.setReadOnly(False)
        self.toolOffsetXDoubleSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.toolOffsetXDoubleSpinBox.setAccelerated(True)
        self.toolOffsetXDoubleSpinBox.setDecimals(2)
        self.toolOffsetXDoubleSpinBox.setMinimum(30.0)
        self.toolOffsetXDoubleSpinBox.setMaximum(42.0)
        self.toolOffsetXDoubleSpinBox.setSingleStep(0.025)
        self.toolOffsetXDoubleSpinBox.setProperty("value", 36.05)
        self.toolOffsetXDoubleSpinBox.setObjectName(_fromUtf8("toolOffsetXDoubleSpinBox"))
        self.toolOffsetXSetButton = QtGui.QPushButton(self.toolOffsetXYPage)
        self.toolOffsetXSetButton.setGeometry(QtCore.QRect(370, 120, 91, 170))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.toolOffsetXSetButton.setFont(font)
        self.toolOffsetXSetButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.toolOffsetXSetButton.setText(_fromUtf8(""))
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/verification-mark.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolOffsetXSetButton.setIcon(icon16)
        self.toolOffsetXSetButton.setIconSize(QtCore.QSize(50, 50))
        self.toolOffsetXSetButton.setObjectName(_fromUtf8("toolOffsetXSetButton"))
        self.toolOffsetYSetButton = QtGui.QPushButton(self.toolOffsetXYPage)
        self.toolOffsetYSetButton.setGeometry(QtCore.QRect(370, 391, 91, 171))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.toolOffsetYSetButton.setFont(font)
        self.toolOffsetYSetButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.toolOffsetYSetButton.setText(_fromUtf8(""))
        self.toolOffsetYSetButton.setIcon(icon16)
        self.toolOffsetYSetButton.setIconSize(QtCore.QSize(50, 50))
        self.toolOffsetYSetButton.setObjectName(_fromUtf8("toolOffsetYSetButton"))
        self.toolOffsetYDoubleSpinBox = QtGui.QDoubleSpinBox(self.toolOffsetXYPage)
        self.toolOffsetYDoubleSpinBox.setGeometry(QtCore.QRect(90, 390, 281, 171))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(20)
        self.toolOffsetYDoubleSpinBox.setFont(font)
        self.toolOffsetYDoubleSpinBox.setStyleSheet(_fromUtf8("QDoubleSpinBox {\n"
"    padding-right: 5px; /* make room for the arrows */\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"   \n"
"}\n"
"QDoubleSpinBox ::text:selected {\n"
"    background-color: rgb(255, 146, 57);\n"
"   \n"
"}\n"
"QDoubleSpinBox::up-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"border-top-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width:80px;\n"
"     height: 80px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-arrow { \n"
"image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"QDoubleSpinBox::up-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"border-bottom-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 80px;\n"
"     height: 80px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-arrow { \n"
"image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"\n"
"}\n"
"\n"
""))
        self.toolOffsetYDoubleSpinBox.setReadOnly(False)
        self.toolOffsetYDoubleSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.toolOffsetYDoubleSpinBox.setAccelerated(True)
        self.toolOffsetYDoubleSpinBox.setDecimals(2)
        self.toolOffsetYDoubleSpinBox.setMinimum(-6.0)
        self.toolOffsetYDoubleSpinBox.setMaximum(6.0)
        self.toolOffsetYDoubleSpinBox.setSingleStep(0.025)
        self.toolOffsetYDoubleSpinBox.setObjectName(_fromUtf8("toolOffsetYDoubleSpinBox"))
        self.toolOffsetYLabel = QtGui.QLabel(self.toolOffsetXYPage)
        self.toolOffsetYLabel.setGeometry(QtCore.QRect(10, 470, 70, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.toolOffsetYLabel.setFont(font)
        self.toolOffsetYLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.toolOffsetYLabel.setObjectName(_fromUtf8("toolOffsetYLabel"))
        self.line_12 = QtGui.QFrame(self.toolOffsetXYPage)
        self.line_12.setGeometry(QtCore.QRect(10, 40, 378, 17))
        self.line_12.setFrameShape(QtGui.QFrame.HLine)
        self.line_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_12.setObjectName(_fromUtf8("line_12"))
        self.stackedWidget.addWidget(self.toolOffsetXYPage)
        self.toolOffsetZpage = QtGui.QWidget()
        self.toolOffsetZpage.setObjectName(_fromUtf8("toolOffsetZpage"))
        self.toolOffsetZSetButton = QtGui.QPushButton(self.toolOffsetZpage)
        self.toolOffsetZSetButton.setGeometry(QtCore.QRect(385, 236, 91, 170))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.toolOffsetZSetButton.setFont(font)
        self.toolOffsetZSetButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.toolOffsetZSetButton.setText(_fromUtf8(""))
        self.toolOffsetZSetButton.setIcon(icon16)
        self.toolOffsetZSetButton.setIconSize(QtCore.QSize(50, 50))
        self.toolOffsetZSetButton.setObjectName(_fromUtf8("toolOffsetZSetButton"))
        self.toolOffsetZDoubleSpinBox = QtGui.QDoubleSpinBox(self.toolOffsetZpage)
        self.toolOffsetZDoubleSpinBox.setGeometry(QtCore.QRect(105, 235, 281, 171))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(20)
        self.toolOffsetZDoubleSpinBox.setFont(font)
        self.toolOffsetZDoubleSpinBox.setStyleSheet(_fromUtf8("QDoubleSpinBox {\n"
"    padding-right: 5px; /* make room for the arrows */\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"   \n"
"}\n"
"QDoubleSpinBox ::text:selected {\n"
"    background-color: rgb(255, 146, 57);\n"
"   \n"
"}\n"
"QDoubleSpinBox::up-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"border-top-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 80px;\n"
"     height: 80px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-arrow { \n"
"image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"QDoubleSpinBox::up-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"border-bottom-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 80px;\n"
"     height: 80px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-arrow { \n"
"image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"\n"
"}\n"
"\n"
""))
        self.toolOffsetZDoubleSpinBox.setReadOnly(False)
        self.toolOffsetZDoubleSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.toolOffsetZDoubleSpinBox.setAccelerated(True)
        self.toolOffsetZDoubleSpinBox.setDecimals(2)
        self.toolOffsetZDoubleSpinBox.setMinimum(-6.0)
        self.toolOffsetZDoubleSpinBox.setMaximum(-2.0)
        self.toolOffsetZDoubleSpinBox.setSingleStep(0.05)
        self.toolOffsetZDoubleSpinBox.setProperty("value", -4.0)
        self.toolOffsetZDoubleSpinBox.setObjectName(_fromUtf8("toolOffsetZDoubleSpinBox"))
        self.tollOffsetXLabel_2 = QtGui.QLabel(self.toolOffsetZpage)
        self.tollOffsetXLabel_2.setGeometry(QtCore.QRect(30, 310, 70, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.tollOffsetXLabel_2.setFont(font)
        self.tollOffsetXLabel_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.tollOffsetXLabel_2.setObjectName(_fromUtf8("tollOffsetXLabel_2"))
        self.toolOffsetLabel_2 = QtGui.QLabel(self.toolOffsetZpage)
        self.toolOffsetLabel_2.setGeometry(QtCore.QRect(10, 10, 231, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.toolOffsetLabel_2.setFont(font)
        self.toolOffsetLabel_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.toolOffsetLabel_2.setObjectName(_fromUtf8("toolOffsetLabel_2"))
        self.toolOffsetZBackButton = QtGui.QPushButton(self.toolOffsetZpage)
        self.toolOffsetZBackButton.setGeometry(QtCore.QRect(0, 719, 480, 81))
        self.toolOffsetZBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.toolOffsetZBackButton.setFont(font)
        self.toolOffsetZBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.toolOffsetZBackButton.setText(_fromUtf8(""))
        self.toolOffsetZBackButton.setIcon(icon5)
        self.toolOffsetZBackButton.setIconSize(QtCore.QSize(50, 50))
        self.toolOffsetZBackButton.setCheckable(False)
        self.toolOffsetZBackButton.setAutoDefault(False)
        self.toolOffsetZBackButton.setDefault(False)
        self.toolOffsetZBackButton.setFlat(False)
        self.toolOffsetZBackButton.setObjectName(_fromUtf8("toolOffsetZBackButton"))
        self.line_13 = QtGui.QFrame(self.toolOffsetZpage)
        self.line_13.setGeometry(QtCore.QRect(12, 40, 378, 17))
        self.line_13.setFrameShape(QtGui.QFrame.HLine)
        self.line_13.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_13.setObjectName(_fromUtf8("line_13"))
        self.stackedWidget.addWidget(self.toolOffsetZpage)
        self.quickStep1Page = QtGui.QWidget()
        self.quickStep1Page.setObjectName(_fromUtf8("quickStep1Page"))
        self.quickStep1CancelButton = QtGui.QPushButton(self.quickStep1Page)
        self.quickStep1CancelButton.setGeometry(QtCore.QRect(240, 740, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.quickStep1CancelButton.setFont(font)
        self.quickStep1CancelButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.quickStep1CancelButton.setIconSize(QtCore.QSize(40, 40))
        self.quickStep1CancelButton.setObjectName(_fromUtf8("quickStep1CancelButton"))
        self.quickStep1NextButton = QtGui.QPushButton(self.quickStep1Page)
        self.quickStep1NextButton.setGeometry(QtCore.QRect(0, 740, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.quickStep1NextButton.setFont(font)
        self.quickStep1NextButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.quickStep1NextButton.setIconSize(QtCore.QSize(40, 40))
        self.quickStep1NextButton.setObjectName(_fromUtf8("quickStep1NextButton"))
        self.calibrateLabel_6 = QtGui.QLabel(self.quickStep1Page)
        self.calibrateLabel_6.setGeometry(QtCore.QRect(10, 10, 461, 181))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calibrateLabel_6.setFont(font)
        self.calibrateLabel_6.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.calibrateLabel_6.setWordWrap(True)
        self.calibrateLabel_6.setObjectName(_fromUtf8("calibrateLabel_6"))
        self.stackedWidget.addWidget(self.quickStep1Page)
        self.quickStep2Page = QtGui.QWidget()
        self.quickStep2Page.setObjectName(_fromUtf8("quickStep2Page"))
        self.quickStep2NextButton = QtGui.QPushButton(self.quickStep2Page)
        self.quickStep2NextButton.setGeometry(QtCore.QRect(0, 740, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.quickStep2NextButton.setFont(font)
        self.quickStep2NextButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.quickStep2NextButton.setIconSize(QtCore.QSize(40, 40))
        self.quickStep2NextButton.setObjectName(_fromUtf8("quickStep2NextButton"))
        self.quickStep2CancelButton = QtGui.QPushButton(self.quickStep2Page)
        self.quickStep2CancelButton.setGeometry(QtCore.QRect(240, 740, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.quickStep2CancelButton.setFont(font)
        self.quickStep2CancelButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.quickStep2CancelButton.setIconSize(QtCore.QSize(40, 40))
        self.quickStep2CancelButton.setObjectName(_fromUtf8("quickStep2CancelButton"))
        self.calibrateLabel_7 = QtGui.QLabel(self.quickStep2Page)
        self.calibrateLabel_7.setGeometry(QtCore.QRect(10, 20, 471, 131))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calibrateLabel_7.setFont(font)
        self.calibrateLabel_7.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.calibrateLabel_7.setWordWrap(True)
        self.calibrateLabel_7.setObjectName(_fromUtf8("calibrateLabel_7"))
        self.stackedWidget.addWidget(self.quickStep2Page)
        self.quickStep3Page = QtGui.QWidget()
        self.quickStep3Page.setObjectName(_fromUtf8("quickStep3Page"))
        self.quickStep3NextButton = QtGui.QPushButton(self.quickStep3Page)
        self.quickStep3NextButton.setGeometry(QtCore.QRect(0, 740, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.quickStep3NextButton.setFont(font)
        self.quickStep3NextButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.quickStep3NextButton.setIconSize(QtCore.QSize(40, 40))
        self.quickStep3NextButton.setObjectName(_fromUtf8("quickStep3NextButton"))
        self.quickStep3CancelButton = QtGui.QPushButton(self.quickStep3Page)
        self.quickStep3CancelButton.setGeometry(QtCore.QRect(240, 740, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.quickStep3CancelButton.setFont(font)
        self.quickStep3CancelButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.quickStep3CancelButton.setIconSize(QtCore.QSize(40, 40))
        self.quickStep3CancelButton.setObjectName(_fromUtf8("quickStep3CancelButton"))
        self.calibrateLabel_10 = QtGui.QLabel(self.quickStep3Page)
        self.calibrateLabel_10.setGeometry(QtCore.QRect(10, 10, 471, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calibrateLabel_10.setFont(font)
        self.calibrateLabel_10.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.calibrateLabel_10.setWordWrap(True)
        self.calibrateLabel_10.setObjectName(_fromUtf8("calibrateLabel_10"))
        self.stackedWidget.addWidget(self.quickStep3Page)
        self.quickStep4Page = QtGui.QWidget()
        self.quickStep4Page.setObjectName(_fromUtf8("quickStep4Page"))
        self.quickStep4NextButton = QtGui.QPushButton(self.quickStep4Page)
        self.quickStep4NextButton.setGeometry(QtCore.QRect(0, 740, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.quickStep4NextButton.setFont(font)
        self.quickStep4NextButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.quickStep4NextButton.setIconSize(QtCore.QSize(40, 40))
        self.quickStep4NextButton.setObjectName(_fromUtf8("quickStep4NextButton"))
        self.quickStep4CancelButton = QtGui.QPushButton(self.quickStep4Page)
        self.quickStep4CancelButton.setGeometry(QtCore.QRect(240, 740, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.quickStep4CancelButton.setFont(font)
        self.quickStep4CancelButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.quickStep4CancelButton.setIconSize(QtCore.QSize(40, 40))
        self.quickStep4CancelButton.setObjectName(_fromUtf8("quickStep4CancelButton"))
        self.calibrateLabel_12 = QtGui.QLabel(self.quickStep4Page)
        self.calibrateLabel_12.setGeometry(QtCore.QRect(10, 10, 471, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calibrateLabel_12.setFont(font)
        self.calibrateLabel_12.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.calibrateLabel_12.setWordWrap(True)
        self.calibrateLabel_12.setObjectName(_fromUtf8("calibrateLabel_12"))
        self.stackedWidget.addWidget(self.quickStep4Page)
        self.nozzleHeightStep1Page = QtGui.QWidget()
        self.nozzleHeightStep1Page.setObjectName(_fromUtf8("nozzleHeightStep1Page"))
        self.nozzleHeightStep1NextButton = QtGui.QPushButton(self.nozzleHeightStep1Page)
        self.nozzleHeightStep1NextButton.setGeometry(QtCore.QRect(0, 740, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.nozzleHeightStep1NextButton.setFont(font)
        self.nozzleHeightStep1NextButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.nozzleHeightStep1NextButton.setIconSize(QtCore.QSize(40, 40))
        self.nozzleHeightStep1NextButton.setObjectName(_fromUtf8("nozzleHeightStep1NextButton"))
        self.nozzleHeightStep1CancelButton = QtGui.QPushButton(self.nozzleHeightStep1Page)
        self.nozzleHeightStep1CancelButton.setGeometry(QtCore.QRect(240, 740, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.nozzleHeightStep1CancelButton.setFont(font)
        self.nozzleHeightStep1CancelButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.nozzleHeightStep1CancelButton.setIconSize(QtCore.QSize(40, 40))
        self.nozzleHeightStep1CancelButton.setObjectName(_fromUtf8("nozzleHeightStep1CancelButton"))
        self.toolZOffsetLabel = QtGui.QLabel(self.nozzleHeightStep1Page)
        self.toolZOffsetLabel.setGeometry(QtCore.QRect(0, 10, 471, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.toolZOffsetLabel.setFont(font)
        self.toolZOffsetLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.toolZOffsetLabel.setWordWrap(True)
        self.toolZOffsetLabel.setObjectName(_fromUtf8("toolZOffsetLabel"))
        self.moveZPT1CaliberateButton = QtGui.QPushButton(self.nozzleHeightStep1Page)
        self.moveZPT1CaliberateButton.setGeometry(QtCore.QRect(15, 303, 221, 141))
        self.moveZPT1CaliberateButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.moveZPT1CaliberateButton.setFont(font)
        self.moveZPT1CaliberateButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-bottom-left-radius: 15px;\n"
"    border-top-left-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.moveZPT1CaliberateButton.setText(_fromUtf8(""))
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/arrows-5.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.moveZPT1CaliberateButton.setIcon(icon17)
        self.moveZPT1CaliberateButton.setIconSize(QtCore.QSize(40, 40))
        self.moveZPT1CaliberateButton.setCheckable(False)
        self.moveZPT1CaliberateButton.setAutoDefault(False)
        self.moveZPT1CaliberateButton.setDefault(False)
        self.moveZPT1CaliberateButton.setFlat(False)
        self.moveZPT1CaliberateButton.setObjectName(_fromUtf8("moveZPT1CaliberateButton"))
        self.moveZMT1CaliberateButton = QtGui.QPushButton(self.nozzleHeightStep1Page)
        self.moveZMT1CaliberateButton.setGeometry(QtCore.QRect(235, 303, 211, 141))
        self.moveZMT1CaliberateButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.moveZMT1CaliberateButton.setFont(font)
        self.moveZMT1CaliberateButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-bottom-right-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.moveZMT1CaliberateButton.setText(_fromUtf8(""))
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/arrows.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.moveZMT1CaliberateButton.setIcon(icon18)
        self.moveZMT1CaliberateButton.setIconSize(QtCore.QSize(40, 40))
        self.moveZMT1CaliberateButton.setCheckable(False)
        self.moveZMT1CaliberateButton.setAutoDefault(False)
        self.moveZMT1CaliberateButton.setDefault(False)
        self.moveZMT1CaliberateButton.setFlat(False)
        self.moveZMT1CaliberateButton.setObjectName(_fromUtf8("moveZMT1CaliberateButton"))
        self.stackedWidget.addWidget(self.nozzleHeightStep1Page)
        self.nozzleOffsetPage = QtGui.QWidget()
        self.nozzleOffsetPage.setObjectName(_fromUtf8("nozzleOffsetPage"))
        self.nozzleOffsetDoubleSpinBox = QtGui.QDoubleSpinBox(self.nozzleOffsetPage)
        self.nozzleOffsetDoubleSpinBox.setGeometry(QtCore.QRect(50, 310, 321, 136))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(20)
        self.nozzleOffsetDoubleSpinBox.setFont(font)
        self.nozzleOffsetDoubleSpinBox.setStyleSheet(_fromUtf8("QDoubleSpinBox {\n"
"    padding-right: 5px; /* make room for the arrows */\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"   \n"
"}\n"
"QDoubleSpinBox ::text:selected {\n"
"    background-color: rgb(255, 146, 57);\n"
"   \n"
"}\n"
"QDoubleSpinBox::up-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"border-top-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-arrow { \n"
"image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"QDoubleSpinBox::up-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"border-bottom-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-arrow { \n"
"image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"\n"
"}\n"
"\n"
""))
        self.nozzleOffsetDoubleSpinBox.setReadOnly(False)
        self.nozzleOffsetDoubleSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.nozzleOffsetDoubleSpinBox.setAccelerated(True)
        self.nozzleOffsetDoubleSpinBox.setDecimals(2)
        self.nozzleOffsetDoubleSpinBox.setMinimum(-2.0)
        self.nozzleOffsetDoubleSpinBox.setMaximum(2.0)
        self.nozzleOffsetDoubleSpinBox.setSingleStep(0.05)
        self.nozzleOffsetDoubleSpinBox.setObjectName(_fromUtf8("nozzleOffsetDoubleSpinBox"))
        self.nozzleOffsetSetButton = QtGui.QPushButton(self.nozzleOffsetPage)
        self.nozzleOffsetSetButton.setGeometry(QtCore.QRect(368, 312, 91, 132))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.nozzleOffsetSetButton.setFont(font)
        self.nozzleOffsetSetButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.nozzleOffsetSetButton.setText(_fromUtf8(""))
        self.nozzleOffsetSetButton.setIcon(icon16)
        self.nozzleOffsetSetButton.setIconSize(QtCore.QSize(50, 50))
        self.nozzleOffsetSetButton.setObjectName(_fromUtf8("nozzleOffsetSetButton"))
        self.feedRateLabelControlPage_3 = QtGui.QLabel(self.nozzleOffsetPage)
        self.feedRateLabelControlPage_3.setGeometry(QtCore.QRect(0, 0, 481, 82))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.feedRateLabelControlPage_3.setFont(font)
        self.feedRateLabelControlPage_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.feedRateLabelControlPage_3.setWordWrap(True)
        self.feedRateLabelControlPage_3.setObjectName(_fromUtf8("feedRateLabelControlPage_3"))
        self.nozzleOffsetBackButton = QtGui.QPushButton(self.nozzleOffsetPage)
        self.nozzleOffsetBackButton.setGeometry(QtCore.QRect(0, 750, 480, 60))
        self.nozzleOffsetBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.nozzleOffsetBackButton.setFont(font)
        self.nozzleOffsetBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.nozzleOffsetBackButton.setText(_fromUtf8(""))
        self.nozzleOffsetBackButton.setIcon(icon5)
        self.nozzleOffsetBackButton.setIconSize(QtCore.QSize(50, 50))
        self.nozzleOffsetBackButton.setCheckable(False)
        self.nozzleOffsetBackButton.setAutoDefault(False)
        self.nozzleOffsetBackButton.setDefault(False)
        self.nozzleOffsetBackButton.setFlat(False)
        self.nozzleOffsetBackButton.setObjectName(_fromUtf8("nozzleOffsetBackButton"))
        self.printPreviewSelected_2 = QtGui.QLabel(self.nozzleOffsetPage)
        self.printPreviewSelected_2.setGeometry(QtCore.QRect(140, 310, 161, 161))
        self.printPreviewSelected_2.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.printPreviewSelected_2.setText(_fromUtf8(""))
        self.printPreviewSelected_2.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/Nozzle Offset.png")))
        self.printPreviewSelected_2.setScaledContents(True)
        self.printPreviewSelected_2.setObjectName(_fromUtf8("printPreviewSelected_2"))
        self.feedRateLabelControlPage_3.raise_()
        self.nozzleOffsetDoubleSpinBox.raise_()
        self.nozzleOffsetSetButton.raise_()
        self.nozzleOffsetBackButton.raise_()
        self.printPreviewSelected_2.raise_()
        self.stackedWidget.addWidget(self.nozzleOffsetPage)
        self.printLocationPage = QtGui.QWidget()
        self.printLocationPage.setObjectName(_fromUtf8("printLocationPage"))
        self.fromUsbButton = QtGui.QPushButton(self.printLocationPage)
        self.fromUsbButton.setGeometry(QtCore.QRect(160, 690, 161, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.fromUsbButton.setFont(font)
        self.fromUsbButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/usb.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fromUsbButton.setIcon(icon19)
        self.fromUsbButton.setIconSize(QtCore.QSize(40, 40))
        self.fromUsbButton.setObjectName(_fromUtf8("fromUsbButton"))
        self.printFromLabel = QtGui.QLabel(self.printLocationPage)
        self.printFromLabel.setGeometry(QtCore.QRect(10, 10, 231, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.printFromLabel.setFont(font)
        self.printFromLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.printFromLabel.setObjectName(_fromUtf8("printFromLabel"))
        self.printLocationScreenBackButton = QtGui.QPushButton(self.printLocationPage)
        self.printLocationScreenBackButton.setGeometry(QtCore.QRect(320, 690, 161, 111))
        self.printLocationScreenBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.printLocationScreenBackButton.setFont(font)
        self.printLocationScreenBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        self.printLocationScreenBackButton.setText(_fromUtf8(""))
        self.printLocationScreenBackButton.setIcon(icon5)
        self.printLocationScreenBackButton.setIconSize(QtCore.QSize(50, 50))
        self.printLocationScreenBackButton.setCheckable(False)
        self.printLocationScreenBackButton.setAutoDefault(False)
        self.printLocationScreenBackButton.setDefault(False)
        self.printLocationScreenBackButton.setFlat(False)
        self.printLocationScreenBackButton.setObjectName(_fromUtf8("printLocationScreenBackButton"))
        self.fromLocalButton = QtGui.QPushButton(self.printLocationPage)
        self.fromLocalButton.setGeometry(QtCore.QRect(0, 690, 161, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.fromLocalButton.setFont(font)
        self.fromLocalButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fromLocalButton.setIcon(icon20)
        self.fromLocalButton.setIconSize(QtCore.QSize(40, 40))
        self.fromLocalButton.setObjectName(_fromUtf8("fromLocalButton"))
        self.line_14 = QtGui.QFrame(self.printLocationPage)
        self.line_14.setGeometry(QtCore.QRect(10, 40, 378, 17))
        self.line_14.setFrameShape(QtGui.QFrame.HLine)
        self.line_14.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_14.setObjectName(_fromUtf8("line_14"))
        self.stackedWidget.addWidget(self.printLocationPage)
        self.fileListLocalPage = QtGui.QWidget()
        self.fileListLocalPage.setObjectName(_fromUtf8("fileListLocalPage"))
        self.fileListWidget = QtGui.QListWidget(self.fileListLocalPage)
        self.fileListWidget.setGeometry(QtCore.QRect(0, 0, 311, 801))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(17)
        self.fileListWidget.setFont(font)
        self.fileListWidget.setStyleSheet(_fromUtf8("\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width\n"
" of the view */\n"
"    background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"}\n"
"\n"
"QListView::item:!selected {\n"
"    color: black;\n"
"outline: none;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    border:  rgb(182, 182, 182);\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"outline: none;\n"
"}\n"
"\n"
"QListView::item:selected:!active {\n"
"     border: 1px solid rgb(182, 182, 182);\n"
"    background-color: rgb(40,40,40);\n"
"outline: none;\n"
"\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"     border: 1px solid  rgb(182, 182, 182);\n"
"    background-color: rgb(40,40,40);\n"
"outline: none;\n"
"}\n"
"\n"
"QListView::item:selected:focus {\n"
"    outline: none;\n"
"}\n"
""))
        self.fileListWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.fileListWidget.setFrameShadow(QtGui.QFrame.Plain)
        self.fileListWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.fileListWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.fileListWidget.setAutoScrollMargin(4)
        self.fileListWidget.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.fileListWidget.setObjectName(_fromUtf8("fileListWidget"))
        self.localStorageBackButton = QtGui.QPushButton(self.fileListLocalPage)
        self.localStorageBackButton.setGeometry(QtCore.QRect(390, 520, 91, 281))
        self.localStorageBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.localStorageBackButton.setFont(font)
        self.localStorageBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"        border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.localStorageBackButton.setText(_fromUtf8(""))
        self.localStorageBackButton.setIcon(icon5)
        self.localStorageBackButton.setIconSize(QtCore.QSize(50, 50))
        self.localStorageBackButton.setCheckable(False)
        self.localStorageBackButton.setAutoDefault(False)
        self.localStorageBackButton.setDefault(False)
        self.localStorageBackButton.setFlat(False)
        self.localStorageBackButton.setObjectName(_fromUtf8("localStorageBackButton"))
        self.localStorageSelectButton = QtGui.QPushButton(self.fileListLocalPage)
        self.localStorageSelectButton.setGeometry(QtCore.QRect(390, 0, 91, 281))
        self.localStorageSelectButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.localStorageSelectButton.setFont(font)
        self.localStorageSelectButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.localStorageSelectButton.setText(_fromUtf8(""))
        self.localStorageSelectButton.setIcon(icon16)
        self.localStorageSelectButton.setIconSize(QtCore.QSize(50, 50))
        self.localStorageSelectButton.setCheckable(False)
        self.localStorageSelectButton.setAutoDefault(False)
        self.localStorageSelectButton.setDefault(False)
        self.localStorageSelectButton.setFlat(False)
        self.localStorageSelectButton.setObjectName(_fromUtf8("localStorageSelectButton"))
        self.localStorageScrollDown = QtGui.QPushButton(self.fileListLocalPage)
        self.localStorageScrollDown.setGeometry(QtCore.QRect(310, 380, 81, 421))
        self.localStorageScrollDown.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.localStorageScrollDown.setFont(font)
        self.localStorageScrollDown.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.localStorageScrollDown.setText(_fromUtf8(""))
        self.localStorageScrollDown.setIcon(icon17)
        self.localStorageScrollDown.setIconSize(QtCore.QSize(40, 40))
        self.localStorageScrollDown.setCheckable(False)
        self.localStorageScrollDown.setAutoRepeat(True)
        self.localStorageScrollDown.setAutoExclusive(False)
        self.localStorageScrollDown.setAutoDefault(False)
        self.localStorageScrollDown.setDefault(False)
        self.localStorageScrollDown.setFlat(False)
        self.localStorageScrollDown.setObjectName(_fromUtf8("localStorageScrollDown"))
        self.localStorageScrollUp = QtGui.QPushButton(self.fileListLocalPage)
        self.localStorageScrollUp.setGeometry(QtCore.QRect(310, 0, 81, 381))
        self.localStorageScrollUp.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.localStorageScrollUp.setFont(font)
        self.localStorageScrollUp.setStyleSheet(_fromUtf8("QPushButton {\n"
"\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.localStorageScrollUp.setText(_fromUtf8(""))
        self.localStorageScrollUp.setIcon(icon18)
        self.localStorageScrollUp.setIconSize(QtCore.QSize(40, 40))
        self.localStorageScrollUp.setCheckable(False)
        self.localStorageScrollUp.setAutoRepeat(True)
        self.localStorageScrollUp.setAutoExclusive(False)
        self.localStorageScrollUp.setAutoDefault(False)
        self.localStorageScrollUp.setDefault(False)
        self.localStorageScrollUp.setFlat(False)
        self.localStorageScrollUp.setObjectName(_fromUtf8("localStorageScrollUp"))
        self.localStorageDeleteButton = QtGui.QPushButton(self.fileListLocalPage)
        self.localStorageDeleteButton.setGeometry(QtCore.QRect(390, 280, 91, 241))
        self.localStorageDeleteButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.localStorageDeleteButton.setFont(font)
        self.localStorageDeleteButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.localStorageDeleteButton.setText(_fromUtf8(""))
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.localStorageDeleteButton.setIcon(icon21)
        self.localStorageDeleteButton.setIconSize(QtCore.QSize(50, 50))
        self.localStorageDeleteButton.setCheckable(False)
        self.localStorageDeleteButton.setAutoDefault(False)
        self.localStorageDeleteButton.setDefault(False)
        self.localStorageDeleteButton.setFlat(False)
        self.localStorageDeleteButton.setObjectName(_fromUtf8("localStorageDeleteButton"))
        self.stackedWidget.addWidget(self.fileListLocalPage)
        self.fileListUSBPage = QtGui.QWidget()
        self.fileListUSBPage.setObjectName(_fromUtf8("fileListUSBPage"))
        self.USBStorageSaveButton = QtGui.QPushButton(self.fileListUSBPage)
        self.USBStorageSaveButton.setGeometry(QtCore.QRect(390, 240, 91, 281))
        self.USBStorageSaveButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.USBStorageSaveButton.setFont(font)
        self.USBStorageSaveButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.USBStorageSaveButton.setText(_fromUtf8(""))
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.USBStorageSaveButton.setIcon(icon22)
        self.USBStorageSaveButton.setIconSize(QtCore.QSize(50, 50))
        self.USBStorageSaveButton.setCheckable(False)
        self.USBStorageSaveButton.setAutoDefault(False)
        self.USBStorageSaveButton.setDefault(False)
        self.USBStorageSaveButton.setFlat(False)
        self.USBStorageSaveButton.setObjectName(_fromUtf8("USBStorageSaveButton"))
        self.USBStorageScrollUp = QtGui.QPushButton(self.fileListUSBPage)
        self.USBStorageScrollUp.setGeometry(QtCore.QRect(310, 0, 81, 401))
        self.USBStorageScrollUp.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.USBStorageScrollUp.setFont(font)
        self.USBStorageScrollUp.setStyleSheet(_fromUtf8("QPushButton {\n"
"\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.USBStorageScrollUp.setText(_fromUtf8(""))
        self.USBStorageScrollUp.setIcon(icon18)
        self.USBStorageScrollUp.setIconSize(QtCore.QSize(40, 40))
        self.USBStorageScrollUp.setCheckable(False)
        self.USBStorageScrollUp.setAutoRepeat(True)
        self.USBStorageScrollUp.setAutoExclusive(False)
        self.USBStorageScrollUp.setAutoDefault(False)
        self.USBStorageScrollUp.setDefault(False)
        self.USBStorageScrollUp.setFlat(False)
        self.USBStorageScrollUp.setObjectName(_fromUtf8("USBStorageScrollUp"))
        self.USBStorageSelectButton = QtGui.QPushButton(self.fileListUSBPage)
        self.USBStorageSelectButton.setGeometry(QtCore.QRect(390, 0, 91, 241))
        self.USBStorageSelectButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.USBStorageSelectButton.setFont(font)
        self.USBStorageSelectButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.USBStorageSelectButton.setText(_fromUtf8(""))
        self.USBStorageSelectButton.setIcon(icon16)
        self.USBStorageSelectButton.setIconSize(QtCore.QSize(50, 50))
        self.USBStorageSelectButton.setCheckable(False)
        self.USBStorageSelectButton.setAutoDefault(False)
        self.USBStorageSelectButton.setDefault(False)
        self.USBStorageSelectButton.setFlat(False)
        self.USBStorageSelectButton.setObjectName(_fromUtf8("USBStorageSelectButton"))
        self.USBStorageBackButton = QtGui.QPushButton(self.fileListUSBPage)
        self.USBStorageBackButton.setGeometry(QtCore.QRect(390, 520, 91, 291))
        self.USBStorageBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.USBStorageBackButton.setFont(font)
        self.USBStorageBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"        border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.USBStorageBackButton.setText(_fromUtf8(""))
        self.USBStorageBackButton.setIcon(icon5)
        self.USBStorageBackButton.setIconSize(QtCore.QSize(50, 50))
        self.USBStorageBackButton.setCheckable(False)
        self.USBStorageBackButton.setAutoDefault(False)
        self.USBStorageBackButton.setDefault(False)
        self.USBStorageBackButton.setFlat(False)
        self.USBStorageBackButton.setObjectName(_fromUtf8("USBStorageBackButton"))
        self.USBStorageScrollDown = QtGui.QPushButton(self.fileListUSBPage)
        self.USBStorageScrollDown.setGeometry(QtCore.QRect(310, 400, 81, 401))
        self.USBStorageScrollDown.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.USBStorageScrollDown.setFont(font)
        self.USBStorageScrollDown.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.USBStorageScrollDown.setText(_fromUtf8(""))
        self.USBStorageScrollDown.setIcon(icon17)
        self.USBStorageScrollDown.setIconSize(QtCore.QSize(40, 40))
        self.USBStorageScrollDown.setCheckable(False)
        self.USBStorageScrollDown.setAutoRepeat(True)
        self.USBStorageScrollDown.setAutoExclusive(False)
        self.USBStorageScrollDown.setAutoDefault(False)
        self.USBStorageScrollDown.setDefault(False)
        self.USBStorageScrollDown.setFlat(False)
        self.USBStorageScrollDown.setObjectName(_fromUtf8("USBStorageScrollDown"))
        self.fileListWidgetUSB = QtGui.QListWidget(self.fileListUSBPage)
        self.fileListWidgetUSB.setGeometry(QtCore.QRect(0, 0, 311, 801))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(17)
        self.fileListWidgetUSB.setFont(font)
        self.fileListWidgetUSB.setStyleSheet(_fromUtf8("\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width\n"
" of the view */\n"
"    background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"}\n"
"\n"
"QListView::item:!selected {\n"
"    color: black;\n"
"outline: none;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    border:  rgb(182, 182, 182);\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"outline: none;\n"
"}\n"
"\n"
"QListView::item:selected:!active {\n"
"     border: 1px solid rgb(182, 182, 182);\n"
"    background-color: rgb(40,40,40);\n"
"outline: none;\n"
"\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"     border: 1px solid  rgb(182, 182, 182);\n"
"    background-color: rgb(40,40,40);\n"
"outline: none;\n"
"}\n"
"\n"
"QListView::item:selected:focus {\n"
"    outline: none;\n"
"}\n"
""))
        self.fileListWidgetUSB.setFrameShape(QtGui.QFrame.NoFrame)
        self.fileListWidgetUSB.setFrameShadow(QtGui.QFrame.Plain)
        self.fileListWidgetUSB.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.fileListWidgetUSB.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.fileListWidgetUSB.setAutoScrollMargin(4)
        self.fileListWidgetUSB.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.fileListWidgetUSB.setObjectName(_fromUtf8("fileListWidgetUSB"))
        self.USBStorageSaveButton.raise_()
        self.USBStorageSelectButton.raise_()
        self.USBStorageBackButton.raise_()
        self.fileListWidgetUSB.raise_()
        self.USBStorageScrollDown.raise_()
        self.USBStorageScrollUp.raise_()
        self.stackedWidget.addWidget(self.fileListUSBPage)
        self.printSelectedLocalPage = QtGui.QWidget()
        self.printSelectedLocalPage.setObjectName(_fromUtf8("printSelectedLocalPage"))
        self.fileSelected = QtGui.QLabel(self.printSelectedLocalPage)
        self.fileSelected.setGeometry(QtCore.QRect(10, 0, 461, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.fileSelected.setFont(font)
        self.fileSelected.setStyleSheet(_fromUtf8("color:  white;\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.fileSelected.setScaledContents(True)
        self.fileSelected.setWordWrap(True)
        self.fileSelected.setObjectName(_fromUtf8("fileSelected"))
        self.fileSelectedBackButton = QtGui.QPushButton(self.printSelectedLocalPage)
        self.fileSelectedBackButton.setGeometry(QtCore.QRect(240, 710, 241, 91))
        self.fileSelectedBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.fileSelectedBackButton.setFont(font)
        self.fileSelectedBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        self.fileSelectedBackButton.setText(_fromUtf8(""))
        self.fileSelectedBackButton.setIcon(icon5)
        self.fileSelectedBackButton.setIconSize(QtCore.QSize(50, 50))
        self.fileSelectedBackButton.setCheckable(False)
        self.fileSelectedBackButton.setAutoDefault(False)
        self.fileSelectedBackButton.setDefault(False)
        self.fileSelectedBackButton.setFlat(False)
        self.fileSelectedBackButton.setObjectName(_fromUtf8("fileSelectedBackButton"))
        self.fileSelectedPrintButton = QtGui.QToolButton(self.printSelectedLocalPage)
        self.fileSelectedPrintButton.setGeometry(QtCore.QRect(0, 710, 241, 91))
        self.fileSelectedPrintButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        self.fileSelectedPrintButton.setFont(font)
        self.fileSelectedPrintButton.setStyleSheet(_fromUtf8("QToolButton {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        self.fileSelectedPrintButton.setIcon(icon6)
        self.fileSelectedPrintButton.setIconSize(QtCore.QSize(40, 40))
        self.fileSelectedPrintButton.setCheckable(False)
        self.fileSelectedPrintButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.fileSelectedPrintButton.setObjectName(_fromUtf8("fileSelectedPrintButton"))
        self.fileSizeSelected = QtGui.QLabel(self.printSelectedLocalPage)
        self.fileSizeSelected.setGeometry(QtCore.QRect(60, 60, 161, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.fileSizeSelected.setFont(font)
        self.fileSizeSelected.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.fileSizeSelected.setScaledContents(True)
        self.fileSizeSelected.setObjectName(_fromUtf8("fileSizeSelected"))
        self.fileDateSelected = QtGui.QLabel(self.printSelectedLocalPage)
        self.fileDateSelected.setGeometry(QtCore.QRect(70, 90, 201, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.fileDateSelected.setFont(font)
        self.fileDateSelected.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.fileDateSelected.setScaledContents(True)
        self.fileDateSelected.setObjectName(_fromUtf8("fileDateSelected"))
        self.filePrintTimeSelected = QtGui.QLabel(self.printSelectedLocalPage)
        self.filePrintTimeSelected.setGeometry(QtCore.QRect(130, 137, 141, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.filePrintTimeSelected.setFont(font)
        self.filePrintTimeSelected.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.filePrintTimeSelected.setScaledContents(True)
        self.filePrintTimeSelected.setObjectName(_fromUtf8("filePrintTimeSelected"))
        self.filamentVolumeSelected = QtGui.QLabel(self.printSelectedLocalPage)
        self.filamentVolumeSelected.setGeometry(QtCore.QRect(110, 160, 161, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.filamentVolumeSelected.setFont(font)
        self.filamentVolumeSelected.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.filamentVolumeSelected.setScaledContents(True)
        self.filamentVolumeSelected.setObjectName(_fromUtf8("filamentVolumeSelected"))
        self.fileSizeSelectedLabel = QtGui.QLabel(self.printSelectedLocalPage)
        self.fileSizeSelectedLabel.setGeometry(QtCore.QRect(10, 60, 51, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fileSizeSelectedLabel.setFont(font)
        self.fileSizeSelectedLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.fileSizeSelectedLabel.setObjectName(_fromUtf8("fileSizeSelectedLabel"))
        self.fileDateSelectedLabel = QtGui.QLabel(self.printSelectedLocalPage)
        self.fileDateSelectedLabel.setGeometry(QtCore.QRect(10, 90, 61, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.fileDateSelectedLabel.setFont(font)
        self.fileDateSelectedLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.fileDateSelectedLabel.setObjectName(_fromUtf8("fileDateSelectedLabel"))
        self.filePrintTimeSelectedLabel = QtGui.QLabel(self.printSelectedLocalPage)
        self.filePrintTimeSelectedLabel.setGeometry(QtCore.QRect(10, 110, 121, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.filePrintTimeSelectedLabel.setFont(font)
        self.filePrintTimeSelectedLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.filePrintTimeSelectedLabel.setWordWrap(True)
        self.filePrintTimeSelectedLabel.setObjectName(_fromUtf8("filePrintTimeSelectedLabel"))
        self.filamentVolumeSelectedLabel = QtGui.QLabel(self.printSelectedLocalPage)
        self.filamentVolumeSelectedLabel.setGeometry(QtCore.QRect(10, 160, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.filamentVolumeSelectedLabel.setFont(font)
        self.filamentVolumeSelectedLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.filamentVolumeSelectedLabel.setObjectName(_fromUtf8("filamentVolumeSelectedLabel"))
        self.filamentLengthFileSelected = QtGui.QLabel(self.printSelectedLocalPage)
        self.filamentLengthFileSelected.setGeometry(QtCore.QRect(110, 190, 161, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.filamentLengthFileSelected.setFont(font)
        self.filamentLengthFileSelected.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.filamentLengthFileSelected.setScaledContents(True)
        self.filamentLengthFileSelected.setObjectName(_fromUtf8("filamentLengthFileSelected"))
        self.filamentLengthSelectedLabel = QtGui.QLabel(self.printSelectedLocalPage)
        self.filamentLengthSelectedLabel.setGeometry(QtCore.QRect(10, 190, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.filamentLengthSelectedLabel.setFont(font)
        self.filamentLengthSelectedLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.filamentLengthSelectedLabel.setObjectName(_fromUtf8("filamentLengthSelectedLabel"))
        self.printPreviewSelected = QtGui.QLabel(self.printSelectedLocalPage)
        self.printPreviewSelected.setGeometry(QtCore.QRect(90, 320, 321, 311))
        self.printPreviewSelected.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.printPreviewSelected.setText(_fromUtf8(""))
        self.printPreviewSelected.setPixmap(QtGui.QPixmap(_fromUtf8("../../JuliaMiniTouchUI/octoprint_JuliaMiniTouchUI/templates/img/thumbnail.png")))
        self.printPreviewSelected.setScaledContents(True)
        self.printPreviewSelected.setObjectName(_fromUtf8("printPreviewSelected"))
        self.stackedWidget.addWidget(self.printSelectedLocalPage)
        self.printSelectedUSBPage = QtGui.QWidget()
        self.printSelectedUSBPage.setObjectName(_fromUtf8("printSelectedUSBPage"))
        self.fileSelectedUSBTransferButton = QtGui.QToolButton(self.printSelectedUSBPage)
        self.fileSelectedUSBTransferButton.setGeometry(QtCore.QRect(0, 710, 161, 91))
        self.fileSelectedUSBTransferButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        self.fileSelectedUSBTransferButton.setFont(font)
        self.fileSelectedUSBTransferButton.setStyleSheet(_fromUtf8("QToolButton {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        self.fileSelectedUSBTransferButton.setIcon(icon22)
        self.fileSelectedUSBTransferButton.setIconSize(QtCore.QSize(40, 40))
        self.fileSelectedUSBTransferButton.setCheckable(False)
        self.fileSelectedUSBTransferButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.fileSelectedUSBTransferButton.setObjectName(_fromUtf8("fileSelectedUSBTransferButton"))
        self.fileSelectedUSBBackButton = QtGui.QPushButton(self.printSelectedUSBPage)
        self.fileSelectedUSBBackButton.setGeometry(QtCore.QRect(320, 710, 161, 91))
        self.fileSelectedUSBBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.fileSelectedUSBBackButton.setFont(font)
        self.fileSelectedUSBBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        self.fileSelectedUSBBackButton.setText(_fromUtf8(""))
        self.fileSelectedUSBBackButton.setIcon(icon5)
        self.fileSelectedUSBBackButton.setIconSize(QtCore.QSize(50, 50))
        self.fileSelectedUSBBackButton.setCheckable(False)
        self.fileSelectedUSBBackButton.setAutoDefault(False)
        self.fileSelectedUSBBackButton.setDefault(False)
        self.fileSelectedUSBBackButton.setFlat(False)
        self.fileSelectedUSBBackButton.setObjectName(_fromUtf8("fileSelectedUSBBackButton"))
        self.fileSelectedUSBName = QtGui.QLabel(self.printSelectedUSBPage)
        self.fileSelectedUSBName.setGeometry(QtCore.QRect(0, 0, 481, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.fileSelectedUSBName.setFont(font)
        self.fileSelectedUSBName.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.fileSelectedUSBName.setObjectName(_fromUtf8("fileSelectedUSBName"))
        self.fileSelectedUSBPrintButton = QtGui.QToolButton(self.printSelectedUSBPage)
        self.fileSelectedUSBPrintButton.setGeometry(QtCore.QRect(160, 710, 161, 91))
        self.fileSelectedUSBPrintButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        self.fileSelectedUSBPrintButton.setFont(font)
        self.fileSelectedUSBPrintButton.setStyleSheet(_fromUtf8("QToolButton {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        self.fileSelectedUSBPrintButton.setIcon(icon6)
        self.fileSelectedUSBPrintButton.setIconSize(QtCore.QSize(40, 40))
        self.fileSelectedUSBPrintButton.setCheckable(False)
        self.fileSelectedUSBPrintButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.fileSelectedUSBPrintButton.setObjectName(_fromUtf8("fileSelectedUSBPrintButton"))
        self.printPreviewSelectedUSB = QtGui.QLabel(self.printSelectedUSBPage)
        self.printPreviewSelectedUSB.setGeometry(QtCore.QRect(70, 130, 341, 341))
        self.printPreviewSelectedUSB.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.printPreviewSelectedUSB.setText(_fromUtf8(""))
        self.printPreviewSelectedUSB.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/thumbnail.png")))
        self.printPreviewSelectedUSB.setScaledContents(True)
        self.printPreviewSelectedUSB.setObjectName(_fromUtf8("printPreviewSelectedUSB"))
        self.stackedWidget.addWidget(self.printSelectedUSBPage)
        self.controlPage = QtGui.QWidget()
        self.controlPage.setObjectName(_fromUtf8("controlPage"))
        self.controlTabWidget = QtGui.QTabWidget(self.controlPage)
        self.controlTabWidget.setGeometry(QtCore.QRect(0, 0, 491, 800))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(12)
        self.controlTabWidget.setFont(font)
        self.controlTabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.controlTabWidget.setAutoFillBackground(False)
        self.controlTabWidget.setStyleSheet(_fromUtf8("QTabWidget::pane { /* The tab widget frame */\n"
"    position: absolute;\n"
"\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"   border-right: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-top-color: #C2C7CB; /* same as the pane color */\n"
"    width: 69px;\n"
"     height: 70px;\n"
"    padding-left: 25px;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"/*    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"*/\n"
"background-color: rgb(40, 40, 40);\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"QTabBar::tab:first {\n"
"    margin-left: 0; /* the first selected tab has nothing to overlap with on the left */\n"
"/*border-bottom-left-radius: 15px;*/\n"
"}\n"
"QTabBar::tab:last {\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"}\n"
"QTabBar::tab:focus {\n"
"    outline: none;\n"
"}\n"
"QTabBar:focus {\n"
"    outline: none;\n"
"}"))
        self.controlTabWidget.setTabPosition(QtGui.QTabWidget.South)
        self.controlTabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.controlTabWidget.setIconSize(QtCore.QSize(45, 45))
        self.controlTabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.controlTabWidget.setUsesScrollButtons(False)
        self.controlTabWidget.setTabsClosable(False)
        self.controlTabWidget.setObjectName(_fromUtf8("controlTabWidget"))
        self.feedRateTab = QtGui.QWidget()
        self.feedRateTab.setObjectName(_fromUtf8("feedRateTab"))
        self.feedRateLabelControlPage = QtGui.QLabel(self.feedRateTab)
        self.feedRateLabelControlPage.setGeometry(QtCore.QRect(89, 167, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.feedRateLabelControlPage.setFont(font)
        self.feedRateLabelControlPage.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.feedRateLabelControlPage.setObjectName(_fromUtf8("feedRateLabelControlPage"))
        self.feedRateSpinBox = QtGui.QSpinBox(self.feedRateTab)
        self.feedRateSpinBox.setGeometry(QtCore.QRect(79, 205, 241, 121))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(24)
        self.feedRateSpinBox.setFont(font)
        self.feedRateSpinBox.setStyleSheet(_fromUtf8("QSpinBox {\n"
"    padding-right: 5px; /* make room for the arrows */\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"   \n"
"}\n"
"QSpinBox ::text:selected {\n"
"    background-color: rgb(255, 146, 57);\n"
"   \n"
"}\n"
"QSpinBox::up-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"border-top-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 55px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox::up-arrow { \n"
"image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"border-bottom-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 55px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow { \n"
"image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"\n"
"}\n"
"\n"
""))
        self.feedRateSpinBox.setFrame(False)
        self.feedRateSpinBox.setReadOnly(False)
        self.feedRateSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.feedRateSpinBox.setAccelerated(True)
        self.feedRateSpinBox.setMinimum(50)
        self.feedRateSpinBox.setMaximum(200)
        self.feedRateSpinBox.setSingleStep(1)
        self.feedRateSpinBox.setProperty("value", 100)
        self.feedRateSpinBox.setObjectName(_fromUtf8("feedRateSpinBox"))
        self.setFeedRateButton = QtGui.QPushButton(self.feedRateTab)
        self.setFeedRateButton.setGeometry(QtCore.QRect(317, 207, 91, 117))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.setFeedRateButton.setFont(font)
        self.setFeedRateButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.setFeedRateButton.setText(_fromUtf8(""))
        self.setFeedRateButton.setIcon(icon16)
        self.setFeedRateButton.setIconSize(QtCore.QSize(50, 50))
        self.setFeedRateButton.setObjectName(_fromUtf8("setFeedRateButton"))
        self.moveZMBabyStep = QtGui.QPushButton(self.feedRateTab)
        self.moveZMBabyStep.setGeometry(QtCore.QRect(243, 475, 161, 138))
        self.moveZMBabyStep.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.moveZMBabyStep.setFont(font)
        self.moveZMBabyStep.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-bottom-right-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.moveZMBabyStep.setText(_fromUtf8(""))
        self.moveZMBabyStep.setIcon(icon18)
        self.moveZMBabyStep.setIconSize(QtCore.QSize(40, 40))
        self.moveZMBabyStep.setCheckable(False)
        self.moveZMBabyStep.setAutoDefault(False)
        self.moveZMBabyStep.setDefault(False)
        self.moveZMBabyStep.setFlat(False)
        self.moveZMBabyStep.setObjectName(_fromUtf8("moveZMBabyStep"))
        self.moveZPBabyStep = QtGui.QPushButton(self.feedRateTab)
        self.moveZPBabyStep.setGeometry(QtCore.QRect(83, 475, 161, 138))
        self.moveZPBabyStep.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.moveZPBabyStep.setFont(font)
        self.moveZPBabyStep.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-bottom-left-radius: 15px;\n"
"    border-top-left-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.moveZPBabyStep.setText(_fromUtf8(""))
        self.moveZPBabyStep.setIcon(icon17)
        self.moveZPBabyStep.setIconSize(QtCore.QSize(40, 40))
        self.moveZPBabyStep.setCheckable(False)
        self.moveZPBabyStep.setAutoDefault(False)
        self.moveZPBabyStep.setDefault(False)
        self.moveZPBabyStep.setFlat(False)
        self.moveZPBabyStep.setObjectName(_fromUtf8("moveZPBabyStep"))
        self.flowRateLabelControlPage_5 = QtGui.QLabel(self.feedRateTab)
        self.flowRateLabelControlPage_5.setGeometry(QtCore.QRect(60, 427, 421, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.flowRateLabelControlPage_5.setFont(font)
        self.flowRateLabelControlPage_5.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.flowRateLabelControlPage_5.setObjectName(_fromUtf8("flowRateLabelControlPage_5"))
        self.line_4 = QtGui.QFrame(self.feedRateTab)
        self.line_4.setGeometry(QtCore.QRect(-10, 721, 480, 16))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.line_7 = QtGui.QFrame(self.feedRateTab)
        self.line_7.setGeometry(QtCore.QRect(21, 370, 440, 20))
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.feedRateSpinBox.raise_()
        self.feedRateLabelControlPage.raise_()
        self.setFeedRateButton.raise_()
        self.moveZMBabyStep.raise_()
        self.moveZPBabyStep.raise_()
        self.flowRateLabelControlPage_5.raise_()
        self.line_4.raise_()
        self.line_7.raise_()
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/wrench.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon23.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/wrench_selected.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.controlTabWidget.addTab(self.feedRateTab, icon23, _fromUtf8(""))
        self.temperatureTab = QtGui.QWidget()
        self.temperatureTab.setObjectName(_fromUtf8("temperatureTab"))
        self.toolLabel = QtGui.QLabel(self.temperatureTab)
        self.toolLabel.setGeometry(QtCore.QRect(10, 105, 208, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.toolLabel.setFont(font)
        self.toolLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.toolLabel.setObjectName(_fromUtf8("toolLabel"))
        self.bedLabel_2 = QtGui.QLabel(self.temperatureTab)
        self.bedLabel_2.setGeometry(QtCore.QRect(9, 340, 70, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.bedLabel_2.setFont(font)
        self.bedLabel_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.bedLabel_2.setObjectName(_fromUtf8("bedLabel_2"))
        self.cooldownButton = QtGui.QPushButton(self.temperatureTab)
        self.cooldownButton.setGeometry(QtCore.QRect(120, 0, 101, 90))
        self.cooldownButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.cooldownButton.setFont(font)
        self.cooldownButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-left-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.cooldownButton.setText(_fromUtf8(""))
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/snowflake.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cooldownButton.setIcon(icon24)
        self.cooldownButton.setIconSize(QtCore.QSize(40, 40))
        self.cooldownButton.setObjectName(_fromUtf8("cooldownButton"))
        self.fanOffButton = QtGui.QPushButton(self.temperatureTab)
        self.fanOffButton.setGeometry(QtCore.QRect(300, 0, 81, 90))
        self.fanOffButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.fanOffButton.setFont(font)
        self.fanOffButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.fanOffButton.setText(_fromUtf8(""))
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/fan-black-silhouette-off.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fanOffButton.setIcon(icon25)
        self.fanOffButton.setIconSize(QtCore.QSize(40, 40))
        self.fanOffButton.setCheckable(False)
        self.fanOffButton.setAutoDefault(False)
        self.fanOffButton.setDefault(False)
        self.fanOffButton.setFlat(False)
        self.fanOffButton.setObjectName(_fromUtf8("fanOffButton"))
        self.fanOnButton = QtGui.QPushButton(self.temperatureTab)
        self.fanOnButton.setGeometry(QtCore.QRect(220, 0, 81, 90))
        self.fanOnButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.fanOnButton.setFont(font)
        self.fanOnButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.fanOnButton.setText(_fromUtf8(""))
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/fan-black-silhouette.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fanOnButton.setIcon(icon26)
        self.fanOnButton.setIconSize(QtCore.QSize(40, 40))
        self.fanOnButton.setCheckable(False)
        self.fanOnButton.setAutoDefault(False)
        self.fanOnButton.setDefault(False)
        self.fanOnButton.setFlat(False)
        self.fanOnButton.setObjectName(_fromUtf8("fanOnButton"))
        self.toolTempSpinBox = QtGui.QSpinBox(self.temperatureTab)
        self.toolTempSpinBox.setGeometry(QtCore.QRect(229, 160, 161, 131))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(20)
        self.toolTempSpinBox.setFont(font)
        self.toolTempSpinBox.setStyleSheet(_fromUtf8("QSpinBox {\n"
"    padding-right: 5px; /* make room for the arrows */\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"   \n"
"}\n"
"QSpinBox ::text:selected {\n"
"    background-color: rgb(255, 146, 57);\n"
"   \n"
"}\n"
"QSpinBox::up-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"border-top-left-radius: 15px;\n"
"\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox::up-arrow { \n"
"image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px; }\n"
"\n"
"\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"border-bottom-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"\n"
"}\n"
"\n"
""))
        self.toolTempSpinBox.setReadOnly(False)
        self.toolTempSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.toolTempSpinBox.setAccelerated(True)
        self.toolTempSpinBox.setMaximum(300)
        self.toolTempSpinBox.setSingleStep(1)
        self.toolTempSpinBox.setProperty("value", 0)
        self.toolTempSpinBox.setObjectName(_fromUtf8("toolTempSpinBox"))
        self.bedTempSpinBox = QtGui.QSpinBox(self.temperatureTab)
        self.bedTempSpinBox.setGeometry(QtCore.QRect(237, 363, 161, 131))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(20)
        self.bedTempSpinBox.setFont(font)
        self.bedTempSpinBox.setStyleSheet(_fromUtf8("QSpinBox {\n"
"    padding-right: 5px; /* make room for the arrows */\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"   \n"
"}\n"
"QSpinBox ::text:selected {\n"
"    background-color: rgb(255, 146, 57);\n"
"   \n"
"}\n"
"QSpinBox::up-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"border-top-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox::up-arrow { image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px; }\n"
"\n"
"\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"border-bottom-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"\n"
"}\n"
"\n"
""))
        self.bedTempSpinBox.setReadOnly(False)
        self.bedTempSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.bedTempSpinBox.setAccelerated(True)
        self.bedTempSpinBox.setMaximum(130)
        self.bedTempSpinBox.setSingleStep(1)
        self.bedTempSpinBox.setProperty("value", 0)
        self.bedTempSpinBox.setObjectName(_fromUtf8("bedTempSpinBox"))
        self.setToolTempButton = QtGui.QPushButton(self.temperatureTab)
        self.setToolTempButton.setGeometry(QtCore.QRect(388, 160, 71, 130))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.setToolTempButton.setFont(font)
        self.setToolTempButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-right-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.setToolTempButton.setText(_fromUtf8(""))
        self.setToolTempButton.setIcon(icon16)
        self.setToolTempButton.setIconSize(QtCore.QSize(50, 50))
        self.setToolTempButton.setObjectName(_fromUtf8("setToolTempButton"))
        self.setBedTempButton = QtGui.QPushButton(self.temperatureTab)
        self.setBedTempButton.setGeometry(QtCore.QRect(396, 365, 71, 127))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.setBedTempButton.setFont(font)
        self.setBedTempButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.setBedTempButton.setText(_fromUtf8(""))
        self.setBedTempButton.setIcon(icon16)
        self.setBedTempButton.setIconSize(QtCore.QSize(50, 50))
        self.setBedTempButton.setObjectName(_fromUtf8("setBedTempButton"))
        self.toolToggleTemperatureButton = QtGui.QPushButton(self.temperatureTab)
        self.toolToggleTemperatureButton.setGeometry(QtCore.QRect(10, 143, 105, 169))
        self.toolToggleTemperatureButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.toolToggleTemperatureButton.setFont(font)
        self.toolToggleTemperatureButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
" border-radius:15px;\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.toolToggleTemperatureButton.setText(_fromUtf8(""))
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/NozzleSelect_0.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon27.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/NozzleSelect_1.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolToggleTemperatureButton.setIcon(icon27)
        self.toolToggleTemperatureButton.setIconSize(QtCore.QSize(90, 90))
        self.toolToggleTemperatureButton.setCheckable(True)
        self.toolToggleTemperatureButton.setChecked(False)
        self.toolToggleTemperatureButton.setAutoDefault(False)
        self.toolToggleTemperatureButton.setDefault(False)
        self.toolToggleTemperatureButton.setFlat(False)
        self.toolToggleTemperatureButton.setObjectName(_fromUtf8("toolToggleTemperatureButton"))
        self.tool250PreheatButton = QtGui.QPushButton(self.temperatureTab)
        self.tool250PreheatButton.setGeometry(QtCore.QRect(130, 247, 90, 62))
        self.tool250PreheatButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.tool250PreheatButton.setFont(font)
        self.tool250PreheatButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-bottom-right-radius: 15px;\n"
"border-bottom-left-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.tool250PreheatButton.setIconSize(QtCore.QSize(40, 40))
        self.tool250PreheatButton.setCheckable(False)
        self.tool250PreheatButton.setAutoDefault(False)
        self.tool250PreheatButton.setDefault(False)
        self.tool250PreheatButton.setFlat(False)
        self.tool250PreheatButton.setObjectName(_fromUtf8("tool250PreheatButton"))
        self.tool180PreheatButton = QtGui.QPushButton(self.temperatureTab)
        self.tool180PreheatButton.setGeometry(QtCore.QRect(130, 145, 90, 55))
        self.tool180PreheatButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.tool180PreheatButton.setFont(font)
        self.tool180PreheatButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-top-right-radius: 15px;\n"
"border-top-left-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.tool180PreheatButton.setIconSize(QtCore.QSize(40, 40))
        self.tool180PreheatButton.setCheckable(False)
        self.tool180PreheatButton.setAutoDefault(False)
        self.tool180PreheatButton.setDefault(False)
        self.tool180PreheatButton.setFlat(False)
        self.tool180PreheatButton.setObjectName(_fromUtf8("tool180PreheatButton"))
        self.tool220PreheatButton = QtGui.QPushButton(self.temperatureTab)
        self.tool220PreheatButton.setGeometry(QtCore.QRect(130, 195, 90, 55))
        self.tool220PreheatButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.tool220PreheatButton.setFont(font)
        self.tool220PreheatButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.tool220PreheatButton.setIconSize(QtCore.QSize(40, 40))
        self.tool220PreheatButton.setCheckable(False)
        self.tool220PreheatButton.setAutoDefault(False)
        self.tool220PreheatButton.setDefault(False)
        self.tool220PreheatButton.setFlat(False)
        self.tool220PreheatButton.setObjectName(_fromUtf8("tool220PreheatButton"))
        self.bed60PreheatButton = QtGui.QPushButton(self.temperatureTab)
        self.bed60PreheatButton.setGeometry(QtCore.QRect(130, 370, 90, 62))
        self.bed60PreheatButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.bed60PreheatButton.setFont(font)
        self.bed60PreheatButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-top-right-radius: 15px;\n"
"border-top-left-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.bed60PreheatButton.setIconSize(QtCore.QSize(40, 40))
        self.bed60PreheatButton.setCheckable(False)
        self.bed60PreheatButton.setAutoDefault(False)
        self.bed60PreheatButton.setDefault(False)
        self.bed60PreheatButton.setFlat(False)
        self.bed60PreheatButton.setObjectName(_fromUtf8("bed60PreheatButton"))
        self.bed100PreheatButton = QtGui.QPushButton(self.temperatureTab)
        self.bed100PreheatButton.setGeometry(QtCore.QRect(130, 431, 90, 64))
        self.bed100PreheatButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.bed100PreheatButton.setFont(font)
        self.bed100PreheatButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-bottom-right-radius: 15px;\n"
"border-bottom-left-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.bed100PreheatButton.setIconSize(QtCore.QSize(40, 40))
        self.bed100PreheatButton.setCheckable(False)
        self.bed100PreheatButton.setAutoDefault(False)
        self.bed100PreheatButton.setDefault(False)
        self.bed100PreheatButton.setFlat(False)
        self.bed100PreheatButton.setObjectName(_fromUtf8("bed100PreheatButton"))
        self.chamber70PreheatButton = QtGui.QPushButton(self.temperatureTab)
        self.chamber70PreheatButton.setGeometry(QtCore.QRect(130, 620, 90, 64))
        self.chamber70PreheatButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.chamber70PreheatButton.setFont(font)
        self.chamber70PreheatButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-bottom-right-radius: 15px;\n"
"border-bottom-left-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.chamber70PreheatButton.setIconSize(QtCore.QSize(40, 40))
        self.chamber70PreheatButton.setCheckable(False)
        self.chamber70PreheatButton.setAutoDefault(False)
        self.chamber70PreheatButton.setDefault(False)
        self.chamber70PreheatButton.setFlat(False)
        self.chamber70PreheatButton.setObjectName(_fromUtf8("chamber70PreheatButton"))
        self.chamberTempSpinBox = QtGui.QSpinBox(self.temperatureTab)
        self.chamberTempSpinBox.setGeometry(QtCore.QRect(231, 558, 161, 131))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(20)
        self.chamberTempSpinBox.setFont(font)
        self.chamberTempSpinBox.setStyleSheet(_fromUtf8("QSpinBox {\n"
"    padding-right: 5px; /* make room for the arrows */\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"   \n"
"}\n"
"QSpinBox ::text:selected {\n"
"    background-color: rgb(255, 146, 57);\n"
"   \n"
"}\n"
"QSpinBox::up-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"border-top-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox::up-arrow { image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px; }\n"
"\n"
"\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"border-bottom-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"\n"
"}\n"
"\n"
""))
        self.chamberTempSpinBox.setReadOnly(False)
        self.chamberTempSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.chamberTempSpinBox.setAccelerated(True)
        self.chamberTempSpinBox.setMaximum(90)
        self.chamberTempSpinBox.setSingleStep(1)
        self.chamberTempSpinBox.setProperty("value", 0)
        self.chamberTempSpinBox.setObjectName(_fromUtf8("chamberTempSpinBox"))
        self.setChamberTempButton = QtGui.QPushButton(self.temperatureTab)
        self.setChamberTempButton.setGeometry(QtCore.QRect(390, 560, 71, 127))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.setChamberTempButton.setFont(font)
        self.setChamberTempButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.setChamberTempButton.setText(_fromUtf8(""))
        self.setChamberTempButton.setIcon(icon16)
        self.setChamberTempButton.setIconSize(QtCore.QSize(50, 50))
        self.setChamberTempButton.setObjectName(_fromUtf8("setChamberTempButton"))
        self.chamber40PreheatButton = QtGui.QPushButton(self.temperatureTab)
        self.chamber40PreheatButton.setGeometry(QtCore.QRect(130, 559, 90, 62))
        self.chamber40PreheatButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.chamber40PreheatButton.setFont(font)
        self.chamber40PreheatButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-top-right-radius: 15px;\n"
"border-top-left-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.chamber40PreheatButton.setIconSize(QtCore.QSize(40, 40))
        self.chamber40PreheatButton.setCheckable(False)
        self.chamber40PreheatButton.setAutoDefault(False)
        self.chamber40PreheatButton.setDefault(False)
        self.chamber40PreheatButton.setFlat(False)
        self.chamber40PreheatButton.setObjectName(_fromUtf8("chamber40PreheatButton"))
        self.bedLabel_4 = QtGui.QLabel(self.temperatureTab)
        self.bedLabel_4.setGeometry(QtCore.QRect(9, 530, 124, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.bedLabel_4.setFont(font)
        self.bedLabel_4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.bedLabel_4.setObjectName(_fromUtf8("bedLabel_4"))
        self.chamberLabel_2 = QtGui.QLabel(self.temperatureTab)
        self.chamberLabel_2.setGeometry(QtCore.QRect(10, 600, 80, 80))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.chamberLabel_2.setFont(font)
        self.chamberLabel_2.setStyleSheet(_fromUtf8("\n"
"   color:  white;\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.chamberLabel_2.setText(_fromUtf8(""))
        self.chamberLabel_2.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/chamberHeatIcon.png")))
        self.chamberLabel_2.setScaledContents(True)
        self.chamberLabel_2.setObjectName(_fromUtf8("chamberLabel_2"))
        self.bedLabel_3 = QtGui.QLabel(self.temperatureTab)
        self.bedLabel_3.setGeometry(QtCore.QRect(10, 400, 80, 80))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.bedLabel_3.setFont(font)
        self.bedLabel_3.setStyleSheet(_fromUtf8("\n"
"   color:  white;\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.bedLabel_3.setText(_fromUtf8(""))
        self.bedLabel_3.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/bed.png")))
        self.bedLabel_3.setScaledContents(True)
        self.bedLabel_3.setObjectName(_fromUtf8("bedLabel_3"))
        self.line = QtGui.QFrame(self.temperatureTab)
        self.line.setGeometry(QtCore.QRect(12, 320, 455, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.temperatureTab)
        self.line_2.setGeometry(QtCore.QRect(11, 510, 455, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.temperatureTab)
        self.line_3.setGeometry(QtCore.QRect(0, 721, 480, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.toolLabel.raise_()
        self.bedLabel_2.raise_()
        self.cooldownButton.raise_()
        self.fanOffButton.raise_()
        self.fanOnButton.raise_()
        self.setToolTempButton.raise_()
        self.setBedTempButton.raise_()
        self.bedTempSpinBox.raise_()
        self.toolTempSpinBox.raise_()
        self.toolToggleTemperatureButton.raise_()
        self.tool250PreheatButton.raise_()
        self.tool180PreheatButton.raise_()
        self.tool220PreheatButton.raise_()
        self.bed60PreheatButton.raise_()
        self.bed100PreheatButton.raise_()
        self.chamber70PreheatButton.raise_()
        self.chamberTempSpinBox.raise_()
        self.setChamberTempButton.raise_()
        self.chamber40PreheatButton.raise_()
        self.bedLabel_4.raise_()
        self.chamberLabel_2.raise_()
        self.bedLabel_3.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/thermometer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon28.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/thermometer_Selected.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.controlTabWidget.addTab(self.temperatureTab, icon28, _fromUtf8(""))
        self.motionTab = QtGui.QWidget()
        self.motionTab.setObjectName(_fromUtf8("motionTab"))
        self.step1Button = QtGui.QPushButton(self.motionTab)
        self.step1Button.setGeometry(QtCore.QRect(92, -10, 100, 70))
        self.step1Button.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.step1Button.setFont(font)
        self.step1Button.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"     border-bottom: none; /* no border for a flat push button */\n"
"border-bottom-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border-bottom: none; /* no border for a flat push button */\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.step1Button.setIconSize(QtCore.QSize(40, 40))
        self.step1Button.setCheckable(False)
        self.step1Button.setAutoDefault(False)
        self.step1Button.setDefault(False)
        self.step1Button.setFlat(False)
        self.step1Button.setObjectName(_fromUtf8("step1Button"))
        self.step10Button = QtGui.QPushButton(self.motionTab)
        self.step10Button.setGeometry(QtCore.QRect(191, -10, 100, 70))
        self.step10Button.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.step10Button.setFont(font)
        self.step10Button.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"     border-bottom: none; /* no border for a flat push button */\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border-bottom: none; /* no border for a flat push button */\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.step10Button.setIconSize(QtCore.QSize(40, 40))
        self.step10Button.setCheckable(False)
        self.step10Button.setAutoDefault(False)
        self.step10Button.setDefault(False)
        self.step10Button.setFlat(False)
        self.step10Button.setObjectName(_fromUtf8("step10Button"))
        self.step100Button = QtGui.QPushButton(self.motionTab)
        self.step100Button.setGeometry(QtCore.QRect(290, -10, 101, 70))
        self.step100Button.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.step100Button.setFont(font)
        self.step100Button.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"     border-bottom: none; /* no border for a flat push button */\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border-bottom: none; /* no border for a flat push button */\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.step100Button.setIconSize(QtCore.QSize(40, 40))
        self.step100Button.setCheckable(True)
        self.step100Button.setChecked(False)
        self.step100Button.setAutoDefault(False)
        self.step100Button.setDefault(False)
        self.step100Button.setFlat(False)
        self.step100Button.setObjectName(_fromUtf8("step100Button"))
        self.moveYPButton = QtGui.QPushButton(self.motionTab)
        self.moveYPButton.setGeometry(QtCore.QRect(195, 386, 105, 105))
        self.moveYPButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.moveYPButton.setFont(font)
        self.moveYPButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.moveYPButton.setText(_fromUtf8(""))
        self.moveYPButton.setIcon(icon18)
        self.moveYPButton.setIconSize(QtCore.QSize(40, 40))
        self.moveYPButton.setCheckable(False)
        self.moveYPButton.setAutoDefault(False)
        self.moveYPButton.setDefault(False)
        self.moveYPButton.setFlat(False)
        self.moveYPButton.setObjectName(_fromUtf8("moveYPButton"))
        self.moveYMButton = QtGui.QPushButton(self.motionTab)
        self.moveYMButton.setGeometry(QtCore.QRect(195, 592, 105, 105))
        self.moveYMButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.moveYMButton.setFont(font)
        self.moveYMButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-bottom-left-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.moveYMButton.setText(_fromUtf8(""))
        self.moveYMButton.setIcon(icon17)
        self.moveYMButton.setIconSize(QtCore.QSize(40, 40))
        self.moveYMButton.setCheckable(False)
        self.moveYMButton.setAutoDefault(False)
        self.moveYMButton.setDefault(False)
        self.moveYMButton.setFlat(False)
        self.moveYMButton.setObjectName(_fromUtf8("moveYMButton"))
        self.moveXPButton = QtGui.QPushButton(self.motionTab)
        self.moveXPButton.setGeometry(QtCore.QRect(298, 490, 105, 105))
        self.moveXPButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.moveXPButton.setFont(font)
        self.moveXPButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.moveXPButton.setText(_fromUtf8(""))
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/arrows-2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.moveXPButton.setIcon(icon29)
        self.moveXPButton.setIconSize(QtCore.QSize(40, 40))
        self.moveXPButton.setCheckable(False)
        self.moveXPButton.setAutoDefault(False)
        self.moveXPButton.setDefault(False)
        self.moveXPButton.setFlat(False)
        self.moveXPButton.setObjectName(_fromUtf8("moveXPButton"))
        self.moveXMButton = QtGui.QPushButton(self.motionTab)
        self.moveXMButton.setGeometry(QtCore.QRect(91, 489, 105, 105))
        self.moveXMButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.moveXMButton.setFont(font)
        self.moveXMButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-top-left-radius: 15px;\n"
"    border-bottom-left-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.moveXMButton.setText(_fromUtf8(""))
        self.moveXMButton.setIcon(icon5)
        self.moveXMButton.setIconSize(QtCore.QSize(40, 40))
        self.moveXMButton.setCheckable(False)
        self.moveXMButton.setAutoDefault(False)
        self.moveXMButton.setDefault(False)
        self.moveXMButton.setFlat(False)
        self.moveXMButton.setObjectName(_fromUtf8("moveXMButton"))
        self.homeXYButton = QtGui.QPushButton(self.motionTab)
        self.homeXYButton.setGeometry(QtCore.QRect(195, 489, 105, 105))
        self.homeXYButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.homeXYButton.setFont(font)
        self.homeXYButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.homeXYButton.setText(_fromUtf8(""))
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/home-icon-silhouette.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeXYButton.setIcon(icon30)
        self.homeXYButton.setIconSize(QtCore.QSize(40, 40))
        self.homeXYButton.setCheckable(False)
        self.homeXYButton.setAutoDefault(False)
        self.homeXYButton.setDefault(False)
        self.homeXYButton.setFlat(False)
        self.homeXYButton.setObjectName(_fromUtf8("homeXYButton"))
        self.homeZButton = QtGui.QPushButton(self.motionTab)
        self.homeZButton.setGeometry(QtCore.QRect(56, 180, 100, 100))
        self.homeZButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.homeZButton.setFont(font)
        self.homeZButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.homeZButton.setText(_fromUtf8(""))
        self.homeZButton.setIcon(icon30)
        self.homeZButton.setIconSize(QtCore.QSize(40, 40))
        self.homeZButton.setCheckable(False)
        self.homeZButton.setAutoDefault(False)
        self.homeZButton.setDefault(False)
        self.homeZButton.setFlat(False)
        self.homeZButton.setObjectName(_fromUtf8("homeZButton"))
        self.motorOffButton = QtGui.QPushButton(self.motionTab)
        self.motorOffButton.setGeometry(QtCore.QRect(390, -10, 90, 70))
        self.motorOffButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.motorOffButton.setFont(font)
        self.motorOffButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"     border-bottom: none; /* no border for a flat push button */\n"
" border-bottom-right-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.motorOffButton.setText(_fromUtf8(""))
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/motor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.motorOffButton.setIcon(icon31)
        self.motorOffButton.setIconSize(QtCore.QSize(40, 40))
        self.motorOffButton.setCheckable(False)
        self.motorOffButton.setAutoDefault(False)
        self.motorOffButton.setDefault(False)
        self.motorOffButton.setFlat(False)
        self.motorOffButton.setObjectName(_fromUtf8("motorOffButton"))
        self.moveZMButton = QtGui.QPushButton(self.motionTab)
        self.moveZMButton.setGeometry(QtCore.QRect(56, 81, 100, 100))
        self.moveZMButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.moveZMButton.setFont(font)
        self.moveZMButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.moveZMButton.setText(_fromUtf8(""))
        self.moveZMButton.setIcon(icon18)
        self.moveZMButton.setIconSize(QtCore.QSize(40, 40))
        self.moveZMButton.setCheckable(False)
        self.moveZMButton.setAutoDefault(False)
        self.moveZMButton.setDefault(False)
        self.moveZMButton.setFlat(False)
        self.moveZMButton.setObjectName(_fromUtf8("moveZMButton"))
        self.moveZPButton = QtGui.QPushButton(self.motionTab)
        self.moveZPButton.setGeometry(QtCore.QRect(56, 278, 100, 100))
        self.moveZPButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.moveZPButton.setFont(font)
        self.moveZPButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-bottom-left-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.moveZPButton.setText(_fromUtf8(""))
        self.moveZPButton.setIcon(icon17)
        self.moveZPButton.setIconSize(QtCore.QSize(40, 40))
        self.moveZPButton.setCheckable(False)
        self.moveZPButton.setAutoDefault(False)
        self.moveZPButton.setDefault(False)
        self.moveZPButton.setFlat(False)
        self.moveZPButton.setObjectName(_fromUtf8("moveZPButton"))
        self.XYLabel = QtGui.QLabel(self.motionTab)
        self.XYLabel.setGeometry(QtCore.QRect(35, 421, 70, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.XYLabel.setFont(font)
        self.XYLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.XYLabel.setObjectName(_fromUtf8("XYLabel"))
        self.ZLabel = QtGui.QLabel(self.motionTab)
        self.ZLabel.setGeometry(QtCore.QRect(20, 60, 31, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ZLabel.setFont(font)
        self.ZLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.ZLabel.setObjectName(_fromUtf8("ZLabel"))
        self.retractButton = QtGui.QPushButton(self.motionTab)
        self.retractButton.setGeometry(QtCore.QRect(351, 270, 100, 100))
        self.retractButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.retractButton.setFont(font)
        self.retractButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-bottom-left-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.retractButton.setText(_fromUtf8(""))
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.retractButton.setIcon(icon32)
        self.retractButton.setIconSize(QtCore.QSize(40, 40))
        self.retractButton.setCheckable(False)
        self.retractButton.setAutoDefault(False)
        self.retractButton.setDefault(False)
        self.retractButton.setFlat(False)
        self.retractButton.setObjectName(_fromUtf8("retractButton"))
        self.extruderButton = QtGui.QPushButton(self.motionTab)
        self.extruderButton.setGeometry(QtCore.QRect(351, 173, 100, 100))
        self.extruderButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.extruderButton.setFont(font)
        self.extruderButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.extruderButton.setText(_fromUtf8(""))
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.extruderButton.setIcon(icon33)
        self.extruderButton.setIconSize(QtCore.QSize(40, 40))
        self.extruderButton.setCheckable(False)
        self.extruderButton.setAutoDefault(False)
        self.extruderButton.setDefault(False)
        self.extruderButton.setFlat(False)
        self.extruderButton.setObjectName(_fromUtf8("extruderButton"))
        self.ELabel = QtGui.QLabel(self.motionTab)
        self.ELabel.setGeometry(QtCore.QRect(300, 78, 31, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ELabel.setFont(font)
        self.ELabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.ELabel.setObjectName(_fromUtf8("ELabel"))
        self.moveByLabel = QtGui.QLabel(self.motionTab)
        self.moveByLabel.setGeometry(QtCore.QRect(0, 0, 111, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.moveByLabel.setFont(font)
        self.moveByLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.moveByLabel.setObjectName(_fromUtf8("moveByLabel"))
        self.toolToggleMotionButton = QtGui.QPushButton(self.motionTab)
        self.toolToggleMotionButton.setGeometry(QtCore.QRect(351, 75, 100, 100))
        self.toolToggleMotionButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.toolToggleMotionButton.setFont(font)
        self.toolToggleMotionButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
" border-top-right-radius:15px;\n"
" border-top-left-radius:15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        icon34 = QtGui.QIcon()
        icon34.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/NozzleSelect.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolToggleMotionButton.setIcon(icon34)
        self.toolToggleMotionButton.setIconSize(QtCore.QSize(30, 30))
        self.toolToggleMotionButton.setCheckable(True)
        self.toolToggleMotionButton.setChecked(False)
        self.toolToggleMotionButton.setAutoDefault(False)
        self.toolToggleMotionButton.setDefault(False)
        self.toolToggleMotionButton.setFlat(False)
        self.toolToggleMotionButton.setObjectName(_fromUtf8("toolToggleMotionButton"))
        self.line_5 = QtGui.QFrame(self.motionTab)
        self.line_5.setGeometry(QtCore.QRect(120, 721, 480, 16))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.moveByLabel.raise_()
        self.step1Button.raise_()
        self.step10Button.raise_()
        self.step100Button.raise_()
        self.moveYPButton.raise_()
        self.moveYMButton.raise_()
        self.moveXPButton.raise_()
        self.moveXMButton.raise_()
        self.homeXYButton.raise_()
        self.homeZButton.raise_()
        self.motorOffButton.raise_()
        self.moveZMButton.raise_()
        self.moveZPButton.raise_()
        self.XYLabel.raise_()
        self.ZLabel.raise_()
        self.retractButton.raise_()
        self.extruderButton.raise_()
        self.ELabel.raise_()
        self.toolToggleMotionButton.raise_()
        self.line_5.raise_()
        icon35 = QtGui.QIcon()
        icon35.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/Motion.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon35.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/Motion_Selected.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.controlTabWidget.addTab(self.motionTab, icon35, _fromUtf8(""))
        self.filamentTab = QtGui.QWidget()
        self.filamentTab.setObjectName(_fromUtf8("filamentTab"))
        self.setFlowRateButton = QtGui.QPushButton(self.filamentTab)
        self.setFlowRateButton.setGeometry(QtCore.QRect(298, 202, 91, 132))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.setFlowRateButton.setFont(font)
        self.setFlowRateButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.setFlowRateButton.setText(_fromUtf8(""))
        self.setFlowRateButton.setIcon(icon16)
        self.setFlowRateButton.setIconSize(QtCore.QSize(50, 50))
        self.setFlowRateButton.setObjectName(_fromUtf8("setFlowRateButton"))
        self.flowRateSpinBox = QtGui.QSpinBox(self.filamentTab)
        self.flowRateSpinBox.setGeometry(QtCore.QRect(60, 200, 241, 136))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(24)
        self.flowRateSpinBox.setFont(font)
        self.flowRateSpinBox.setStyleSheet(_fromUtf8("QSpinBox {\n"
"    padding-right: 5px; /* make room for the arrows */\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"   \n"
"}\n"
"QSpinBox ::text:selected {\n"
"    background-color: rgb(255, 146, 57);\n"
"   \n"
"}\n"
"QSpinBox::up-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"border-top-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox::up-arrow { image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px; }\n"
"\n"
"\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"border-bottom-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"\n"
"}\n"
"\n"
""))
        self.flowRateSpinBox.setFrame(False)
        self.flowRateSpinBox.setReadOnly(False)
        self.flowRateSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.flowRateSpinBox.setAccelerated(True)
        self.flowRateSpinBox.setMinimum(75)
        self.flowRateSpinBox.setMaximum(125)
        self.flowRateSpinBox.setSingleStep(1)
        self.flowRateSpinBox.setProperty("value", 100)
        self.flowRateSpinBox.setObjectName(_fromUtf8("flowRateSpinBox"))
        self.flowRateLabelControlPage = QtGui.QLabel(self.filamentTab)
        self.flowRateLabelControlPage.setGeometry(QtCore.QRect(40, 210, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.flowRateLabelControlPage.setFont(font)
        self.flowRateLabelControlPage.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.flowRateLabelControlPage.setObjectName(_fromUtf8("flowRateLabelControlPage"))
        self.changeFilamentButton = QtGui.QToolButton(self.filamentTab)
        self.changeFilamentButton.setGeometry(QtCore.QRect(0, 0, 240, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(12)
        self.changeFilamentButton.setFont(font)
        self.changeFilamentButton.setStyleSheet(_fromUtf8("QToolButton  {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QToolButton :pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton :flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton :default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QToolButton :focus {\n"
"    outline: none;\n"
"}"))
        icon36 = QtGui.QIcon()
        icon36.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/changeFilament.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.changeFilamentButton.setIcon(icon36)
        self.changeFilamentButton.setIconSize(QtCore.QSize(60, 60))
        self.changeFilamentButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.changeFilamentButton.setObjectName(_fromUtf8("changeFilamentButton"))
        self.toggleFilamentSensorButton = QtGui.QToolButton(self.filamentTab)
        self.toggleFilamentSensorButton.setEnabled(True)
        self.toggleFilamentSensorButton.setGeometry(QtCore.QRect(240, 0, 240, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(12)
        self.toggleFilamentSensorButton.setFont(font)
        self.toggleFilamentSensorButton.setStyleSheet(_fromUtf8("QToolButton  {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QToolButton :pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"    /* #dadbde #f6f7fa */\n"
"}\n"
"\n"
"\n"
"QToolButton :flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton :default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QToolButton :focus {\n"
"    outline: none;\n"
"}"))
        icon37 = QtGui.QIcon()
        icon37.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/filamentSensorOn.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toggleFilamentSensorButton.setIcon(icon37)
        self.toggleFilamentSensorButton.setIconSize(QtCore.QSize(60, 60))
        self.toggleFilamentSensorButton.setCheckable(False)
        self.toggleFilamentSensorButton.setChecked(False)
        self.toggleFilamentSensorButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toggleFilamentSensorButton.setObjectName(_fromUtf8("toggleFilamentSensorButton"))
        self.line_6 = QtGui.QFrame(self.filamentTab)
        self.line_6.setGeometry(QtCore.QRect(70, 721, 480, 16))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.flowRateSpinBox.raise_()
        self.setFlowRateButton.raise_()
        self.flowRateLabelControlPage.raise_()
        self.changeFilamentButton.raise_()
        self.toggleFilamentSensorButton.raise_()
        self.line_6.raise_()
        icon38 = QtGui.QIcon()
        icon38.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/Spool.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon38.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/Spool_Selected.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon38.addPixmap(QtGui.QPixmap(_fromUtf8("png/Spool.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon38.addPixmap(QtGui.QPixmap(_fromUtf8("png/Spool_Selected.png")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        icon38.addPixmap(QtGui.QPixmap(_fromUtf8("png/Spool_Selected.png")), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.controlTabWidget.addTab(self.filamentTab, icon38, _fromUtf8(""))
        self.controlBackButton = QtGui.QPushButton(self.controlPage)
        self.controlBackButton.setGeometry(QtCore.QRect(380, 730, 100, 70))
        self.controlBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.controlBackButton.setFont(font)
        self.controlBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"    border: none; /* no border for a flat push button */\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    /*border-bottom-right-radius: 15px;*/\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        self.controlBackButton.setText(_fromUtf8(""))
        self.controlBackButton.setIcon(icon5)
        self.controlBackButton.setIconSize(QtCore.QSize(40, 40))
        self.controlBackButton.setCheckable(False)
        self.controlBackButton.setAutoDefault(False)
        self.controlBackButton.setDefault(False)
        self.controlBackButton.setFlat(False)
        self.controlBackButton.setObjectName(_fromUtf8("controlBackButton"))
        self.stackedWidget.addWidget(self.controlPage)
        self.changeFilamentPage = QtGui.QWidget()
        self.changeFilamentPage.setObjectName(_fromUtf8("changeFilamentPage"))
        self.selectFilamentlabel = QtGui.QLabel(self.changeFilamentPage)
        self.selectFilamentlabel.setGeometry(QtCore.QRect(0, 0, 381, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.selectFilamentlabel.setFont(font)
        self.selectFilamentlabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.selectFilamentlabel.setObjectName(_fromUtf8("selectFilamentlabel"))
        self.changeFilamentComboBox = QtGui.QComboBox(self.changeFilamentPage)
        self.changeFilamentComboBox.setGeometry(QtCore.QRect(0, 40, 481, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(24)
        self.changeFilamentComboBox.setFont(font)
        self.changeFilamentComboBox.setStyleSheet(_fromUtf8(" QScrollBar:vertical {\n"
"     border: 1px solid black;\n"
"border-radius: 5px;\n"
"    background-color: rgb(40,40,40);\n"
"     width: 60px;\n"
"     margin: 67px 0 67px 0;\n"
" }\n"
"\n"
"/* Sets up the color and height of handle */\n"
"QScrollBar::handle:vertical {\n"
"border-radius: 5px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"min-height: 7px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"     border: 1px solid black;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     height:65px;\n"
"border-radius: 5px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"     border: 1px solid black;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     height: 65px;\n"
"border-radius: 5px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
" image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
" padding: 5px;\n"
" }\n"
"QScrollBar::down-arrow:vertical {\n"
" image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
" padding: 5px;\n"
" }\n"
"\n"
"/* need this to get rid of crosshatching on scrollbar background */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"background: none;\n"
"}\n"
"\n"
"QComboBox {\n"
"border: 1px solid black;\n"
"    padding: 0px 18px 0px 3px;\n"
"    min-width: 6em;\n"
"\n"
"}\n"
"\n"
"QComboBox::item {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"background: white;\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"background: white;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"border-left: 1px solid black;\n"
"border-right: 1px solid black;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 50px;\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"\n"
"image: url(./templates/img/arrows-5.png);\n"
"width: 30px;\n"
"height: 30px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(40, 40, 40);\n"
"    background: white;\n"
"}"))
        self.changeFilamentComboBox.setEditable(False)
        self.changeFilamentComboBox.setMaxVisibleItems(8)
        self.changeFilamentComboBox.setIconSize(QtCore.QSize(30, 30))
        self.changeFilamentComboBox.setObjectName(_fromUtf8("changeFilamentComboBox"))
        self.changeFilamentLoadButton = QtGui.QPushButton(self.changeFilamentPage)
        self.changeFilamentLoadButton.setGeometry(QtCore.QRect(0, 170, 481, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(20)
        self.changeFilamentLoadButton.setFont(font)
        self.changeFilamentLoadButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        icon39 = QtGui.QIcon()
        icon39.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/load.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.changeFilamentLoadButton.setIcon(icon39)
        self.changeFilamentLoadButton.setIconSize(QtCore.QSize(60, 60))
        self.changeFilamentLoadButton.setObjectName(_fromUtf8("changeFilamentLoadButton"))
        self.toolToggleChangeFilamentButton = QtGui.QPushButton(self.changeFilamentPage)
        self.toolToggleChangeFilamentButton.setGeometry(QtCore.QRect(0, 90, 480, 81))
        self.toolToggleChangeFilamentButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(30)
        self.toolToggleChangeFilamentButton.setFont(font)
        self.toolToggleChangeFilamentButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.toolToggleChangeFilamentButton.setText(_fromUtf8(""))
        self.toolToggleChangeFilamentButton.setIcon(icon27)
        self.toolToggleChangeFilamentButton.setIconSize(QtCore.QSize(120, 50))
        self.toolToggleChangeFilamentButton.setCheckable(True)
        self.toolToggleChangeFilamentButton.setChecked(False)
        self.toolToggleChangeFilamentButton.setAutoDefault(False)
        self.toolToggleChangeFilamentButton.setDefault(False)
        self.toolToggleChangeFilamentButton.setFlat(False)
        self.toolToggleChangeFilamentButton.setObjectName(_fromUtf8("toolToggleChangeFilamentButton"))
        self.changeFilamentUnloadButton = QtGui.QPushButton(self.changeFilamentPage)
        self.changeFilamentUnloadButton.setGeometry(QtCore.QRect(0, 260, 483, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(20)
        self.changeFilamentUnloadButton.setFont(font)
        self.changeFilamentUnloadButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        icon40 = QtGui.QIcon()
        icon40.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/unload.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.changeFilamentUnloadButton.setIcon(icon40)
        self.changeFilamentUnloadButton.setIconSize(QtCore.QSize(60, 60))
        self.changeFilamentUnloadButton.setObjectName(_fromUtf8("changeFilamentUnloadButton"))
        self.changeFilamentBackButton = QtGui.QPushButton(self.changeFilamentPage)
        self.changeFilamentBackButton.setGeometry(QtCore.QRect(0, 707, 480, 94))
        self.changeFilamentBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.changeFilamentBackButton.setFont(font)
        self.changeFilamentBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.changeFilamentBackButton.setText(_fromUtf8(""))
        self.changeFilamentBackButton.setIcon(icon5)
        self.changeFilamentBackButton.setIconSize(QtCore.QSize(50, 50))
        self.changeFilamentBackButton.setCheckable(False)
        self.changeFilamentBackButton.setAutoDefault(False)
        self.changeFilamentBackButton.setDefault(False)
        self.changeFilamentBackButton.setFlat(False)
        self.changeFilamentBackButton.setObjectName(_fromUtf8("changeFilamentBackButton"))
        self.stackedWidget.addWidget(self.changeFilamentPage)
        self.changeFilamentProgressPage = QtGui.QWidget()
        self.changeFilamentProgressPage.setObjectName(_fromUtf8("changeFilamentProgressPage"))
        self.changeFilamentStatus = QtGui.QLabel(self.changeFilamentProgressPage)
        self.changeFilamentStatus.setGeometry(QtCore.QRect(0, 640, 471, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.changeFilamentStatus.setFont(font)
        self.changeFilamentStatus.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.changeFilamentStatus.setObjectName(_fromUtf8("changeFilamentStatus"))
        self.changeFilamentProgress = QtGui.QProgressBar(self.changeFilamentProgressPage)
        self.changeFilamentProgress.setGeometry(QtCore.QRect(0, 670, 481, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.changeFilamentProgress.setFont(font)
        self.changeFilamentProgress.setStyleSheet(_fromUtf8("QProgressBar::chunk {\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.517, x2:0, y2:0.512, stop:0 rgba(255, 28, 35, 255), stop:1 rgba(255, 68, 74, 255));\n"
"border-bottom-right-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
" /*  border-bottom-left-radius: 10px;\n"
" border-bottom-right-radius: 10px;*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(180, 180, 180, 255));\n"
"}\n"
""))
        self.changeFilamentProgress.setMaximum(100)
        self.changeFilamentProgress.setProperty("value", 0)
        self.changeFilamentProgress.setAlignment(QtCore.Qt.AlignCenter)
        self.changeFilamentProgress.setTextVisible(True)
        self.changeFilamentProgress.setOrientation(QtCore.Qt.Horizontal)
        self.changeFilamentProgress.setObjectName(_fromUtf8("changeFilamentProgress"))
        self.changeFilamentNameOperation = QtGui.QLabel(self.changeFilamentProgressPage)
        self.changeFilamentNameOperation.setGeometry(QtCore.QRect(0, 0, 471, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.changeFilamentNameOperation.setFont(font)
        self.changeFilamentNameOperation.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.changeFilamentNameOperation.setObjectName(_fromUtf8("changeFilamentNameOperation"))
        self.changeFilamentBackButton2 = QtGui.QPushButton(self.changeFilamentProgressPage)
        self.changeFilamentBackButton2.setGeometry(QtCore.QRect(0, 709, 481, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.changeFilamentBackButton2.setFont(font)
        self.changeFilamentBackButton2.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.changeFilamentBackButton2.setText(_fromUtf8(""))
        self.changeFilamentBackButton2.setIcon(icon5)
        self.changeFilamentBackButton2.setIconSize(QtCore.QSize(50, 50))
        self.changeFilamentBackButton2.setObjectName(_fromUtf8("changeFilamentBackButton2"))
        self.label_2 = QtGui.QLabel(self.changeFilamentProgressPage)
        self.label_2.setGeometry(QtCore.QRect(191, 246, 100, 100))
        self.label_2.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/changeFilament2.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.stackedWidget.addWidget(self.changeFilamentProgressPage)
        self.changeFilamentExtrudePage = QtGui.QWidget()
        self.changeFilamentExtrudePage.setObjectName(_fromUtf8("changeFilamentExtrudePage"))
        self.feedFilamentlabel = QtGui.QLabel(self.changeFilamentExtrudePage)
        self.feedFilamentlabel.setGeometry(QtCore.QRect(10, 10, 461, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.feedFilamentlabel.setFont(font)
        self.feedFilamentlabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.feedFilamentlabel.setObjectName(_fromUtf8("feedFilamentlabel"))
        self.loadDoneButton = QtGui.QPushButton(self.changeFilamentExtrudePage)
        self.loadDoneButton.setGeometry(QtCore.QRect(0, 711, 480, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(16)
        self.loadDoneButton.setFont(font)
        self.loadDoneButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.loadDoneButton.setIconSize(QtCore.QSize(40, 40))
        self.loadDoneButton.setObjectName(_fromUtf8("loadDoneButton"))
        self.ExtrudeButton = QtGui.QPushButton(self.changeFilamentExtrudePage)
        self.ExtrudeButton.setGeometry(QtCore.QRect(0, 621, 480, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(16)
        self.ExtrudeButton.setFont(font)
        self.ExtrudeButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ExtrudeButton.setIconSize(QtCore.QSize(40, 40))
        self.ExtrudeButton.setObjectName(_fromUtf8("ExtrudeButton"))
        self.feedFilamentlabel_2 = QtGui.QLabel(self.changeFilamentExtrudePage)
        self.feedFilamentlabel_2.setGeometry(QtCore.QRect(10, 40, 461, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.feedFilamentlabel_2.setFont(font)
        self.feedFilamentlabel_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.feedFilamentlabel_2.setObjectName(_fromUtf8("feedFilamentlabel_2"))
        self.stackedWidget.addWidget(self.changeFilamentExtrudePage)
        self.changeFilamentRetractPage = QtGui.QWidget()
        self.changeFilamentRetractPage.setObjectName(_fromUtf8("changeFilamentRetractPage"))
        self.feedFilamentlabel_3 = QtGui.QLabel(self.changeFilamentRetractPage)
        self.feedFilamentlabel_3.setGeometry(QtCore.QRect(10, 40, 461, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.feedFilamentlabel_3.setFont(font)
        self.feedFilamentlabel_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.feedFilamentlabel_3.setObjectName(_fromUtf8("feedFilamentlabel_3"))
        self.unloadDoneButton = QtGui.QPushButton(self.changeFilamentRetractPage)
        self.unloadDoneButton.setGeometry(QtCore.QRect(0, 711, 480, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(16)
        self.unloadDoneButton.setFont(font)
        self.unloadDoneButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.unloadDoneButton.setIconSize(QtCore.QSize(40, 40))
        self.unloadDoneButton.setObjectName(_fromUtf8("unloadDoneButton"))
        self.feedFilamentlabel_4 = QtGui.QLabel(self.changeFilamentRetractPage)
        self.feedFilamentlabel_4.setGeometry(QtCore.QRect(10, 10, 461, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.feedFilamentlabel_4.setFont(font)
        self.feedFilamentlabel_4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.feedFilamentlabel_4.setObjectName(_fromUtf8("feedFilamentlabel_4"))
        self.retractFilamentButton = QtGui.QPushButton(self.changeFilamentRetractPage)
        self.retractFilamentButton.setGeometry(QtCore.QRect(0, 621, 480, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(16)
        self.retractFilamentButton.setFont(font)
        self.retractFilamentButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.retractFilamentButton.setIconSize(QtCore.QSize(40, 40))
        self.retractFilamentButton.setObjectName(_fromUtf8("retractFilamentButton"))
        self.stackedWidget.addWidget(self.changeFilamentRetractPage)
        MainWindow.setCentralWidget(self.mainApplication)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.controlTabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.FileNameLabel.setText(_translate("MainWindow", "File:", None))
        self.printTimeLabel.setText(_translate("MainWindow", "Print Time:", None))
        self.fileName.setText(_translate("MainWindow", "fileName", None))
        self.printTime.setText(_translate("MainWindow", "printTime", None))
        self.timeLeftLabel.setText(_translate("MainWindow", "Time Left:", None))
        self.bedTempBar.setFormat(_translate("MainWindow", "%v", None))
        self.tool0TargetTemperature.setText(_translate("MainWindow", "0", None))
        self.tool0TempBar.setFormat(_translate("MainWindow", "%v", None))
        self.tool0ActualTemperature.setText(_translate("MainWindow", "0", None))
        self.bedActualTemperatute.setText(_translate("MainWindow", "0", None))
        self.bedTargetTemperature.setText(_translate("MainWindow", "0", None))
        self.printProgressBar.setFormat(_translate("MainWindow", "%p%", None))
        self.timeLeft.setText(_translate("MainWindow", "timeLeft", None))
        self.printerStatus.setText(_translate("MainWindow", "STATUS", None))
        self.celciusLabel.setText(_translate("MainWindow", "°C", None))
        self.tool1TargetTemperature.setText(_translate("MainWindow", "0", None))
        self.tool1TempBar.setFormat(_translate("MainWindow", "%v", None))
        self.tool1ActualTemperature.setText(_translate("MainWindow", "0", None))
        self.celciusLabel_2.setText(_translate("MainWindow", "°C", None))
        self.celciusLabel_3.setText(_translate("MainWindow", "°C", None))
        self.chamberTempBar.setFormat(_translate("MainWindow", "%v", None))
        self.chamberActualTemperatute.setText(_translate("MainWindow", "0", None))
        self.celciusLabel_4.setText(_translate("MainWindow", "°C", None))
        self.chamberTargetTemperature.setText(_translate("MainWindow", "0", None))
        self.filboxTempBar.setFormat(_translate("MainWindow", "%v", None))
        self.filboxActualTemperatute.setText(_translate("MainWindow", "0", None))
        self.filboxTargetTemperature.setText(_translate("MainWindow", "0", None))
        self.celciusLabel_5.setText(_translate("MainWindow", "°C", None))
        self.tool0TargetTemperature_2.setText(_translate("MainWindow", "0", None))
        self.tool0TargetTemperature_3.setText(_translate("MainWindow", "1", None))
        self.doorLockButton.setText(_translate("MainWindow", "Unlock Door", None))
        self.virtualPrinterMode.setText(_translate("MainWindow", "V", None))
        self.menuControlButton.setText(_translate("MainWindow", "Control", None))
        self.menuPrintButton.setText(_translate("MainWindow", "Print", None))
        self.menuSettingsButton.setText(_translate("MainWindow", "Settings", None))
        self.menuCartButton.setText(_translate("MainWindow", "Cart", None))
        self.menuCalibrateButton.setText(_translate("MainWindow", "Calibrate", None))
        self.networkSettingsButton.setText(_translate("MainWindow", "Network Settings", None))
        self.displaySettingsButton.setText(_translate("MainWindow", "Display Settings", None))
        self.pairPhoneButton.setText(_translate("MainWindow", "Open in Smartphone", None))
        self.OTAButton.setText(_translate("MainWindow", "Check for Updates", None))
        self.versionButton.setText(_translate("MainWindow", "Version", None))
        self.restorePrintSettingsButton.setText(_translate("MainWindow", "Restore Print Settings", None))
        self.restoreFactoryDefaultsButton.setText(_translate("MainWindow", "Restore Factory Defaults", None))
        self.restartButton.setText(_translate("MainWindow", "Restart", None))
        self.ssidlabel.setText(_translate("MainWindow", "Enter SSID:", None))
        self.passwordlabel.setText(_translate("MainWindow", "Enter Password:", None))
        self.wifiSettingsDoneButton.setText(_translate("MainWindow", "Done", None))
        self.wifiSettingsCancelButton.setText(_translate("MainWindow", "Cancel", None))
        self.wifiSettingsSSIDKeyboardButton.setText(_translate("MainWindow", "...", None))
        self.hiddenCheckBox.setText(_translate("MainWindow", "Hidden ", None))
        self.ethSettingsDoneButton.setText(_translate("MainWindow", "Done", None))
        self.ethSettingsCancelButton.setText(_translate("MainWindow", "Cancel", None))
        self.ethStaticCheckBox.setText(_translate("MainWindow", "Static IP", None))
        self.ethStaticIpLabel.setText(_translate("MainWindow", "IP Address", None))
        self.ethStaticGatewayLabel.setText(_translate("MainWindow", "Gateway", None))
        self.ethStaticGatewayKeyboardButton.setText(_translate("MainWindow", "...", None))
        self.ethStaticIpKeyboardButton.setText(_translate("MainWindow", "...", None))
        self.networkInfoButton.setText(_translate("MainWindow", "Network Info", None))
        self.configureWifiButton.setText(_translate("MainWindow", "Configure WiFi", None))
        self.configureEthButton.setText(_translate("MainWindow", "Configure Ethernet", None))
        self.calibrateTouch.setText(_translate("MainWindow", "Calibrate Touch", None))
        self.rotateDisplay.setText(_translate("MainWindow", "Rotate Display", None))
        self.rotateDisplaySettingsDoneButton.setText(_translate("MainWindow", "Done", None))
        self.rotateDisplaySettingsCancelButton.setText(_translate("MainWindow", "Cancel", None))
        self.rotateDisplaySettingsComboBox.setItemText(0, _translate("MainWindow", "Normal", None))
        self.rotateDisplaySettingsComboBox.setItemText(1, _translate("MainWindow", "Flipped", None))
        self.rotateDisplaySettingsLabel.setText(_translate("MainWindow", "Rotation", None))
        self.hostnameLabel.setText(_translate("MainWindow", "mDNS URL", None))
        self.hostname.setText(_translate("MainWindow", "Hostname", None))
        self.wifiIpLabel.setText(_translate("MainWindow", "Wi-Fi MAC", None))
        self.wifiMac.setText(_translate("MainWindow", "WiFi", None))
        self.lanIpLabel.setText(_translate("MainWindow", "Ethernet MAC", None))
        self.lanMac.setText(_translate("MainWindow", "Ethernet", None))
        self.wifiMacLabel.setText(_translate("MainWindow", "Wi-Fi IP", None))
        self.lanMacLabel.setText(_translate("MainWindow", "Ethernet IP", None))
        self.wifiIp.setText(_translate("MainWindow", "WiFi", None))
        self.lanIp.setText(_translate("MainWindow", "Ethernet", None))
        self.wifiApLabel.setText(_translate("MainWindow", "Wi-Fi AP", None))
        self.wifiAp.setText(_translate("MainWindow", "WiFi", None))
        self.performUpdateButton.setText(_translate("MainWindow", "Update", None))
        self.logTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gotham\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Software Update Starting, Please Wait....</p></body></html>", None))
        self.firmwareUpdateLog.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gotham\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Firmware Update Starting, Please Wait....</span></p></body></html>", None))
        self.calibrateLabel.setText(_translate("MainWindow", "Calibrate:", None))
        self.calibrationWizardButton.setText(_translate("MainWindow", "Calibration Wizard", None))
        self.toolOffsetXYButton.setText(_translate("MainWindow", "Tool Offset X/Y", None))
        self.nozzleOffsetButton.setText(_translate("MainWindow", "Initial Height", None))
        self.toolOffsetZButton.setText(_translate("MainWindow", "Tool Offsets Z", None))
        self.testPrintsButton.setText(_translate("MainWindow", "Test Prints", None))
        self.calibrateLabel_2.setText(_translate("MainWindow", "Caliberation and Test Prints :", None))
        self.testPrintsTool0SizeComboBox.setItemText(0, _translate("MainWindow", "0.6", None))
        self.testPrintsTool0SizeComboBox.setItemText(1, _translate("MainWindow", "0.4", None))
        self.testPrintsTool0SizeComboBox.setItemText(2, _translate("MainWindow", "0.8", None))
        self.testPrintsTool1SizeComboBox.setItemText(0, _translate("MainWindow", "0.6", None))
        self.testPrintsTool1SizeComboBox.setItemText(1, _translate("MainWindow", "0.4", None))
        self.testPrintsTool1SizeComboBox.setItemText(2, _translate("MainWindow", "0.8", None))
        self.tool0TargetTemperature_5.setText(_translate("MainWindow", "0", None))
        self.tool0TargetTemperature_6.setText(_translate("MainWindow", "1", None))
        self.calibrateLabel_3.setText(_translate("MainWindow", "Select Installed Nozzles DIameter\'s:", None))
        self.testPrintsNextButton.setText(_translate("MainWindow", "Next", None))
        self.calibrateLabel_4.setText(_translate("MainWindow", "Ensure PLA material of different colors are loaded into both nozzles before continuing ", None))
        self.calibrateLabel_8.setText(_translate("MainWindow", "Ensure Tool 1 nozzle diameter is greater or equal to the nozzle diameter of Tool 0", None))
        self.testPrintsCancelButton.setText(_translate("MainWindow", "Cancel", None))
        self.dualCaliberationPrintButton.setText(_translate("MainWindow", "Dual Caliberation Print", None))
        self.bedLevelPrintButton.setText(_translate("MainWindow", "Bed Leveling Print", None))
        self.movementTestPrintButton.setText(_translate("MainWindow", "Movement Stress Test", None))
        self.singleNozzlePrintButton.setText(_translate("MainWindow", "Single Nozzle Test Print", None))
        self.dualNozzlePrintButton.setText(_translate("MainWindow", "Dual Nozzle Test Print", None))
        self.calibrateLabel_5.setText(_translate("MainWindow", "Ensure PLA material of different colors are loaded into both nozzles before continuing ", None))
        self.tollOffsetXLabel.setText(_translate("MainWindow", "X:", None))
        self.toolOffsetLabel.setText(_translate("MainWindow", "Tool Offset X/Y :", None))
        self.toolOffsetXDoubleSpinBox.setSuffix(_translate("MainWindow", "mm", None))
        self.toolOffsetYDoubleSpinBox.setSuffix(_translate("MainWindow", "mm", None))
        self.toolOffsetYLabel.setText(_translate("MainWindow", "Y:", None))
        self.toolOffsetZDoubleSpinBox.setSuffix(_translate("MainWindow", "mm", None))
        self.tollOffsetXLabel_2.setText(_translate("MainWindow", "Z:", None))
        self.toolOffsetLabel_2.setText(_translate("MainWindow", "Tool Offset Z :", None))
        self.quickStep1CancelButton.setText(_translate("MainWindow", "Cancel", None))
        self.quickStep1NextButton.setText(_translate("MainWindow", "Next", None))
        self.calibrateLabel_6.setText(_translate("MainWindow", "Homing In progress. Wait for all moves to finish, make sure nozzle tip is clean and then click Next", None))
        self.quickStep2NextButton.setText(_translate("MainWindow", "Next", None))
        self.quickStep2CancelButton.setText(_translate("MainWindow", "Cancel", None))
        self.calibrateLabel_7.setText(_translate("MainWindow", "Loosen or tighten the front right leveling screw untill leveling light just turns solid RED.", None))
        self.quickStep3NextButton.setText(_translate("MainWindow", "Next", None))
        self.quickStep3CancelButton.setText(_translate("MainWindow", "Cancel", None))
        self.calibrateLabel_10.setText(_translate("MainWindow", "Repeat the same using the front left leveling screw", None))
        self.quickStep4NextButton.setText(_translate("MainWindow", "Next", None))
        self.quickStep4CancelButton.setText(_translate("MainWindow", "Cancel", None))
        self.calibrateLabel_12.setText(_translate("MainWindow", "Repeat the same using the back leveling screw", None))
        self.nozzleHeightStep1NextButton.setText(_translate("MainWindow", "Next", None))
        self.nozzleHeightStep1CancelButton.setText(_translate("MainWindow", "Cancel", None))
        self.toolZOffsetLabel.setText(_translate("MainWindow", "Move the bed up or down to the First Nozzle , testing height using paper ", None))
        self.nozzleOffsetDoubleSpinBox.setSuffix(_translate("MainWindow", "mm", None))
        self.feedRateLabelControlPage_3.setText(_translate("MainWindow", "Change the initial height for the first layer of the print. +ve value increases height, -ve value reduces it.", None))
        self.fromUsbButton.setText(_translate("MainWindow", "USB", None))
        self.printFromLabel.setText(_translate("MainWindow", "Print From :", None))
        self.fromLocalButton.setText(_translate("MainWindow", "Local ", None))
        self.fileSelected.setText(_translate("MainWindow", "You Selected: ", None))
        self.fileSelectedPrintButton.setText(_translate("MainWindow", "Print", None))
        self.fileSizeSelected.setText(_translate("MainWindow", "Size", None))
        self.fileDateSelected.setText(_translate("MainWindow", "Date", None))
        self.filePrintTimeSelected.setText(_translate("MainWindow", "EST", None))
        self.filamentVolumeSelected.setText(_translate("MainWindow", "Fil. Volume", None))
        self.fileSizeSelectedLabel.setText(_translate("MainWindow", "Size:", None))
        self.fileDateSelectedLabel.setText(_translate("MainWindow", "Date:", None))
        self.filePrintTimeSelectedLabel.setText(_translate("MainWindow", "Estimated Print Time:", None))
        self.filamentVolumeSelectedLabel.setText(_translate("MainWindow", "Volume:", None))
        self.filamentLengthFileSelected.setText(_translate("MainWindow", "Fil. Length", None))
        self.filamentLengthSelectedLabel.setText(_translate("MainWindow", "Length:", None))
        self.fileSelectedUSBTransferButton.setText(_translate("MainWindow", "Save to Local", None))
        self.fileSelectedUSBName.setText(_translate("MainWindow", "File Name", None))
        self.fileSelectedUSBPrintButton.setText(_translate("MainWindow", "Print", None))
        self.feedRateLabelControlPage.setText(_translate("MainWindow", "Feed Rate :", None))
        self.feedRateSpinBox.setSuffix(_translate("MainWindow", "%", None))
        self.flowRateLabelControlPage_5.setText(_translate("MainWindow", "Tune Bed Height during Print :", None))
        self.toolLabel.setText(_translate("MainWindow", "Nozzles:", None))
        self.bedLabel_2.setText(_translate("MainWindow", "Bed:", None))
        self.toolTempSpinBox.setSuffix(_translate("MainWindow", "°C", None))
        self.bedTempSpinBox.setSuffix(_translate("MainWindow", "°C", None))
        self.tool250PreheatButton.setText(_translate("MainWindow", "250°C", None))
        self.tool180PreheatButton.setText(_translate("MainWindow", "180°C", None))
        self.tool220PreheatButton.setText(_translate("MainWindow", "220°C", None))
        self.bed60PreheatButton.setText(_translate("MainWindow", "60°C", None))
        self.bed100PreheatButton.setText(_translate("MainWindow", "100°C", None))
        self.chamber70PreheatButton.setText(_translate("MainWindow", "70°C", None))
        self.chamberTempSpinBox.setSuffix(_translate("MainWindow", "°C", None))
        self.chamber40PreheatButton.setText(_translate("MainWindow", "40°C", None))
        self.bedLabel_4.setText(_translate("MainWindow", "Chamber:", None))
        self.step1Button.setText(_translate("MainWindow", "1 mm", None))
        self.step10Button.setText(_translate("MainWindow", "10 mm", None))
        self.step100Button.setText(_translate("MainWindow", "100 mm", None))
        self.XYLabel.setText(_translate("MainWindow", "X/Y :", None))
        self.ZLabel.setText(_translate("MainWindow", "Z:", None))
        self.ELabel.setText(_translate("MainWindow", "E:", None))
        self.moveByLabel.setText(_translate("MainWindow", "Move By:", None))
        self.toolToggleMotionButton.setText(_translate("MainWindow", "1", None))
        self.flowRateSpinBox.setSuffix(_translate("MainWindow", "%", None))
        self.flowRateLabelControlPage.setText(_translate("MainWindow", "Flow Rate :", None))
        self.changeFilamentButton.setText(_translate("MainWindow", "Change Filament", None))
        self.toggleFilamentSensorButton.setText(_translate("MainWindow", "Filament Sensor", None))
        self.selectFilamentlabel.setText(_translate("MainWindow", "Select Filament :", None))
        self.changeFilamentLoadButton.setText(_translate("MainWindow", "Load", None))
        self.changeFilamentUnloadButton.setText(_translate("MainWindow", "Unload", None))
        self.changeFilamentStatus.setText(_translate("MainWindow", "Heating ...", None))
        self.changeFilamentProgress.setFormat(_translate("MainWindow", "%p%", None))
        self.changeFilamentNameOperation.setText(_translate("MainWindow", "Loading Filament", None))
        self.feedFilamentlabel.setText(_translate("MainWindow", "Feed Filament into Extruder", None))
        self.loadDoneButton.setText(_translate("MainWindow", "Done", None))
        self.ExtrudeButton.setText(_translate("MainWindow", "Extrude", None))
        self.feedFilamentlabel_2.setText(_translate("MainWindow", "Click \"Extrude\" untill filament starts extruding", None))
        self.feedFilamentlabel_3.setText(_translate("MainWindow", "Click \"Retract\" untill filament is removed", None))
        self.unloadDoneButton.setText(_translate("MainWindow", "Done", None))
        self.feedFilamentlabel_4.setText(_translate("MainWindow", "Retract Filament From Extruder", None))
        self.retractFilamentButton.setText(_translate("MainWindow", "Retract", None))

