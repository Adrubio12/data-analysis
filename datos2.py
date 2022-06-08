import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

header_list = ["user_id","name","num_reviews","user_since","useful","fun","cool","expert","friends","followers","average_rating","like_fashion","like_extras","like_profile","like_format","like_list","like_comment","like_simple","like_cool","like_fun","like_texts","like_pics"]
fields = ["user_id","name","num_reviews","user_since","useful","fun","cool","expert","friends","followers","average_rating"]
reviews = pd.read_csv("toronto_reviews.csv")
users = pd.read_csv("user_data.csv", usecols=fields, names=header_list, skiprows=3000001, nrows=4000000)

toronto_users = users.loc[users['user_id'].isin(reviews.user_id)]
print(toronto_users)

toronto_users.to_csv('toronto_users.csv', mode='a', header=False)