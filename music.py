import pygame

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()

        # Load sound effects
        self.colliding_effect = pygame.mixer.Sound('/home/nemesis/nokia-snake/hit_effect.mp3')
        self.game_over_effect = pygame.mixer.Sound('/home/nemesis/nokia-snake/death_effect.mp3')

    def play_background(self):
        music_file_path = '/home/nemesis/nokia-snake/backgroundmsc.mp3'
        pygame.mixer.music.load(music_file_path)
        pygame.mixer.music.play(-1)  # -1 plays the music in an infinite loop

    def play_game_over(self):
        self.stop_background_music()
        self.game_over_effect.play()

    def play_colliding_effect(self, playback_speed=2.0):
        self.colliding_effect.play()

    def stop_background_music(self):
        pygame.mixer.music.stop()

    def quit(self):
        pygame.mixer.music.stop()
        pygame.mixer.quit()
