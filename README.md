contextimap
===========

Handles the base to the connection to a Imap based host  , encapsulated in a context manager environment.

Usage:
==========
Create the configuration properties file using the following instructions:

touch ~/.imaplibrc.config

Use the following as the basic properties configuration:
[connection_properties]
hostname=imap.gmail.com ; can be any IMAP hostname gmail's just an example
usessl=true
port=993

[user_properties]
username:[your_username]
password:[your_password] #Extend this to encapsulate encryption if required.

Usage Example:
=============

with ImapHandler() as handler:
                folderlist = handler.list()
                print folderlist

This print's the folder list for the particular user.

Advantages:
==========
1. Learning about Imap lib can be a thing of the past. :P Although you have to.
2. Code is a lot simplified as with any context management code.
3. Connection is automatically opened and closed as required.









