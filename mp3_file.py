from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, TKEY

class Mp3File():
    KEYS_MAP = {
        # put your translation map here.
    }

    def __init__(self, file_location):
        """ Class representing an mp3 file.
        - Throws IOError if file not found.
        - self.file is None if not mp3"""
        self.file_location = file_location
        self.easyid3 = EasyID3(file_location)
        self.id3 = ID3(file_location)

    def get_key(self):
        return self.id3["TKEY"][0]

    def convert_key(self, old_key):
        return self.KEYS_MAP[old_key]

    def update_key(self):
        tkey = self.get_key()
        new_key = self.KEYS_MAP[tkey]
        self.id3.add(TKEY(encoding=3, text=[new_key]))

    def save_updated_file(self):
        self.id3.save()

    def __str__(self):
        return """Artist: {} Title: {} Key: [{}]""".format(self.easyid3["artist"], self.easyid3["title"], self.id3["TKEY"][0])
