class Song:
    def __init__(self, title, artist, album):
        self.title = title
        self.artist = artist
        self.album = album

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.album})"

    # For comparison in BST and sorting, we will compare songs by title
    def __lt__(self, other):
        return self.title < other.title

    def __eq__(self, other):
        return self.title == other.title

class TreeNode:
    def __init__(self, song):
        self.song = song
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, song):
        if self.root is None:
            self.root = TreeNode(song)
        else:
            self._insert_recursive(self.root, song)

    def _insert_recursive(self, node, song):
        if song < node.song:
            if node.left is None:
                node.left = TreeNode(song)
            else:
                self._insert_recursive(node.left, song)
        else:
            if node.right is None:
                node.right = TreeNode(song)
            else:
                self._insert_recursive(node.right, song)

    def search(self, song):
        return self._search_recursive(self.root, song)

    def _search_recursive(self, node, song):
        if node is None:
            return False
        if node.song == song:
            return True
        elif song < node.song:
            return self._search_recursive(node.left, song)
        else:
            return self._search_recursive(node.right, song)

class MusicApp:
    def __init__(self):
        self.songs = []
        self.bst = BinarySearchTree()

    def add_song(self, title, artist, album):
        song = Song(title, artist, album)
        self.songs.append(song)
        self.songs.sort()  # Sorting for display and linear search
        self.bst.insert(song)  # Insert into the Binary Search Tree
        print(f"'{song}' added to your music library.")

    def delete_song(self, title):
        # Search for the song by title
        song_to_delete = next((s for s in self.songs if s.title == title), None)
        if song_to_delete:
            self.songs.remove(song_to_delete)
            # Rebuild the binary search tree after deletion
            self.bst = BinarySearchTree()
            for s in self.songs:
                self.bst.insert(s)
            print(f"'{song_to_delete}' removed from your music library.")
        else:
            print(f"'{title}' not found in your music library.")

    def display_songs(self):
        if self.songs:
            print("Your music library:")
            for i, song in enumerate(self.songs, 1):
                print(f"{i}. {song}")
        else:
            print("Your music library is empty.")

    def linear_search(self, title):
        for index, song in enumerate(self.songs):
            if song.title == title:
                return index
        return -1

    def binary_search(self, title):
        song_to_search = Song(title, "", "")
        return self.bst.search(song_to_search)

    def search_song(self):
        print("Search for a song:")
        search_method = input("Choose search method - (L)inear or (B)inary: ").strip().lower()
        title = input("Enter song title: ").strip()

        if search_method == 'l':
            result = self.linear_search(title)
            if result != -1:
                print(f"'{self.songs[result]}' found in your music library at position {result + 1}.")
            else:
                print(f"'{title}' not found in your music library.")
        elif search_method == 'b':
            found = self.binary_search(title)
            if found:
                print(f"'{title}' found in your music library.")
            else:
                print(f"'{title}' not found in your music library.")
        else:
            print("Invalid search method selected.")


def main():
    app = MusicApp()

    while True:
        print("\n--- Music App ---")
        print("1. Add Song")
        print("2. Delete Song")
        print("3. Display Songs")
        print("4. Search Song")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            title = input("Enter song title: ").strip()
            artist = input("Enter artist name: ").strip()
            album = input("Enter album name: ").strip()
            app.add_song(title, artist, album)

        elif choice == '2':
            title = input("Enter song title to delete: ").strip()
            app.delete_song(title)

        elif choice == '3':
            app.display_songs()

        elif choice == '4':
            app.search_song()

        elif choice == '5':
            print("Exiting Music App. Goodbye!")
            break

        else:
            print("Invalid choice. Please select again.")


if __name__ == "__main__":
    main()
