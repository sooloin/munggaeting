# duribun.py
import pygame
import os
import sys
import meeting as mt

BACKGROUND_CHANGE_INTERVAL = 1295
CONSTANTS_CLOCK = 60

class stage2_5:
    def __init__(self, selected_temperature, selection_index):
        pygame.init()
        pygame.mixer.init()
        #pygame.mixer.set_num_channels(1) 
        self.selected_temperature = selected_temperature  # 사용자가 선택한 온도
        self.selected_clothes = selection_index  # 게임 내에서 선택된 정답 인덱스
        self.screen_width = 800  # 창 크기
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("뭉개팅")

        self.setup_positions()
        self.load_images()
        self.load_sound()
        self.clock = pygame.time.Clock()

        pygame.mixer.set_num_channels(3)
        pygame.mixer.Channel(0).play(self.ddubuk_sound)  
  
        
        self.index = 0
        self.last_background_change_time = pygame.time.get_ticks()
        self.image_finised = None
        self.running = True
        self.done_time = None
        

    def load_sound(self):
        sound_dir = os.path.join("src", "src_duribun")
        self.ddubuk_sound = pygame.mixer.Sound(os.path.join(sound_dir, "ddubuk.mp3"))
        self.shuk_sound = pygame.mixer.Sound(os.path.join(sound_dir, "shuk.mp3"))
        self.Ding_sound = pygame.mixer.Sound(os.path.join(sound_dir, "Ding.mp3"))
    
    def load_images(self):
        # 이미지 디렉토리 경로
        image_dir = os.path.join("src", "src_duribun")

        # 걷는 이미지 로드
        self.image = [
            pygame.image.load(os.path.join(image_dir, "working", "w1.png")),
            pygame.image.load(os.path.join(image_dir, "working", "w2.png")),
            pygame.image.load(os.path.join(image_dir, "working", "w3.png")),
            pygame.image.load(os.path.join(image_dir, "duribun", "duri1.png")),
            pygame.image.load(os.path.join(image_dir, "duribun", "duri2.png")),
            pygame.image.load(os.path.join(image_dir, "duribun", "duri3.png")),
            pygame.image.load(os.path.join(image_dir, "duribun", "duri4.png")),
            pygame.image.load(os.path.join(image_dir, "duribun", "duri5.png")),
            pygame.image.load(os.path.join(image_dir, "duribun", "duri6.png"))]

    # 변수의 초기값을 설정하면서, 게임이 초기 상태로 돌아감!
    def setup_positions(self):  # 위치
        self.button_x = 0
        self.button_y = 0
        self.background_x = 0
        self.background_y = 0

    # working
    def working_screen(self):
        self.screen.fill((255, 255, 255))
        if self.index < len(self.image):
            current_background = self.image[self.index]
            self.screen.blit(current_background, (self.background_x, self.background_y))
        pygame.display.flip() 

    def working_change_background(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_background_change_time > BACKGROUND_CHANGE_INTERVAL:
            if self.index < len(self.image) - 1:  # 이미지 인덱스가 최대값에 도달하지 않았을 때
                self.index += 1
                self.last_background_change_time = current_time

                # 이미지 인덱스에 따라 다른 효과음 재생
                if self.index == 4 or self.index == 5 or self.index == 6 :
                    pygame.mixer.Channel(1).play(self.shuk_sound)
                
                elif self.index == 7 :
                    pygame.mixer.Channel(0).play(self.Ding_sound)  

                elif self.index == 8 :
                
                    self.running = False
                    stage3 = mt.MeetingMan(self.selected_temperature, self.selected_clothes)
                    stage3.run()

                elif self.index >= len(self.image) - 1:
                    self.image_finised = True  # working이 끝났음을 표시
            
                

    

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def working_update(self):
        self.working_change_background()

    def working_render(self):
        self.working_screen()



    def working(self):
        self.working_update()
        self.working_render()
        # working이 끝나면 duribun 실행
        if self.image_finised and self.done_time is None:
            self.done_time = pygame.time.get_ticks()

    
    def run(self):
        while self.running:
            self.handle_events()
            self.working()
            self.clock.tick(CONSTANTS_CLOCK)



     
