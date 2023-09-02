import sqlite3

class Song:
    all = []

    def __init__(self, name, album):
        self.name = name
        self.album = album
        Song.add_to_all(self)

    @classmethod
    def add_to_all(cls, song):
        cls.all.append(song)

    def save(self, cursor):
        cursor.execute(
            'INSERT INTO song (name, album) VALUES (?, ?)',
            (self.name, self.album)
        )
       

db_connection = sqlite3.connect("mydatabase.db")
db_cursor = db_connection.cursor()


#song_instance = Song("Walk like a talk it", "Culture")
song_instance=Song("Mama" , "Culture")

song_instance.save(db_cursor)

db_connection.commit()

db_cursor.close()
db_connection.close()

