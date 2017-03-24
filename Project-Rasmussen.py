from kivy.app import App
#kivy required 1.8.0
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader


class Main(BoxLayout):

    def sound1(self):
        print 'Piano note A played!'
        sound = SoundLoader.load('sounds/68437_pinkyfinger_piano-a.wav')
        if sound:
            print ('Sound found at %s' %sound.source)
        sound.volume = 1
        sound.play()

    def sound2(self):
        print 'Piano note B played!'
        sound = SoundLoader.load('sounds/68438_pinkyfinger_piano-b.wav')
        if sound:
            print ('Sound found at %s' %sound.source)
        sound.volume = 1
        sound.play()

    def sound3(self):
        print 'Piano note C played!'
        sound = SoundLoader.load('sounds/68441_pinkyfinger_piano-c.wav')
        if sound:
            print ('Sound found at %s' %sound.source)
        sound.volume = 1
        sound.play()

    def sound4(self):
        print 'Piano note D played!'
        sound = SoundLoader.load('sounds/68442_pinkyfinger_piano-d.wav')
        if sound:
            print ('Sound found at %s' %sound.source)
        sound.volume = 1
        sound.play()

    def sound5(self):
        print 'Piano note E played!'
        sound = SoundLoader.load('sounds/68443_pinkyfinger_piano-e.wav')
        if sound:
            print ('Sound found at %s' %sound.source)
        sound.volume = 1
        sound.play()

    def sound6(self):
        print 'Piano note F played!'
        sound = SoundLoader.load('sounds/68445_pinkyfinger_piano-f.wav')
        if sound:
            print ('Sound found at %s' %sound.source)
        sound.volume = 1
        sound.play(self)

class projectApp(App):
    def build(self):
        self.title = "Rasmussen's Project"
        return Main()

if __name__ == '__main__':
    projectApp().run()
