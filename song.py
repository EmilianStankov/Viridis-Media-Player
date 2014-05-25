import stagger
from stagger.id3 import *


class Song():
    """A song object, contains the path of the song and its tags,
    comparable by rating"""

    def __init__(self, path):
        self._path = path
        self._tag = stagger.read_tag(self._path)

    def __repr__(self):
        return "{} - {}".format(self.get_artist(), self.get_title())

    def __eq__(self, other):
        return int(self.get_rating()) == int(other.get_rating())

    def __lt__(self, other):
        return int(self.get_rating()) < int(other.get_rating())

    def __le__(self, other):
        return int(self.get_rating()) <= int(other.get_rating())

    def __gt__(self, other):
        return int(self.get_rating()) > int(other.get_rating())

    def __ge__(self, other):
        return int(self.get_rating()) >= int(other.get_rating())

    def __ne__(self, other):
        return int(self.get_rating()) != int(other.get_rating())

    def get_artist(self):
        try:
            return self._tag.artist
        except AttributeError:
            return None

    def get_title(self):
        try:
            return self._tag.title
        except AttributeError:
            return None

    def get_genre(self):
        try:
            return self._tag.genre
        except AttributeError:
            return None

    def get_album(self):
        try:
            return self._tag.album
        except AttributeError:
            return None

    def get_year(self):
        try:
            return self._tag[TYER].text[0]
        except AttributeError:
            return None

    def get_picture(self):
        try:
            return self._tag[APIC]
        except AttributeError:
            return None

    def get_track(self):
        try:
            return self._tag[TRCK].text[0]
        except AttributeError:
            return None

    def get_rating(self):
        try:
            return self._tag.rating
        except AttributeError:
            return None

    def set_artist(self, artist):
        self._tag.artist = artist
        self._tag.write()

    def set_title(self, title):
        self._tag.title = title
        self._tag.write()

    def set_genre(self, genre):
        self._tag.genre = genre
        self._tag.write()

    def set_album(self, album):
        self._tag.album = album
        self._tag.write()

    def set_year(self, year):
        try:
            if 1000 <= int(year) <= 9999:
                self._tag[TYER] = TYER(text=year)
            else:
                self._tag[TYER] = self.get_year()
        except ValueError:
            self._tag[TYER] = self.get_year()
        self._tag.write()

    def set_track(self, track):
        try:
            if int(track) > 0:
                self._tag[TRCK] = track
            else:
                self._tag[TRCK] = self.get_track()
        except ValueError:
            self._tag[TRCK] = self.get_track()
        self._tag.write()

    def set_rating(self, rating):
        try:
            if 0 <= int(rating) <= 5:
                self._tag.rating = rating
            else:
                self._tag.rating = self.get_rating()
        except ValueError:
            self._tag.rating = self.get_rating()
        self._tag.write()
