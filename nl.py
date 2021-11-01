# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 06:52:11 2020

@author: KarthickB
"""

from imapclient import IMAPClient
mail = IMAPClient('imap.gmail.com', ssl=True, port=993)
mail.login("karthickbmca@gmail.com", "July@2021")
totalMail = mail.select_folder('Inbox')
#Shows how many messages are there - both read and unread
print('You have total %d messages in your folder' % totalMail[b'EXISTS'])
delMsg = mail.search(('UNSEEN'))
mail.delete_messages(delMsg)
#Shows number of unread messages that have been deleted now
print('%d unread messages in your folder have been deleted' % len(delMsg))
mail.logout()
n