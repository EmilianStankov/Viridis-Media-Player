from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon
from song import Song


class VideoPlayer(QtGui.QWidget):
    """The VideoPlayer itself"""
    def __init__(self, url):

        self.url = url
        self.title = None
        self.album = None
        self.artist = None
        self.genre = None
        self.rating = None
        self.year = None
        self.track = None

        QtGui.QWidget.__init__(self)
        self.setSizePolicy(
            QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)

        self.player = Phonon.VideoPlayer(Phonon.VideoCategory)
        self.player.setFixedWidth(700)
        self.player.setFixedHeight(300)
        self.player.setSizePolicy(QtGui.QSizePolicy.Fixed,
                                  QtGui.QSizePolicy.Fixed)
        self.player.load(Phonon.MediaSource(self.url))
        self.player.mediaObject().setTickInterval(200)
        self.player.mediaObject().tick.connect(self.timer)

        self.shortcut_full = QtGui.QShortcut(self)
        self.shortcut_full.setKey(QtGui.QKeySequence('F11'))
        self.shortcut_full.setContext(QtCore.Qt.ApplicationShortcut)
        self.shortcut_full.activated.connect(self.handleFullScreen)

        self.shortcut_play_pause = QtGui.QShortcut(self)
        self.shortcut_play_pause.setKey(QtGui.QKeySequence('Space'))
        self.shortcut_play_pause.setContext(QtCore.Qt.ApplicationShortcut)
        self.shortcut_play_pause.activated.connect(self.change_state)

        self.progress_bar = Phonon.SeekSlider(self.player.mediaObject())

        self.timer = QtGui.QLabel("00:00:00")

        self.play_pause = QtGui.QPushButton()
        self.play_pause.setIcon(QtGui.QIcon('play.png'))
        self.play_pause.clicked.connect(self.change_state)

        if self.url.endswith(".mp3"):
            self.apply_changes_button = QtGui.QPushButton("&Apply changes")
            self.apply_changes_button.setFixedWidth(300)
            self.apply_changes_button.clicked.connect(self.save_tags)
            self.top_layout = QtGui.QVBoxLayout()
            self.layout = QtGui.QHBoxLayout()
            self.layout.addWidget(self.play_pause)
            self.layout.addWidget(self.progress_bar)
            self.layout.addWidget(self.timer)
            self.top_layout.addLayout(self.layout)
            self.top_layout.addLayout(self.set_mp3_layout())
            self.setLayout(self.top_layout)

        else:
            self.top_layout = QtGui.QVBoxLayout()
            self.top_layout.addWidget(self.player)
            self.layout = QtGui.QHBoxLayout()
            self.layout.addWidget(self.play_pause)
            self.layout.addWidget(self.progress_bar)
            self.layout.addWidget(self.timer)
            self.top_layout.addLayout(self.layout)
            self.setLayout(self.top_layout)

    def save_tags(self):
        self.song.set_artist(self.artist.text())
        self.song.set_title(self.title.text())
        self.song.set_album(self.album.text())
        self.song.set_genre(self.genre.text())
        self.song.set_year(self.year.text())
        self.song.set_track(self.track.text())

    def handleFullScreen(self):
        videoWidget = self.player.videoWidget()
        if videoWidget.isFullScreen():
            videoWidget.exitFullScreen()
        else:
            videoWidget.enterFullScreen()

    def set_mp3_layout(self):
        self.song = Song(self.url)
        self.id3layout = QtGui.QGridLayout()
        self.title = QtGui.QLineEdit(self.song.get_title())
        self.album = QtGui.QLineEdit(self.song.get_album())
        self.artist = QtGui.QLineEdit(self.song.get_artist())
        self.genre = QtGui.QLineEdit(self.song.get_genre())
        self.rating = QtGui.QLineEdit(self.song.get_rating())
        self.year = QtGui.QLineEdit(self.song.get_year())
        self.track = QtGui.QLineEdit(self.song.get_track())
        self.id3layout.addWidget(QtGui.QLabel("Artist: "), 0, 0)
        self.id3layout.addWidget(self.artist, 0, 1)
        self.id3layout.addWidget(QtGui.QLabel("Title:  "), 1, 0)
        self.id3layout.addWidget(self.title, 1, 1)
        self.id3layout.addWidget(QtGui.QLabel("Album:  "), 2, 0)
        self.id3layout.addWidget(self.album, 2, 1)
        self.id3layout.addWidget(QtGui.QLabel("Genre:  "), 3, 0)
        self.id3layout.addWidget(self.genre, 3, 1)
        self.id3layout.addWidget(QtGui.QLabel("Year:   "), 4, 0)
        self.id3layout.addWidget(self.year, 4, 1)
        self.id3layout.addWidget(QtGui.QLabel("Track:  "), 5, 0)
        self.id3layout.addWidget(self.track, 5, 1)
        self.id3layout.addWidget(self.apply_changes_button, 6, 1)
        return self.id3layout

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
