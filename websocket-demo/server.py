import asyncio
import websockets
import json
import random

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
"""
terms = ['左手食指放在 E 鍵上 右手食指放在 I 鍵上<br>按「空白鍵」開始', '真誠', '吳敦義', '厭惡', 'DPP/F.jpg', '結束囉～']
cnpt_attrs = ['dontmatter', 'a', 'c', 'a', 'c', 'dontmatter']
answers = ['dontmatter', 'left', 'right', 'right', 'left', 'dontmatter']
blocks = ['01', 3, 3, 3, 3, 6]
stim_lst = [Stim(term, cnpt_attr, ans, blk) for term, cnpt_attr, ans, blk in zip(terms, cnpt_attrs, answers, blocks)]

"""
DPP_list = ["蔡英文", "謝長廷", "蘇貞昌", "賴清德", "陳菊", "林佳龍", "鄭文燦", "陳水扁", "陳其邁", "柯建銘"]
KMT_list = ["馬英九", "朱立倫", "韓國瑜", "吳敦義", "王金平", "侯友宜", "盧秀燕", "連戰", "丁守中", "郝龍斌"]
positive_list = ["讚","棒","好","優秀","了不起","卓越","進步","開明","友善", "聰明"]
negative_list = ["爛","廢","遜","糟糕","拙劣","黑箱","退步","惡劣","獨裁", "愚蠢"]
left_ans = ['left']*10
right_ans = ['right']*10
cnpts = ['c']*10
attrs = ['a']*10
DPP_rt_list = []
KMT_rt_list = []
block1 = [1]*10
block2 = [2]*10
block3 = [3]*10
block4 = [4]*10
block5 = [5]*10

block1_stim_list = [Stim(term, cnpt_attr, ans, blk) for term, cnpt_attr, ans, blk in zip(DPP_list, cnpts, left_ans, block1)] + [Stim(term, cnpt_attr, ans, blk) for term, cnpt_attr, ans, blk in zip(KMT_list, cnpts, right_ans, block1)]
block2_stim_list = [Stim(term, cnpt_attr, ans, blk) for term, cnpt_attr, ans, blk in zip(positive_list, attrs, left_ans, block2)] + [Stim(term, cnpt_attr, ans, blk) for term, cnpt_attr, ans, blk in zip(negative_list, attrs, right_ans, block2)]
block3_cnpt_list = [Stim(term, cnpt_attr, ans, blk) for term, cnpt_attr, ans, blk in zip(DPP_list, cnpts, left_ans, block3)] + [Stim(term, cnpt_attr, ans, blk) for term, cnpt_attr, ans, blk in zip(KMT_list, cnpts, right_ans, block3)]
block3_attr_list = [Stim(term, cnpt_attr, ans, blk) for term, cnpt_attr, ans, blk in zip(positive_list, attrs, left_ans, block3)] + [Stim(term, cnpt_attr, ans, blk) for term, cnpt_attr, ans, blk in zip(negative_list, attrs, right_ans, block3)]
block4_stim_list = [Stim(term, cnpt_attr, ans, blk) for term, cnpt_attr, ans, blk in zip(KMT_list, cnpts, left_ans, block4)] + [Stim(term, cnpt_attr, ans, blk) for term, cnpt_attr, ans, blk in zip(DPP_list, cnpts, right_ans, block4)]
block5_cnpt_list = [Stim(term, cnpt_attr, ans, blk) for term, cnpt_attr, ans, blk in zip(KMT_list, cnpts, left_ans, block5)] + [Stim(term, cnpt_attr, ans, blk) for term, cnpt_attr, ans, blk in zip(DPP_list, cnpts, right_ans, block5)]
block5_attr_list = [Stim(term, cnpt_attr, ans, blk) for term, cnpt_attr, ans, blk in zip(positive_list, attrs, left_ans, block5)] + [Stim(term, cnpt_attr, ans, blk) for term, cnpt_attr, ans, blk in zip(negative_list, attrs, right_ans, block5)]

random.shuffle(block1_stim_list)
random.shuffle(block2_stim_list)
random.shuffle(block3_cnpt_list)
random.shuffle(block3_attr_list)
random.shuffle(block4_stim_list)
random.shuffle(block5_cnpt_list)
random.shuffle(block5_attr_list)

block3_stim_list = []
block5_stim_list = []
for i in range(10):
	block3_stim_list.append(block3_attr_list[i])
	block3_stim_list.append(block3_cnpt_list[i])
	block5_stim_list.append(block5_attr_list[i])
	block5_stim_list.append(block5_cnpt_list[i])
    
block0_1 = [Stim("左手食指放在 E 鍵上 右手食指放在 I 鍵上<br>按「空白鍵」開始", "dontmatter", "dontmatter", 0)]
block1_1 = [Stim("Part1<br>E:DPP I:KMT", "dontmatter", "dontmatter", "01")]
block2_1 = [Stim("Part2<br>E:positive I:negative", "dontmatter", "dontmatter", 12)]
block3_1 = [Stim("Part3<br>E:DPP&positive I:KMT&negative", "dontmatter", "dontmatter", 23)]
block4_1 = [Stim("Part4<br>E:KMT I:DPP", "dontmatter", "dontmatter", 34)]
block5_1 = [Stim("Part5<br>E:KMT&positive I:DPP&negative", "dontmatter", "dontmatter", 45)]
    
stim_lst = block0_1 + block1_1 + block1_stim_list + block2_1 + block2_stim_list + block3_1 + block3_stim_list + block4_1 + block4_stim_list + block5_1 + block5_stim_list

# Websockets server function
async def experiment(websocket, path):
    for i in range(len(stim_lst)):
        # Send stimulus to client
        sending = stim_lst[i]
        await websocket.send(sending.toJSON())
        ##print('Sent to client:\n', sending, sep='')
        
        # Receive repsonse from client
        res = await websocket.recv()
        msg = json.loads(res)
        sending.rt = float(msg['rt'])
        sending.correct = str2bool(msg['correct'])
        stim_lst[i] = sending  # Save received result
        ##print('Received from client:\n', sending, '\n', sep='')

        # hold for 1sec before next round
        #await asyncio.sleep(1)
        
        # Print final result after receiving the last trial
        if i == len(stim_lst) - 2:
            print('Printing results ...')
            for stim in stim_lst:
                print(stim)
                print()

start_server = websockets.serve(experiment, 'localhost', 8765)        


asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
