#CharacterCustomization.py
class CharacterCustomization: #index
    def __init__(self):
        #현재 선택된 index 번호
        self.current_eyebrows_index = 0
        self.current_eyeline_index = 0
        self.current_mascara_index = 0
        self.current_cheek_index = 0
        self.current_clothes_index = 0
        self.current_ACC_index = 0
        self.current_muff_index = 0

        self.current_say_index = 0

        #사용자가 선택한 옷 index번호 저장
        self.clothes_index = 0

        # 선택 완료 여부도 클래스 속성으로 변경
        self.eyebrows_selected = False
        self.eyeline_selected = False
        self.mascara_selected = False
        self.cheek_selected = False
        self.clothes_selected = False
        self.ACC_selected = False
        self.muff_selected = False

    def set_current_eyebrows_index(self, index):
        self.current_eyebrows_index = index

    def set_current_eyeline_index(self, index):
        self.current_eyeline_index = index

    def set_current_mascara_index(self, index):
        self.current_mascara_index = index

    def set_current_cheek_index(self, index):
        self.current_cheek_index = index

    def set_current_clothes_index(self, index):
        self.current_clothes_index = index

    def set_current_ACC_index(self, index):
        self.current_ACC_index = index

    def set_current_muff_index(self, index):
        self.current_muff_index = index

    def set_current_say_index(self, index):
        self.current_say_index = index