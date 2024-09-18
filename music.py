import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.current_track = None
        self.playlist = []

    def load_playlist(self, playlist):
        self.playlist = playlist
        print(f"Loaded playlist with {len(self.playlist)} songs.")

    def add_to_playlist(self, song):
        if os.path.exists(song):
            self.playlist.append(song)
            print(f"Added {song} to playlist.")
        else:
            print(f"File {song} does not exist.")

    def play(self, track_number=0):
        if not self.playlist:
            print("The playlist is empty.")
            return

        if track_number >= len(self.playlist) or track_number < 0:
            print("Invalid track number.")
            return

        self.current_track = self.playlist[track_number]
        pygame.mixer.music.load(self.current_track)
        pygame.mixer.music.play()
        print(f"Now playing: {self.current_track}")

    def stop(self):
        pygame.mixer.music.stop()
        print("Music stopped.")

    def pause(self):
        pygame.mixer.music.pause()
        print("Music paused.")

    def unpause(self):
        pygame.mixer.music.unpause()
        print("Music unpaused.")

    def show_playlist(self):
        print("Current Playlist:")
        for index, song in enumerate(self.playlist):
            print(f"{index + 1}: {song}")

def main():
    player = MusicPlayer()
    
    while True:
        print("\nOptions:")
        print("1. Add song to playlist")
        print("2. Load playlist")
        print("3. Play song")
        print("4. Stop music")
        print("5. Pause music")
        print("6. Unpause music")
        print("7. Show playlist")
        print("8. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            song = input("Enter the path of the song to add: ")
            player.add_to_playlist(song)

        elif choice == '2':
            playlist = input("Enter the paths of songs separated by commas: ").split(',')
            playlist = [song.strip() for song in playlist]
            player.load_playlist(playlist)

        elif choice == '3':
            track_number = int(input("Enter track number to play: ")) - 1
            player.play(track_number)

        elif choice == '4':
            player.stop()

        elif choice == '5':
            player.pause()

        elif choice == '6':
            player.unpause()

        elif choice == '7':
            player.show_playlist()

        elif choice == '8':
            print("Exiting music player.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()