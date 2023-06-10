#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
	n_tple = ()
	tple_f = tuple_a + (0, 0)
	tple_s = tuple_b + (0, 0)
	n_tple = tple_f[0] + tple_s[0], tple_f[1], tple_s[1]
	return n_tple
	
