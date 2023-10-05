#!/usr/bin/env python
"""
    This file is used for the 'pwd' command. It is responsible for printing the
    current working directory.
"""
import os,sys

def pwd(**kwargs):
    """
        pwd command : prints the current working directory
        Usage: pwd

        Parameters:
            kwargs (dict): dictionary of flags and parameters
        Returns:
            string: current working directory
        Examples:
            pwd
    """
    if not kwargs['stdin']:
        print(os.getcwd())
    return os.getcwd()

if __name__ == '__main__':
    pwd()