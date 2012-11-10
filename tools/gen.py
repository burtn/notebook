import os
import sys
import re
import platform

usageinfo =  \
"""
    Usage: gen.py /path/to/dir/containing/notes/
    \t Read more at http://github.com/jake5991/notebook \n
    
    Note: To enable colour output on Windows the colorama module must be installed.

"""

class colour:
	INFO = '\033[36m'
	OK = '\033[32m'
	WARN = '\033[33m'
	END = '\033[0m'
    
	def disable(self):
		self.INFO = ''
		self.OK = ''
		self.WARN = ''
		self.END = ''

colour = colour()

try:
	from colorama import init
	init()
except ImportError:
	if (platform.system() == "Windows"):
		colour.disable()

class expression:
	pass

class config:
    pass

def dictFromLine(line):
	pairs = []
	ValueString = re.findall('[a-z]*=".+"', line)
	Seperate = re.split('"\s', ValueString[0])
	for i in Seperate:
		pairs.append(i.replace("\"","").split('='))
	
	return dict(pairs)

def main():
    pass

def isDir(path):
    pass

