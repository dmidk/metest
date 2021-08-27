#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Master module for metest.logharmonie
Called from metest.logmetric
"""
import datetime as dt

class logDate:

    def __init__(self, hmdate_file:str) -> None:
        """Initialiser for HM_Date logfiles

        Parameters
        ----------
        hmdate_file : str
            Path to HM_Date logfile
        """

        file = open(hmdate_file, mode='r')
        self.file_content = file.readlines() #Read everything into memory
        file.close()
        return


    def get_date(self) -> dt.datetime:
        """Get the date of the cycle

        Returns
        -------
        dt.datetime
            Datetime object of logfile
        """
        substring = 'log files of HARMONIE cycle'
        for line in self.file_content:
            if substring in line:
                cycle = dt.datetime.strptime(line, '<H1>log files of HARMONIE cycle %Y%m%d%H</H1>\n')
                break

        return cycle

    
    def get_bator_bufr_total_selected_synop(self) -> int:
        """Get number of total selected BUFR synops in Bator

        Returns
        -------
        int
            Number of total selected BUFR synops
        """

        header = '*** INFO - BATOR : reading data from BUFR.synop'
        substring = 'Total selected Obs'

        found_header = False

        for line in self.file_content:
            if header in line:
                found_header = True
            if substring in line and found_header:
                selected_obs = int(line.split()[4]) # ['Total', 'selected', 'Obs', '=', '874', '-->', '5889', 'datas.']
                break

        return selected_obs