import os

class Song:
    def __init__(self, title, artist, album):
        self.title = title
        self.artist = artist
        self.album = album

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.album})"

    def __lt__(self, other):
        return self.title < other.title

    def __eq__(self, other):
        return self.title == other.title

class RedBlackNode:
    def __init__(self, song):
        self.song = song
        self.color = "RED"  # All newly inserted nodes are red by default
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = RedBlackNode(None)
        self.NIL.color = "BLACK"
        self.root = self.NIL

    def insert(self, song):
        new_node = RedBlackNode(song)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.song < current.song:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.song < parent.song:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = "RED"
        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node != self.root and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.left_rotate(node.parent.parent)

        self.root.color = "BLACK"

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def search(self, song):
        return self._search_recursive(self.root, song)

    def _search_recursive(self, node, song):
        if node == self.NIL or node.song == song:
            return node != self.NIL
        if song < node.song:
            return self._search_recursive(node.left, song)
        else:
            return self._search_recursive(node.right, song)

class MusicApp:
    FILENAME = "songs.csv"

    def __init__(self):
        self.songs = []
        self.rbt = RedBlackTree()
        self.load_songs()

    def load_songs(self):
        """Load songs from a file when the app starts."""
        if os.path.exists(self.FILENAME):
            with open(self.FILENAME, 'r') as file:
                for line in file:
                    title, artist, album = line.strip().split(',')
                    song = Song(title, artist, album)
                    self.songs.append(song)
                    self.rbt.insert(song)  # Insert into the Red-Black Tree
            print(f"{len(self.songs)} songs loaded from {self.FILENAME}.")
        else:
            print("No songs found. Starting with an empty music library.")

    def save_songs(self):
        """Save all songs to a file."""
        with open(self.FILENAME, 'w') as file:
            for song in self.songs:
                file.write(f"{song.title},{song.artist},{song.album}\n")
        print(f"{len(self.songs)} songs saved to {self.FILENAME}.")

    def add_song(self, title, artist, album):
        song = Song(title, artist, album)
        self.songs.append(song)
        self.rbt.insert(song)  # Insert into the Red-Black Tree
        self.save_songs()  # Save after adding a song
        print(f"'{song}' added to your music library.")

    def delete_song(self, title):
        song_to_delete = next((s for s in self.songs if s.title == title), None)
        if song_to_delete:
            self.songs.remove(song_to_delete)
            # Note: Red-Black Tree deletion would require a delete operation to be implemented
            self.save_songs()  # Save after deleting a song
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
        return self.rbt.search(song_to_search)

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

    def sort_songs(self, algorithm):
        if algorithm == '1':
            self.bubble_sort()
        elif algorithm == '2':
            self.insertion_sort()
        elif algorithm == '3':
            self.songs = self.merge_sort(self.songs)
        elif algorithm == '4':
            self.quick_sort(0, len(self.songs) - 1)
        else:
            print("Invalid choice.")
            return

        print(f"Songs sorted using algorithm {algorithm}.")
        self.display_songs()
        self.save_songs()  # Save the sorted list to file

    def bubble_sort(self):
        n = len(self.songs)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if self.songs[j] > self.songs[j + 1]:
                    self.songs[j], self.songs[j + 1] = self.songs[j + 1], self.songs[j]
                    swapped = True
            if not swapped:
                break
        print("Sorted using Bubble Sort.")

    def insertion_sort(self):
        for i in range(1, len(self.songs)):
            key_song = self.songs[i]
            j = i - 1
            while j >= 0 and key_song < self.songs[j]:
                self.songs[j + 1] = self.songs[j]
                j -= 1
            self.songs[j + 1] = key_song
        print("Sorted using Insertion Sort.")

    def merge_sort(self, array):
        if len(array) <= 1:
            return array

        mid = len(array) // 2
        left_half = self.merge_sort(array[:mid])
        right_half = self.merge_sort(array[mid:])

        return self.merge(left_half, right_half)

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def quick_sort(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort(low, pi - 1)
            self.quick_sort(pi + 1, high)

    def partition(self, low, high):
        pivot = self.songs[high]
        i = low - 1

        for j in range(low, high):
            if self.songs[j] < pivot:
                i += 1
                self.songs[i], self.songs[j] = self.songs[j], self.songs[i]

        self.songs[i + 1], self.songs[high] = self.songs[high], self.songs[i + 1]
        return i + 1


def main():
    app = MusicApp()

    while True:
        print("\n--- Music App ---")
        print("1. Add Song")
        print("2. Delete Song")
        print("3. Display Songs")
        print("4. Search Song")
        print("5. Sort Songs using Bubble Sort")
        print("6. Sort Songs using Insertion Sort")
        print("7. Sort Songs using Merge Sort")
        print("8. Sort Songs using Quick Sort")
        print("9. Exit")

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
            app.sort_songs('1')

        elif choice == '6':
            app.sort_songs('2')

        elif choice == '7':
            app.sort_songs('3')

        elif choice == '8':
            app.sort_songs('4')

        elif choice == '9':
            print("Exiting Music App. Goodbye!")
            break

        else:
            print("Invalid choice. Please select again.")


if __name__ == "__main__":
    main()