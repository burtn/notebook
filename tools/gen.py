import os
import sys
import re
import platform
import tempfile as temp
import random

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
	BOOK_INFO = re.compile('<book.+>')
	LICENCE_INFO = re.compile('.*<licence .+/>')
	COLOPHON = re.compile('.*<colophon.+>')
	UNKNOWN = re.compile('.*<.+>.*')
	ABOUT_DIR = re.compile('.*<about.+/>.*')
	WORD = re.compile('.*<word>.+</word>.*')
	FILE = re.compile('.*<file.+/>.*')
	
class config:
    path = ''
    aboutfiles = []
    metadata = {'title': '', 'colophon': '', 'extra': '', 'licence': '', 'licence-url': '', 'ver': ''}

	
def dictFromLine(line):
	pairs = []
	ValueString = re.findall('[a-z]*=".+"', line)
	Seperate = re.split('"\s', ValueString[0])
	for i in Seperate:
		pairs.append(i.replace("\"","").split('='))
	
	return dict(pairs)

def main():
    print "Checked path \t" + colour.OK + "OK" + colour.END
    try:
    	prelims = open(config.path + "prelims.xml", 'r')
    except:
    	abort("File Error")
    	
    for line in prelims:
    	if (expression.BOOK_INFO.match(line)):
    		xml = dictFromLine(line)
    		config.metadata['title'] = xml['title']
    	elif (expression.LICENCE_INFO.match(line)):
    		xml = dictFromLine(line)
    		config.metadata['licence-url'] = xml['url']
    		config.metadata['licence'] = xml['name']
    	elif (expression.COLOPHON.match(line)):
    		xml = dictFromLine(line)
    		config.metadata['ver'] = xml['version']
    	else:
    		if not (expression.UNKNOWN.match(line)):
    			config.metadata['colophon'] = config.metadata['colophon'] + line.lstrip()
    	
    prelims.close()
    
    for root, dirs, files in os.walk(config.path):
    	for filename in files:
       		if (filename.endswith('about.xml')):
       			config.aboutfiles.append(root + "/" + filename)
    
    for path in config.aboutfiles:
    	tmp = open('../out/' + str(random.randint(1,100)), 'w')
    	file = open(path, 'r')
    	keywords = []
    	filelist = []
    	topic = ''
    	directory = os.path.dirname(path) + "/"
    	for line in file:
    		if (expression.ABOUT_DIR.match(line)):
    			try:
    				xml = dictFromLine(line)
    				topic = xml['topic'].strip()
    			except:
    				abort("XML Error")
    		elif (expression.WORD.match(line)):
    			keywords.append(line.replace('<word>', '').replace('</word>', '').strip())
    		elif (expression.FILE.match(line)):
    			try:
    				xml = dictFromLine(line)
    				filelist.append(directory + xml['path'].strip())
    			except:
    				abort("XML Error")
    	for file in filelist:
    		tmp.write(os.path.basename(file).strip().replace('.md', '').replace('_', ' ') + '\n')
    		read = open(file, 'r')
    		for keyword in keywords:
    			for line in read:
    				if (keyword in line):
    					 tmp.write(line.replace(keyword, '<strong>' + keyword + '</strong>'))
    				else:
    					tmp.write(line)
    					


def isDir(path):
	return os.path.isdir(path)

def abort(message):
	print colour.WARN + message + colour.END
	sys.exit()
	
config = config()

if (len(sys.argv) == 2):
	if (isDir(sys.argv[1])):
		config.path = sys.argv[1]
		main()
else:
	print usageinfo

