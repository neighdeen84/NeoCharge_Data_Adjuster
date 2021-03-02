# Importing called functions:
from Data_Adjuster import Data_Adjuster_1
from GridLABD_Data_Adjuster import Data_Adjuster_2
from Zero_Padder import Zero_Padder


# Running the first data adjuster function:
Data_Adjuster_1('Neocharge_log_2_21_2021_OUT_MDF.xlsx')

# Running the second GridLAB-D data adjuster function:
Data_Adjuster_2('Neocharge_log_2_21_2021_OUT_MDF2.xlsx')

# Running the zero padding function:
Zero_Padder('Neocharge_log_2_21_2021_OUT_MDF2_GLD.csv')




