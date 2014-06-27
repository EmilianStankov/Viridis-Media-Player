import os
import enzyme


class Movie():
    """A movie object,
       only has title and duration metadata."""

    def __init__(self, path):
        self._path = path
        with open(self._path, 'rb') as f:
            self._tag = enzyme.MKV(f)

    def get_extension(self):
        return os.path.splitext(self._path)[1]

    def get_filename(self):
        filename = os.path.splitext(self._path)[0].split('/')[-1]
        return filename

    def get_title(self):
        try:
            return self._tag.info.title
        except AttributeError:
            return None

    def get_duration(self):
        try:
            return str(self._tag.info.duration).split('.')[0]
        except AttributeError:
            return None
