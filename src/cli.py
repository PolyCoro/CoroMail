#!/usr/bin/python3
"""
Usage:
	cli.py [-s|--server] [--port=<int>]
	cli.py send (--name=<str>) 

Options:
	-h --help     Show this screen.
	-s --server   Launch a server (default behavior is launching a client)
	-n --name	  The name of the receiver we want to send the data to	  
	--port=<int>    The port used by the underlying program [default: 0] @int
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
	server = False
	# Necessary for pytest automation

	ARGS = docopt(__doc__,argv=args)
	print(ARGS)
	if(ARGS["--port"]):
		if(int(ARGS["--port"])<0):
			raise ValueError
		port = int(ARGS["--port"] )
	else :
		#TODO : <> are supposed to make something mandatory, but it doesnt seem to work
		if (ARGS["--port"]=='') :
			raise ValueError
	

	if( "-s", "--server" in ARGS):
		if ARGS["-s"] or ARGS["--server"]:
			ARGS["--server"],ARGS["-s"] =True,True
	

	return ARGS


if __name__ == '__main__':
	main()
