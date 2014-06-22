from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon


class VideoPlayer(QtGui.QWidget):
    """The VideoPlayer itself"""
    def __init__(self, url):

        self.url = url

        QtGui.QWidget.__init__(self)
        self.setSizePolicy(
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)

        self.player = Phonon.VideoPlayer(Phonon.VideoCategory)
        self.player.setSizePolicy(QtGui.QSizePolicy.Expanding,
                                  QtGui.QSizePolicy.Preferred)
        self.player.load(Phonon.MediaSource(self.url))
        self.player.mediaObject().setTickInterval(200)
        self.player.mediaObject().tick.connect(self.timer)
        self.shortcutFull = QtGui.QShortcut(self)
        self.shortcutFull.setKey(QtGui.QKeySequence('F11'))
        self.shortcutFull.setContext(QtCore.Qt.ApplicationShortcut)
        self.shortcutFull.activated.connect(self.handleFullScreen)

        self.progress_bar = Phonon.SeekSlider(self.player.mediaObject())

        self.timer = QtGui.QLabel()
        self.timer.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.play_pause = QtGui.QPushButton()
        self.play_pause.setIcon(QtGui.QIcon('play.png'))
        self.play_pause.clicked.connect(self.change_state)

        top_layout = QtGui.QVBoxLayout()
        top_layout.addWidget(self.player)
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.play_pause)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.timer)
        top_layout.addLayout(layout)
        self.setLayout(top_layout)

    def handleFullScreen(self):
        videoWidget = self.player.videoWidget()
        if videoWidget.isFullScreen():
            videoWidget.exitFullScreen()
        else:
            videoWidget.enterFullScreen()

    def change_state(self):
        if self.player.mediaObject().state() == Phonon.PlayingState:
            self.player.pause()
            self.play_pause.setIcon(QtGui.QIcon('play.png'))
        else:
            self.player.play()
            self.play_pause.setIcon(QtGui.QIcon('pause.png'))

    def timer(self, time):
        seconds = int(time / 1000) % 60
        hours = int(time / 3600000) % 60
        minutes = int(time / 60000) % 60
        self.timer.setText('{h}:{m}:{s}'.format(
            h='0'+str(hours) if hours < 10 else str(hours),
            m='0'+str(minutes) if minutes < 10 else str(minutes),
            s='0'+str(seconds) if seconds < 10 else str(seconds)))
