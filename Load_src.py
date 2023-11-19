#Load_src.py
import pygame
import os


class Load_src: 
    # src를 불러오는 class
    def __init__(self):
        self.load_images()
        self.load_sounds()


    def load_images(self):
        # 이미지 로드 코드...

        # 이미지 디렉토리 경로
        image_dir = os.path.join("src", "src2", "image")

        # 배경 이미지 로드
        self.background_image = pygame.image.load(os.path.join(image_dir, "background.png"))

        # 캐릭터 이미지 로드
        self.character_image = pygame.image.load(os.path.join(image_dir, "character.png"))

        #말풍선 이미지 로드
        self.say_image = [pygame.image.load(os.path.join(image_dir, "say", "say1.png")),
                          pygame.image.load(os.path.join(image_dir, "say", "say2.png"))]
        
        self.say_finish = pygame.image.load(os.path.join(image_dir, "say", "say3.png"))

        # 옷 이미지 로드
        self.clothes_images = [
            pygame.image.load(os.path.join(image_dir, "clothes", "noneclothes.png")),
            pygame.image.load(os.path.join(image_dir, "clothes", "baegsu.png")),
            pygame.image.load(os.path.join(image_dir, "clothes", "christmas.png")),
            pygame.image.load(os.path.join(image_dir, "clothes", "rock.png")),
            pygame.image.load(os.path.join(image_dir, "clothes", "coat.png"))
            # 추가적인 옷 이미지들...
        ]

        # muff 이미지 로드
        self.muff_images = [
            pygame.image.load(os.path.join(image_dir, "muff", "nonemuff.png")),
            pygame.image.load(os.path.join(image_dir, "muff", "muff.png"))
            # 추가적인 muff 이미지들...
        ]


        # ACC 이미지 로드
        self.ACC_images = [
            pygame.image.load(os.path.join(image_dir, "ACC", "noneacc.png")),
            pygame.image.load(os.path.join(image_dir, "ACC", "bandage.png")),
            pygame.image.load(os.path.join(image_dir, "ACC", "ribon.png")),
            pygame.image.load(os.path.join(image_dir, "ACC", "sunglass.png")),
            pygame.image.load(os.path.join(image_dir, "ACC", "pin.png")),
            pygame.image.load(os.path.join(image_dir, "ACC", "sunglasswithpin.png")),
            pygame.image.load(os.path.join(image_dir, "ACC", "christmashorn.png")),
            pygame.image.load(os.path.join(image_dir, "ACC", "glass.png")),
            pygame.image.load(os.path.join(image_dir, "ACC", "earcover.png")),
            # 추가적인 ACC 이미지들...
        ]

        # make up 이미지 로드
        # eyebrow
        self.eyebrows_images = [
            pygame.image.load(os.path.join(image_dir, "makeup", "eyebrow", "noneyebrow.png")),
            pygame.image.load(os.path.join(image_dir, "makeup", "eyebrow", "eyebrow1.png")),
            pygame.image.load(os.path.join(image_dir, "makeup", "eyebrow", "eyebrow2.png")),
            pygame.image.load(os.path.join(image_dir, "makeup", "eyebrow", "eyebrow3.png")),
            pygame.image.load(os.path.join(image_dir, "makeup", "eyebrow", "eyebrow4.png")),
            pygame.image.load(os.path.join(image_dir, "makeup", "eyebrow", "eyebrow5.png"))
            # 추가적인 eyebrow 이미지들...
        ]

        #eyeline
        self.eyeline_images = [
            pygame.image.load(os.path.join(image_dir, "makeup", "eyeline", "noneyeline.png")),
            pygame.image.load(os.path.join(image_dir, "makeup", "eyeline", "eyeline1.png")),
            pygame.image.load(os.path.join(image_dir, "makeup", "eyeline", "eyeline2.png")),
            pygame.image.load(os.path.join(image_dir, "makeup", "eyeline", "eyeline3.png")),
            pygame.image.load(os.path.join(image_dir, "makeup", "eyeline", "eyeline4.png")),
            pygame.image.load(os.path.join(image_dir, "makeup", "eyeline", "eyeline5.png"))
            # 추가적인 eyebrow 이미지들...
        ]

        # mascara
        self.mascara_images = [
            pygame.image.load(os.path.join(image_dir, "makeup", "mascara", "nonemascara.png")),
            pygame.image.load(os.path.join(image_dir, "makeup", "mascara", "mascara1.png")),
            pygame.image.load(os.path.join(image_dir, "makeup", "mascara", "mascara2.png")),
            pygame.image.load(os.path.join(image_dir, "makeup", "mascara", "mascara3.png")),
            pygame.image.load(os.path.join(image_dir, "makeup", "mascara", "mascara4.png")),
            pygame.image.load(os.path.join(image_dir, "makeup", "mascara", "mascara5.png"))
            # 추가적인 eyebrow 이미지들...
        ]

        # cheek
        self.cheek_images = [
            pygame.image.load(os.path.join(image_dir, "makeup", "cheek", "nonecheek.png")),
            pygame.image.load(os.path.join(image_dir, "makeup", "cheek", "cheek1.png")),
            pygame.image.load(os.path.join(image_dir, "makeup", "cheek", "cheek2.png")),
            pygame.image.load(os.path.join(image_dir, "makeup", "cheek", "cheek3.png")),
            pygame.image.load(os.path.join(image_dir, "makeup", "cheek", "cheek4.png")),
            pygame.image.load(os.path.join(image_dir, "makeup", "cheek", "cheek5.png"))
            # 추가적인 eyebrow 이미지들...
        ]


    def load_sounds(self):
        # 사운드 로드 코드...
        sound_dir = os.path.join("src", "src2", "sound")

        self.choose_sound = pygame.mixer.Sound(os.path.join(sound_dir, "choosesound.mp3"))
        self.finish_sound = pygame.mixer.Sound(os.path.join(sound_dir, "finishsound.mp3"))
        self.fix_sound = pygame.mixer.Sound(os.path.join(sound_dir, "fixsound.mp3"))