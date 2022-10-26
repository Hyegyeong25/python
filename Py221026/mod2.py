PI = 3.141592
class Math:
    # self란 클래스의 인스턴스를 나타내는 변수
    def solv(self, r):
        #반지름 계산 클래스, r**2는 r의 제곱을 의미
        return PI * (r ** 2)

def sum(a, b):
    return a+b

if __name__=="__main__":
    print(PI)
    a=Math() #클래스 실행
    print(a.solv(2))
    print(sum(PI, 4.4))