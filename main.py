#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import re

from base import Base
from os import path

# 核心替换函数
def replaceVersion(replacedfiles, replaceLinks):
	for f in replacedfiles:	
		f1 = open(f,'r+',encoding= 'utf-8')
		infos = f1.readlines()
		f1.seek(0,0)
		for line in infos:	
			line_new = line
			for rfile in replaceLinks:
				file_new = rfile.strip().lstrip().replace("\n", "")
				#print(file_new)
				if path.exists(file_new):
					# 是否有需要替换的文件
					if line.find(file_new) == -1:
						continue;
					
					print(line)
					line_new = base.replaceLine(line, "201")			

			f1.write(line_new)
		f1.close()
	print("处理完成")
base = Base();
#print("md5:"+base.md5file('modifyPassword.html'))

excludeTemplateDirs=["WEB-INF1"]
templateDirs=["WEB-INF"]
templateFileTypes=[".html"]

# 获取需要被替换引用文件的列表
replacedfiles = base.listFiles(templateDirs, templateFileTypes, excludeTemplateDirs)
print(replacedfiles)

# 获取引用文件的列表
replaceLinks = base.readLines("replaceLinks.txt")
print("待替换的前端文件")
print(replaceLinks)
print("\n开始替换\n")
replaceVersion(replacedfiles, replaceLinks);
