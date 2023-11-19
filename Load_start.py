
#Load_src.py
import pygame
import os


class Load_start: 
    def __init__(self):
        self.load_images()
        self.load_sounds()
        


    def load_images(self):
        # 이미지 디렉토리 경로
        image_dir = os.path.join("src", "src0")

        # 배경 이미지 로드
        self.background_image = [
            pygame.image.load(os.path.join(image_dir, "background1.png")),
            pygame.image.load(os.path.join(image_dir, "background2.png"))]
                                 

   

    def load_sounds(self):
        # 사운드 로드 코드...
        sound_dir = os.path.join("src", "src0", "sound")

        self.bgm_start = pygame.mixer.Sound(os.path.join(sound_dir, "woodland_caper.mp3"))
      
         