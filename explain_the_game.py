# explain_the_game.py
import pygame
import os
import sys
import push_the_button_game as ptbg

BACKGROUND_CHANGE_INTERVAL = 1500
CONSTANTS_CLOCK = 60

class ExplainTheGame:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.set_num_channels(2) 
        self.screen_width = 800  # 창 크기
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("뭉개팅")

        self.setup_positions()
        self.load_images()
        self.load_sound()
        self.clock = pygame.time.Clock()
        self.explain_index = 0
        self.last_background_change_time = pygame.time.get_ticks()
        self.running = True
        self.stage_finished = False  # 스테이지가 끝났는지 여부를 저장하는 변수

    def load_sound(self):
        sound_dir = os.path.join("src", "src_explain")
        self.message = pygame.mixer.Sound(os.path.join(sound_dir, "Pling_Sound.mp3"))
        self.bgm = pygame.mixer.Sound(os.path.join(sound_dir, "spring_day.mp3"))
        pygame.mixer.Channel(0).play(self.message)
        pygame.mixer.Channel(0).play(self.bgm)

        pygame.mixer.Channel(0).set_volume(0.5)  # 볼륨 조절
        pygame.mixer.Channel(1).set_volume(0.5)  # 볼륨 조절

    
        pygame.mixer.Channel(1).play(self.bgm, loops=-1)  # 무한 반복
        
    
    def load_images(self):
        # 이미지 디렉토리 경로
        image_dir = os.path.join("src", "src_explain")

        # 설명 이미지 로드
        self.explain_images = [
            pygame.image.load(os.path.join(image_dir, "ex1.png")),
            pygame.image.load(os.path.join(image_dir, "ex2.png")),
            pygame.image.load(os.path.join(image_dir, "ex3.png")),
            pygame.image.load(os.path.join(image_dir, "ex4.png")),
            pygame.image.load(os.path.join(image_dir, "ex5.png"))]

    def setup_positions(self):
        # 위치 설정 코드 추가
        pass

    def explain_screen(self):
        self.screen.fill((255, 255, 255))
        current_background = self.explain_images[self.explain_index]
        self.screen.blit(current_background, (0, 0))
        pygame.display.flip()

    def explain_change_background(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_background_change_time > BACKGROUND_CHANGE_INTERVAL:
            if self.explain_index < len(self.explain_images) - 1:
                self.explain_index += 1
                self.last_background_change_time = current_time
                # 인덱스가 증가할 때마다 소리를 재생합니다.
                pygame.mixer.Channel(0).play(self.message)
            else:
                self.stage_finished = True  # 스테이지가 끝났음을 표시

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.stage_finished:
                    stage1 = ptbg.Push_the_buttonGame()
                    stage1.run()
                    self.running = False  # 스테이지가 끝나면 스페이스 바로 게임 종료

    def explain_update(self):
        self.explain_change_background()

    def explain_render(self):
        self.explain_screen()

    def explain(self):
        self.explain_update()
        self.explain_render()

    def run(self):
        while self.running:
            self.handle_events()
            if not self.stage_finished:
                self.explain()
            self.clock.tick(CONSTANTS_CLOCK)

