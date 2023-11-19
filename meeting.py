# meeting.py
import pygame
import Load_meeting as Lm
import random
import sys
import start

# 상수 정의
CONSTANTS_CLOCK = 60
BACKGROUND_CHANGE_INTERVAL = 1800

class MeetingMan:
    def __init__(self, selected_temperature, selection_flag):
        pygame.init()  # 파이게임 모듈을 초기화
        self.selected_temperature = selected_temperature  # 사용자가 선택한 온도
        self.selected_clothes = selection_flag  # 게임 내에서 선택된 정답 인덱스
        self.load_src3 = Lm.Load_meeting()
        self.screen = pygame.display.set_mode((800, 800))  # 화면 초기화
        pygame.display.set_caption("Meeting Game")
        self.clock = pygame.time.Clock()  # Clock 객체 생성
        self.setup_positions()

        pygame.mixer.set_num_channels(4)
        self.last_background_change_time = pygame.time.get_ticks()
        self.done_time = None
        self.running = True

        #failure
        self.failure_index = 0
        self.exit_after_fail = False
        self.failure_image = random.choice(self.load_src3.failure_image)

        #success
        self.success_index = 0
        self.exit_after_success = False

        
        

    def setup_positions(self):
        # 배경 위치
        self.background_x = 0
        self.background_y = 0

    def get_result(self):
        if self.selected_temperature == 1:  # ~4도
            self.selected_c2()
        elif self.selected_temperature == 2:  # 5~8도
            self.selected_c4()
        elif self.selected_temperature == 3:  # 9~11도
            self.selected_c1_or_c3()
        elif self.selected_temperature == 4:  # 12~16도
            self.selected_c0()

    def selected_c2(self):
        self.process_selection(2)

    def selected_c4(self):
        self.process_selection(4)

    def selected_c1_or_c3(self):
        self.process_selection(1, 3)

    def selected_c0(self):
        self.process_selection(0)

    


    def process_selection(self, *valid_clothes): #함수 정의에서 *를 사용하면, 해당 매개변수는 여러 개의 인자를 받을 수 있는 튜플로 처리
        if self.selected_clothes not in valid_clothes:
            self.failure()


        else:
            self.success()


    # failure
    def failure(self):
        self.failure_screen()
        self.failure_change_background()


    def failure_screen(self):
        self.screen.fill((255, 255, 255))
        if self.failure_index < len(self.load_src3.fail_ending):
            current_background = self.load_src3.fail_ending[self.failure_index]
            self.screen.blit(current_background, (self.background_x, self.background_y))
        pygame.display.flip() 

    def failure_change_background(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_background_change_time > BACKGROUND_CHANGE_INTERVAL:
            if self.failure_index < len(self.load_src3.fail_ending) - 1:  # 이미지 인덱스가 최대값에 도달하지 않았을 때
                self.failure_index += 1
                self.last_background_change_time = current_time

                # 이미지 인덱스에 따라 다른 효과음 재생
                if self.failure_index == 4:
                    pygame.mixer.Channel(1).play(self.load_src3.joke_sound)

                elif self.failure_index == 5:
                    pygame.mixer.Channel(0).play(self.load_src3.failure_sound)

            elif self.failure_index >= len(self.load_src3.fail_ending) - 1:
                self.exit_after_fail = True



    
    # success
    def success(self):
        self.success_screen()
        self.success_change_background()


    def success_screen(self):
        self.screen.fill((255, 255, 255))
        if self.success_index < len(self.load_src3.success_image):
            current_background = self.load_src3.success_image[self.success_index]
            self.screen.blit(current_background, (self.background_x, self.background_y))
        pygame.display.flip() 

    def success_change_background(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_background_change_time > BACKGROUND_CHANGE_INTERVAL:
            if self.success_index < len(self.load_src3.success_image) - 1:  # 이미지 인덱스가 최대값에 도달하지 않았을 때
                self.success_index += 1
                self.last_background_change_time = current_time

                # 이미지 인덱스에 따라 다른 효과음 재생
                if self.success_index == 4:
                    pygame.mixer.Channel(2).play(self.load_src3.success_sound)

            elif self.success_index >= len(self.load_src3.success_image) - 1:
                self.exit_after_success = True

    
    def restart_program(self):
        # 프로그램 재시작을 위해 run() 메서드를 호출합니다.
        restart_the_game = start.Hell_of_solo()
        restart_the_game.run()


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.get_result()
            self.clock.tick(CONSTANTS_CLOCK)

             # 조크 이미지가 나오면 종료
            if self.exit_after_fail:
                self.restart_program()  # 프로그램 재시작
            
            if self.exit_after_success:
                pygame.quit()
                sys.exit()  # 프로그램 종료


        pygame.quit()


       





