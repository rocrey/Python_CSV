import pandas as pd

'''If headers are included, then header argument gets removed or changed to indicate headers row'''
df = pd.read_csv("C:/Users/DAVIDREY/Documents/CSVTest.csv", header=None)

'''If headers are included, then this next line is not necessary'''
df.columns = ['user_id', 'first_name', 'last_name', 'version', 'ins_co']

ins_companies = df.ins_co.unique()
df = df.sort_values(by=['last_name', 'first_name', 'version'], ascending=[True, True, False])
df = df.drop_duplicates(subset=['user_id', 'ins_co'], keep='first')

for ic in ins_companies:
    temp_df = df.loc[df['ins_co'] == ic]
    temp_df.to_csv("C:/Users/DAVIDREY/Documents/"+ic+".csv")
