#main.py
import start 


#현재 스크립트가 직접 실행될 때만 코드 블록이 실행되도록 하는 조건문. 다른 스크립트에서 이 파일을 모듈로 사용 시 실행 X
if __name__ == "__main__": 

    start_the_game = start.Hell_of_solo()
    start_the_game.run()
     
