#!/usr/bin/python3
"""
Usage:
	cli.py [-s|--server] [--port=int]

Options:
	-h --help     Show this screen.
	-s --server   Launch a server (default behavior is launching a client)
	--port=int    The port used by the underlying program [default: 0] 
"""
import logging
from docopt import docopt

def main(*args,**kwargs):
	""" Parse the options and launch the program accordingly 
		Args:
		*args (tuple) : Argument passed to the program
		**kwargs (tuple) : unused
	""" 
	port = 000

	# Necessary for pytest automation

	ARGS = docopt(__doc__,argv=args)
	print(ARGS)
	if( "-s", "--server" in ARGS):
		if ARGS["-s"] or ARGS["--server"]:
			ARGS["--server"],ARGS["-s"] =True,True


	return ARGS


if __name__ == '__main__':
	main()
