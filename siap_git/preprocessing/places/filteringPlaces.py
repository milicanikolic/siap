import pandas as pd
import numpy as np

"""
    Iz pronadjenih mesta izbacujemo one koji nemaju popunjen rejting.
"""

dfAll = pd.read_csv('placesFiles/MANHATTAN/MANHATTAN.csv')
print dfAll.shape

dfAll = dfAll[~dfAll['rating'].isnull()]
print( dfAll.shape)
dfAll.to_csv('placesFiles/MANHATTANfiltered.csv', index=False)
