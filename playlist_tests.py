import unittest
from playlist import Playlist


class TestPlaylist(unittest.TestCase):
    """Playlist tests"""

    def setUp(self):
        self.pl = Playlist("playlist", ["song_one", "song_two"])

    def test_get_playlist_name(self):
        self.assertEqual(self.pl.get_name(), "playlist")

    def test_get_playlist_files(self):
        self.assertEqual(self.pl.get_files(), ["song_one", "song_two"])

    def test_add_new_file_to_playlist(self):
        self.pl.add_file("song_three")
        self.assertEqual(self.pl.get_files(),
                         ["song_one", "song_two", "song_three"])

    def test_remove_file_from_playlist(self):
        self.pl.remove_file("song_one")
        self.assertEqual(self.pl.get_files(), ["song_two"])

    def test_remove_file_that_is_not_in_playlist(self):
        self.assertRaises(ValueError, self.pl.remove_file("song_three"))


if __name__ == '__main__':
    unittest.main()
