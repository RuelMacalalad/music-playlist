import pytest
from playlist import Song, Playlist
from unittest.mock import patch

def test_song_init():
    song = Song("The Night We Met", "Lord Huron", 2015, "Hip hop")
    assert song.title == "The Night We Met"
    assert song.author == "Lord Huron"
    assert song.year == 2015
    assert song.genre == "Hip hop"

def test_song_str():
    song = Song("The Night We Met", "Lord Huron", 2015, "Hip hop")
    assert str(song) == "'The Night We Met' by Lord Huron (2015) - Hip hop"

def test_playlist_init():
    playlist = Playlist()
    assert playlist.songs == []
    assert len(playlist.library) > 0

def test_add_song():
    playlist = Playlist()
    song = Song("The Night We Met", "Lord Huron", 2015, "Hip hop")
    playlist.add_song(song)
    assert song in playlist.songs

def test_add_song_already_in_playlist():
    playlist = Playlist()
    song = Song("The Night We Met", "Lord Huron", 2015, "Hip hop")
    playlist.add_song(song)
    playlist.add_song(song)
    assert len(playlist.songs) == 1

def test_remove_song():
    playlist = Playlist()
    song = Song("The Night We Met", "Lord Huron", 2015, "Hip hop")
    playlist.add_song(song)
    with patch('builtins.input', side_effect=['1']):
        playlist.remove_song()
    assert len(playlist.songs) == 0

def test_view_playlist():
    playlist = Playlist()
    song = Song("The Night We Met", "Lord Huron", 2015, "Hip hop")
    playlist.add_song(song)
    playlist.view_playlist()

def test_play_song():
    playlist = Playlist()
    song = Song("The Night We Met", "Lord Huron", 2015, "Hip hop")
    playlist.add_song(song)
    with patch('builtins.input', side_effect=['1']):
        playlist.play_song()

def test_add_from_library():
    playlist = Playlist()
    with patch('builtins.input', side_effect=['1']):
        playlist.add_from_library()
    assert len(playlist.songs) > 0

def test_invalid_input_remove_song():
    playlist = Playlist()
    with patch('builtins.input', side_effect=['1']):
        playlist.remove_song()

def test_invalid_input_play_song():
    playlist = Playlist()
    with patch('builtins.input', side_effect=['1']):
        playlist.play_song()
