class AudioFile:

    def __init__(self, filename):

        if not filename.endswith(self.ext):
            raise Exception('Formato Inválido')
        
        self.filename = filename

class MP3File(AudioFile):

    ext = 'mp3'
    def play(self):
        print('Tocando arquivo mp3')


class WavFile(AudioFile):

    ext = 'wav'
    def play(self):
        print('Tocando Arquivo WAV')


class OggFile(AudioFile):

    ext = 'ogg'
    def play(self):
        print("Tocando arquivo ogg")

mp3 = MP3File('musica.mp3')
mp3.play()

ogg = OggFile('musica.ogg')
ogg.play()

mp3_falso = MP3File('musica.ogg')
mp3_falso.play()
