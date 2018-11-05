import sys
import re

def readSyntax(filename, regexList):
	"""
	Opening and reading syntax file (regex)
	Using "".join() to concatenate the element of list
	that is returned by re.findall()
	"""
	syntaxfile = open(filename, 'r')
	regex = syntaxfile.readlines()
	for x in regex:
		search = "".join(re.findall('"(.*)"', x))
		name = "".join(re.findall('": .+$', x))[3:]
		regexList.append((name, search))
	syntaxfile.close()

def readTheme(filename, colorList):
	"""
	Opening and reading themefile file (colors)
	Using "".join() to concatenate the element of list
	that is returned by re.findall()
	"""
	themefile = open(filename, 'r')
	theme = themefile.readlines()

	for x in theme:
		colorValue = "".join(re.findall('[0-9];[0-9]+$', x))
		name = "".join(re.findall('.+:', x))[:-1]
		colorList.append((name, colorValue))
	themefile.close()

def readFile(filename):
	"""
	Opening and reading sourcefile_to_color file (target file to color)
	"""
	sourcefile_to_color = open(filename, 'r')
	text = sourcefile_to_color.read()
	sourcefile_to_color.close()
	return text
def mergeLists(regexList, colorList, library):
	"""
	Merging my two list to one single list as my own library.
	I'm asuming that the syntax and theme files are equally long,
	and at the same order (order with name)
	"""

	if len(regexList) == len(colorList):

		for x in range(len(regexList)):
			for y in range(len(colorList)):
				if regexList[x][0] == colorList[y][0]:
					library.append((regexList[x][1], colorList[y][1]))
					break




if __name__ == '__main__':
    regexList = []
    colorList = []
    library = []

    readSyntax(sys.argv[1], regexList)
    readTheme(sys.argv[2], colorList)
    mergeLists(regexList, colorList, library)
    text = readFile(sys.argv[3])
    mylist=[]
    mylist2=[]
    mylist3={}
    mylist='hello ther world it is me'.split(' ')
    mylist2='it is me that is me'.split(' ')
    for x in range(len(mylist)):
        for y in range(len(mylist2)):
            mylist.append(mylist[x][0],mylist2[y][1])

    print(mylist)
    print(mylist2)
    print(mylist3)
