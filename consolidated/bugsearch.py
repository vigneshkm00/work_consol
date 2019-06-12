import pandas as pd 
import glob, os
os.chdir("C:\\Users\\vikm\\Documents\\cosnolpro")
df = pd.read_csv("consowo.csv")
df.columns = ['platform','release','project_type','assg_date','sora_id','bug_id','sev','compo','ini_bug_cat','fin_bug_cat','executor','exec_comp_date','reviewer','rev_comp_date','rev_feed','modif','approv','add_rem']
as_date = 'Assigned Date for execution'
ex_date = 'Execution Completion Date'
while True:
    bugid = input("Enter bug id:")
    print(df[(df.bug_id == bugid)].release)
    print(df[(df.bug_id == bugid)].platform)
    print(df[(df.bug_id == bugid)].project_type)
    print(df[(df.bug_id == bugid)].assg_date)
    print(df[(df.bug_id == bugid)].executor)
    print(df[(df.bug_id == bugid)].reviewer)
    print(df[(df.bug_id == bugid)].fin_bug_cat)
    print(df[(df.bug_id == bugid)].rev_feed)


