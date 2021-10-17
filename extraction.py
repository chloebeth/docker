import os
from glob import glob

import socket
from collections import Counter

home = os.path.expanduser('~')
dir = os.getcwd()

os.chdir('data')

files = []
count = []
for f in glob('*.txt'): # only reading my text files (in mapped dir
    file = open(f, mode='r', encoding='utf-8')
    word = file.read()
    word = word.split()
    files.append(file.name)
    count.append(len(word))
    file.close()

listdir = os.listdir()
os.chdir(dir + '/output')

res = open('result.txt', mode='w', encoding='utf-8')
res.write('File Names in /home/data: ' + str(listdir) + '\n\n')

for id in range(len(files)):
    res.write('File Name ' + files[id] + ' has word count of ' + str(count[id]) + '\n')
res.write('Grand total words: ' + str(sum(count)) + '\n')

file = open('../data/IF.txt', mode='r', encoding='utf-8')
words = file.read()
words = words.split()

freq = Counter(map(lambda x: x.lower(), words))
three = sorted(freq.items(), key=lambda x: x[1], reverse=True)[0:3]

word = []
freq = []
for each in three:
    word.append(each[0])
    freq.append(each[1])

three = ''
for i in range(len(word)):
    three += str(word[i]) + ' : ' + str(freq[i]) + '\n'

res.write('\nTop three words of IF.txt:\n\n' + str(three) + '\n\n')

local = socket.gethostname()
ip = socket.gethostbyname(local)

res.write('IP Address ' + str(ip))

file.close()
res.close()

res = open('result.txt', mode='r', encoding='utf-8')

output = res.read()

print(output)
res.close()