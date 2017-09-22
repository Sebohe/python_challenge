#!/usr/bin/env python3
import zipfile


def followFile(path):

    with open(path, 'r') as f:
        text = f.readline()

    text = text.split(" ")
    load = text
    if "nothing" in text:
        load = "nothing"

    next = text[-1]

    return [load, next]


if __name__ == "__main__":

    path = "channel/"

    output = followFile(path+"90052.txt")
    #print (output)
    counter = 0

    chars = ''
    zipfile = zipfile.ZipFile('channel.zip')
    while True:


        #convert b'' to string
        chars += str(zipfile.getinfo(output[1]+".txt").comment,'utf-8')

        counter += 1
        lastLink = output
        output = followFile(path+lastLink[1]+".txt")

        if output[0] != "nothing":
            break


    print (lastLink)
    print (output)
    print (chars)
