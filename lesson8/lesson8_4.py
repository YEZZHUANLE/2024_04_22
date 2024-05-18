import random
import pyinputplus as pyip

def play_game():
    while True:
        min = 1
        max = 10
        count = 0
        math = random.randint(min,max)
        print ("=========猜數字遊戲========\n")

        while True:
            count += 1
            keyin = pyip.inputInt(f"猜數字的範圍{min}~{max}\n")
            if keyin == math :
                print(f"賓果!猜對了 ,  答案是:{math}")
                print(f"您總共猜了{count}次")
                break
            elif(keyin > math):
                print("在小一點")
                max = keyin - 1
            elif(keyin < math):
                print("在大一點")
                min = keyin + 1
            print(f"您已經猜了{count}次")
while True:
    play_game()
    play_again = pyip.inputYesNo("還要繼續嗎?(y,n)")
    if play_again =='no'
        break
print("遊戲結束")
