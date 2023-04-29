import threading
import time

## 클래스 선언 부분 ## 
class Sum :
    num = ''
    def __init__(self, num) :
        self.num = num
    
    def runSum(self) :
        hap = 0 
        for i in range(0, self.num + 1) :
            hap += i
        print("1+2+3+......+", self.num, '=', hap)

            
## 메인 코드 부분 ## 
num1 = Sum(1000)
num2 = Sum(100000)
num3 = Sum(10000000)

th1 = threading.Thread(target = num1.runSum)
th2 = threading.Thread(target = num2.runSum)
th3 = threading.Thread(target = num3.runSum)

th1.start()
th2.start()
th3.start()
