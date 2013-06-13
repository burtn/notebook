#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# coding: utf-8
import sys
from random import randint
import time
stopwords = \
"""
in
it
be
both
which
It
if
may
can
have
of
-
so
a
an
on
into
such
as
but
its
are
the
The
from
also
they
at
for
For
These
these
is
that
to
too
This
this
and
include
by
has
""".split("\n")

try:
	filepath = sys.argv[1]
	if sys.argv[1] == '--WORDS':
		print stopwords
		raise IOError
except:
	print "You must supply a file argument!\n	e.g. \x1b[30;1m delete.py Overfishing.md \x1b[0m"
	sys.exit()
	
with open(filepath, 'r') as cfile:
    contents = cfile.read()
    sentences = contents.split('.')

for sentence in sentences:
	sentence = sentence.strip()
	if not sentence == "":
		words = sentence.split()
		for i in range(3):
			rand = randint(0,words.__len__() -1)
			if not (words[rand] == '[...]' or words[rand] in stopwords):
				sentence = sentence.replace(words[rand], '[...]')
				print sentence
				correct = False
				while not correct:
					if sys.stdin.readline().strip() == words[rand]:
						print '\x1b[32;1m ✔ \x1b[0m'
						correct = True
					else:
						print '\x1b[31;1m ✘ ' + words[rand] + '\x1b[0m'
						
				
				sentence = sentence.replace('[...]', words[rand])
				time.sleep(0.5)
				print chr(27) + "[2J"
				
		
			
	
	