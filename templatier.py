#!/usr/bin/python3

import re
import sys
import pprint

class TypeDecl:
	def __init__(self, name, types, typenames):
		self.name = name
		self.types = types
		self.typenames = typenames
	def __str__(self):
		return "{0}: {1}".format(self.name, list(zip(self.types, self.typenames)))
	def __repr__(self):
		return self.__str__()
	
def is_whitespace(c):
	return c in [' ', '\t', '\r', '\n']

def is_alpha(c):
	return \
		(ord(c) >= ord('a') and ord(c) <= ord('z')) and \
		(ord(c) >= ord('A') and ord(c) <= ord('Z'))

def is_num(c):
	return ord(c) >= ord('0') and ord(c) <= ord('9')

def next_token(text):
	if len(text) == 0:
		return text, None
	stream = iter(text)
	c = next(stream)
	if is_whitespace(c):
		while is_whitespace(c):
			c = next(stream)
		return next_token(''.join(list(stream)))
	if is_alpha(c) or c == '_':
		chars = [c]
		c = next(stream)
		while is_alpha(c) or is_num(c) or c == '_':
			chars.append(c)
			c = next(stream)
		s = ''.join(chars)
		return ''.join(list(stream)), ''.join(chars)
	

def template(text):
	text = "abcdf ef_3"
	text, token_a = next_token(text)
	text, token_b = next_token(text)
	print(token_a, token_b)
	
	return None
	type_pattern = re.compile("^@type [^\n]*", flags=re.MULTILINE);
	file_pattern = re.compile("^@file [^\n]*", flags=re.MULTILINE);

	type_decls = type_pattern.findall(text)
	file_segments = list(zip(file_pattern.findall(text), file_pattern.split(text)[1:]))

	#types = [parse_type_decl(decl) for decl in type_decls]
	for decl in type_decls:
		tokens = []
		while True:
			decl, token = next_token(decl)
			if not token:
				break
			tokens.append(token)
		print(tokens)
		
	print(types)

def main(argv):
	if len(argv) < 2:
		print("Kindly provide at least one template")
		exit(1)
	for arg in argv[1:]:
		with open(arg, "r") as f:
			s = f.read()
		template(s)

if __name__ == "__main__":
	main(sys.argv)
	
