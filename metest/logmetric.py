#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Master module for metest.logmetric
"""
from metest.logharmonie import logDate
import sys
import argparse
from dmit import ostools
import logharmonie

class logmetric:

    def __init__(self, args:argparse.Namespace) -> None:
        """Init function for logmetric
        """
        
        if args.model=='harmonie':
            self.read_harmonie_logs(args)

        return


    def read_harmonie_logs(self, args:argparse.Namespace) -> None:
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
                if ostools.does_file_exist(logfile):
                    prefix = logfile.split('/')[-1]
                    logfamiliy = prefix.split('_')[1] #"Date", "MakeCycleInput"
                    
                    if logfamiliy=="Date":
                        logDate = logharmonie.logDate(logfile)
                        cycle = logDate.get_date()
                        bator_selected_bufr_synop = logDate.get_bator_bufr_total_selected_synop()
                        print(bator_selected_bufr_synop)
                else:
                    print("File: {}, does not exist".format(logfile), flush=True)
        return