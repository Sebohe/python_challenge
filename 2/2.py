#!/usr/bin/env python3
#http://www.pythonchallenge.com/pc/def/equality.html

def charify(filename):

    characters = ""
    with open(filename, 'r') as file:
        lines = file.readlines()

        for line in lines:
            for char in line:
                characters += char



    file.close()
    return characters



if __name__ =="__main__":

    characters = charify("comments")

    solution = ""

    for k, char in enumerate(characters):
        if char.islower():
            
            examine = characters[k-4:k+5]
            
            countUpperCase = 0

            for member in examine:
                if member.isupper():
                    countUpperCase += 1

            if examine[0].islower() and examine[-1].islower() and countUpperCase == 6:

                solution += char


print (solution)
