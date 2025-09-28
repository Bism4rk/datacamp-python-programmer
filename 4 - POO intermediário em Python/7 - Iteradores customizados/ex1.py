import random

class Playlist:
  def __init__(self, songs, shuffle=False):
    self.songs = songs
    self.index = 0
    
    if shuffle:
      random.shuffle(self.songs)
    
  def __iter__(self):
    return self
  
  # Define a magic method to iterate through songs
  def __next__(self):
    if self.index >= len(self.songs):
      raise StopIteration
    
    # Pull the next song, increment index, and return
    song = self.songs[self.index]
    self.index += 1
    return song

# Shuffle a Playlist, use for loop to iterate through
favorite_songs = Playlist(["Ticking", "Tiny Dancer"], shuffle=True)
for song in favorite_songs:
  print(song)


'''
O código acima demonstra como criar um iterador customizado em Python usando uma classe chamada Playlist. A classe aceita uma lista de músicas e uma opção para embaralhar a ordem das músicas. Ele implementa os métodos mágicos __iter__() e __next__() para permitir a iteração sobre as músicas na playlist. Se a opção de embaralhamento for ativada, as músicas são embaralhadas aleatoriamente. O exemplo final mostra como usar um loop for para iterar sobre as músicas na playlist.
'''