import os
import json
from pathlib import Path
from typing import List
import music21 as m21

# Constants
ROOT_PATH = Path.cwd()
KERN_DATASET_PATH = f"{ROOT_PATH}/data"
SAVE_DIR = f"{ROOT_PATH}/datasets/"
SINGLE_FILE_DATASET = f"{ROOT_PATH}"
SEQUENCE_LENGTH = 64
MAPPING_PATH = f"{ROOT_PATH}"

# Acceptable durations expressed in quarternote length
# They will map to a time series representation
ACCEPTABLE_DURATIONS = [
    0.25,
    0.5,
    0.75,
    1.0,
    1.5,
    2,
    3,
    4
]

def create_mapping(songs, mapping_path: str):
    """
    This creates the one hot encoding for our model
    """
    mappings = {}
    # identify the vocabulary
    songs = songs.split() # very long list
    vocabulary = list(set(songs))

    # create mappings
    # it is just a dict that maps a symbol to a number
    for i, symbol in enumerate(vocabulary):
        mappings[symbol] = i

    # save vocabulary to JSON
    save_path = os.path.join(mapping_path, "note-mappings.json")
    with open(save_path, "w+") as fp:
        json.dump(mappings, fp, indent=4)


def load_encoded_song(file_path: str) -> str:
    song = ""
    try:
        with open(file_path, "r") as fp:
            song = fp.read()
    except:
        print("aaaaaaaaaa")
    return song

def create_single_file_dataset(dataset_path: str, file_dataset_path: str, sequence_length: int):
    """

    """
    # When we are training our LSTM we must path a fixed length sequence
    # this means at the end of a song we denote that by using this delimiter that is the same length as the song
    new_song_delimiter = "/ " * sequence_length

    songs = ""

    # Load encoded songs and add delimiters
    for path, _, files in os.walk(dataset_path):
        for file in files:
            if file[-3:] == "mds":
                file_path = os.path.join(path, file)
                song = load_encoded_song(file_path)

                # This is gonna be a massive string lol
                songs = songs + song + " " + new_song_delimiter
    
    # Get rid of the last empty space introduced by the new_song_delimiter
    songs = songs[:-1]

    # save string that contains all data
    save_path = os.path.join(file_dataset_path, f"massive_song_file.txt")
    with open(save_path, "w+") as fp:
        fp.write(songs)
    
    return songs


def encode_song(song, time_step=0.25):
    """ 
    This takes a music21 song object and turns it into a time series representation 
    time_step is set to a 16th note by default 
    """

    # We flatten the hierachy of the song into a single list and filter out notes and rests
    for event in song.flat.notesAndRests:
        symbol = ""
        encoded_song = []

        # handle notes and rests
        if isinstance(event, m21.note.Note):
            # This is the unique encoding, since each midi instruction maps to a unique number
            symbol = event.pitch.midi 
        elif isinstance(event, m21.note.Rest):
            # This is the unique encoding, since each midi instruction maps to a unique number
            symbol = "r"

        # convert the note/rest into time series notation
        # the undercore symbol indicates the note is being held
        # the more underscore symbols the longer the note is being held
        steps = int(event.duration.quarterLength / time_step)
        for step in range(steps):
            if step ==  0:
                encoded_song.append(symbol)
            else:
                encoded_song.append("_")

    # cast encoded song into a string
    encoded_song = " ".join(map(str, encoded_song))
    return encoded_song


def transpose(song):
    """ 
    We transpose songs so the model doesnt have to learn so many keys and can generalize better
    around the two transpositions you specifiy
    """
    # get the key from the song directly
    parts = song.getElementsByClass(m21.stream.Part)
    measures_part0 = parts[0].getElementsByClass(m21.stream.Measure)
    key = measures_part0[0][4] # 4 is where the m21 keyobject is stored


    # estimate key using music21
    if not isinstance(key, m21.key.Key):
        key = song.analyze("key")

    # get interval for transposition
    if key.mode == "major":
        interval = m21.interval.Interval(key.tonic, m21.pitch.Pitch("C"))
    elif key.mode == "minor":
        interval = m21.interval.Interval(key.tonic, m21.pitch.Pitch("A"))

    # transpose song by calculated interval
    transposed_song = song.transpose(interval)
    return transposed_song


def has_acceptable_duration(song, accetable_durations) -> bool:
    """ Iterates through our song and ensures all notes/rests are within our acceptable durations"""
    for note in song.flat.notesAndRests:
        if note.duration.quarterLength not in accetable_durations:
            return False
        
    return True

def load_songs_in_kern(dataset_path: str, accetable_durations):
    songs = []
    directories = list(os.walk(dataset_path))

    # go through all the files in dataset and load them with music21
    for root_path, _, files in directories:
        for file in files:
            # Filter out any non .krn files
            if file[-3:] == "krn":
                song_path = os.path.join(root_path, file)
                song = m21.converter.parse(song_path)

                # Filter out songs that have notes/rests that are too long
                if has_acceptable_duration(song, accetable_durations):
                    songs.append(song)


    return songs


def preprocess(dataset_path: str, accpetable_durations, save_dir) -> None:
    print(f"dataset_path: {dataset_path}")

    # Load folk songs
    print("Loading songs.......")
    songs = load_songs_in_kern(dataset_path, accpetable_durations)
    print(f"Loaded {len(songs)} songs")


    for i, song in enumerate(songs):
        # transpose songs to Cmaj/Amin
        transposed_song = transpose(song)
        
        # encode songs with music time series representation
        encoded_song = encode_song(transposed_song)

        # save the song to a text file
        save_path = os.path.join(save_dir, f"{str(i)}.mds")
        with open(save_path, "w+") as fp:
            fp.write(encoded_song)

if __name__ == "__main__":
    preprocess(KERN_DATASET_PATH, ACCEPTABLE_DURATIONS, SAVE_DIR)
    songs = create_single_file_dataset(SAVE_DIR, SINGLE_FILE_DATASET, SEQUENCE_LENGTH)
    create_mapping(songs, MAPPING_PATH)

