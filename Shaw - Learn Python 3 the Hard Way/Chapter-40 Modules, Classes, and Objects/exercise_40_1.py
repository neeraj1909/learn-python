"""
Write some more songs using this and make sure you understand that you’re passing a list of
strings as the lyrics.
"""

class  Song(object):
    """docstring for  Song"""
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)



despacito = Song([
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
])

laung_laachi = Song([
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
])


despacito.sing_me_a_song()
print("****************************************************************")
laung_laachi.sing_me_a_song()
