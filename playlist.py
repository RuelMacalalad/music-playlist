class Playlist:
    def __init__(self):
        self.songs = []  # Playlist na nagaad ng song
        # Predefined, fixed library of songs
        self.library = [
            "The Night We Met",
            "Those Eyes",
            "Say You Won't Let Go",
            "Ulan",
            "Arcade"
        ]

    def add_song(self, song):
        """Add a song to the playlist if it's not already present"""
        if song in self.songs:
            print(f"'{song}' is already in your playlist.")
        else:
            self.songs.append(song)
            print(f"'{song}' has been added to your playlist.")  # sa playlist lang nagaad

    def remove_song(self):
        """Remove a song from the playlist using the song's index"""
        if not self.songs:
            print("Walang laman playlist mo!, walng maalis eh!.")
            return
        self.view_playlist()  # Display the playlist
        try:
            song_index = int(input("Enter the song number you want to remove: "))
            if 1 <= song_index <= len(self.songs):
                removed_song = self.songs.pop(song_index - 1)  # Remove song by index
                print(f"'{removed_song}' has been removed from your playlist.")
            else:
                print("Invalid song number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def view_playlist(self):
        """View all songs in the playlist"""
        if not self.songs:
            print("Your playlist is empty.")
        else:
            print("Your Playlist:")
            for idx, song in enumerate(self.songs, 1):
                print(f"{idx}. {song}")

    def play_song(self):
        """Play a song from the playlist"""
        if not self.songs:
            print("Your playlist is empty. No songs to play.")
            return
        self.view_playlist()  # Display current playlist
        try:
            song_index = int(input("Enter the song number to play: "))
            if 1 <= song_index <= len(self.songs):
                print(f"Now playing: '{self.songs[song_index - 1]}'")
            else:
                print("Invalid song number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def add_from_library(self):
        """Add a song from the library to the playlist"""
        print("\nAvailable Songs in the Library:")
        for idx, song in enumerate(self.library, 1):
            print(f"{idx}. {song}")
        try:
            choice = int(input("Select a song number to add to your playlist: "))
            if 1 <= choice <= len(self.library):
                song = self.library[choice - 1]
                self.add_song(song)  # Add song from library to playlist
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def display_menu():
    """Display the menu for the user"""
    print("\nMusic Playlist Menu:")
    print("1. Add Song")
    print("2. Add Song from Library")
    print("3. Remove Song")
    print("4. View Playlist")
    print("5. Play Song")
    print("6. Exit")


def main():
    playlist = Playlist()

    while True:
        display_menu()  # Display the menu before every action
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            song = input("Enter the song name you want to add: ")
            playlist.add_song(song)  # Add song to playlist directly
        elif choice == '2':
            playlist.add_from_library()  # Add a song from the library to playlist
        elif choice == '3':
            playlist.remove_song()  # Remove a song from the playlist
        elif choice == '4':
            playlist.view_playlist()  # View all songs in the playlist
        elif choice == '5':
            playlist.play_song()  # Play a song from the playlist
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
