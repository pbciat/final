import random
import msvcrt
import time

def timing(class_list, right_answer):
    """主程式-計算反應時間"""
    #show the pictures or words
    select_stimulate = random.randint(0, len(class_list) - 1)
    print(class_list[select_stimulate])
    #react time calculate
    if right_answer == 1:
        return timing_sub1(97)
    elif right_answer == 2:
        return timing_sub1(108)

def timing_sub1(unicode):
    """檢查實驗者是否答對"""
    t_start = time.time()
    char = msvcrt.getch()
    if ord(char) == unicode:
        t_end = time.time()
        react_time = t_end - t_start
        print("Correct!")
        return (react_time, 1)
    else:
        print("Wrong Answer!")
        return (0, 0)
    
    
#class_list 各種刺激因子
DPP_list = ["蔡英文", "謝長廷", "蘇貞昌", "賴清德", "陳菊", "林佳龍", "鄭文燦"]
KMT_list = ["馬英九", "朱立倫", "韓國瑜", "吳敦義", "王金平", "侯友宜", "盧秀燕"]
positive_list = ["讚","棒","好","優秀","了不起","卓越","進步","開明","友善"]
negative_list = ["爛","廢","遜","糟糕","拙劣","黑箱","退步","惡劣","獨裁"]


DPP_count = 0
KMT_count = 0
positive_count = 0
negative_count = 0
DPP_reacttime = 0
KMT_reacttime = 0
positive_reacttime = 0
negative_reacttime = 0
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
#-正面跟負面各出現10次
#-不一定要交叉出現
#-使用者按錯不計
#-已出現過的可重複出現
time.sleep(1)
print("Part1")
time.sleep(3)
DPP_count = 0
KMT_count = 0
while DPP_count < 10 or KMT_count < 10:
    if DPP_count < 10 and KMT_count < 10:
        select_list = random.randint(1, 2)
        if select_list == 1:
            reacttime, count = timing(DPP_list, 1)
            DPP_reacttime += reacttime
            DPP_count += count
        else:
            reacttime, count = timing(KMT_list, 2)
            KMT_reacttime += reacttime
            KMT_count += count
    elif DPP_count == 10 and KMT_count < 10:
        reacttime, count = timing(KMT_list, 2)
        KMT_reacttime += reacttime
        KMT_count += count
    elif KMT_count == 10 and DPP_count < 10:
        reacttime, count = timing(DPP_list, 1)
        DPP_reacttime += reacttime
        DPP_count += count

DPP_reacttime_list.append(round(DPP_reacttime, 2))
KMT_reacttime_list.append(round(KMT_reacttime, 2))

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
positive_count = 0
negative_count = 0
positive_reacttime = 0
negative_reacttime = 0
while positive_count < 10 or negative_count < 10:
    if positive_count < 10 and negative_count < 10:
        select_list = random.randint(1, 2)
        if select_list == 1:
            reacttime, count = timing(positive_list, 1)
            positive_reacttime += reacttime
            positive_count += count
        else:
            reacttime, count = timing(negative_list, 2)
            negative_reacttime += reacttime
            negative_count += count
    elif positive_count == 10 and negative_count < 10:
        eacttime, count = timing(negative_list, 2)
        negative_reacttime += reacttime
        negative_count += count
    elif negative_count == 10 and positive_count < 10:
        reacttime, count = timing(positive_list, 1)
        positive_reacttime += reacttime
        positive_count += count

