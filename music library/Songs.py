
class Song:
        """Class to represent a song

        Attributes :
                Title(str) : the title of the song
                Artist(object) : An artist object represent song creator
                Duration(int) : The duration of the song in seconds my be zero
        """

        def __init__(self , title , artist , duration=0):
                """Song init method

                Args:
                  title(str) : Initialises the title attribute
                  artist : An artist object representing song's creator
                  duration(optional[int]) : Initial value for the duration attribute.
                  will be default to zero if not specified
                """
                self.title = title
                self.artist = artist
                self.duration = duration

class Album:
        """Class to represent an Album , using it's track list
        
        Attributes:
                Album_name(str) : The name of the Album
                Year(int) : The year album was released
                Artist(artist(object)) : THe artist responsible for album
                        if not specified , the artist will default to an artist
                        with the name "various Artist" 
                tracks(List[Songs]): A list of the Songs in Album
        Methods:
                addsong : used to add new song to album track list
        """
        def __init__(self , name , year , artist=None):
                self.name = name
                self.year = year
                if artist is None:
                        self.artist = artist("Various Artists")
                else:
                        self.artist = artist

                self.tracks = []

        def add_song(self , song , position=None):
                """Adds a song to the track list
                
                Args
                        song(song(object)) : A song to add.
                        Position(optional[int]) : IF specified , the song wiil be added to that posiition
                        in the track list - Inserting it between other songs if necessary
                        Otherwise, the song will be added to the end of the list
                """
                if position is None :
                        self.tracks.append(song)
                else:
                        self.tracks.insert(position , song)

class Artist:
        """Basic class to store artist details.
        
        Attributes:
                name (str) : The name of the Artist.
                albums (list[Album]): A list of the albums by this artist.
                        the list includes only those albums in this collection , it is 
                        not an exhaustive list of the artist's publishedalbums.
        Methods :
                Add_album: Use to add a new album to artist's album list.
        """
        def __init__(self , name):
                self.name = name
                self.albums=[]
        def Add_album(self , Album):
                """Add a new album to the list
                Arg:
                        album (Album) : Album object to added to the list
                                If the album is already present , it will not added again (although this is yet to implemented).
                """
                self.albums.append(Album)

def load_data():
        new_artist = None
        new_album = None
        artist_list = []

        with open("albums.txt" , "r") as albums:
                for line in albums:
                        #data row should consist of (artist , album , year , song)
                        artist_field, album_field, year_field, song_field= tuple(line.strip('\n').split('\t'))
                        year_field =int(year_field)
                        print("{}:{}:{}:{}".format(artist_field,album_field,year_field,song_field))

                        if new_artist is None :
                                new_artist = Artist(artist_field)
                        elif new_artist.name != artist_field :
                                # We've just read details from new artist
                                # Store the current album in the current artist collection then create new artist object
                                new_artist.Add_album(new_album)
                                artist_list.append(new_artist)
                                new_artist = Artist(artist_field)
                                new_album = None

                        if new_album is None :
                                new_album = Album(album_field , year_field , artist_field)
                        elif new_album.name != album_field :
                                # we've just read details from new album for the current artist
                                # store the current album in the current artist's collection then create new album object
                                new_artist.Add_album(new_album)
                                new_album= Album(album_field , year_field , new_artist)

                        # create new song object and add it to the current album's collection
                        new_song = Song(song_field , new_artist)
                        new_album.add_song(new_song)
                # After read last line of the text file , we will have an artist and album that haven't been stored - process them now
                if new_artist is not None:
                        if new_album is not None:
                                 new_artist.Add_album(new_album)
                        artist_list.append(new_artist)
        
        return artist_list

def create_checkfile(artist_list):
        """Create a check file from the object data for comparison with the original file"""
        with open("checkfile.txt" , 'w') as checkfile:
                for new_artist in artist_list:
                        for new_album in new_artist.albums:
                                for new_song in new_album.tracks:
                                        print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist , new_album , new_song),
                                        file=checkfile)




if __name__ == '__main__':
        artist = load_data()
        print("{}".format(len(artist)))

        create_checkfile(artist)

    