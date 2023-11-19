#start.py
import pygame
import Load_start 
import explain_the_game as etg
import sys

# 상수 정의
CONSTANTS_CLOCK = 60
BACKGROUND_CHANGE_INTERVAL = 500

class Hell_of_solo:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen_width = 800  # 창 크기
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("뭉개팅")

        self.setup_positions()
        self.load_src0 = Load_start.Load_start()
        #pygame.mixer.set_num_channels(2) 
        pygame.mixer.Channel(0).play(self.load_src0.bgm_start)
        self.clock = pygame.time.Clock()
        self.stage_index = 0
        self.last_background_change_time = pygame.time.get_ticks()
        self.running = True
        self.stage_finished = False  

        
    # 변수의 초기값을 설정하면서, 게임이 초기 상태로 돌아감!
    def setup_positions(self):  # 위치
        self.button_x = 0
        self.button_y = 0
        self.background_x = 0
        self.background_y = 0

    def draw_screen(self):
        self.screen.fill((255, 255, 255))
        current_background = self.load_src0.background_image[self.stage_index]
        self.screen.blit(current_background, (self.background_x, self.background_y))
        pygame.display.flip()


    def change_background(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_background_change_time > BACKGROUND_CHANGE_INTERVAL:
            self.stage_index += 1
            if self.stage_index >= len(self.load_src0.background_image):
                self.stage_index = 0
            self.last_background_change_time = current_time


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.explain_stage = etg.ExplainTheGame()
                    self.explain_stage.run()
                    self.running = False

    def update(self):
        self.change_background()

    def render(self):
        self.draw_screen()


    # run 메서드
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(CONSTANTS_CLOCK)

        


