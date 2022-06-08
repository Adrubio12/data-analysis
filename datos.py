import math

import pandas as pd
import seaborn as sn
import matplotlib

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

header_list = ["review_id", "user_id", "business_id", "rating", "useful", "fun", "cool", "description", "date"]
df = pd.read_csv("review_data.csv", names=header_list,  skiprows=3500001, nrows=4500000)
bs = pd.read_csv("ids_business_toronto.csv")
toronto_reviews = df.loc[df['business_id'].isin(bs.business_id)]

print(toronto_reviews)

toronto_reviews.to_csv('toronto_reviews.csv', mode='a', header=False)



#df.to_csv('test.csv', sep='\t', header=None, mode='a')
