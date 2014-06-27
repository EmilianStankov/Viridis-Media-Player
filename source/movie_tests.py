import unittest
from movie import Movie


class TestMovie(unittest.TestCase):
    """Tests for movie objects"""
    def setUp(self):
        self.movie = Movie('../test.mkv')

    def test_get_extension(self):
        self.assertEqual('.mkv', self.movie.get_extension())

    def test_get_filename(self):
        self.assertEqual('test', self.movie.get_filename())

    def test_get_title(self):
        self.assertEqual(None, self.movie.get_title())

    def test_get_duration(self):
        self.assertEqual('0:21:37', self.movie.get_duration())

if __name__ == '__main__':
    unittest.main()
