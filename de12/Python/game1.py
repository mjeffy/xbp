
import random
from re import I
from tkinter import Y


counter=0

print("18を超えないように限界まで挑戦してください")
print("現在の数字は0です")
while counter<=18:
    a = random.randint(1,3)
    question=input("まだ足しますか")
    if question=="yes":
        counter=counter+a
        print("現在の合計は",counter,"です")
    elif counter==18:
        print("おめでとうございます、99ぴったりです")
        break
    elif question=="no":
        print("ハイスコアは",counter,"です")
        break


if counter>18:
        print("18を超えました、失敗です")
