import signal
import sys

def ctrlc(sig, frame):
    print('Goodbye')
    sys.exit(0)


def ctrld(sig, frame):
    print('Hard Goodbye')
    sys.exit(0)

class talk_interface:
	
    def __init__(self,talker,talkee,session):
        """ Chat like interface to talk to someone.
        Args:
                talker (str): the app user currently talking 
                talkee (str): the remote app user that talker is talking to
                session (Session) : the underlying session from which the message will be displayed
        """

        self.talker = talker
        self.talkee = talkee
        self.session = session
	
    def new_message(self,from_remote,text):
        """ Display message to someone
            Args:
                from_remote (boolean): is the message coming from outside  
                text (str): the message
        """
        
        if(from_remote):
            speaker = self.talkee 
        else:
            speaker = self.talker
        print(speaker + " : " + text)

    def run():
        """ Launch the interface
        """
        signal.signal(signal.SIGINT, ctrlc)
        signal.signal(signal.SIGKILL, ctrld)
        while(True):
            pass
            