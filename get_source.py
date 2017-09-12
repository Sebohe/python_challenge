#!/usr/bin/env python3
import requests
import sys
def main(argv):
    
    requestPage = requests.get(argv[0])

    f1 =  open('source','w+')
    f1.write(requestPage.text)
    f1.close()

    f1 = open('source','r')

    withinCommentBlock = False
    comments = ''
    for line in f1.readlines():
        
        if '<!--' in line:
            withinCommentBlock = True

        if '-->' in line:
            withinCommentBlock = False

        if withinCommentBlock:
            comments += line

    #print (comments)
    with open('comments','w+') as f2:
        f2.write(comments)



if __name__ == "__main__":
    main(sys.argv[1:])

