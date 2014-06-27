from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QLabel, QPixmap
from playlist import Playlist, load_playlist_from_db, get_playlists
from VideoPlayer import VideoPlayer


class MainScreen(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setSizePolicy(
            QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)

        self.splash = self.splash_screen()
        self.__playlists = get_playlists()
        self.scroll_area = None
        self.playlist = None
        self.vp = None
        self.current = 0
        self.initialize_buttons()

        self.create_playlist_button = QtGui.QPushButton("&Create Playlist")
        self.create_playlist_button.setFixedWidth(300)
        self.create_playlist_button.clicked.connect(self.create_playlist)

        self.load_playlist_button = QtGui.QPushButton("&Load Playlist")
        self.load_playlist_button.setFixedWidth(300)
        self.load_playlist_button.clicked.connect(self.load_playlist)

        self.show_playlists_button = QtGui.QPushButton("&Show Playlists")
        self.show_playlists_button.setFixedWidth(300)
        self.show_playlists_button.clicked.connect(self.show_playlists)

        self.layout = QtGui.QVBoxLayout()
        self.layout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.layout.addWidget(self.splash)
        self.layout.addWidget(self.create_playlist_button)
        self.layout.addWidget(self.load_playlist_button)
        self.layout.addWidget(self.show_playlists_button)
        self.setLayout(self.layout)

    def show_playlists(self):
        playlists = QLabel()
        playlists.setText("\n".join(get_playlists()))
        self.scroll_area = QtGui.QScrollArea()
        self.scroll_area.setFixedHeight(120)
        self.scroll_area.setWidget(playlists)
        self.scroll_area.setAlignment(QtCore.Qt.AlignHCenter)
        self.layout.addWidget(self.scroll_area)
        self.show_playlists_button.setDisabled(True)

    def show_files(self):
        files = QLabel()
        files.setAlignment(QtCore.Qt.AlignLeft)
        files_text = ""
        for file in self.playlist.get_files():
            files_text += file.split("/")[-1] + "\n"
        files.setText(files_text)
        self.scroll_area = QtGui.QScrollArea()
        self.scroll_area.setAlignment(QtCore.Qt.AlignLeft)
        self.scroll_area.setFixedHeight(200)
        self.scroll_area.setWidget(files)
        self.layout.addWidget(self.scroll_area)
        self.show_files_button.setDisabled(True)
        self.hide_files_button.setEnabled(True)

    def hide_files(self):
        self.layout.removeWidget(self.scroll_area)
        self.scroll_area.deleteLater()
        self.scroll_area = None
        self.show_files_button.setEnabled(True)
        self.hide_files_button.setDisabled(True)

    def create_playlist(self):
        files = QtGui.QFileDialog.getOpenFileNames(
            self, self.tr("Open Image"),
            "/home/", self.tr(
                "Music Files (*.mp3 *.wav);;Video Files (*.avi *.mkv);;\
                Both (*.mp3 *.wav *.avi *.mkv)"))
        if files:
            text = QtGui.QInputDialog.getText(self, 'Save Playlist',
                                              'Enter playlist name:')
            playlist_name = str(text[0])
            pl = Playlist(playlist_name, files)
            if text:
                pl.save_to_db()

    def splash_screen(self):
        label = QLabel()
        label.setFixedWidth(300)
        label.setFixedHeight(100)
        label.setScaledContents(True)
        logo = QPixmap("viridis.bmp")
        label.setPixmap(logo)
        return label

    def initialize_buttons(self):
        self.next_button = QtGui.QPushButton()
        self.next_button.setIcon(QtGui.QIcon('next.png'))
        self.next_button.setFixedWidth(100)
        self.next_button.clicked.connect(self.next)

        self.previous_button = QtGui.QPushButton()
        self.previous_button.setIcon(QtGui.QIcon('previous.png'))
        self.previous_button.setFixedWidth(100)
        self.previous_button.clicked.connect(self.previous)

        self.show_files_button = QtGui.QPushButton("&Show files")
        self.show_files_button.setFixedWidth(100)
        self.show_files_button.clicked.connect(self.show_files)

        self.hide_files_button = QtGui.QPushButton("&Hide files")
        self.hide_files_button.setFixedWidth(100)
        self.hide_files_button.clicked.connect(self.hide_files)
        self.hide_files_button.setDisabled(True)

    def load_playlist(self):
        text = QtGui.QInputDialog.getText(self, 'Load Playlist',
                                          'Enter playlist name:')
        pl = load_playlist_from_db(str(text[0]))
        self.playlist = pl
        self.remove_initial_screen_widgets()
        self.vp = VideoPlayer(self.playlist.get_files()[0])
        self.layout.addWidget(self.vp)
        btn_layout = QtGui.QHBoxLayout()
        btn_layout.addWidget(self.previous_button)
        btn_layout.addWidget(self.next_button)
        btn_layout.addWidget(self.show_files_button)
        btn_layout.addWidget(self.hide_files_button)
        self.layout.addLayout(btn_layout)

        self.vp.player.mediaObject().finished.connect(self.next)

    def remove_initial_screen_widgets(self):
        self.layout.removeWidget(self.load_playlist_button)
        self.load_playlist_button.deleteLater()
        self.load_playlist_button = None
        self.layout.removeWidget(self.create_playlist_button)
        self.create_playlist_button.deleteLater()
        self.create_playlist_button = None
        self.layout.removeWidget(self.show_playlists_button)
        self.show_playlists_button.deleteLater()
        self.show_playlists_button = None
        if self.scroll_area is not None:
            self.layout.removeWidget(self.scroll_area)
            self.scroll_area.deleteLater()
            self.scroll_area = None
        self.layout.removeWidget(self.splash)
        self.splash.deleteLater()
        self.splash = None

    def fix_layout(self):
        self.layout.removeWidget(self.next_button)
        self.next_button.deleteLater()
        self.next_button = None
        self.layout.removeWidget(self.previous_button)
        self.previous_button.deleteLater()
        self.previous_button = None
        self.layout.removeWidget(self.show_files_button)
        self.show_files_button.deleteLater()
        self.show_files_button = None
        self.layout.removeWidget(self.hide_files_button)
        self.hide_files_button.deleteLater()
        self.hide_files_button = None
        if self.scroll_area is not None:
            self.layout.removeWidget(self.scroll_area)
            self.scroll_area.deleteLater()
            self.scroll_area = None
        self.initialize_buttons()
        self.layout.addWidget(self.vp)
        btn_layout = QtGui.QHBoxLayout()
        btn_layout.addWidget(self.previous_button)
        btn_layout.addWidget(self.next_button)
        btn_layout.addWidget(self.show_files_button)
        btn_layout.addWidget(self.hide_files_button)
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
        self.vp.player.mediaObject().finished.connect(self.next)

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
