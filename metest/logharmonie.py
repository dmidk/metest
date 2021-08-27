#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Master module for metest.logharmonie
Called from metest.logmetric
"""
import datetime as dt
import pandas as pd
from typing import Union

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


    def get_date(self) -> pd.DataFrame:
        """Get the date of the cycle

        Returns
        -------
        pd.DataFrame
            Datetime object of logfile wrapped in dataframe.
        """
        cycle = None
        substring = 'log files of HARMONIE cycle'
        for line in self.file_content:
            if substring in line:
                cycle = dt.datetime.strptime(line, '<H1>log files of HARMONIE cycle %Y%m%d%H</H1>\n')
                break

        df = pd.DataFrame([cycle], columns=['CYCLE'])
        df.table = 'cycle'

        return df

#NSTEP, CPU

    def get_minimisation_iterations_statistics(self) -> pd.DataFrame:
        """Fetch statistics from minimisation iterations

        Returns
        -------
        pd.DataFrame
            Dataframe holding statistics from minimisation
        """

        df = pd.DataFrame(columns = ['ITER', 'J'])

        iterations = []
        costfunction = []

        header = '--- Variational job : minimization (quasi-Newton method)------------------'
        substring = 'GREPGRAD - LSIMPLE,ITER,SIM,GRAD,J'
        # GREPGRAD - LSIMPLE,ITER,SIM,GRAD,J      0   0 0.4057364254001857E+03 0.2381451615987310E+05

        found_header = False

        for line in self.file_content:
            if header in line:
                found_header = True
            if substring in line and found_header:
                line_data = line.split()
                
                iteration = int(line_data[4])
                J = float(line_data[6])
                
                if iteration < 999: 
                    iterations.append(iteration)
                    costfunction.append(J)

        
        df['ITER'] = iterations
        df['J'] = costfunction
        df.table = 'get_minimisation_iterations_statistics'

        return df