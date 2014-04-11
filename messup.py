# -*- coding: utf-8 -*-

import sys
import random
from random import randint

def main():
	if len(sys.argv) < 2:
		print 'Usage: python messup.py <file-name-inclued-postifx> <amount-of-random-file-to-generate>'
		sys.exit(0)

def saveToFile(file, count):
	i = 0
	while i < int(count):
		i += 1
		with open(file, "r") as fin:
			with open(file.split('.')[0]+str(i)+getRandPostfix(), "a") as fout:
				while True: 
					bin = fin.read(randint(64,4096))
					if bin:
						if randint(0,1) == 1:
							fout.write(bin)
					else:
						break

def getRandPostfix():
	postfixarray = ['.bin','.iso','.mp3','.doc','.gif','.avi']
	return random.choice(postfixarray)

if __name__=="__main__":

    main()
