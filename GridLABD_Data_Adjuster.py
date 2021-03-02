######################################## GRIDLAB-D DATA ADJUSTMENT ########################################
# Importing libraries used:
import pandas as pd
import datetime
import numpy as np
import io

def Data_Adjuster_2(filepath):

    #df = pd.read_csv('Test_mdf.csv')
    df2 = pd.read_excel(filepath)
    ########################################################################################
    #df2 = pd.read_csv('P1-39_2.21-2.22_MDF2.csv')

    df = df2[['timestamp', 'Dryer Power', 'New Row_difference for unix']]
    ########################################################################################
    Indicator = df['New Row_difference for unix']

    df['timestamp'] = pd.to_datetime(df['timestamp'],format='%Y-%m-%d %H:%M:%S')
    #
    df['time_diff'] = (df.timestamp.shift(-1) - df.timestamp).dt.seconds.fillna(0).astype(int)
    df['next_ind'] = Indicator.shift(-1).fillna(0).astype(int)
    #
    df.loc[(Indicator < 1) & (df.next_ind == 0), 'time_diff'] = 1
    df.loc[(Indicator == 0) & (df.next_ind == 0), 'time_diff'] = 1
    #
    df['timestamp'] = df.apply(lambda x: list(pd.date_range(x['timestamp'], periods=x['time_diff'], freq=pd.DateOffset(seconds=1))),axis=1)
    df = df.explode('timestamp')
    # df.drop(columns=['time_diff','next_ind'],inplace=True)
    #print(df)
    #
    columns = ['time_diff','next_ind','New Row_difference for unix']
    df.drop(columns, axis=1, inplace=True)
    #
    # cols = list(df.columns)
    # cols[0], cols[1] = cols[1], cols[0]
    # df = df[cols]

    # df.columns.name = None
    # df.index.name = None

    df.to_csv('Neocharge_log_2_21_2021_OUT_MDF2_GLD.csv', header=None, index=False)
    #df.to_excel('Neocharge_log_2_21_2021_OUT_MDF2_GLD.xlsx', index=False)

#if __name__ == '__main__':
#   Data_Adjuster_2('Neocharge_log_2_21_2021_OUT_MDF2.xlsx')