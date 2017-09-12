#!/usr/bin/env python3

from comments2 import TEXT

def charify(filename):

    with open(filename, 'r') as file:
        lines =  file.readline()

    file.close()
    return lines

if __name__ == "__main__":
    


    print (ord('a'), ord('z'))
    nonRareCharacters = ''
    for ch in TEXT:
       
        if ord(ch) <= ord('z') and ord(ch) >= ord('a'):

            print (ch)
            nonRareCharacters =  nonRareCharacters + ch
    
    print (nonRareCharacters)

