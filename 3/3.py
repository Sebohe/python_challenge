#!/usr/bin/env python3
import requests


def followLink(node):


    page = requests.get(node)
    for line in page.iter_lines():
        if "php" in str(line):

            #https://docs.python.org/3.3/library/stdtypes.html#bytes.decode
            data = bytes.decode(line)
            break

    load = data.split("?")[1]

    

    load = load.split("=")[0]

    return [load,next]

def followPHP(link):

    text = requests.get(link).text

    textList = text.split(" ")

    load = text

    if "nothing" in text:
        load = "nothing"

    link = textList[-1]

    return [load, link]

if __name__ == "__main__":
    

    #output = followLink("http://www.pythonchallenge.com/pc/def/linkedlist.php")

    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    output = followPHP(url+"12345")
    print (output)



    counter = 0

    while counter <= 400:


        counter += 1
        lastLink = output
        output = followPHP(url+lastLink[1])

        if output[1] == '16044':
            #http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=16044
            #https://i.imgur.com/JGzNZX9.jpg
            output[1] = str(int(output[1])/2)
            output[0] = "nothing"

        if output[0] != "nothing":
            break


    print (lastLink)
    print (output)



