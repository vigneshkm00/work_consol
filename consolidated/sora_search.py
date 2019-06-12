import pandas as pd 
import glob, os
os.chdir("C:\\Users\\vikm\\Desktop\\New folder")
df = pd.read_excel("consol_asa.xlsx")
df.columns = ['release','bug_id','sev','comments','state','sme','sev','comp','executor']
pd.set_option('display.max_colwidth', -1)
while True:
    bugid = input("Enter bug id:")
    # print(df[(df.bug_id == bugid)].release)
    # print(df[(df.bug_id == bugid)].bug_id)
    # # print(df[(df.bug_id == bugid)].ver_bugid)
    # print(df[(df.bug_id == bugid)].sev)
    print(df[(df.bug_id == bugid)].comments)
    # print(df[(df.bug_id == bugid)].state)
    # print(df[(df.bug_id == bugid)].executor)


