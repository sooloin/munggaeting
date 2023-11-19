#CharacterCustomizationGame.py

import pygame
import sys
import CharacterCustomization as CC
import Load_src as Ls
import Load_button as Lb
import duribun 


#상수 정의
CONSTANTS_CLOCK = 60


class CharacterCustomizationGame:
    def __init__(self, selected_temperature):
        self.screen_width = 800
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("뭉개팅")
        self.selected_temperature = selected_temperature
        self.clock = pygame.time.Clock()
        self.load_src = Ls.Load_src()
        self.load_src1 = Lb.Load_button()
        self.character_customization = CC.CharacterCustomization()
        self.running = True
        

        # self.show_the_temperature()
        self.setup_positions()
        self.setup_selection_flags()


    
    def setup_positions(self): # 위치 설정 코드...
            # 캐릭터 위치
            self.character_x = self.screen_width // 2 - self.load_src.character_image.get_width() // 2
            self.character_y = self.screen_height - self.load_src.character_image.get_height()

            
            # 배경 위치
            self.background_x = 0
            self.background_y = 0


    def setup_selection_flags(self): # 선택 완료 여부 설정 코드...
        # 선택 완료 여부를 리스트로 관리
        self.selection_flags = [False] * 7 # -> [F][F][F][F][F][F][F]
        # self.selection_flag == 인스턴스 변수
        # 게임 시작 시 선택 완료 여부 나타내는 플래그 초기화 가능


    def get_character_info(self): # 다음 스테이지로 전환
        return {
            'selected_temperature': self.selected_temperature,
            'selected_clothes_index': self.character_customization.clothes_index,
            # 기타 관련 정보 추가
        }
    


    #이벤트 처리 로직 분리
    def handle_eyebrows_selection(self, event):
        if event.key == pygame.K_LEFT:
            self.character_customization.set_current_eyebrows_index(
                (self.character_customization.current_eyebrows_index - 1) % len(self.load_src.eyebrows_images))
            self.load_src.choose_sound.play()
        elif event.key == pygame.K_RIGHT:
            self.character_customization.set_current_eyebrows_index(
                (self.character_customization.current_eyebrows_index + 1) % len(self.load_src.eyebrows_images))
            self.load_src.choose_sound.play()
        elif event.key == pygame.K_SPACE:
            self.character_customization.eyebrows_selected = True
            # 선택한 정보 저장
            self.character_customization.set_current_eyebrows_index(self.character_customization.current_eyebrows_index)
            self.load_src.fix_sound.play()

    def handle_eyeline_selection(self, event):
        if event.key == pygame.K_LEFT:
            self.character_customization.set_current_eyeline_index(
                (self.character_customization.current_eyeline_index - 1) % len(self.load_src.eyeline_images))
            self.load_src.choose_sound.play()
        elif event.key == pygame.K_RIGHT:
            self.character_customization.set_current_eyeline_index(
                (self.character_customization.current_eyeline_index + 1) % len(self.load_src.eyeline_images))
            self.load_src.choose_sound.play()
        elif event.key == pygame.K_SPACE:
            self.character_customization.eyeline_selected = True
            # 선택한 정보 저장
            self.character_customization.set_current_eyeline_index(self.character_customization.current_eyeline_index)
            self.load_src.fix_sound.play()

    def handle_mascara_selection(self, event):
        if event.key == pygame.K_LEFT:
            self.character_customization.set_current_mascara_index(
                (self.character_customization.current_mascara_index - 1) % len(self.load_src.mascara_images))
            self.load_src.choose_sound.play()
        elif event.key == pygame.K_RIGHT:
            self.character_customization.set_current_mascara_index(
                (self.character_customization.current_mascara_index + 1) % len(self.load_src.mascara_images))
            self.load_src.choose_sound.play()
        elif event.key == pygame.K_SPACE:
            self.character_customization.mascara_selected = True
            # 선택한 정보 저장
            self.character_customization.set_current_mascara_index(self.character_customization.current_mascara_index)
            self.load_src.fix_sound.play()

    def handle_cheek_selection(self, event):
        if event.key == pygame.K_LEFT:
            self.character_customization.set_current_cheek_index(
                (self.character_customization.current_cheek_index - 1) % len(self.load_src.cheek_images))
            self.load_src.choose_sound.play()
        elif event.key == pygame.K_RIGHT:
            self.character_customization.set_current_cheek_index(
                (self.character_customization.current_cheek_index + 1) % len(self.load_src.cheek_images))
            self.load_src.choose_sound.play()
        elif event.key == pygame.K_SPACE:
            self.character_customization.cheek_selected = True
            # 선택한 정보 저장
            self.character_customization.set_current_cheek_index(self.character_customization.current_cheek_index)
            self.load_src.fix_sound.play()

    def handle_clothes_selection(self, event):
        # 옷 선택 중
        
        if event.key == pygame.K_LEFT:
            self.character_customization.set_current_clothes_index(
                (self.character_customization.current_clothes_index - 1) % len(self.load_src.clothes_images))
            self.load_src.choose_sound.play()
        elif event.key == pygame.K_RIGHT:
            self.character_customization.set_current_clothes_index(
                (self.character_customization.current_clothes_index + 1) % len(self.load_src.clothes_images))
            self.load_src.choose_sound.play()
        elif event.key == pygame.K_SPACE:
        # 스페이스 바를 누르면 옷 선택이 완료되고 ACC 선택으로 넘어감
            self.character_customization.clothes_selected = True
            # 선택한 정보 저장
            self.character_customization.set_current_clothes_index (self.character_customization.current_clothes_index)
            self.load_src.fix_sound.play()

    def handle_ACC_selection(self, event):
        # ACC 선택 중
        if event.key == pygame.K_LEFT:
            self.character_customization.set_current_ACC_index(
                (self.character_customization.current_ACC_index - 1) % len(self.load_src.ACC_images))
            self.load_src.choose_sound.play()
        elif event.key == pygame.K_RIGHT:
            self.character_customization.set_current_ACC_index(
                (self.character_customization.current_ACC_index + 1) % len(self.load_src.ACC_images))
            self.load_src.choose_sound.play()
        elif event.key == pygame.K_SPACE:
            # 스페이스 바를 누르면 ACC 선택이 완료되고 게임 종료
            self.character_customization.ACC_selected = True
            # 선택한 정보 저장
            self.character_customization.set_current_ACC_index(self.character_customization.current_ACC_index)
            self.load_src.fix_sound.play()
            

    
    def handle_muff_selection(self, event):
        # muff 선택 중
        if event.key == pygame.K_LEFT:
            self.character_customization.set_current_muff_index(
                (self.character_customization.current_muff_index - 1) % len(self.load_src.muff_images))
            self.load_src.choose_sound.play()
        elif event.key == pygame.K_RIGHT:
            self.character_customization.set_current_muff_index(
                (self.character_customization.current_muff_index + 1) % len(self.load_src.muff_images))
            self.load_src.choose_sound.play()
        elif event.key == pygame.K_SPACE:
            # 스페이스 바를 누르면 ACC 선택이 완료되고 게임 종료
            self.character_customization.muff_selected = True
            # 선택한 정보 저장
            self.show_the_say_finish
            self.character_customization.set_current_muff_index(self.character_customization.current_muff_index)
            self.load_src.finish_sound.play()
            

            


    def handle_events(self): # 키 눌렀을 시 일어나는 일들 설정
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                # 인스턴스 변수를 참조하려면 self. 사용
                if not self.character_customization.eyebrows_selected:
                    self.handle_eyebrows_selection(event)
                    
                elif not self.character_customization.eyeline_selected:
                    self.handle_eyeline_selection(event)

                elif not self.character_customization.mascara_selected: #마스카라
                    self.handle_mascara_selection(event)

                elif not self.character_customization.cheek_selected:
                    self.handle_cheek_selection(event)

                elif not self.character_customization.clothes_selected:
                    self.handle_clothes_selection(event)
                   

                elif not self.character_customization.ACC_selected:
                    self.handle_ACC_selection(event)

                elif not self.character_customization.muff_selected:
                    self.handle_muff_selection(event)
                    
                    

                elif event.key == pygame.K_SPACE:
                    # stage3으로 넘어감
                    duri = duribun.stage2_5(self.selected_temperature, self.character_customization.current_clothes_index)
                    duri.run()
                    self.running = False
                
               

                
    # 그리기 로직 분리
    def draw_character(self):
        self.screen.blit(self.load_src.character_image, (self.character_x, self.character_y))

    def draw_screen(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.load_src.background_image, (self.background_x, self.background_y))
        self.draw_character()  # 이미지 및 위치 정보를 전달하지 않아도 됨
        self.draw_selected_images()
        self.draw_screen_with_say_image()
        self.show_the_temperature()
        pygame.display.flip()

    def show_the_say_image(self, say_index):
        self.screen.blit(self.load_src.say_image[say_index], (self.character_x, self.character_y))
    
    def show_the_say_finish(self):
        self.screen.blit(self.load_src.say_finish, (self.character_x, self.character_y))


    def draw_screen_with_say_image(self):
        if not self.character_customization.mascara_selected:
            # 마스카라 선택 전이면 say_image[0]을 표시
            self.show_the_say_image(0)
        elif self.character_customization.cheek_selected:
            # 볼 선택 전이면 say_image[1]을 표시
            self.show_the_say_image(1)
       
            
            


    def show_the_temperature(self):
        if self.selected_temperature == 1 :
            self.screen.blit(self.load_src1.button1_image, (-475, -600))
        elif self.selected_temperature == 2:
            self.screen.blit(self.load_src1.button2_image, (-450, -474))
        elif self.selected_temperature == 3:
            self.screen.blit(self.load_src1.button3_image, (-428, -357))
        elif self.selected_temperature == 4:
            self.screen.blit(self.load_src1.button4_image, (-433, -227))

    def draw_selected_images(self):
        self.screen.blit(self.load_src.eyebrows_images[self.character_customization.current_eyebrows_index], (self.character_x, self.character_y))
        self.screen.blit(self.load_src.eyeline_images[self.character_customization.current_eyeline_index], (self.character_x, self.character_y))
        self.screen.blit(self.load_src.mascara_images[self.character_customization.current_mascara_index], (self.character_x, self.character_y))
        self.screen.blit(self.load_src.cheek_images[self.character_customization.current_cheek_index], (self.character_x, self.character_y))
        self.screen.blit(self.load_src.clothes_images[self.character_customization.current_clothes_index], (self.character_x, self.character_y))
        self.screen.blit(self.load_src.ACC_images[self.character_customization.current_ACC_index], (self.character_x, self.character_y))
        self.screen.blit(self.load_src.muff_images[self.character_customization.current_muff_index], (self.character_x, self.character_y))

    def run(self):
        
        while self.running:
            self.draw_screen()
            self.handle_events()
            self.clock.tick(CONSTANTS_CLOCK)

