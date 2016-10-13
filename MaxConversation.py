#!/usr/bin/env python3
import argparse

res={}

parser=argparse.ArgumentParser(description='add file to find who spoke and who didn\'t')
k=open('logs','r')
parser.add_argument('-g',metavar='FILES',type=argparse.FileType('r'),nargs='*',default=[k])

parser.add_argument('-f',metavar='FILE',type=argparse.FileType('r'),nargs='?',default=k)

args = parser.parse_args()

files=[]

if args.f:
	files=[args.f]
elif args.f is None:
	files=[k]
elif args.g:
	files=args.g

if len(files)==0:
	print('Also input filenames as arguments')
	exit()

for i in files:
	#open file and process users
	for line in i:
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
	i.close()

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

