""" 
命令行快速休眠工具
"""
import os

repos = [
    {'path': "D:/learning/note", 'name': 'note'},
    {'path': "D:/learning/graduate-design", 'name': 'graduate-design'}
]

def main():
    # 判断git代码是否推送
    for repo in repos:
        os.chdir(repo['path'])
        status = os.popen("git status")
        result = status.read()
        if 'Your branch is up to date with' not in result:
            print("\033[1;31;1m" + repo['name'] + "代码未推送，请及时推送\033[0m")

    print("按下回车休眠")
    str = input()
    if (str == ""):
        os.system("shutdown -h")

main()