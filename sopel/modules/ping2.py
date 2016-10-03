# coding=utf-8
"""
ping.py - Sopel Ping Module
Author: Sean B. Palmer, inamidst.com
About: http://sopel.chat
"""
""""
Trying to fix ping2 it doesnt seem to work on irc. 
"""
from __future__ import unicode_literals, absolute_import, print_function, division

import random
from sopel.module import rule, priority, thread

from sopel.module import rule, priority, thread, commands

@commands('ping')
def ping2(bot, trigger):
    bot.say('Pong!')

@rule('\!ping')
def bangping(bot, trigger):
    bot.say('Pling.')
