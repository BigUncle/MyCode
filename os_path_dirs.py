# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 20:01:38 2017

@author: Cy
"""

import os
import subprocess


err = []
result = []
with open('c:\\syncdirs.txt', 'w') as outfile:
                              # 以追加方式打开输出文件
    for dirpath, dirs, files in os.walk(u'j:\\'):                # 递归遍历当前目录和所有子目录的文件和目录
        for name in files:                                   # files保存的是所有的文件名
            filename = os.path.join(dirpath, name)       # 加上路径，dirpath是遍历时文件对应的路径
            #print(filename)
            try:
                if os.path.splitext(filename)[-1]=='.mp3':
                    outfile.write('%s\n' % filename)                          # 写入输出文件
                    result.append(filename)
            except:
                err.append(filename)
                print(filename)
                #break
def replace_white_space()
for dirpath, dirs, files in os.walk(u'j:\\'):                # 递归遍历当前目录和所有子目录的文件和目录
    for name in files:
        if name.count(' ') and os.path.splitext(filename)[-1]=='.mp3':
            new_filename = os.path.join(dirpath, name.replace(' ', ''))                                       # files保存的是所有的文件名
            filename = os.path.join(dirpath, name)       # 加上路径，dirpath是遍历时文件对应的路径
        #print(filename)
            try:
                os.rename(filename, new_filename)
            except Exception as e:
                print(e)


#item.split(' ')[0]
try:
    out_bytes = subprocess.check_call(['ffmpeg', '-i', result[1]], shell=False)
    #"j:\\粤语\\Bon Jovi\\Bon Jovi - Have a Nice Day.mp3"'], stderr=subprocess.STDOUT)
    out_bytes = subprocess.check_output(['ffmpeg', '-i', result[3].encode('utf-8')])
    #""j:\\粤语\\Bon Jovi\\Bon Jovi - Have a Nice Day.mp3""'])
except subprocess.CalledProcessError as e:
    out_bytes = e.output       # Output generated before error
    code      = e.returncode
for item in result:
    print(item, '\n')
#for e in err:
    #print('error occurs in filenames:\n', e)

