from PyQt4 import QtGui
from PyQt4.QtGui import QLabel, QPixmap
from playlist import Playlist, load_playlist_from_db, get_playlists
from VideoPlayer import VideoPlayer


class MainScreen(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        self.__splash = self.splash_screen()
        self.__playlists = get_playlists()
        self.playlist = None
        self.vp = None
        self.current = 0
        self.initialize_buttons()

        self.create_playlist_button = QtGui.QPushButton("&Create Playlist")
        self.create_playlist_button.clicked.connect(self.create_playlist)

        self.load_playlist_button = QtGui.QPushButton("&Load Playlist")
        self.load_playlist_button.clicked.connect(self.load_playlist)

        self.layout = QtGui.QVBoxLayout()
        self.layout.addWidget(self.__splash)
        self.layout.addWidget(self.create_playlist_button)
        self.layout.addWidget(self.load_playlist_button)
        self.setLayout(self.layout)
        #self.resize(self.height, self.width)

    def create_playlist(self):
        files = QtGui.QFileDialog.getOpenFileNames(
            self, self.tr("Select files"),
            QtGui.QDesktopServices.storageLocation(
                QtGui.QDesktopServices.MusicLocation))
        text = QtGui.QInputDialog.getText(self, 'Save Playlist',
                                          'Enter playlist name:')
        playlist_name = str(text[0])
        pl = Playlist(playlist_name, files)
        pl.save_to_db()
        return pl

    def splash_screen(self):
        label = QLabel()
        label.setFixedWidth(1050)
        label.setFixedHeight(383)
        logo = QPixmap("viridis.bmp")
        label.setPixmap(logo)
        return label

    def initialize_buttons(self):
        self.next_button = QtGui.QPushButton()
        self.next_button.setIcon(QtGui.QIcon('next.png'))
        self.next_button.setMaximumWidth(100)
        self.next_button.clicked.connect(self.next)

        self.previous_button = QtGui.QPushButton()
        self.previous_button.setIcon(QtGui.QIcon('previous.png'))
        self.previous_button.setMaximumWidth(100)
        self.previous_button.clicked.connect(self.previous)

    def load_playlist(self):
        text = QtGui.QInputDialog.getText(self, 'Load Playlist',
                                          'Enter playlist name:')
        pl = load_playlist_from_db(str(text[0]))
        self.playlist = pl
        self.remove_widgets()
        self.vp = VideoPlayer(self.playlist.get_files()[0])
        self.layout.addWidget(self.vp)
        btn_layout = QtGui.QHBoxLayout()
        btn_layout.addWidget(self.next_button)
        btn_layout.addWidget(self.previous_button)
        self.layout.addLayout(btn_layout)

    def remove_widgets(self):
        self.layout.removeWidget(self.load_playlist_button)
        self.load_playlist_button.deleteLater()
        self.load_playlist_button = None
        self.layout.removeWidget(self.create_playlist_button)
        self.create_playlist_button.deleteLater()
        self.create_playlist_button = None
        self.layout.removeWidget(self.__splash)
        self.__splash.deleteLater()
        self.__splash = None

    def fix_layout(self):
        self.layout.removeWidget(self.next_button)
        self.next_button.deleteLater()
        self.next_button = None
        self.layout.removeWidget(self.previous_button)
        self.previous_button.deleteLater()
        self.previous_button = None
        self.initialize_buttons()
        self.layout.addWidget(self.vp)
        btn_layout = QtGui.QHBoxLayout()
        btn_layout.addWidget(self.next_button)
        btn_layout.addWidget(self.previous_button)
        self.layout.addLayout(btn_layout)

    def next(self):
        if self.current > len(self.playlist.get_files()) - 2:
            self.current = len(self.playlist.get_files()) - 2
        self.layout.removeWidget(self.vp)
        try:
            self.vp.deleteLater()
        except AttributeError:
            pass
        self.current += 1
        self.vp = None
        self.vp = VideoPlayer(self.playlist.get_files()[self.current])
        self.fix_layout()

    def previous(self):
        if self.current < 1:
            self.current = 1
        self.layout.removeWidget(self.vp)
        try:
            self.vp.deleteLater()
        except AttributeError:
            pass
        self.current -= 1
        self.vp = None
        self.vp = VideoPlayer(self.playlist.get_files()[self.current])
        self.fix_layout()
