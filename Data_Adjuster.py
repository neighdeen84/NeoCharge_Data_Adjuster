######################################## DATA ADJUSTMENT ########################################
# Importing libraries used:
import pandas as pd
import datetime

def Data_Adjuster_1(filepath):
    # Read csv file or excel file
    #df = pd.read_csv('Neocharge_log_1_18_2020_mdf.csv')
    df = pd.read_excel(filepath)

    # Filter data
    #df = excel[['hr_msg','timestamp', 'P0', 'P1','S0','S1']] [0:373]
    #print(df)

    # Converting unix code to pacific time
    df['converted_time'] = pd.to_datetime(df['time'], unit='s')
    df['converted_time'] = df['converted_time'].dt.tz_localize('utc').dt.tz_convert('US/Pacific')
    df['converted_time'] = df['converted_time'].dt.strftime('%Y-%m-%d %H:%M:%S')


    # Compute Row difference between n row and n-1 row
    for index, row in df.iterrows():
        df['Row_difference for P0'] = df['P0'].diff()
        df['Row_difference for P1'] = df['P1'].diff()
        df['Row_difference for S0'] = df['S0'].diff()
        df['Row_difference for S1'] = df['S1'].diff()
        #df['delta'] = (df['P0']-df['P0'].shift()).fillna(0)
        #df2 = df.loc[(df['hr_msg'] == "POWER_CHANGE")]
        #print(df2)

    df['Row_difference for unix'] = df['time'].diff()


    # Calculating Total dryer Power
    p = df['P1'] - df['P0']
    df['Dryer Power'] = ((240 * df['P0']) + (120 * p))/1000
    #New code
    df2 = df #new dataframe
    new_index = 0 #to keep track of index in df2 inside the loop

    for i,row in df.iterrows():
        new_row = {}
        if (row['hr_msg'] == "POWER_CHANGE") and (row['Row_difference for unix'] > 1) or (row['hr_msg'] == "Pri_LOCKOUT") \
                and (row['Row_difference for unix'] == 0) and (i!=0):
            for column in df.columns:
                if column == 'timestamp':
                    new_row[column] = row[column] + datetime.timedelta(seconds=-1)
                else:
                    new_row[column] = prev_row[column]

            line = pd.DataFrame(new_row, index=[new_index])
            df2 = pd.concat([df2.iloc[:new_index,:], line, df2.iloc[new_index:,:]]).reset_index(drop=True)
            new_index+=2 # Adding 2 instead of 1 because we have added a new row to the new dataframe
        else:
            new_index+=1
        prev_row = row


    df2['New Row_difference for unix'] = df2['time'].diff()
    #df2['New Row_difference for unix'] = df2['timestamp_unix_full'].diff()

    #df2.to_csv('Neocharge_log_2_20_2021_OUT_MDF2.csv', index=False)
    df2.to_excel('Neocharge_log_2_21_2021_OUT_MDF2.xlsx', index=False)
    #print(df)

    #df2.to_csv('Neocharge_log_1_18_2020_MDF_filter.csv',index=False)
    #print(index,row [['timestamp','P0','P1','S0','S1']])

#if __name__ == '__main__':
#    Data_Adjuster_1('Neocharge_log_2_21_2021_OUT_MDF.xlsx')
