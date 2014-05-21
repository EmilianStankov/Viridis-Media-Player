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
