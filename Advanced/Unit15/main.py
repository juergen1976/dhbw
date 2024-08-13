import json
import os

class Song:
    def __init__(self, name, artist, album, genre, duration):
        self.name = name
        self.artist = artist
        self.album = album
        self.genre = genre
        self.duration = duration

    def __str__(self):
        return f"{self.name} by {self.artist} - Album: {self.album}, Genre: {self.genre}, Duration: {self.duration}"

    def to_dict(self):
        return {
            "name": self.name,
            "artist": self.artist,
            "album": self.album,
            "genre": self.genre,
            "duration": self.duration
        }

    @staticmethod
    def from_dict(data):
        return Song(data['name'], data['artist'], data['album'], data['genre'], data['duration'])

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __str__(self):
        return f"Playlist: {self.name}, Songs: {len(self.songs)}"

    def to_dict(self):
        return {
            "name": self.name,
            "songs": [song.to_dict() for song in self.songs]
        }

    @staticmethod
    def from_dict(data):
        playlist = Playlist(data['name'])
        playlist.songs = [Song.from_dict(song_data) for song_data in data['songs']]
        return playlist

class MusicApp:
    def __init__(self, data_file='music_data.json'):
        self.data_file = data_file
        self.songs = []
        self.playlists = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.songs = [Song.from_dict(song_data) for song_data in data.get('songs', [])]
                self.playlists = [Playlist.from_dict(pl_data) for pl_data in data.get('playlists', [])]
            print("Data loaded successfully.")
        else:
            print("No data file found. Starting with an empty database.")

    def save_data(self):
        data = {
            "songs": [song.to_dict() for song in self.songs],
            "playlists": [playlist.to_dict() for playlist in self.playlists]
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=4)
        print("Data saved successfully.")

    def add_song(self):
        name = input("Enter song name: ")
        artist = input("Enter artist name: ")
        album = input("Enter album name: ")
        genre = input("Enter genre: ")
        duration = input("Enter duration (mm:ss): ")
        song = Song(name, artist, album, genre, duration)
        self.songs.append(song)
        print(f"Added song: {song}")

    def create_playlist(self):
        name = input("Enter playlist name: ")
        playlist = Playlist(name)
        self.playlists.append(playlist)
        print(f"Created playlist: {playlist}")

    def add_song_to_playlist(self):
        playlist_name = input("Enter the name of the playlist: ")
        playlist = next((pl for pl in self.playlists if pl.name == playlist_name), None)
        if not playlist:
            print("Playlist not found.")
            return

        song_name = input("Enter the name of the song to add: ")
        song = next((s for s in self.songs if s.name == song_name), None)
        if not song:
            print("Song not found.")
            return

        playlist.add_song(song)
        print(f"Added {song.name} to playlist {playlist.name}")

    def search_songs(self):
        search_term = input("Enter song name or artist to search: ")
        results = [song for song in self.songs if search_term.lower() in song.name.lower() or search_term.lower() in song.artist.lower()]
        if results:
            print("Search Results:")
            for song in results:
                print(song)
        else:
            print("No songs found.")

    def sort_songs(self):
        criterion = input("Sort by 'name' or 'artist': ").lower()
        if criterion == 'name':
            self.songs.sort(key=lambda song: song.name.lower())
        elif criterion == 'artist':
            self.songs.sort(key=lambda song: song.artist.lower())
        else:
            print("Invalid sort criterion.")
            return
        print("Songs sorted.")
        self.display_all_songs()

    def display_all_songs(self):
        if not self.songs:
            print("No songs available.")
        else:
            for song in self.songs:
                print(song)

    def display_playlists(self):
        if not self.playlists:
            print("No playlists available.")
        else:
            for playlist in self.playlists:
                print(playlist)
                for song in playlist.songs:
                    print(f"  - {song}")

    def main_menu(self):
        while True:
            print("\n--- Music App ---")
            print("1. Add New Song")
            print("2. Create Playlist")
            print("3. Add Song to Playlist")
            print("4. Search Songs")
            print("5. Sort Songs")
            print("6. Display All Songs")
            print("7. Display Playlists")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_song()
            elif choice == '2':
                self.create_playlist()
            elif choice == '3':
                self.add_song_to_playlist()
            elif choice == '4':
                self.search_songs()
            elif choice == '5':
                self.sort_songs()
            elif choice == '6':
                self.display_all_songs()
            elif choice == '7':
                self.display_playlists()
            elif choice == '8':
                self.save_data()
                print("Exiting the app.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = MusicApp()
    app.main_menu()