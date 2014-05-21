import sqlite3


class Playlist():
    """Generates a new Playlist"""
    def __init__(self, name, files):
        self._name = name
        self._files = files

    def get_name(self):
        return self._name

    def get_files(self):
        return self._files

    def add_file(self, file):
        self._files.append(file)

    def remove_file(self, file):
        try:
            self._files.remove(file)
        except ValueError:
            pass

    def save_to_db(self):
        db_path = sqlite3.connect("playlists.db")
        cursor = db_path.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS playlists
                          (name UNIQUE, files)""")
        files_query = ("""INSERT INTO playlists (name, files)
                          VALUES(?, ?)""")
        files_data = [self.get_name(), "$#$".join(self.get_files())]
        cursor.execute(files_query, files_data)
        db_path.commit()
        db_path.close()

    def delete_from_db(self):
        db_path = sqlite3.connect("playlists.db")
        cursor = db_path.cursor()
        deletion_query = ("DELETE FROM playlists WHERE name = ?")
        deletion_data = ([self.get_name()])
        cursor.execute(deletion_query, deletion_data)
        db_path.commit()
        db_path.close()


def load_playlist_from_db(name):
    """Creates a playlist from a previously saved one"""
    db_path = sqlite3.connect("playlists.db")
    cursor = db_path.cursor()
    selection_query = ("""SELECT files FROM playlists WHERE name = ?""")
    selection_data = [name]
    cursor.execute(selection_query, selection_data)
    files = cursor.fetchone()[0].split("$#$")
    return Playlist(name, files)
