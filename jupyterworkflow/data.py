import os
from  urllib.request import urlretrieve

import numpy as np
import pandas as pd

FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'
FREMONT_FILE = 'fremont.csv'

def get_fremont_data(filename=FREMONT_FILE, url=FREMONT_URL, force_download=False):
    """Download and cache the Fremont bike data
    
    Parameters
    ----------
    filename: string (optional)
        Location of the downloaded file
    
    url: string (optional)
        Web location of the data
        
    force_download: bool (optional)
        if True, force re-download of the data
    
    Returns
    -------
    data: pandas.DataFrame
        The Fremont bridge data 
            index: Date (datetime)
            columns: East, West, Total (number)
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(url, 'fremont.csv')
        
    cols = ["Date", "Fremont Bridge East Sidewalk", "Fremont Bridge West Sidewalk"]
    
    data = pd.read_csv('fremont.csv', index_col='Date', usecols=cols)
    try:
        data.index = pd.to_datetime(data.index, format='%m/%d/%Y %H:%M:%S %p')
    except TypeError:
        data.index = pd.to_datatime(data.index)
        
    data.columns = ['East', 'West']
    data['Total'] = data['East'] + data['West']
    return data