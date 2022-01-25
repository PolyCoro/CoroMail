#!/usr/bin/python3
"""
Usage:
	polycoro (((-s|--server) [--port=<int>] ) | ( -d | --debug) )
	polycoro send (NAME) [--port=<int>] [ -d | --debug] (TEXT | (--file=<str>))
	polycoro check (NAME) [--port=<int>] [ -d | --debug]  
	polycoro show (NAME)  
	polycoro setup (NAME) [config_path]
	polycoro getpub (NAME) [--port=<int>] [ -d | --debug] 

Options:
	-h --help     Show this screen.
	-s --server   Launch a server (default behavior is launching a client)
	-d --debug    Launch the application in debugging mode, AKA print the arguments this program can receive [default: False] 
	--port=<int>  The port used by the underlying program [default: 0] @int
	--file=<str>  Replace the TEXT entry with text provided in a file (evaluated from the execution directory)
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
		ARGS = docopt(__doc__,argv=args[0])
	else :
		ARGS = docopt(__doc__)

	if ARGS["-s"] or ARGS["--server"]:
		ARGS["--server"],ARGS["-s"] =True,True

	if(ARGS["--port"]):
		if((int(ARGS["--port"])<0) or (ARGS["--port"]=='')) :
			raise ValueError
		port = int(ARGS["--port"] )
	else :
		if ARGS["--port"]=='':
			raise ValueError

	if ARGS["-d"] or ARGS["--debug"]:
		debug = True
		ARGS["--debug"],ARGS["-d"] =True,True
		print(ARGS)

	if(ARGS["check"]):
		# The user still needs to be checked
		logging.info("Checked" + ARGS["NAME"] + " public key :\n")
	
	if(ARGS["show"]):

		logging.info("Showed" + ARGS["NAME"] + " infos :\n")


	if(ARGS["send"]):
		# The message still needs to be sent
		logging.info("Message sent to" + ARGS["NAME"] + " :\n")
		if ARGS["--file"] :
			with  open( ARGS["--file"], 'r') as f:
				logging.info(f.read())
		if ARGS["TEXT"]:
				logging.info(ARGS["TEXT"])

	return ARGS

if __name__ == '__main__':
	main()
