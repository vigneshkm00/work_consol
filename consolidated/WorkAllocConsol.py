import pandas as pd 
import glob, os
os.chdir("C:\\Users\\vikm\\Documents\\cosnolpro")
path = os.getcwd()
all_files = os.listdir(path)
work_files = [f for f in all_files if f[-4:] == 'xlsx']
print(work_files)
dataframe = pd.DataFrame()
for file_name in work_files:
    data = pd.read_excel(file_name,'Security - IC - Work allocation')
    dataframe = dataframe.append(data,sort=False)
file_nametosav = input("Enter file name to save:")
dataframe.to_excel(file_nametosav+".xlsx")
print("Success...")