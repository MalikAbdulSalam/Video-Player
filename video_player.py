import sys
import os
from PyQt5 import QtGui, uic ,QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtWidgets import QFileDialog
from subprocess import call
import glob
from shutil import copyfile
# import cv2
root = os.path.expanduser('~')
class MyWindow(QtWidgets.QDialog):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('GUI.ui', self)
        self.show()
        # self.setupUi(self)
        self.start_btn.clicked.connect(self.start)
        self.hide_btn.clicked.connect(self.hide)
        self.show_btn.clicked.connect(self.showw)
        self.pause_btn.clicked.connect(self.pause)
        self.play_btn.clicked.connect(self.play)
        self.stop_btn.clicked.connect(self.stop)
        self.open_btn.clicked.connect(self.open)
        self.pth = "/home/malik/Downloads/12.mp4"



        #below given code will be used to play start up video
        # self.mediaPlayer = QtMultimedia.QMediaPlayer(self)
        # self.mediaPlayer.setVideoOutput(self.widget)
        # fileName = "/home/malik/Downloads/12.mp4"
        # url = QtCore.QUrl.fromLocalFile(fileName)
        # # url = QtCore.QUrl("/home/malik/Downloads/12.mp4")
        # self.mediaPlayer.setMedia(QtMultimedia.QMediaContent(url))
        # self.mediaPlayer.play()

    def hide(self):
        print("hide")
        self.widget.setVisible(False)

    def start(self):
        print("play")
        self.mediaPlayer = QtMultimedia.QMediaPlayer(self)
        self.mediaPlayer.setVideoOutput(self.widget)
        fileName = self.pth
        url = QtCore.QUrl.fromLocalFile(fileName)
        # url = QtCore.QUrl("/home/malik/Downloads/12.mp4")
        self.mediaPlayer.setMedia(QtMultimedia.QMediaContent(url))
        self.mediaPlayer.play()

    def showw(self):
        print("show")
        self.widget.setVisible(True)
    def pause(self):
        print("pause")
        self.mediaPlayer.pause()
    def play(self):
        print("play")
        self.mediaPlayer.play()

    def stop(self):
        print("stop")
        self.mediaPlayer.stop()

    def open(self):
        print("open file")
        # to delete existing files from input directory
        files = glob.glob('./input/*')
        for f in files:
            os.remove(f)
        fname = QFileDialog.getOpenFileNames(self, 'Open file', '/images/', 'Wav File (*.mp4)')
        # print(len(fname))
        # print(fname)
        name = fname[0]
        # print(name)
        for i in name:
            print(i)
            self.pth = i
        # self.filename.setText(fname[0])
        # fname = fname[:-1]
        # # print(fname,'/////////////////')
        # len(fname)
        # # fname= list(fname)
        # # print(len(fname))
        # for item in fname:
        #     print(item)
        #     for ind in item:
        #         print('This is index', ind)
        #         filename = os.path.basename(ind)
        #         print('file name is', filename)
        #         copyfile(ind, os.path.join("./",
        #             "video.mp4"))

    def duration(filename):
        video = cv2.VideoCapture(filename)

        duration = video.get(cv2.CAP_PROP_POS_MSEC)
        frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)

        return duration, frame_count

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = MyWindow()
    window.setWindowTitle("Player")
    sys.exit(app.exec_())
