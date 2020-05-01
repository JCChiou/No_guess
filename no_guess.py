#產生一個隨機整數(不印出來)
#讓使用者重複輸入數字去猜
import random
r = random.randint(0, 100)
u_guess = 0
retry_cnt = 0
print('1~100,數字猜猜看')
while u_guess != r:
	retry_cnt = retry_cnt + 1
	u_guess = int(input('請猜!'))
	u_guess = int(u_guess)
	if u_guess == r:
		print('恭喜猜對了,你共猜了', retry_cnt ,'次')		
	else:
		if u_guess < r:
			print('比答案小')
		else:
			print('比答案大')

