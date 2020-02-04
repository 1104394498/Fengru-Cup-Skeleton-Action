from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from design import Ui_MainWindow
import sys


class myMainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)

        # self.widget = QVideoWidget()
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.widget)  # 视频播放输出的widget，就是上面定义的

        self.player2 = QMediaPlayer()
        self.player2.setVideoOutput(self.widget_2)

        self.choose.clicked.connect(self.openVideoFile)  # 打开视频文件按钮
        self.start.clicked.connect(self.playVideo)  # play
        self.suspend.clicked.connect(self.pauseVideo)  # pause

        self.player.positionChanged.connect(self.changeSlide)  # change Slide

    def openVideoFile(self):
        self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))  # 选取视频文件
        self.player.play()  # 播放视频

    def playVideo(self):
        self.player.play()

    def pauseVideo(self):
        self.player.pause()

    def changeSlide(self, position):
        self.vidoeLength = self.player.duration() + 0.1
        self.horizontalSlider.setValue(round((position / self.vidoeLength) * 100))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    vieo_gui = myMainWindow()
    vieo_gui.show()
    sys.exit(app.exec_())
