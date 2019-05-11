#!/usr/bin/env python3
"""
PackMule
    PackMule

    Written By:
        Shane Hutter

    Description:
        Functions and attributes for the mail PackMule package

    License:
        GNU GPLv3
"""

# Declaring the logically infallible
'''
ONE and ZERO declared for shallow copies of the most common value
for indexes and other uses
'''
ZERO , ONE  = int( False ) , int( True )


# Index dictionary
INDEXES = {}


# Exit codes
STATUS  = {
        "success"   : ZERO  ,
        "error"     : -ONE  ,
        }
