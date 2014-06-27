import unittest
from song import Song


class TestSong(unittest.TestCase):
    """Tests for song objects"""
    def setUp(self):
        self.song = Song("../test.mp3")
        self.song.set_artist("artist")
        self.song.set_title("title")
        self.song.set_genre("genre")
        self.song.set_album("album")
        self.song.set_year("2014")
        self.song.set_track("10")
        self.song.set_rating("5")

    def tearDown(self):
        self.song.set_artist("artist")
        self.song.set_title("title")
        self.song.set_genre("genre")
        self.song.set_album("album")
        self.song.set_year("2014")
        self.song.set_track("10")
        self.song.set_rating("5")

    def test_get_artist(self):
        self.assertEqual("artist", self.song.get_artist())

    def test_get_title(self):
        self.assertEqual("title", self.song.get_title())

    def test_get_genre(self):
        self.assertEqual("genre", self.song.get_genre())

    def test_get_album(self):
        self.assertEqual("album", self.song.get_album())

    def test_get_year(self):
        self.assertEqual('2014', self.song.get_year())

    def test_get_track(self):
        self.assertEqual('10', self.song.get_track())

    def test_get_rating(self):
        self.assertEqual('5', self.song.get_rating())

    def test_set_rating_bigger_than_allowed(self):
        self.song.set_rating('100')
        self.assertEqual('5', self.song.get_rating())

    def test_set_rating_smaller_than_allowed(self):
        self.song.set_rating('-123')
        self.assertEqual('5', self.song.get_rating())

    def test_set_valid_rating(self):
        self.song.set_rating('2')
        self.assertEqual('2', self.song.get_rating())

    def test_set_artist(self):
        self.song.set_artist("new_artist")
        self.assertEqual("new_artist", self.song.get_artist())

    def test_set_title(self):
        self.song.set_title("new_title")
        self.assertEqual("new_title", self.song.get_title())

    def test_set_genre(self):
        self.song.set_genre("new_genre")
        self.assertEqual("new_genre", self.song.get_genre())

    def test_set_album(self):
        self.song.set_album("new_album")
        self.assertEqual("new_album", self.song.get_album())

    def test_set_valid_year(self):
        self.song.set_year("2005")
        self.assertEqual("2005", self.song.get_year())

    def test_set_invalid_year(self):
        self.song.set_year("20000")
        self.assertEqual("2014", self.song.get_year())

        self.song.set_year("10")
        self.assertEqual("2014", self.song.get_year())

        self.song.set_year("-123")
        self.assertEqual("2014", self.song.get_year())

        self.song.set_year("asda")
        self.assertEqual("2014", self.song.get_year())

    def test_set_valid_track(self):
        self.song.set_track('2')
        self.assertEqual('2', self.song.get_track())

    def test_set_invalid_track(self):
        self.song.set_track("asd")
        self.assertEqual('10', self.song.get_track())

        self.song.set_track('-1')
        self.assertEqual('10', self.song.get_track())

    def test_compare_tracks_by_rating(self):
        song2 = Song("../test.mp3")
        song2.set_artist("artist2")
        song2.set_title("title2")
        song2.set_genre("genre2")
        song2.set_album("album2")
        song2.set_year("2014")
        song2.set_track("11")
        song2.set_rating("1")

        self.assertTrue(song2 < self.song)
        self.assertFalse(song2 > self.song)
        self.assertFalse(song2 >= self.song)
        self.assertFalse(song2 == self.song)
        self.assertTrue(song2 <= self.song)
        self.assertTrue(song2 != self.song)


if __name__ == '__main__':
    unittest.main()
