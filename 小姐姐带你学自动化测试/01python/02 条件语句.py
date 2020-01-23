#该实例演示数字猜谜游戏
guess = 0
number = 5
print("猜数字游戏")
while guess != number:
    guess = int(input("请输入你猜的数字:"))
    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("在猜哦，猜的数字小了")
    elif guess > number:
        print("在猜哦，猜的数字大了")