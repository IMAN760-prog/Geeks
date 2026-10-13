class song():
    def __init__(self,lyrics):
        self.lyrics=lyrics
    def sing_me_a_song(self):
     for line in self.lyrics:
        print(line)
zombie=song([" But you see,it`s not me, it`s not my family\n In you head, In your head, they are fightin"])
zombie.sing_me_a_song()