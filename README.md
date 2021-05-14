# NeoCharge Data Adjuster

## Project Description
This script combines three seperate python functions used to adjust the NeoCharge data to prepare it to be processed by GridLAB-D. The output of each function is the input of the next one. See figure below.


![Untitled Diagram(3)](https://user-images.githubusercontent.com/60201315/118065929-a745ed00-b352-11eb-8cc1-f525202c45a6.png)

The Data_Adjuster script has a function Data_Adjuster_1 that takes an input file (.xlsx or .csv) and converts the unix code to pacific time. Then it iterates through all the rows and computes the difference between the previous row and next row. This row difference between the previous unix time code and the next time code along with the “hr_msg” column which indicates the status of the Neocharge device is used to insert a row where there’s a “power change” or “primary lockout” and repeat the previous row values. Additionally, the power calculation of the Neocharge currents on the primary side is computed in the script. The output of function Data_Adjuster_1 is fed into function Data_Adjuster_2, which is created in the GridLABD_Data_Adjuster script.


The GridLABD_Data_Adjuster script has a function that takes an input csv.file (usually the output of the Data Adjuster Script), creates a column called “indicator” and another column “time_diff” then uses these columns to create a 1 second resolution that extends over the full timestamp of the input data. This is done by repeating the previous row values in the input file until there is a timestamp change. Finally, Zero_Padder has a function Zero_Padder that takes in the output of function Data_Adjuster_2 and finalizes the profile by adding all the missing rows in the 24-hour period (top and bottom of the dataset), then assigns those rows a poewr value of zero.




## Requirements

```
pip install pandas datetime numpy
```

### To get the code
```
git clone https://github.com/neighdeen84/NeoCharge_Data_Adjuster.git
```


## Usage
```
cd NeoCharge_Data_Adjuster
python main.py
```
