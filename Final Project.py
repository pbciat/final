import random
import msvcrt
import time
import sys

def reset():
    """將反應時間及計次歸零"""
    global DPP_count
    global KMT_count
    global positive_count
    global negative_count
    global DPP_reacttime
    global KMT_reacttime
    global positive_reacttime
    global negative_reacttime
    global wrong_count_total
    DPP_count = 0
    KMT_count = 0
    positive_count = 0
    negative_count = 0
    DPP_reacttime = 0
    KMT_reacttime = 0
    positive_reacttime = 0
    negative_reacttime = 0
    wrong_count_total = 0

def timing_main(classA_count, classB_count, classA_list, classB_list, classA_reacttime, classB_reacttime, wrong_count_total):
    """主程式-決定隨機的刺激因子"""
    if classA_count < 10 and classB_count < 10:
        select_list = random.randint(1, 2)
        if select_list == 1:
            reacttime, count, wrong_count = show_stimulate(classA_list, 1)
            classA_reacttime += reacttime
            classA_count += count
            wrong_count_total += wrong_count
        else:
            reacttime, count, wrong_count = show_stimulate(classB_list, 2)
            classB_reacttime += reacttime
            classB_count += count
            wrong_count_total += wrong_count
    elif classA_count == 10 and classB_count < 10:
        reacttime, count, wrong_count = show_stimulate(classB_list, 2)
        classB_reacttime += reacttime
        classB_count += count
        wrong_count_total += wrong_count
    elif classB_count == 10 and classA_count < 10:
        reacttime, count, wrong_count  = show_stimulate(classA_list, 1)
        classA_reacttime += reacttime
        classA_count += count
        wrong_count_total += wrong_count
    print(wrong_count_total)
    if wrong_count_total == 6:
        print("Too much wrong answer!")
        sys.exit()

    return classA_count, classB_count, classA_reacttime, classB_reacttime, wrong_count_total

def show_stimulate(class_list, right_answer):
    """印出刺激並根據答案進行檢查"""
    #show the pictures or words
    select_stimulate = random.randint(0, len(class_list) - 1)
    print(class_list[select_stimulate])
    #react time calculate
    if right_answer == 1:
        return check(97)
    elif right_answer == 2:
        return check(108)

def check(unicode):
    """檢查實驗者是否答對"""
    t_start = time.time()
    char = msvcrt.getch()
    if ord(char) == unicode:
        t_end = time.time()
        react_time = t_end - t_start
        print("Correct!")
        return (react_time, 1, 0)
    else:
        print("Wrong Answer!")
        return (0, 0, 1)

#class_list 各種刺激因子
DPP_list = ["蔡英文", "謝長廷", "蘇貞昌", "賴清德", "陳菊", "林佳龍", "鄭文燦"]
KMT_list = ["馬英九", "朱立倫", "韓國瑜", "吳敦義", "王金平", "侯友宜", "盧秀燕"]
positive_list = ["讚","棒","好","優秀","了不起","卓越","進步","開明","友善"]
negative_list = ["爛","廢","遜","糟糕","拙劣","黑箱","退步","惡劣","獨裁"]

DPP_reacttime_list = []
KMT_reacttime_list  = []
positive_reacttime_list  = []
negative_reacttime_list  = []

#資料輸入
print("You are? (DPP or KMT)")
tendency = input()

#實驗區塊1
#民進黨A
#國民黨L
#-民進黨跟國民黨各出現10次
#-不一定要交叉出現
#-使用者按錯不計
#-已出現過的可重複出現
time.sleep(1)
print("Part1")
time.sleep(3)
reset()
while DPP_count < 10 or KMT_count < 10:
    DPP_count, KMT_count, DPP_reacttime, KMT_reacttime, wrong_count_total = timing_main(DPP_count, KMT_count, DPP_list, KMT_list, DPP_reacttime, KMT_reacttime, wrong_count_total)

DPP_reacttime_list.append(round(DPP_reacttime, 4))
KMT_reacttime_list.append(round(KMT_reacttime, 4))

