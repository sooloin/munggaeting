# push_the_button_game.py

import pygame
import sys
import Load_start as L_start
import Load_button as Lb
import CharacterCustomizationGame as CCG # 리스트의 index 다룸

#상수 정의
CONSTANTS_CLOCK = 60

class Push_the_buttonGame:
    def __init__(self):
        pygame.mixer.set_num_channels(2)  # 2개의 오디오 채널 설정
        self.screen_width = 800 # 창크기
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("뭉개팅") 
        

        self.setup_positions() 
        self.load_start = L_start.Load_start()
        self.load_src1 = Lb.Load_button()
        self.clicked_buttons = {}  # 클릭된 버튼 (비어있음)
        self.overlay_images = {}  # overlay 이미지를 저장할 딕셔너리 추가
        self.selected_temperature = None  # 선택한 온도를 저장하는 변수 (비어있음)
        self.clock = pygame.time.Clock()
        
    #변수의 초기값을 설정하면서, 게임이 초기 상태로 돌아감!
    def setup_positions(self): #위치
        self.button_x = 0
        self.button_y = 0
        self.background_x = 0
        self.background_y = 0

    
    def set_selected_temperature(self, temperature):
        self.selected_temperature = temperature

    def get_selected_temperature(self):
        return self.selected_temperature

    def handle_mouse_motion(self, mouse_x, mouse_y):
        buttons = {
            "button1": (pygame.Rect(self.button_x + 475, self.button_y + 600, 150, 75), "button1"),
            "button2": (pygame.Rect(self.button_x + 450, self.button_y + 475, 200, 75), "button2"),
            "button3": (pygame.Rect(self.button_x + 425, self.button_y + 350, 225, 75), "button3"),
            "button4": (pygame.Rect(self.button_x + 425, self.button_y + 225, 225, 75), "button4")
        }

        for button_rect, button_id in buttons.values():
            if button_rect.collidepoint(mouse_x, mouse_y):
                if button_id not in self.overlay_images:
                    base_image = self.load_src1.button_info[button_id]["image"]
                    overlay_image = self.load_src1.button_info[button_id]["light_image"]
                    position = (self.button_x, self.button_y)
                    overlay_result, overlay_rect = self.load_src1.create_overlay(base_image, overlay_image, position)
                    self.overlay_images[button_id] = (overlay_result, overlay_rect)
                    pygame.mixer.Channel(0).play(self.load_src1.click_sound)  # 클릭 소리 재생
            elif button_id in self.overlay_images:
                del self.overlay_images[button_id]


    def check_button_release(self):
        if self.clicked_buttons:
            for button_id in self.clicked_buttons:
                # button_id에 따른 처리 수행
                print(f"{button_id} 버튼 클릭!")

                # 선택한 온도 저장
                if button_id == "button1":
                    self.selected_temperature = 1  

                    # 다음 스테이지로 전환
                    stage2 = CCG.CharacterCustomizationGame(self.selected_temperature)
                    selected_temperature = CCG.run()  # 다음 스테이지의 run 메서드를 호출하고 선택한 온도를 받아옴

                    # 여기서 selected_temperature를 활용하거나 필요한 로직 수행
                    print(f"Selected temperature in Push_the_buttonGame: {selected_temperature}")

                # 릴리즈된 버튼에 대한 overlay 이미지 제거
                if button_id in self.overlay_images:
                    del self.overlay_images[button_id]

            self.clicked_buttons = {}  # 처리가 끝난 후 딕셔너리 초기화

    #이벤트 처리 로직 분리(1)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.mixer.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_down(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.handle_mouse_up()
            elif event.type == pygame.MOUSEMOTION:
                self.handle_mouse_motion(*event.pos)

    #이벤트 처리 로직 분리(2)
    def handle_mouse_up(self): # 마우스 버튼이 떼어졌을 때
        pass #아무 일도 없음

    def handle_mouse_down(self, event): # 마우스 버튼이 눌렸을 때
        if event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            button_id = self.check_button_click(mouse_x, mouse_y)
            if button_id:
                self.handle_button_click(button_id)

    # 이벤트 처리 로직 분리(3) > 마우스 클릭 이벤트를 처리하고 버튼 클릭 여부를 확인
    def check_button_click(self, mouse_x, mouse_y):
        buttons = {
            "button1": (pygame.Rect(self.button_x + 475, self.button_y + 600, 150, 75), "button1"),
            "button2": (pygame.Rect(self.button_x + 450, self.button_y + 475, 200, 75), "button2"),
            "button3": (pygame.Rect(self.button_x + 425, self.button_y + 350, 225, 75), "button3"),
            "button4": (pygame.Rect(self.button_x + 425, self.button_y + 225, 225, 75), "button4")
        }

        for button_rect, button_id in buttons.values():
            if button_rect.collidepoint(mouse_x, mouse_y): # 현재 마우스의 좌표가 해당 버튼의 영역에 속하는가?
                if button_id not in self.clicked_buttons: # 해당 버튼이 클릭되지 않았는가? == clicked_buttons 딕셔너리가 비어있는가?
                    self.handle_button_click(button_id) # handle_button_click(button_id) 호출
                    return button_id # button_id를 114번 줄인 button_id에 반환


    #이벤트 처리 로직 분리(4) > 버튼 클릭 로직 처리
    def handle_button_click(self, button_id):
        if button_id == "button1":
            self.set_selected_temperature(1)
        
        elif button_id == "button2":
            self.set_selected_temperature(2)
        
        elif button_id == "button3":
            self.set_selected_temperature(3)
        
        elif button_id == "button4":
            self.set_selected_temperature(4)
        
        # Stage2 객체를 생성하고 선택한 온도를 전달
        stage2 = CCG.CharacterCustomizationGame(self.get_selected_temperature())
        stage2.run()

        # 현재 스테이지의 루프를 빠져나가고 다음 스테이지의 루프를 시작
        return # break는 while이나 for문에서만 사용할 수 있으므로 return 사용해 현재 루프 빠져나가고 다음 스테이지 루프 시작시킴.
    

    # 화면을 그리는 역할           
    def render_screen(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.load_src1.background_image, (self.background_x, self.background_y))

        for button_name, button_info in self.load_src1.button_info.items():
            button_image = button_info["image"]
            button_rect = button_image.get_rect(topleft=(self.button_x, self.button_y))

            if button_name in self.overlay_images:
                overlay_image, overlay_rect = self.overlay_images[button_name]
                self.screen.blit(overlay_image, overlay_rect)

            self.screen.blit(button_image, button_rect)

        pygame.display.flip()


    #메인 루프
    def main_loop(self):
        running = True
        while running:
            self.handle_events()
            self.render_screen()
            self.clock.tick(CONSTANTS_CLOCK) 

            # 종료 조건을 확인하여 루프를 종료합니다 (예: 버튼 클릭 또는 게임 완료)
            if self.selected_temperature is not None :
                running = False

    #run 메서드 > main에서 실행됨
    def run(self): 
        self.setup_positions() #초기화 
        self.main_loop() 
        


