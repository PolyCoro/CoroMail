#!/usr/bin/python3
"""
Usage:
	cli.py [-s|--server] [--port=<int>] [ -d | --debug]
	cli.py send (--name=<str>) 

Options:
	-h --help     Show this screen.
	-s --server   Launch a server (default behavior is launching a client)
	-d --debug    Launch the application in debugging mode [default: False]
	-n --name	  The name of the receiver we want to send the data to	  
	--port=<int>  The port used by the underlying program [default: 0] @int
"""
import logging
from docopt import docopt

def main(*args,**kwargs):
	""" Parse the options and launch the program accordingly 
		Args:
		*args (tuple) : Argument passed to the program
		**kwargs (tuple) : unused
		test (Boolean) : if True, search for the input in args instead of stdin
	""" 
	port = 000
	server = False
	debug = False
	# Necessary for pytest automation
	if args:
		ARGS = docopt(__doc__,argv=args)
	else :
		ARGS = docopt(__doc__)


	if(ARGS["--port"]):
		if((int(ARGS["--port"])<0) or (ARGS["--port"]=='')) :
			raise ValueError
		port = int(ARGS["--port"] )
	else :
		if ARGS["--port"]=='':
			raise ValueError

	if( "-d", "--debug" in ARGS):
		if ARGS["-d"] or ARGS["--debug"]:
			print(ARGS)
			debug = True
			ARGS["--debug"],ARGS["-d"] =True,True

	if( "-s", "--server" in ARGS):
		if ARGS["-s"] or ARGS["--server"]:
			ARGS["--server"],ARGS["-s"] =True,True
	

	return ARGS


if __name__ == '__main__':
	main()
