import subprocess
import os
import time

## ps: cmd 指令 进入 嵌套命令行 在本程序中是失效的
## ps: cd 盘符:\ 在本程序中是失效的
## ps: 部分命令执行了没有提示
## ps: cmd命令执行为阻塞式

class CMDSupport(object):
    default_path = ""
    now_path = ""

    def __init__(self):
        self.default_path = os.getcwd()
        self.now_path = self.default_path
        pass

    def chdir(self,new_path):
        os.chdir(new_path)
        self.last_result = "原目录：" + self.now_path + "\n切换当前目录：" + os.getcwd()
        self.now_path = os.getcwd()
        pass
    def excute_cmd(self,str_cmd):
        if str_cmd.startswith("cd ") and os.path.exists(os.getcwd()+"\\" + str_cmd[len("cd "):]):
            self.chdir(os.path.join(os.getcwd()+"\\" + str_cmd[len("cd "):]))            
        elif os.path.exists(str_cmd):          
            self.chdir(str_cmd)           
        else:
            a = subprocess.Popen(str_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            b = a.stdout.readlines()
            result = ""
            for i in range(len(b)):
                result = result + b[i].decode("gbk")
            self.last_result = result
        return( self.last_result)

if __name__ == '__main__':
    
    demo = CMDSupport()
    while True:
        str_cmd = input("请输入命令:")
        rtn = demo.excute_cmd(str_cmd)
        rtn = "\n-----输出begin-----\n\n" + rtn + "\n-----输出end-----\n"
        print(rtn)
