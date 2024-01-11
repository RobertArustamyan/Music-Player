from PyQt5.QtCore import QFileInfo,QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem,QDialog
import pygame
import numpy as np

class Ui_Ecualizer(object):
    def setupUi(self, Ecualizer):
        Ecualizer.setObjectName("Ecualizer")
        Ecualizer.resize(300, 400)
        Ecualizer.setStyleSheet("background:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41,61,132,235),stop:1 rgba(155,79,165,255));")
        self.label = QtWidgets.QLabel(Ecualizer)
        self.label.setGeometry(QtCore.QRect(25, 220, 20, 29))
        self.label.setStyleSheet("background-color:none;\n"
"color:white;\n"
"font-size:10px;")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Ecualizer)
        self.label_3.setGeometry(QtCore.QRect(50, 220, 20, 29))
        self.label_3.setStyleSheet("background-color:none;\n"
"color:white;\n"
"font-size:10px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Ecualizer)
        self.label_4.setGeometry(QtCore.QRect(75, 220, 20, 29))
        self.label_4.setStyleSheet("background-color:none;\n"
"color:white;\n"
"font-size:10px;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Ecualizer)
        self.label_5.setGeometry(QtCore.QRect(100, 220, 20, 29))
        self.label_5.setStyleSheet("background-color:none;\n"
"color:white;\n"
"font-size:10px;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Ecualizer)
        self.label_6.setGeometry(QtCore.QRect(125, 220, 20, 29))
        self.label_6.setStyleSheet("background-color:none;\n"
"color:white;\n"
"font-size:10px;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Ecualizer)
        self.label_7.setGeometry(QtCore.QRect(155, 220, 20, 29))
        self.label_7.setStyleSheet("background-color:none;\n"
"color:white;\n"
"font-size:10px;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Ecualizer)
        self.label_8.setGeometry(QtCore.QRect(183, 220, 20, 29))
        self.label_8.setStyleSheet("background-color:none;\n"
"color:white;\n"
"font-size:10px;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Ecualizer)
        self.label_9.setGeometry(QtCore.QRect(208, 220, 20, 29))
        self.label_9.setStyleSheet("background-color:none;\n"
"color:white;\n"
"font-size:10px;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Ecualizer)
        self.label_10.setGeometry(QtCore.QRect(235, 220, 20, 29))
        self.label_10.setStyleSheet("background-color:none;\n"
"color:white;\n"
"font-size:10px;")
        self.label_10.setObjectName("label_10")
        self.label_19 = QtWidgets.QLabel(Ecualizer)
        self.label_19.setGeometry(QtCore.QRect(260, 220, 20, 29))
        self.label_19.setStyleSheet("background-color:none;\n"
"color:white;\n"
"font-size:10px;")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(Ecualizer)
        self.label_20.setGeometry(QtCore.QRect(90, 20, 120, 81))
        self.label_20.setStyleSheet("background-color:none;\n"
"color:white;\n"
"font-size:30px;")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.frame = QtWidgets.QFrame(Ecualizer)
        self.frame.setGeometry(QtCore.QRect(10, 250, 276, 86))
        self.frame.setStyleSheet("background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);    \n"
"border-radius: 7px;")
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalSlider_1 = QtWidgets.QSlider(self.frame)
        self.verticalSlider_1.setStyleSheet("background-color:none;")
        self.verticalSlider_1.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_1.setObjectName("verticalSlider_1")
        self.horizontalLayout.addWidget(self.verticalSlider_1)
        self.verticalSlider_2 = QtWidgets.QSlider(self.frame)
        self.verticalSlider_2.setStyleSheet("background-color:none;")
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.horizontalLayout.addWidget(self.verticalSlider_2)
        self.verticalSlider_3 = QtWidgets.QSlider(self.frame)
        self.verticalSlider_3.setStyleSheet("background-color:none;")
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.horizontalLayout.addWidget(self.verticalSlider_3)
        self.verticalSlider_5 = QtWidgets.QSlider(self.frame)
        self.verticalSlider_5.setStyleSheet("background-color:none;")
        self.verticalSlider_5.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_5.setObjectName("verticalSlider_5")
        self.horizontalLayout.addWidget(self.verticalSlider_5)
        self.verticalSlider_4 = QtWidgets.QSlider(self.frame)
        self.verticalSlider_4.setStyleSheet("background-color:none;")
        self.verticalSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_4.setObjectName("verticalSlider_4")
        self.horizontalLayout.addWidget(self.verticalSlider_4)
        self.verticalSlider_7 = QtWidgets.QSlider(self.frame)
        self.verticalSlider_7.setStyleSheet("background-color:none;")
        self.verticalSlider_7.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_7.setObjectName("verticalSlider_7")
        self.horizontalLayout.addWidget(self.verticalSlider_7)
        self.verticalSlider_6 = QtWidgets.QSlider(self.frame)
        self.verticalSlider_6.setStyleSheet("background-color:none;")
        self.verticalSlider_6.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_6.setObjectName("verticalSlider_6")
        self.horizontalLayout.addWidget(self.verticalSlider_6)
        self.verticalSlider_8 = QtWidgets.QSlider(self.frame)
        self.verticalSlider_8.setStyleSheet("background-color:none;")
        self.verticalSlider_8.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_8.setObjectName("verticalSlider_8")
        self.horizontalLayout.addWidget(self.verticalSlider_8)
        self.verticalSlider_10 = QtWidgets.QSlider(self.frame)
        self.verticalSlider_10.setStyleSheet("background-color:none;")
        self.verticalSlider_10.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_10.setObjectName("verticalSlider_10")
        self.horizontalLayout.addWidget(self.verticalSlider_10)
        self.verticalSlider_9 = QtWidgets.QSlider(self.frame)
        self.verticalSlider_9.setStyleSheet("background-color:none;")
        self.verticalSlider_9.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_9.setObjectName("verticalSlider_9")
        self.horizontalLayout.addWidget(self.verticalSlider_9)

        self.retranslateUi(Ecualizer)
        QtCore.QMetaObject.connectSlotsByName(Ecualizer)

        default_value = 50
        self.verticalSlider_1.setValue(default_value)
        self.verticalSlider_2.setValue(default_value)
        self.verticalSlider_3.setValue(default_value)
        self.verticalSlider_4.setValue(default_value)
        self.verticalSlider_5.setValue(default_value)
        self.verticalSlider_6.setValue(default_value)
        self.verticalSlider_7.setValue(default_value)
        self.verticalSlider_8.setValue(default_value)
        self.verticalSlider_9.setValue(default_value)
        self.verticalSlider_10.setValue(default_value)

        self.verticalSlider_1.valueChanged.connect(self.on_slider_change
                                                   )
        self.verticalSlider_2.valueChanged.connect(self.on_slider_change
                                                   )
        self.verticalSlider_3.valueChanged.connect(self.on_slider_change
                                                   )
        self.verticalSlider_4.valueChanged.connect(self.on_slider_change
                                                   )
        self.verticalSlider_5.valueChanged.connect(self.on_slider_change
                                                   )
        self.verticalSlider_6.valueChanged.connect(self.on_slider_change
                                                   )
        self.verticalSlider_7.valueChanged.connect(self.on_slider_change
                                                   )
        self.verticalSlider_8.valueChanged.connect(self.on_slider_change
                                                   )
        self.verticalSlider_9.valueChanged.connect(self.on_slider_change
                                                   )
        self.verticalSlider_10.valueChanged.connect(self.on_slider_change
                                                    )

    def on_slider_change(self):
        slider_values = [
            self.verticalSlider_1.value(),
            self.verticalSlider_2.value(),
            self.verticalSlider_3.value(),
            self.verticalSlider_4.value(),
            self.verticalSlider_5.value(),
            self.verticalSlider_6.value(),
            self.verticalSlider_7.value(),
            self.verticalSlider_8.value(),
            self.verticalSlider_9.value(),
            self.verticalSlider_10.value(),
        ]
        return slider_values

    def retranslateUi(self, Ecualizer):
        _translate = QtCore.QCoreApplication.translate
        Ecualizer.setWindowTitle(_translate("Ecualizer", "Dialog"))
        self.label.setText(_translate("Ecualizer", "32"))
        self.label_3.setText(_translate("Ecualizer", "64"))
        self.label_4.setText(_translate("Ecualizer", "125"))
        self.label_5.setText(_translate("Ecualizer", "250"))
        self.label_6.setText(_translate("Ecualizer", "500"))
        self.label_7.setText(_translate("Ecualizer", "1K"))
        self.label_8.setText(_translate("Ecualizer", "2K"))
        self.label_9.setText(_translate("Ecualizer", "4K"))
        self.label_10.setText(_translate("Ecualizer", "8K"))
        self.label_19.setText(_translate("Ecualizer", "16K"))
        self.label_20.setText(_translate("Ecualizer", "Equalizer"))
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        MainWindow.setStyleSheet("background:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41,61,132,235),stop:1 rgba(155,79,165,255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(120, 430, 160, 22))
        self.horizontalSlider.setStyleSheet("background-color:None;")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.managment = QtWidgets.QFrame(self.centralwidget)
        self.managment.setGeometry(QtCore.QRect(100, 390, 200, 31))
        self.managment.setStyleSheet("background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);    \n"
"border-radius: 7px;")
        self.managment.setObjectName("managment")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.managment)
        self.horizontalLayout.setContentsMargins(10, 3, 10, 3)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.previous_btn = QtWidgets.QPushButton(self.managment)
        self.previous_btn.setStyleSheet("QPushButton{\n"
"color:white;    \n"
"background-color:rgba(255,255,255,30);\n"
"border:1px solid rgba(255,255,255,40);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        self.previous_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/skip_previous_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previous_btn.setIcon(icon)
        self.previous_btn.setObjectName("previous_btn")
        self.horizontalLayout.addWidget(self.previous_btn)
        self.stop_btn = QtWidgets.QPushButton(self.managment)
        self.stop_btn.setStyleSheet("QPushButton{\n"
"color:white;    \n"
"background-color:rgba(255,255,255,30);\n"
"border:1px solid rgba(255,255,255,40);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        self.stop_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/pause_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_btn.setIcon(icon1)
        self.stop_btn.setObjectName("stop_btn")
        self.horizontalLayout.addWidget(self.stop_btn)
        self.continue_btn = QtWidgets.QPushButton(self.managment)
        self.continue_btn.setStyleSheet("QPushButton{\n"
"color:white;    \n"
"background-color:rgba(255,255,255,30);\n"
"border:1px solid rgba(255,255,255,40);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        self.continue_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/play_arrow_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.continue_btn.setIcon(icon2)
        self.continue_btn.setObjectName("continue_btn")
        self.horizontalLayout.addWidget(self.continue_btn)
        self.next_btn = QtWidgets.QPushButton(self.managment)
        self.next_btn.setStyleSheet("QPushButton{\n"
"color:white;    \n"
"background-color:rgba(255,255,255,30);\n"
"border:1px solid rgba(255,255,255,40);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        self.next_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/skip_next_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_btn.setIcon(icon3)
        self.next_btn.setObjectName("next_btn")
        self.horizontalLayout.addWidget(self.next_btn)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 420, 47, 41))
        self.label.setStyleSheet("background-color:none;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/icons/volume_mute_FILL0_wght400_GRAD0_opsz24.svg"))
        self.label.setObjectName("label")
        self.setting_btn = QtWidgets.QPushButton(self.centralwidget)
        self.setting_btn.setGeometry(QtCore.QRect(280, 430, 21, 21))
        self.setting_btn.setStyleSheet("/* Default styles */\n"
"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 30);\n"
"    color: white;\n"
"    border: none;  /* Remove the border */\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"/* Hover styles */\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"/* Active (pressed) styles */\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 70);\n"
"}\n"
"")
        self.setting_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/tune_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting_btn.setIcon(icon4)
        self.setting_btn.setObjectName("setting_btn")
        self.currentSongLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentSongLabel.setGeometry(QtCore.QRect(50, 10, 300, 30))
        self.currentSongLabel.setStyleSheet("QLabel#currentSongLabel {\n"
"    background-color: rgba(255,255,255,30);; \n"
"    color: white;\n"
"    padding: 10px;\n"
"    border:1px solid rgba(255,255,255,40);    \n"
"    border-radius: 7px;\n"
"    font-size: 10px;\n"
"}\n"
"")
        self.currentSongLabel.setObjectName("currentSongLabel")
        self.list_of_songs = QtWidgets.QListWidget(self.centralwidget)
        self.list_of_songs.setGeometry(QtCore.QRect(10, 50, 380, 321))
        self.list_of_songs.setStyleSheet("QListWidget {\n"
"    background-color: rgba(255,255,255,30);; \n"
"    color: white;\n"
"    padding: 10px;\n"
"    border:1px solid rgba(255,255,255,40);    \n"
"    border-radius: 7px;\n"
"    font-size: 10px;\n"
"}\n"
"")
        self.list_of_songs.setObjectName("list_of_songs")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.actionAdd_Music = QtWidgets.QAction(MainWindow)
        self.actionAdd_Music.setObjectName("actionAdd_Music")
        self.menuFile.addAction(self.actionAdd_Music)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.actionAdd_Music.triggered.connect(self.add_music_clicked)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.load_playlist()
        self.list_of_songs.itemClicked.connect(self.update_cur_song_label)

        pygame.init()
        pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)
        self.current_song = None
        self.play_timer = QTimer(self.centralwidget)
        self.play_timer.timeout.connect(self.check_music_state)

        self.next_btn.clicked.connect(self.play_next_song)
        self.previous_btn.clicked.connect(self.play_prev_song)

        self.stop_btn.clicked.connect(self.pause_song)
        self.continue_btn.clicked.connect(self.continue_song)

        default_slider_value = 50
        self.horizontalSlider.setValue(default_slider_value)
        self.horizontalSlider.valueChanged.connect(self.volume_change)

        self.setting_btn.clicked.connect(self.show_equalizer)

    def show_equalizer(self):
        equalizer_dialog = QDialog()
        ui_equalizer = Ui_Ecualizer()
        ui_equalizer.setupUi(equalizer_dialog)
        equalizer_dialog.exec_()
        slider_values = ui_equalizer.on_slider_change()
        self.apply_equalizer_settings(slider_values)

    def apply_equalizer_settings(self, slider_values):
        pass
    def update_cur_song_label(self, item: QListWidgetItem):
        all_songs = self.get_song_list

        song_name = item.text()
        self.currentSongLabel.setText(f"Current Song: {song_name}")
        for song in all_songs:
            if song_name in song:
                break
        if self.current_song is None:
            self.current_song = song
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            self.play_timer.start(1000)
        elif self.current_song != song:
            pygame.mixer.music.load(song)
            self.current_song = song
            pygame.mixer.music.play()
            self.play_timer.start(1000)
        elif self.current_song == song:
            pygame.mixer.music.rewind()
            self.play_timer.start(1000)

    def check_music_state(self):
        if not pygame.mixer.music.get_busy():
            self.play_timer.stop()
            self.play_next_song()

    def play_next_song(self):
        if self.get_song_list and self.current_song != self.get_song_list[-1]:
            cur_index = self.get_song_list.index(self.current_song)
            next_song = self.get_song_list[cur_index + 1]
            self.update_cur_song_label(QListWidgetItem(QFileInfo(next_song).fileName()))
    def play_prev_song(self):
        if self.current_song != self.get_song_list[0]:
            cur_index = self.get_song_list.index(self.current_song)
            next_song = self.get_song_list[cur_index - 1]
            temporary_item = QtWidgets.QListWidgetItem(QFileInfo(next_song).fileName())
            self.update_cur_song_label(temporary_item)
        else:
            temporary_item = QtWidgets.QListWidgetItem(QFileInfo(self.current_song).fileName())
            self.update_cur_song_label(temporary_item)

    def continue_song(self):
        pygame.mixer.music.unpause()
        self.play_timer.start(1000)

    def pause_song(self):
        pygame.mixer.music.pause()
        self.play_timer.stop()

    def volume_change(self):
        slider_value = self.horizontalSlider.value()
        volume = slider_value/ 100.0
        pygame.mixer.music.set_volume(volume)
    @property
    def get_song_list(self):
        with open("playlist.txt", 'r') as file:
            content = file.read()
            all_songs = content.split('\n')
            all_songs = [element for element in all_songs if element]
        return all_songs
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music"))
        self.currentSongLabel.setText(_translate("MainWindow", "Current Song:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionAdd_Music.setText(_translate("MainWindow", "Add_Music"))


    def add_music_clicked(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Music files (*.mp3 *.wav *.ogg)")
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            self.add_item_playlist(selected_files)


    def add_item_playlist(self,songs):
        try:
            elements = self.get_song_list
        except FileNotFoundError:
            print(f"The file does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

        for song in songs:
            if song not in elements:
                elements.append(song)
        with open('playlist.txt','w') as file:
            for element in elements:
                file.write(element + '\n')
        self.load_playlist()

    def load_playlist(self):
        elements = self.get_song_list
        self.list_of_songs.clear()
        for file in elements:
            item = QListWidgetItem(f"{QFileInfo(file).fileName()}")
            self.list_of_songs.addItem(item)

import res_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
