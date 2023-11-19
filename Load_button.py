# load_button.py

import pygame
import os

class Load_button:
    def __init__(self):
        self.load_images()
        self.load_sounds()

    def load_images(self):
        # 이미지 로드
        image_dir = os.path.join("src", "src1", "image")
        self.background_image = pygame.image.load(os.path.join(image_dir, "background.png"))
        self.button1_image = pygame.image.load(os.path.join(image_dir, "button", "button1.png"))
        self.button2_image = pygame.image.load(os.path.join(image_dir, "button", "button2.png"))
        self.button3_image = pygame.image.load(os.path.join(image_dir, "button", "button3.png"))
        self.button4_image = pygame.image.load(os.path.join(image_dir, "button", "button4.png"))

        self.button1_light_image = pygame.image.load(os.path.join(image_dir, "button", "button1_light.png"))
        self.button2_light_image = pygame.image.load(os.path.join(image_dir, "button", "button2_light.png"))
        self.button3_light_image = pygame.image.load(os.path.join(image_dir, "button", "button3_light.png"))
        self.button4_light_image = pygame.image.load(os.path.join(image_dir, "button", "button4_light.png"))


        # 각 버튼에 대응하는 온도 범위와 이미지를 딕셔너리로 저장
        self.button_info = {
            "button1": {"temperature": "4 degrees or below", "image": self.button1_image, "light_image": self.button1_light_image},
            "button2": {"temperature": "5~8 degrees", "image": self.button2_image, "light_image": self.button2_light_image},
            "button3": {"temperature": "9~11 degrees", "image": self.button3_image, "light_image": self.button3_light_image},
            "button4": {"temperature": "12~16 degrees", "image": self.button4_image, "light_image": self.button4_light_image}
        }

    def create_overlay(self, base_image, overlay_image, position):
        result_image = base_image.copy()
        result_rect = result_image.get_rect(topleft=position)
        result_image.blit(overlay_image, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        return result_image, result_rect
        

    def load_sounds(self):
        # 사운드 로드 코드...
        sound_dir = os.path.join("src", "src1", "sound")

        self.click_sound = pygame.mixer.Sound(os.path.join(sound_dir, "click.mp3"))