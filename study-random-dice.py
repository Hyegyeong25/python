
import random

myList = ["하나", "둘", "셋", "넷", "다섯", "여섯"]

while(True):
    response = input('주사위 던지기를 계속하시겠습니까?(Y/N)');
    if response == 'Y':
        coin = random.choice(myList)
        print(coin)
    else :
        break

print("프로그램을 종료합니다.")