#實驗區塊2
#正面A
#負面L
#-正面跟負面各出現10次
#-不一定要交叉出現
#-使用者按錯不計
#-已出現過的可重複出現
time.sleep(1)
print("Part2")
time.sleep(3)
reset()
while positive_count < 10 or negative_count < 10:
    positive_count, negative_count, positive_reacttime, negative_reacttime, wrong_count_total = timing_main(positive_count, negative_count, positive_list, negative_list, positive_reacttime, negative_reacttime, wrong_count_total)

positive_reacttime_list.append(round(positive_reacttime, 4))
negative_reacttime_list.append(round(negative_reacttime, 4))

#實驗區塊3
#民進黨A
#國民黨L
#正面A
#負面L
#-四種類別各出現10次
#-詞彙與政黨須交叉出現
#-詞彙間不須交叉出現
#-政黨間不須交叉出現
#-使用者按錯不計
#-已出現過的可重複出現
time.sleep(1)
print("Part3")
time.sleep(3)
reset()
while positive_count < 10 or negative_count < 10 or KMT_count < 10 or DPP_count < 10:
    positive_count, negative_count, positive_reacttime, negative_reacttime, wrong_count_total = timing_main(positive_count, negative_count, positive_list, negative_list, positive_reacttime, negative_reacttime, wrong_count_total)
    DPP_count, KMT_count, DPP_reacttime, KMT_reacttime, wrong_count_total = timing_main(DPP_count, KMT_count, DPP_list, KMT_list, DPP_reacttime, KMT_reacttime, wrong_count_total)

positive_reacttime_list.append(round(positive_reacttime, 4))
negative_reacttime_list.append(round(negative_reacttime, 4))
DPP_reacttime_list.append(round(DPP_reacttime, 4))
KMT_reacttime_list.append(round(KMT_reacttime, 4))

#實驗區塊4
#國民黨A
#民進黨L
#-民進黨跟國民黨各出現10次
#-不一定要交叉出現
#-使用者按錯不計
#-已出現過的可重複出現
time.sleep(1)
print("Part4")
time.sleep(3)
reset()
while KMT_count < 10 or DPP_count < 10:
    KMT_count, DPP_count, KMT_reacttime, DPP_reacttime, wrong_count_total = timing_main(KMT_count, DPP_count, KMT_list, DPP_list, KMT_reacttime, DPP_reacttime, wrong_count_total)

KMT_reacttime_list.append(round(KMT_reacttime, 4))
DPP_reacttime_list.append(round(DPP_reacttime, 4))

#實驗區塊5
#國民黨A
#民進黨L
#正面A
#負面L
#-四種類別各出現10次
#-詞彙與政黨須交叉出現
#-詞彙間不須交叉出現
#-政黨間不須交叉出現
#-使用者按錯不計
#-已出現過的可重複出現
time.sleep(1)
print("Part5")
time.sleep(3)
reset()
while positive_count < 10 or negative_count < 10 or KMT_count < 10 or DPP_count < 10:
    positive_count, negative_count, positive_reacttime, negative_reacttime, wrong_count_total = timing_main(positive_count, negative_count, positive_list, negative_list, positive_reacttime, negative_reacttime, wrong_count_total)
    KMT_count, DPP_count, KMT_reacttime, DPP_reacttime, wrong_count_total = timing_main(KMT_count, DPP_count, KMT_list, DPP_list, KMT_reacttime, DPP_reacttime, wrong_count_total)

positive_reacttime_list.append(round(positive_reacttime, 4))
negative_reacttime_list.append(round(negative_reacttime, 4))
KMT_reacttime_list.append(round(KMT_reacttime, 4))
DPP_reacttime_list.append(round(DPP_reacttime, 4))

#結果
time.sleep(1)
if tendency == "DPP":
    if KMT_reacttime_list[1] + DPP_reacttime_list[1] <= KMT_reacttime_list[3] + DPP_reacttime_list[3]:
        print("綠皮綠骨!")
    else:
        print("綠皮藍骨!")
else:
    if KMT_reacttime_list[1] + DPP_reacttime_list[1] < KMT_reacttime_list[3] + DPP_reacttime_list[3]:
        print("藍皮綠骨!")
    else:
        print("藍皮藍骨!")