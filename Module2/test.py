# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 13:47:42 2020

@author: subha
"""
json = ['sender', 'receiver', 'amount']
transaction_keys = ['sender', 'receiver', 'amount']
if not all [keys in json for keys in transaction_keys]:
    print("Missing parameters from the part")