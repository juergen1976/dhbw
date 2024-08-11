class Song:
    def __init__(self, title, artist, album, year):
        self.title = title
        self.artist = artist
        self.album = album
        self.year = year

    def __lt__(self, other):
        return self.title < other.title if isinstance(other, Song) else self.year < other

    def __gt__(self, other):
        return self.title > other.title if isinstance(other, Song) else self.year > other

    def __eq__(self, other):
        return self.title == other.title if isinstance(other, Song) else self.year == other

def add_song(library):
    title = input("Enter the title: ")
    artist = input("Enter the artist: ")
    album = input("Enter the album: ")
    year = int(input("Enter the year: "))
    library.append(Song(title, artist, album, year))

def delete_song(library):
    title = input("Enter the title of the song to delete: ")
    for i, song in enumerate(library):
        if song.title == title:
            del library[i]
            print("Song deleted successfully!")
            return
    print("Song not found.")

def linear_search(library, term):
    for song in library:
        if any([term in str(getattr(song, attr)) for attr in ['title', 'artist', 'album', 'year']]):
            print(song)

def binary_search_tree(library, sort_by='title'):
    class Node:
        def __init__(self, song):
            self.left = None
            self.right = None
            self.song = song

        def insert(self, song):
            if self.song > song:
                if self.left is None:
                    self.left = Node(song)
                else:
                    self.left.insert(song)
            elif self.song < song:
                if self.right is None:
                    self.right = Node(song)
                else:
                    self.right.insert(song)

        def inorder_traversal(self):
            if self.left is not None:
                self.left.inorder_traversal()
            print(self.song)
            if self.right is not None:
                self.right.inorder_traversal()

    root = None
    for song in library:
        if root is None:
            root = Node(song)
        else:
            root.insert(song)

    def binary_search(node, term):
        if node is None or node.song == term:
            return node

        if node.song > term:
            return binary_search(node.left, term)

        return binary_search(node.right, term)

    def search(tree, term):
        root = tree
        current = binary_search(root, term)

        if current is not None:
            current.inorder_traversal()
        else:
            print("Song not found.")

        if sort_by == 'year':
            library.sort(key=lambda x: x.year)
        else:
            library.sort()

        search(root, term)

def main():
    library = []

    while True:
        print("\nChoose an option:")
        print("1. Add song")
        print("2. Delete song")
        print("3. Linear search")
        print("4. Binary search (title)")
        print("5. Binary search (year)")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_song(library)
        elif choice == 2:
            delete_song(library)
        elif choice == 3:
            term = input("Enter the search term: ")
            linear_search(library, term)
        elif choice == 4 or choice == 5:
            sort_by = 'title' if choice == 4 else 'year'
            binary_search_tree(library, sort_by)
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()