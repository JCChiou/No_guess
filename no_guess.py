#產生一個隨機整數(不印出來)
#讓使用者重複輸入數字去猜
import random
r = random.randint(0, 100)
print('0~100,數字猜猜看')
while True:
	u_guess = int(input('請猜!'))
	if u_guess == r:
		print('恭喜猜對了')
		break
	else:
		if u_guess < r:
			print('比答案小')
		else:
			print('比答案大')

