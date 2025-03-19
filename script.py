import pandas as pd

# Load codes and IDs from excel file
file_path = r"code.xlsx"  
df = pd.read_excel(file_path)

codes,ids = [],[]

for index, row in df.iterrows():
    if not pd.isna(row['Code']):
        codes.append(row['Code'])
    if not pd.isna(row['ID']): 
        ids.append(str(row['ID'])[:-2]) 
