import asyncio
import websockets
import json

# Helpers
def str2bool(sting):
    return sting.lower() in ("yes", "true", "t", "1")

# stimulus obj
class Stim():
    def __init__(self, content, cnpt_attr, answer='left', block=1):
        """
        content: str. Either a file path for image stimuls or 
                 a string for text stimulus.
        cnpt_attr: str. Either 'c' (concept, 政黨) or 'a' (attribute, 正負向詞彙).
                   The category that argument `content` belongs to (政黨 or 正負向詞彙).
        answer: str. 'left' or 'right'. Should the subject press
                the key `e` ('left') or the key `i` ('right') to 
                answer the question correctly?
        block: int or str. Can be one of the values below:
               1, 2, 3 ,4, 5: the block the stimulus belongs to
               01, 12, 23, 34, 45: intervals between blocks (指導語出現的地方)
               0: 起始畫面
               6: test feedback (block 3 & 5 之 RT 計算完後，給受試者的 feedback
        """
        self.content = content
        self.cnpt_attr = cnpt_attr
        self.answer = answer
        self.block = str(block)
        self.type = 'img' if content.endswith(('.png', '.jpg')) else 'text'
        self.rt = None
        self.correct = None

    def __str__(self):
        return "content: %s\nanswer: %s\nblock: %s\ntype: %s\nrt: %s\ncorrect: %s" % \
               (self.content, self.answer, self.block, self.type, self.rt, self.correct)
    
    def toJSON(self):
        stim_dict = {'content': self.content,
                    'answer': self.answer,
                    'block': self.block,
                    'type': self.type,
                    'cnpt_attr': self.cnpt_attr}
        return json.dumps(stim_dict)


# Calculating the result of the experiment from the list of Stim objects
def judge(stim_lst, DPP_list):
    valid = 1
    for i in range(len(stim_lst)): 
        if stim_lst[i].block == "3" or stim_lst[i].block == "5":
            if stim_lst[i - 1].block == "23" or stim_lst[i - 1].block == "45":
                DPPcount = 0
                KMTcount = 0
                DPP_rt = 0
                KMT_rt = 0
                wrongcount = 0
                totalcount = 0
            totalcount += 1
            if totalcount > 8:
                if stim_lst[i].correct == True and stim_lst[i].cnpt_attr == 'c':
                    if stim_lst[i].content in DPP_list:
                        DPPcount += 1
                        DPP_rt += stim_lst[i].rt
                    else:
                        KMTcount += 1
                        KMT_rt += stim_lst[i].rt
                elif stim_lst[i].correct == False:
                    wrongcount += 1
            if totalcount == 40:
                if wrongcount >= 16 or DPPcount == 0 or KMTcount == 0:
                    valid = 0
                    stim_lst[len(stim_lst) - 1].content = "tooMany"
                elif DPPcount != 0 and KMTcount != 0 and valid == 1:
                    if stim_lst[i].block == "3":
                        block3_rt_lst = []
                        block3_rt_lst.append("Reaction time for DPP : " + str(round(DPP_rt/DPPcount, 4)))
                        block3_rt_lst.append("Reaction time for KMT : " + str(round(KMT_rt/KMTcount, 4)))
                        block3_rt = round((DPP_rt + KMT_rt)/(DPPcount + KMTcount), 4)
                        block3_rt_lst.append("Average reaction time : " + str(block3_rt))
                    else:
                        block5_rt_lst = []
                        block5_rt_lst.append("Reaction time for DPP : " + str(round(DPP_rt/DPPcount, 4)))
                        block5_rt_lst.append("Reaction time for KMT : " + str(round(KMT_rt/KMTcount, 4)))
                        block5_rt = round((DPP_rt + KMT_rt)/(DPPcount + KMTcount), 4)
                        block5_rt_lst.append("Average reaction time : " + str(block5_rt))

    if valid == 1:
        if block3_rt < block5_rt - 0.15:
            stim_lst[len(stim_lst) - 1].content = "DPP"
        elif block3_rt - 0.05 > block5_rt:
            stim_lst[len(stim_lst) - 1].content = "KMT"
        else:
            stim_lst[len(stim_lst) - 1].content = "neutral"
        print("Block3 reaction time")
        for i in range(3):
            print(block3_rt_lst[i])
        print()
        print("Block5 reaction time")
        for i in range(3):    
            print(block5_rt_lst[i])
    else:
        print("invalid!")
        
    return stim_lst[len(stim_lst) - 1].content
