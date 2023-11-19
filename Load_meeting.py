#Load_meeting.py
import pygame
import os
import random

class Load_meeting:
    def __init__(self):
        self.load_meet()
        self.load_sounds()

    def load_meet(self):
        # 이미지 로드 코드...

        image_dir = os.path.join("src", "src3")

        #failure
        self.before_image1 = pygame.image.load(os.path.join(image_dir, "fail", "before0.png"))
        self.before_image2 = pygame.image.load(os.path.join(image_dir, "fail", "before1.png"))
        self.before_image3 = pygame.image.load(os.path.join(image_dir, "fail", "before2.png"))
                
        self.failure_image = [
        pygame.image.load(os.path.join(image_dir, "fail", "failure1.png")),
        pygame.image.load(os.path.join(image_dir, "fail", "failure2.png")),
        pygame.image.load(os.path.join(image_dir, "fail", "failure3.png")),
        pygame.image.load(os.path.join(image_dir, "fail", "failure4.png")),
        pygame.image.load(os.path.join(image_dir, "fail", "failure5.png"))]

        self.fail =  random.choice(self.failure_image)

        self.joke_image = pygame.image.load(os.path.join(image_dir, "fail", "joke.png"))
        self.fail_end0 = pygame.image.load(os.path.join(image_dir, "fail", "finish.png"))
        self.fail_end1 = pygame.image.load(os.path.join(image_dir, "fail", "finish.png"))


        #fail_ending   
        self.fail_ending = [ self.before_image1,
                             self.before_image2,
                             self.before_image3,
                             self.fail,
                             self.joke_image,
                             self.fail_end0,
                             self.fail_end1]


        #success
        self.success_image = [pygame.image.load(os.path.join(image_dir, "success", "s1.png")),
                              pygame.image.load(os.path.join(image_dir, "success", "s2.png")),
                              pygame.image.load(os.path.join(image_dir, "success", "s3.png")),
                              pygame.image.load(os.path.join(image_dir, "success", "s4.png")),
                              pygame.image.load(os.path.join(image_dir, "success", "success.png")),
                              pygame.image.load(os.path.join(image_dir, "success", "finish.png"))]



    def load_sounds(self):
        # 사운드 로드 코드...
        sound_dir = os.path.join("src", "src3")

        self.joke_sound = pygame.mixer.Sound(os.path.join(sound_dir, "joke.mp3"))
        self.hey_sound = pygame.mixer.Sound(os.path.join(sound_dir, "hey.mp3"))
        self.success_sound = pygame.mixer.Sound(os.path.join(sound_dir, "sc.mp3"))
        self.failure_sound =pygame.mixer.Sound(os.path.join(sound_dir, "fail.mp3"))
        