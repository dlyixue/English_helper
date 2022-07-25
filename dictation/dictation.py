import imp
from itertools import count
import pandas as pd
import os
import time
from turtle import right

from sklearn.metrics import accuracy_score
def get_now_time():
    """
    获取当前日期时间
    :return:当前日期时间
    """
    now =  time.localtime()
    # now_time = time.strftime("%Y-%m-%d %H:%M:%S", now)
    now_time = time.strftime("%Y-%m-%d ", now)
    return now_time
print("Start")
ch = int(input("chapter: "))
te = int(input("test: "))
f = open("./English_Learning_Helper/dictation/data/test/test.txt","w+")
ls = []
while(1):
    word = input()
    if(word == "end"):
        break;
    ls.append(word)

align = 15
for i in range(len(ls)):
    word = ls[i]
    f.write(word)
    for j in range(len(word),align):
        f.write(" ")
    if(i % 4 == 3):
        f.write("\n")
f.close()

now_time = get_now_time()
right_file = "c"+str(ch)+"t"+str(te)+".txt"
f_result = "./English_Learning_Helper/dictation/data/result/test"+now_time+".csv"
f_right  = open("./English_Learning_Helper/dictation/data/right/"+right_file,"r")
read_right = f_right.read()
right_words = read_right.split()
result = pd.DataFrame(columns=['right', 'your'])
accuracy = 0

for i in range(len(right_words)):
    if i >= len(ls) :
        result.loc[len(result.index)] = [right_words[i],"no words"]
        #f_result.write("right words: " + right_words[i] + " -> no your words" + "\n")
        #continue
    elif ls[i] != right_words[i]:
        result.loc[len(result.index)] = [right_words[i],ls[i]]
        #f_result.write("right words: " + right_words[i] + " -> your words: " + ls[i] + "\n")
    else:
        accuracy = accuracy + 1

print("accuracy : ", accuracy,"   all:    ", len(right_words) , "   "   ,accuracy*100/len(right_words), "%")
f_right.close()
result.to_csv(f_result, header=['right', 'your'], index=False, mode='w+')