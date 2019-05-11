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


# Program Information

__author__  = "Shane Hutter"
__version__ = "0.0.0-1"
__bin__     = "packmule"

PROG_INFO   = {
        "prog"          : __bin__                                       ,
        "description"   : """
        A Python3 based wrapper and package manager for RHEL based Linux
        distributions.
        """                                                             ,
        }
