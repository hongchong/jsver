#!/usr/bin/python
# -*- coding: UTF-8 -*-

from hashlib import md5
import re
import os

class Base:
	def listFiles(self, templateDirs, templateFileTypes, excludeTemplateDirs):
		for templateDir in templateDirs:
			for root, dirs, files in os.walk(templateDir):
				i = 0
				list = []
				while i < len(dirs):
					if os.path.join(root, dirs[i]) in excludeTemplateDirs:
						dirs.pop(i)
					else:
						i = i + 1
					
				for file in files:
					srcFile = os.path.join(root, file)
					fileParts = os.path.splitext(srcFile)
					if fileParts[1] in templateFileTypes:
						 list.append(srcFile)
	
				
				return list;
				
	def mkdirs(self, filePath):
		l = filePath.split("/")[:-1]
		savedir = "//".join(l)
		try:
			os.makedirs(savedir)
		except:
			pass
	
	def readFile(self, filePath):
		file = open(filePath, "r")
		content = file.read()
		file.close()
		return content
	
	def writeFile(self, filePath, content):
		if os.path.exists(filePath) == False:
			self.mkdirs(filePath)
		file = open(filePath, "w")
		file.write(content)
		file.close()
	
	def readLines(self, filePath):
		file = open(filePath, 'r')
		lines = file.readlines()
		file.close()
		return lines
	
	def writeLines(self, filePath, lines):
		if os.path.exists(filePath) == False:
			self.mkdirs(filePath)
		file = open(filePath, "w")
		file.writelines(lines)
		file.close()
	
	def isRelIconLine(self, line):
		m = re.match(r'.*<link.*rel\s*=\s*"[^\"]*icon[^\"]*".*',line)
		if m:
			return True
		return False
	
	def isImgLine(self, line):
		m = re.match(r'.*<img.*src\s*=\s*"[^"]*".*', line)
		if m:
			return True
		return False
	
	def isCssLine(self, line):
		m = re.match(r'.*<link.*(?=rel\s*=\s*"stylesheet").*', line)
		if m:
			return True
		return False
	
	def isJsLine(self, line):
		m = re.match(r'.*<script.*src\s*=\s*"[^"]*".*',line)
		if m:
			return True
		return False
	
	def replaceLine(self, line, ver):
		m1 = re.match(r'.*<script.*src\s*=\s*"([^\:\"]*)".*', line)
		m2 = re.match(r'.*<link.*href\s*=\s*"([^\:\"]*)".*', line)
		m3 = re.match(r'.*<img.*src\s*=\s*"[^"]*".*', line)
		line_new = line
		if m1 and m1.group(1) != '':
			str = m1.group(1).split('?')[0]
			line_new = line.replace(m1.group(1),str+"?v="+ver)
		elif m2 and m2.group(1) != '':
			str = m2.group(1).split('?')[0]
			line_new = line.replace(m2.group(1),str+"?v="+ver)
		
		return line_new		
	
	def md5file(self, filePath):
		file = open(filePath, 'rb')
		m = md5()
		while True:
			b = file.read(8096)
			if not b:
				break
			m.update(b)
		file.close()
		return m.hexdigest()

	def md5string(self, string):
		m = md5()
		m.update(string)
		return m.hexdigest()
