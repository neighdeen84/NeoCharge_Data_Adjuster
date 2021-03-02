######################################## ZERO PADDING ########################################
# Importing libraries used:
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import datetime

def Zero_Padder(filepath):
    # Enter in the csv you want to process:
    df = pd.read_csv(filepath, header=None)

    # Labeling columns:
    df.columns = ['Date', 'Power']

    # Converting the date column to type datetime:
    df.Date = df.Date.astype('datetime64[ns]')

    #print(df)
    df.set_index('Date',inplace=True)
    #print (df.dtypes)


    # #The time stamp in the csv you read in is seen as a string
    # #lines 11-12 changes the string to actual numbers
    # date_time_str = '2021-01-31 10:59:06' # Class str
    # date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S') # Class datetime.datetime


    #line 18-20 sets up a timestamp that is a 24 hour period
    #in a dataframe called dg
    date = pd.to_datetime("20th of feb, 2021")
    date_series = date + pd.to_timedelta(np.arange(1440*60), 's')
    dg =  pd.DataFrame(date_series)
    dg.columns = ['Date']
    #print(dg)
    dg.set_index('Date',inplace=True)
    #print (dg.dtypes)

    # Merging:
    dg2 = pd.merge(dg, df, left_index = True, right_index = True, how = 'left')

    # Resetting indices for god knows why:
    dg2 = dg2.reset_index(drop=False)

    # Replacing NaN values with zeroes:
    dg2.fillna(0, inplace=True)

    ################################################################
    # d = dg2['Date']
    # dg2['Date'] = pd.to_datetime(year= 2021, month=2,)
    dg2['Date']=dg2['Date'].apply(lambda dt: dt.replace(year=2021, day=7, month=2))

    print(dg2)
    print(dg2.shape) # checking dg2 dimensions
    print(dg2.isnull().values.any()) # checking for NaN values


    # Printing out the final output CSV: :D
    dg2.to_csv('TEST_dryer_profile_611_1.csv',header=None, index=False)

#if __name__ == '__main__':
#   Data_Adjuster_2('Neocharge_log_2_21_2021_OUT_MDF2_GLD.csv')