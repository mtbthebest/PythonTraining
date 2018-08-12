# coding=utf-8

import re
import reprlib
RE_WORD = re.compile('\w+')

class Sentence:
	def __init__(self, text):
		self.text = text
		self.words = RE_WORD.findall(text)
	def __getitem__(self, index):
		return self.words[index]
	def __len__(self):
		return len(self.words)
	def __repr__(self):
		return 'Sentence(%s)' % reprlib.repr(self.text)
	
	def __iter__(self):
		return (match.group() for match in RE_WORD.finditer(self.text))

if __name__ == '__main__':
	s = Sentence('"The time has come," the Walrus said,')
	print(s)
	for word in s:  
		print(word)
	print(list(s))