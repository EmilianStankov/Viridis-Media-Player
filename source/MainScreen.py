from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QLabel, QPixmap
from .playlist import Playlist, load_playlist_from_db, get_playlists
from .VideoPlayer import VideoPlayer


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

        self.initialize_navigation_buttons()

        self.initialize_main_buttons()

        self.shortcut_back = QtGui.QShortcut(self)
        self.shortcut_back.setKey(QtGui.QKeySequence('ESC'))
        self.shortcut_back.setContext(QtCore.Qt.ApplicationShortcut)
        self.shortcut_back.activated.connect(self.back_to_main)

        self.layout = QtGui.QVBoxLayout()
        self.layout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.layout.addWidget(self.splash)
        self.layout.addWidget(self.create_playlist_button)
        self.layout.addWidget(self.load_playlist_button)
        self.layout.addWidget(self.show_playlists_button)
        self.setLayout(self.layout)

    def remove(self, widget):
        if widget is not None:
            self.layout.removeWidget(widget)
            widget.deleteLater()
            widget = None

    def back_to_main(self):
        self.vp.player.pause()
        self.remove(self.next_button)
        self.remove(self.previous_button)
        self.remove(self.show_files_button)
        self.remove(self.hide_files_button)
        self.remove(self.scroll_area)
        self.remove(self.vp)

        self.splash = self.splash_screen()

        self.initialize_main_buttons()

        self.initialize_navigation_buttons()

        self.layout.addWidget(self.splash)
        self.layout.addWidget(self.create_playlist_button)
        self.layout.addWidget(self.load_playlist_button)
        self.layout.addWidget(self.show_playlists_button)

    def initialize_main_buttons(self):
        self.create_playlist_button = QtGui.QPushButton("&Create Playlist")
        self.create_playlist_button.setFixedWidth(300)
        self.create_playlist_button.clicked.connect(self.create_playlist)

        self.load_playlist_button = QtGui.QPushButton("&Load Playlist")
        self.load_playlist_button.setFixedWidth(300)
        self.load_playlist_button.clicked.connect(self.load_playlist)

        self.show_playlists_button = QtGui.QPushButton("&Show Playlists")
        self.show_playlists_button.setFixedWidth(300)
        self.show_playlists_button.clicked.connect(self.show_playlists)

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
        self.remove(self.scroll_area)
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
        logo = QPixmap("source/pics/viridis.bmp")
        label.setPixmap(logo)
        return label

    def initialize_navigation_buttons(self):
        self.next_button = QtGui.QPushButton()
        self.next_button.setIcon(QtGui.QIcon('source/pics/next.png'))
        self.next_button.setFixedWidth(100)
        self.next_button.clicked.connect(self.next)

        self.previous_button = QtGui.QPushButton()
        self.previous_button.setIcon(QtGui.QIcon('source/pics/previous.png'))
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
        self.remove(self.load_playlist_button)
        self.remove(self.create_playlist_button)
        self.remove(self.show_playlists_button)
        self.remove(self.scroll_area)
        self.remove(self.splash)

    def fix_layout(self):
        self.remove(self.next_button)
        self.remove(self.previous_button)
        self.remove(self.show_files_button)
        self.remove(self.hide_files_button)
        self.remove(self.scroll_area)
        self.initialize_navigation_buttons()
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
