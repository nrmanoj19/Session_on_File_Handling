import pandas as pd


my_df = pd.read_csv('my_csv1.csv')
print(my_df.head(3))
my_df.to_csv("df_to_csv.csv", index=False)