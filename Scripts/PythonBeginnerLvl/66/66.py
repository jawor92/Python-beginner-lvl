# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 21:42:13 2019

@author: Mateusz.Jaworski
"""

chanels = {'Google':'1480', 'Email':'300', 'Natural Traffic':'440', 'TV Spot':'700' }

#print(chanels['Email'])

chanelsUpdate = {'Natural Traffic':'520', 'News':'600'}

#print(chanelsUpdate)

chanels.update(chanelsUpdate)

#print(chanels)

print(chanels.keys())

chanels.pop('Email')

print(chanels)