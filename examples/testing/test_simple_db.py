import os
import sqlite3
import unittest

import simple_db

class TestMusicDatabase(unittest.TestCase):
    """
    Test Music database
    """

    def setUp(self):
        """
        Setup the temporary database
        """
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE albums
        (title text, artist test, release_date text, publisher text, media_type text)
        """)

        cursor.execute("INSERT INTO albums VALUES ('Glow', 'Andy Hunter', '7/24/2021','Xplore Records', 'MP3')")
        conn.commit()
        albums = [
            ('Exodus', 'Andy Hunter', '7/9/2020', 'Sparrow Records', 'CD'),
            ('Until We Have Faces', 'Redder', '2/1/2011', 'Essential Records', 'CD'),
            ('The End is Where We Begin', 'Thousand Foot Krutch', '4/7/2012', 'TipsMusic', 'CD'),
            ('The Good Life', 'Trip Lee', '4/20/2012', 'Reach Records', 'CD')
        ]
        cursor.executemany("INSERT INTO albums VALUES (?, ?, ?, ?, ?)", albums)
        conn.commit()

    # def tearDown(self):
    #     """
    #     Delete the database
    #     """
    #     os.remove("mydatabase.db")

    def test_updating_artist(self):
        simple_db.update_artist('Red', 'Redder')
        actual = simple_db.select_all_albums('Redder')
        expected = [('Until We Have Faces', 'Redder', '2/1/2011', 'Essential Records', 'CD')]
        print(actual)
        print(expected)
        self.assertListEqual(expected, actual)

    def test_artist_does_not_exist(self):
        result = simple_db.select_all_albums('Redder')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()