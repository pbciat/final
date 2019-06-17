import asyncio
import websockets
import json
import random
from stim import *

DPP_list = ["DPP/A.png", "DPP/B.jpg", "DPP/C.jpg", "DPP/D.jpg", "DPP/E.jpg", "DPP/F.jpg", "DPP/G.jpg", "DPP/H.jpg", "DPP/I.jpg", "DPP/J.jpg"]
KMT_list = ["KMT/A.png", "KMT/B.jpg", "KMT/C.jpg", "KMT/D.jpg", "KMT/E.jpg", "KMT/F.jpg", "KMT/G.jpg", "KMT/H.jpg", "KMT/I.png", "KMT/J.jpg"]
positive_list = ["真誠","卓越","進步","開明","友善","大方","機智","愛台","清廉", "勤政"]
negative_list = ["虛偽","拙劣","退步","獨裁","惡劣","小氣","愚昧","賣台","貪汙", "怠惰"]
left_ans = ['left']*10
right_ans = ['right']*10
cnpts = ['c']*10
attrs = ['a']*10
block1 = [1]*10
block2 = [2]*10
block3 = [3]*10
block4 = [4]*10
block5 = [5]*10
DPP_rt_list = []
KMT_rt_list = []
block3_rt = 0
block5_rt = 0

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
for i in range(20):
	block3_stim_list.append(block3_attr_list[i])
	block3_stim_list.append(block3_cnpt_list[i])
	block5_stim_list.append(block5_attr_list[i])
	block5_stim_list.append(block5_cnpt_list[i])
    
block0_1 = [Stim("左手食指放在 E 鍵上 右手食指放在 I 鍵上<br>按「空白鍵」開始", "dontmatter", "dontmatter", 0)]
block1_1 = [Stim("", "dontmatter", "dontmatter", "01")]
block2_1 = [Stim("", "dontmatter", "dontmatter", 12)]
block3_1 = [Stim("", "dontmatter", "dontmatter", 23)]
block4_1 = [Stim("", "dontmatter", "dontmatter", 34)]
block5_1 = [Stim("", "dontmatter", "dontmatter", 45)]
block6_1 = [Stim("", "dontmatter", "dontmatter", 6)]
    
stim_lst = block0_1 + block1_1 + block1_stim_list + block2_1 + block2_stim_list + block3_1 + block3_stim_list + block4_1 + block4_stim_list + block5_1 + block5_stim_list + block6_1

# Websockets server function
async def experiment(websocket, path):
    for i in range(len(stim_lst)):
        if i != len(stim_lst) - 1:
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
        else:
            stim_lst[len(stim_lst) - 1].content = judge(stim_lst, DPP_list)
            sending = stim_lst[i]
            await websocket.send(sending.toJSON())

# Start server
start_server = websockets.serve(experiment, 'localhost', 8765)        
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

