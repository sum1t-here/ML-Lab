class AudioFile:
    def play(self):
        raise NotImplementedError("Subclass must implement this method")
    

class Mp3File(AudioFile):
    def play(self):
        print("Playing Mp3")

class WavFile(AudioFile):
    def play(self):
        print("Playing wav file")

class MkvFile(AudioFile):
    def pause(self):
        print("Pausing")

mp3_file = Mp3File().play()
# Playing Mp3
wav_file = WavFile().play()
# Playing wav file
mkv_file = MkvFile().play()
# raise NotImplementedError("Subclass must implement this method")
# NotImplementedError: Subclass must implement this method