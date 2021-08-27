#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Master module for metest.logmetric
"""
from metest.logharmonie import logDate
import sys
import argparse
import sqlite3
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
                        minim_iteration_statistics = logDate.get_minimisation_iterations_statistics()
                        
                        dataframes = [cycle, minim_iteration_statistics]
                        self.write_results(dataframes, args)
                else:
                    print("File: {}, does not exist".format(logfile), flush=True)
        return


    def write_results(self, dataframes:list, args:argparse.Namespace) -> None:
        """Write the results to database

        Parameters
        ----------
        dataframes : list
            List of pandas dataframes to write. Each dataframe is written to individual tables.
            A dataframe holding CYCLE must always be first.
        """

        db = dataframes[0]['CYCLE'][0].strftime('{}/logmetric_{}_%Y%m%d_%H%M.db'.format(args.output_dir, args.model))

        connection = sqlite3.connect(db)

        for dataframe in dataframes:
            dataframe.to_sql(dataframe.table, connection, if_exists='replace')
            print('Successful write to table: {}'.format(dataframe.table))

        connection.close()

        print('Output database: {}'.format(db))

        return