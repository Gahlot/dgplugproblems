#!/usr/bin/env python3
import sys

res = {}
files=[]
#files list passed as arguments in shell
for i in sys.argv[1:]:
	files.append(i)

if len(files)==0:
	print('Also input filenames as arguments')
	exit()

for i in files:
	#open file and process users
	with open(i) as fob:
		for line in fob:
		    if line.find('<') != -1:
		        k = line[12:].split('>')[0]
		        res[k] = res.get(k,{})
		    s = line.find('<')
		    if s != -1:
		        k = line[12:].split('>')
		        for call in k[1].split(' '):
		            so = call.strip(',:')
		            if so in res:
		                res[k[0]][so]=res[k[0]].get(so,0) + 1

#result
for i in res:
    if res[i] == {}:
        print(i,"not spoke")
    else:
        maxn = 0
        strname = ''
        for p in res[i]:
            if maxn < res[i][p]:
                strname = p
                maxn = res[i][p]
        print(i," spoke to ", strname, maxn, " times")

