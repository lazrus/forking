import re
from mymodul import *

def grep(syntax,file):
    with open(file,'r') as text:
        for line in text:

            start_code = "\033[{}m".format(93)
            end_code="\033[0m"

            match=re.finditer(syntax,line)

            if match:
                for i in match:
                    start_code = "\033[{}m".format(94)
                    end_code="\033[0m"
                    change=start_code + i.group() + end_code
                    print(i.group())
                    line=re.sub(syntax,change,line)
                    print(line)
                print(line)

if __name__ == '__main__':
    reg=r"bb"
    grep(reg,sys.argv[1])
    txt="aabbbcccc is the real"
    start_code = "\033[{}m".format(94)
    end_code="\033[0m"
    change=start_code + 'cc' + end_code
    tx=re.sub("bb",change,txt)
    print(tx)
