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
        "version"    : {
            "title"         : "Version"                                 ,
            "description"   : """
            Display PackMule version, and other details
            """                                                         ,
            }
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
    create              = (
            primary_switches.add_argument_group(
                PRIMARY_SWITCHES[ "create" ]
                )
            )
    databases           = (
            primary_switches.add_argument_group(
                PRIMARY_SWITCHES[ "databases" ]
                )
            )
    info                = (
            primary_switches.add_argument_group(
                PRIMARY_SWITCHES[ "info" ]
                )
            )
    query               = (
            primary_switches.add_argument_group(
                PRIMARY_SWITCHES[ "query" ]
                )
            )
    remove              = (
            primary_switches.add_argument_group(
                PRIMARY_SWITCHES[ "remove" ]
                )
            )
    sync                = (
            primary_switches.add_argument_group(
                PRIMARY_SWITCHES[ "sync" ]
                )
            )
    update              = (
            primary_switches.add_argument_group(
                PRIMARY_SWITCHES[ "update" ]
                )
            )
    version             = (
            primary_switches.add_argument_group(
                PRIMARY_SWITCHES[ "version" ]
                )
            )



    return parser.parse_args()
