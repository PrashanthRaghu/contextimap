import imaplib
import ConfigParser
import os

"""

@@Authored By : Prashanth Raghu
@@Email : p.is.prashanth@gmail.com
@@Licensed under: Creative Commons.  Free to copy and distribute. Attribution would be great, atleast do not change the name of the author in this file :P.
@@version : 1.0

Logging is not configured under this module. You are free to add the same in a branch/ I will add that in the next change.

"""


class ImapHandler(object):
	"""
	 handles the base to the connection to a Imap based folder
	 encapsulated in a context manager environment
	"""
	__hostname__=''
	__port__=''
	__usessl__=''
	__username__=''
	__password__=''
	connection = '' # Holds the connection object

	def __init__(self):
		configmap = ConfigParser.SafeConfigParser()
		configmap.read([os.path.expanduser('~/.imaplibrc.config')])
		self.__hostname__= configmap.get('connection_properties','hostname')
		self.__port__ = configmap.getint('connection_properties','port')
		self.__usessl__= configmap.getboolean('connection_properties','usessl')
		self.__username__ = configmap.get('user_properties','username') 
	        self.__password__ = configmap.get('user_properties','password') # Can be encrypted if needed
	
	def __enter__(self):
		if self.__usessl__:
			self.connection = imaplib.IMAP4_SSL(self.__hostname__) 
		else:
			self.connection = imaplib.IMAP4(self.__hostname__) #Normal text based sockets

		self.connection.login(self.__username__ , self.__password__)	
		print '%s logged into IMAP host %s successfully'%(self.__username__,self.__hostname__)
		return self.connection
	
	def __exit__(self,exc_type, exc_val, exc_tb):
		#Just exiting the connection here no exception handling
		print 'Imap connection closed down'
		self.connection.logout()

	""" 
	     The functions of imap handler is just too exhaustive.
	     So avoid repitition, have exposed the method to obtain the connection. use the connection to continue the
	     normal IMAP functions.
        """


if __name__=="__main__":
	with ImapHandler() as handler:
		folderlist = handler.list()
		print folderlist