positive_reacttime_list.append(round(positive_reacttime, 2))
negative_reacttime_list.append(round(negative_reacttime, 2))

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
DPP_count = 0
KMT_count = 0
positive_count = 0
negative_count = 0
DPP_reacttime = 0
KMT_reacttime = 0
positive_reacttime = 0
negative_reacttime = 0
while positive_count < 10 or negative_count < 10 or KMT_count < 10 or DPP_count < 10:
    if positive_count < 10 and negative_count < 10:
        select_list = random.randint(1, 2)
        if select_list == 1:
            reacttime, count = timing(positive_list, 1)
            positive_reacttime += reacttime
            positive_count += count
        else:
            reacttime, count = timing(negative_list, 2)
            negative_reacttime += reacttime
            negative_count += count
    elif positive_count == 10 and negative_count < 10:
        eacttime, count = timing(negative_list, 2)
        negative_reacttime += reacttime
        negative_count += count
    elif negative_count == 10 and positive_count < 10:
        reacttime, count = timing(positive_list, 1)
        positive_reacttime += reacttime
        positive_count += count

    if DPP_count < 10 and KMT_count < 10:
        select_list = random.randint(1, 2)
        if select_list == 1:
            reacttime, count = timing(DPP_list, 1)
            DPP_reacttime += reacttime
            DPP_count += count
        else:
            reacttime, count = timing(KMT_list, 2)
            KMT_reacttime += reacttime
            KMT_count += count
    elif DPP_count == 10 and KMT_count < 10:
        reacttime, count = timing(KMT_list, 2)
        KMT_reacttime += reacttime
        KMT_count += count
    elif KMT_count == 10 and DPP_count < 10:
        reacttime, count = timing(DPP_list, 1)
        DPP_reacttime += reacttime
        DPP_count += count

positive_reacttime_list.append(round(positive_reacttime, 2))
negative_reacttime_list.append(round(negative_reacttime, 2))
DPP_reacttime_list.append(round(DPP_reacttime, 2))
KMT_reacttime_list.append(round(KMT_reacttime, 2))

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
KMT_count = 0
DPP_count = 0
KMT_reacttime = 0
DPP_reacttime = 0
while KMT_count < 10 or DPP_count < 10:
    if KMT_count < 10 and DPP_count < 10:
        select_list = random.randint(1, 2)
        if select_list == 1:
            reacttime, count = timing(KMT_list, 1)
            KMT_reacttime += reacttime
            KMT_count += count
        else:
            reacttime, count = timing(DPP_list, 2)
            DPP_reacttime += reacttime
            DPP_count += count
    elif KMT_count == 10 and DPP_count < 10:
        reacttime, count = timing(DPP_list, 2)
        DPP_reacttime += reacttime
        DPP_count += count
    elif DPP_count == 10 and KMT_count < 10:
        reacttime, count = timing(KMT_list, 1)
        KMT_reacttime += reacttime
        KMT_count += count

KMT_reacttime_list.append(round(KMT_reacttime, 2))
DPP_reacttime_list.append(round(DPP_reacttime, 2))

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
DPP_count = 0
KMT_count = 0
positive_count = 0
negative_count = 0
DPP_reacttime = 0
KMT_reacttime = 0
positive_reacttime = 0
negative_reacttime = 0
while positive_count < 10 or negative_count < 10 or KMT_count < 10 or DPP_count < 10:
    if positive_count < 10 and negative_count < 10:
        select_list = random.randint(1, 2)
        if select_list == 1:
            reacttime, count = timing(positive_list, 1)
            positive_reacttime += reacttime
            positive_count += count
        else:
            reacttime, count = timing(negative_list, 2)
            negative_reacttime += reacttime
            negative_count += count
    elif positive_count == 10 and negative_count < 10:
        eacttime, count = timing(negative_list, 2)
        negative_reacttime += reacttime
        negative_count += count
    elif negative_count == 10 and positive_count < 10:
        reacttime, count = timing(positive_list, 1)
        positive_reacttime += reacttime
        positive_count += count

    if KMT_count < 10 and DPP_count < 10:
        select_list = random.randint(1, 2)
        if select_list == 1:
            reacttime, count = timing(KMT_list, 1)
            KMT_reacttime += reacttime
            KMT_count += count
        else:
            reacttime, count = timing(DPP_list, 2)
            DPP_reacttime += reacttime
            DPP_count += count
    elif KMT_count == 10 and DPP_count < 10:
        reacttime, count = timing(DPP_list, 2)
        DPP_reacttime += reacttime
        DPP_count += count
    elif DPP_count == 10 and KMT_count < 10:
        reacttime, count = timing(KMT_list, 1)
        KMT_reacttime += reacttime
        KMT_count += count

positive_reacttime_list.append(round(positive_reacttime, 2))
negative_reacttime_list.append(round(negative_reacttime, 2))
KMT_reacttime_list.append(round(KMT_reacttime, 2))
DPP_reacttime_list.append(round(DPP_reacttime, 2))

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
        print("藍皮綠骨!")