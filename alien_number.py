#!/usr/bin/python -tt

import sys

def anum_to_int(anum,alang):
	base = len(alang)
	j = 0
	digit = []
	while j < len(anum):
		digit.append(alang.find(anum[j]))
		j = j + 1
	
	integer = 0
	k = 0
	
	while k < len(anum):
		integer = integer + digit[k] * base ** ( len(anum) - k -1 )
		k = k + 1

	return integer 

def int_to_anum(int,alang):
	base = len(alang)
	anum = ""	
	q = int
	
	while True:
		r = q % base
		q = q / base
		anum = alang[r] + anum
		if q == 0:
			break

	return anum

N = input()

i = 0

while i < N:
	i = i + 1
	line = sys.stdin.readline()
	words = line.split()

	if len(words) != 3:
		print "error: invalid input %s" % (line)

	print "Case #%d: %s" %(i, int_to_anum( anum_to_int(words[0],words[1]),words[2]))
	
