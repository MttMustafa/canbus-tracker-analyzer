import pandas as pd
import matplotlib.pyplot as plt

print("Importing spreadsheet...")
sheetDF = pd.read_excel('../docs/düzenli veriler delphi için.xlsx')
print("Import complete.")

print("Donusturmek istediginiz formati seciniz:")
conversion = input()

print("Converting data...")
for column in sheetDF.columns[5:9]:
    for (idx, val) in sheetDF[column].dropna().items():
        if(conversion == 'dec'):
            sheetDF.at[idx, column] = int(str(val), 16)
        elif(conversion == 'bin'):
            sheetDF.at[idx, column] = bin(int(str(val), 16))


# print(sheetDF.to_string())

# sheetDF[sheetDF["Data1"] != 0].loc[:,'Data1'].dropna().plot()
# plt.savefig("mygraph.png")

print(sheetDF[sheetDF.columns[5:9]].dropna().values.max())