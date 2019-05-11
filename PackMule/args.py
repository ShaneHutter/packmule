#!/usr/bin/env python3
"""
PackMule
    PackMule.args

    Written By:
        Shane Hutter

    Description:
        Argument parsing for packmule

    License:
        GNU GPLv3
"""

__all__ = [ argparser , ]


from argparse   import ArgumentParser


PRIMARY_SWITCHES    = {
        "create"    : {
            "title"         : "Create"                                  ,
            "description"   : """
            Create and manage a locally (remotely?) built package
            repository

            """                                                         ,
            }
        "database"    : {
            "title"         : "Database"                                ,
            "description"   : """
            Clean and maintain the local databases
            """                                                         ,
            }
        "info"      : {
            "title"         : "Information"                             ,
            "description"   : """
            Display package, package group, and repository information 
            from packages, package groups, and repositories installed 
            or setup locally on the system
            """                                                         ,
            }           ,
        "query"     : {
            "title"         : "Query"                                   ,
            "description"   : """
            Query package, package group, and repository information
            from a remote package repository
            """                                                         ,
            }           ,
        "remove"    : {
            "title"         : "Remove"                                  ,
            "description"   : """
            Remove packages and package groups from the local system.
            Delete locally created package repositories off of the
            system.
            """                                                         ,
            }           ,
        "sync"      : {
            "title"         : "Sync"                                    ,
            "description"   : """
            Syncronize and packages from a repository
            """                                                         ,
            }           ,
        "update"    : {
            "title"         : "Update"                                  ,
            "description"   : """
            Update and upgrade local repository database and packages
            from remote repositories.
            """                                                         ,
            }           ,
        }


def argparser():
    """
        Command line arguments for PackMule
    """
    parser              = ArgumentParser( **PROGRAM_INFO )
    primary_swicthes    = (
            parser.add_mutually_exclusive_group( required = True )
            )
    '''
        Can I add argument groups connected to each primary switch?
    '''
    info                = (
            primary_switches.add_argument_group()
            )
    query               = (
            primary_switches.add_argument_group()
            )
    remove              = (
            primary_switches.add_argument_group()
            )
    sync                = (
            primary_switches.add_argument_group()
            )
    update              = (
            primary_switches.add_argument_group()
            )



    return parser.parse_args()
