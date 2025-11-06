from abc import ABC, abstractmethod

class MediaFile(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class AudioFile(MediaFile):
    def play(self):
        print(self.filename)

    def stop(self):
        print(self.filename)