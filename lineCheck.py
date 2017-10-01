'''This program will allow you to go through a directory and it's subdirectories in order to figure out if there exists a line of a particular length '''

import os 
import argparse
from os.path import join


argparser = argparse.ArgumentParser (description 'Gettin started')
argparser.add_argument('--input', default =".", type=str, help="Tell me the path to the file")
argparser.add_argument('--len', type=int, help="Tell me the length of the string you want to find")

args = argparser.parse_args()
place = args.input
length = args.len

def find(place, length):
	newlist =[]
	for root, dirs, files in os.walk(place):
            for j in files:
                if j in files:
                    if j.endswith(".txt"):
                        newlist.append(join(root,j))
                    for i in newlist:
                        with open(i) as fi:
                            for count,line in enumerate(fi, 1):
                                if len(line) > length:
                                    print(len(line),count,i)
find(place,length)

