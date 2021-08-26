#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Master module for metest.logmetric
"""
import sys
import argparse

class logmetric:

    def __init__(self, args:argparse.Namespace) -> None:
        """Init function for logmetric
        """
        
        if args.model=='harmonie':
            self.read_harmonie(args)

        return


    def read_harmonie(self, args:argparse.Namespace) -> None:
        """Read log files from Harmonie

        Parameters
        ----------
        args : argparse.Namespace
            Class of arguments to module

        Notes
        -----
        Three main log files exist with different prefix. 
        These are read from the file input and different functions
        are called accordingly
        """

        logfiles = [args.file, args.file2]
        for logfile in logfiles:
            if logfile is not None:
                prefix = logfile.split('/')[-1]
                logfamiliy = prefix.split('_')[1] #"Date", "MakeCycleInput"
                print(logfamiliy)
        return