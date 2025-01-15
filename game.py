import random

def game():
    #ユーザーの数値(m < n)入力
    question = "整数mと整数nをスペース区切りで入力してください（m < n）："
    m, n = (int(x) for  x in input(question).split())

    print("====================================================")
    print("今から4回で %d<= x <= %dの中で生成された数字を当ててください！" %(m,n))

    #ランダム数値の生成
    ans = random.randint(m, n)

    for i in range(5):
        guess = int(input(str(i+1) + "回目の予想を入力してください："))
        if(guess == ans): 
            print("正解!やるじゃん！")
            break
        else: 
            print("違うよ^^")
            if(ans > guess): print("答えはもっと大きいかも")
            else: print("答えはもっと小さいかも")
        print("============================================")
    else: print("残念!答えに辿り着けなかった、、、^^")


game()