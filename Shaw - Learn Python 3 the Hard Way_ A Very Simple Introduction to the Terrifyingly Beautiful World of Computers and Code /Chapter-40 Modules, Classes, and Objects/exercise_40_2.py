"""
Put the lyrics in a separate variable, then pass that variable to the class to use instead.
"""

class  Song(object):
    """docstring for  Song"""
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)



song1 = [
"Sí, sabes que ya llevo un rato mirándote",
"Tengo que bailar contigo hoy (DY)",
"Muéstrame el camino que yo voy (Oh)",
"Tú, tú eres el imán y yo soy el metal",
"Me voy acercando y voy armando el plan",
"Solo con pensarlo se acelera el pulso (Oh yeah)",
"Ya, ya me está gustando más de lo normal",
"Todos mis sentidos van pidiendo más",
"Esto hay que tomarlo sin ningún apuro",
"Despacito"
]

song2 = [
"ve tu long",
"ve mai laachi",
"tere piche aa gawachi",
"ve mai laachi",
"tere piche aa gawachi",
"tere ishq ne mari",
"kudi kach di kuwari",
"ve mai chande de",
"pahada wali shym ve mundeyua",
"sundli sundli nainna",
"vich tera naam mundeya",
]


despacito = Song(song1)

laung_laachi = Song(song2)


despacito.sing_me_a_song()
print("****************************************************************")
laung_laachi.sing_me_a_song()
