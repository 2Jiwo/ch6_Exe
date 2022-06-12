# 제 6장 반복문의 연습문제를 시작해보겠습니다.
# 1. 2부터 100사이의 모든 짝수를 출력하는 반복 루프를 작성해보자.
# x%2한 결과가 0이면 x는 짝수이다.
for in in range(2, 101):
    if i%2 == 0 :
        print(i,end = " ")


# 2. 복리이자율 7%로 1000만원을 저축했을 경우 2000만원인 되는데 몇 년이 걸리는지 계산하기 위해 아래의 코드를 작성하였다.
#    잘못된 점은 없는지 체크하라.

year = 0
balance = 1000

while balance <= 2000 :           
    year = year + 1
    interes = balance * 0.07
    balance = balance + interest
print(year, "년이 걸립니다.")

# 3. 다음 코드의 출력을 예상해보자. 각 단계에서 변수의 값을 예상해 보자.

n = 1234
sum = 0
while n > 0 :
    digit = n % 10
    sum = sum + digit
    n = n // 10
print(sum)

# 4. 사용자에게 곱셈 퀴즈를 내고 답을 사용자로부터 받는 프로그램에서 사용자가 올바른 답을 입력할 때까지 반복하게 수정하라.
# 어떤 조건이 만족될 때까지 반복하는 것은 while 루프를 사용하는 것이다.

ans = 0
while ans != 3*9 :
    ans = int(input("3 x 9는 ?"))
print("맞았습니다.")

# 5. 사용자가 입력한 정수의 합을 계산하는 프로그램을 작성하라. 사용자가 0을 입력하기 전까지 정수를 계속하여 읽도록 하자.
# 무한루프를 작성하고 사용자가 입력한 값이 0이면 break 문장을 실행하여 반복 루프를 종료한다. 무한루프는 while True" 이다.

sum = 0
while True:
    x = int(input("정수를 입력하시오."))
    if x == 0:
        break;
    sum = sum + x
print("합은" , sum, "입니다."

# 6. 난수 생성 함수를 사용하여 2개의 주사위를 던졌을 때 나오는 수를 제공하는 화면과 같이 출력하여 본다. 
# 1부터 6사이의 난수를 발생하려면 r = random.randint(1,6) 문장을 사용, 프로그램의 첫 부분이 import random 문장
# 잊지 마세요.

from random import randint

for i in range(3) : 
    d1 = randint(1,6)
    d2 = randint(1.6)
    print("첫번째 주사위=", d1, "두번째 주사위=", d2)

# 7. 

import turtle
t = turtle.Turtle()
t.shape("turtle")
t.left(90)

for i in range(1,7)
    t.fd(100)
    t.fd(-30)
    t.lt(60)
    t.fd(30)
    t.fd (-30)
   
    t.rt(120)
    t.fd(30)
    t.fd(-30)

    t.lt(60)
    t.fd(-70)
    t.left(60)
    t. _streen. exitonclick()


# 8.

import turtle

myPen = turtle.Turtle()
myPen.spped(0)
myPen.color("#ff0000")

for j in range(1,10) :
    for i in range(1,6) :
        my Pen.left(144)
        myPen.forward(200)
    my Pen.left(10)

myPen._ screen.exitoniclick()

# 9. 

import turtle
import random

t = turtle.Turtle()
t.shape("turtle")

for j in range (1,10) : 
    t.up()
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    r = random.randint(10, 200)
    t.goto(x,y)
    t.down()
    t.circle(r)
t._screen.exitonclick