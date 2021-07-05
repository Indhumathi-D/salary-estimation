# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 17:02:02 2021

@author: Indhumathi
"""

import time
import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/Indhumathi/Documents/salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 1000, False, path, 15)


df.to_csv('glassdoor_jobs.csv', index = False)