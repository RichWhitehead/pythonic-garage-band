class Musician:
  musician_list = []
  def __init__(self, name='none'):
    self.name = name
    Musician.musician_list.append(self)
          
      
  def __str__(self):
    return(f'{self.name}')
        
  def __repr__(self):
    return(f'{self.name}')
        
        
  def to_list(cls):
    return cls.musician_list
    
class Band(Musician):
  list_of_band = []
  
  def __init__(self, band_name, members):
    self.band_name = band_name 
    self.members = members
    Band.list_of_band.append(self.band_name)
    
    
  def __str__(self):
    return(f'{self.band_name} coldplay')
    
  def __repr__(self):
    return(f'{self.band_name} coldplay')
  
  def play_solos(self):
    for member in self.members:
      member.play_solo()
        
  @classmethod
  def to_list(cls):
    print(cls.list_of_band)
    return cls.list_of_band #this should print
      
class Guitarist(Musician):
          
  def get_instrument(self):
    return 'guitar'
       
  def play_solo(self):
    print('whammy bar champion')
    return 'whammy bar champion'

class Bassist(Musician):
  
  def get_instrument(self):
    return 'bass'
  
  def play_solo(self):
    print('drop that bass')
    return 'drop that base'

class Drummer(Musician):
  
        
  def get_instrument(self):
    return 'drums'
      
  def play_solo(self):
    return 'rocking out'

# coldplay = Band('coldplay', ['johnny', 'chris', 'leroy', 'jason', 'hank'])
# leroy = Drummer
johnny = Guitarist('johnny')
jason = Bassist('jason')
# print(johnny.get_instrument())
# print(johnny.play_solo())
coldplay = Band('coldplay', [johnny, jason])
coldplay.play_solos()
# print(coldplay(str))
# print(coldplay(repr))
# mcr = Band('mcr', ['jerad', 'mikey','ray', 'frank']) 
# coldplay.to_list()
# mcr.to_list()







