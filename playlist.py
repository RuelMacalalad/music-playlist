import csv

class Song:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year}) - {self.genre}"


class Playlist:
    def __init__(self):
        self.songs = []  # Playlist na nagaad ng song
        # Predefined, fixed library of songs
        self.library = [
            Song("The Night We Met", "Lord Huron", 2015, "Hip hop"),
            Song("The one", "Renz", 2020, "Hip hop"),
            Song("train wreck", "Arthur", 2020, "Hip hop"),
            Song("Those Eyes", "New West", 2020, "Hip hop"),
            Song("Yellow", "Cold Play", 2020, "Hip hop"),
            Song("Those Eyes", "New West", 2020, "Pop"),
            Song("Say You Won't Let Go", "James Arthur", 2016, "Pop"),
            Song("Arcade", "Duncan Laurence", 2019, "Pop"),
            Song("You be safe here", "Rico blanco", 2020, "Pop"),
            Song("Car Outside", "James Arthur", 2021, "Pop"),
            Song("Ulan", "Moira Dela Torre", 2019, "Opm"),
            Song("Hanggang Dito Na Lang", "TJ Monterde", 2024, "Opm"),
            Song("Eroplanong Papel", "December Avenue", 2022, "Opm"),
            Song("14", "Silent Sanctuary", 2023, "Opm"),
            Song("Atlantis", "Seafret", 2021, "Opm"),
        ]

    def add_song(self, song):
        """Add a song to the playlist if it's not already present"""
        if song in self.songs:
            print(f"'{song.title}' is already in your playlist.")
        else:
            self.songs.append(song)
            print(f"'{song.title}' has been added to your playlist.")
            self.save_to_csv(song)

    def save_to_csv(self, song):
        with open('song.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([song.title, song.author, song.year, song.genre])

    def remove_song(self):
        """Remove a song from the playlist using the song's index"""
        if not self.songs:
            print("Walang laman playlist mo!, walng maalis eh!")
            return
        self.view_playlist()
        try:
            song_index = int(input("Enter the song number you want to remove: "))
            if 1 <= song_index <= len(self.songs):
                removed_song = self.songs.pop(song_index - 1)  # Remove song gamit index
                print(f"'{removed_song.title}' has been removed from your playlist.")
            else:
                print("Invalid song number hyss. ulitin mo.")
        except ValueError:
            print("mali nmn eh input. Please enter a valid number.")

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
            print("walang laman playlist mo. No songs to play.")
            return
        self.view_playlist()  # Display current playlist.
        try:
            song_index = int(input("Enter the song number to play: "))
            if 1 <= song_index <= len(self.songs):
                print(f"Now playing: '{self.songs[song_index - 1].title}'")
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
                self.add_song(song)  # nagaadd ng song from library to playlist
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def display_menu():
    """Display the menu for the user"""
    print("\n\t\t\t\t\t ----Our Music Playlist Menu:----")
    print("\t\t\t\t\t1. Add Song")
    print("\t\t\t\t\t2. Add Song from Library")
    print("\t\t\t\t\t3. Remove Song")
    print("\t\t\t\t\t4. View Playlist")
    print("\t\t\t\t\t5. Play Song")
    print("\t\t\t\t\t6. Exit")


def main():
    playlist = Playlist()

    while True:
        display_menu()  # Display the menu before every action
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            title = input("Enter the song title: ")
            author = input("Enter the song author: ")
            while True:
                try:
                    year = int(input("Enter the song year: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid year.")
            genre = input("Enter the song genre : ")
            while not genre.replace(" ", "").isalpha():
                print("Invalid input. Please enter a valid genre (letters only).")
                genre = input("Enter the song genre (spaces allowed): ")
            song = Song(title, author, year, genre)
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
            print("Exiting the program. Goodbye Arigato!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
