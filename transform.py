import pandas as pd


header_list = ["user_id","name","num_reviews","user_since","useful","fun","cool","expert","friends","followers","average_rating","like_fashion","like_extras","like_profile","like_format","like_list","like_comment","like_simple","like_cool","like_fun","like_texts","like_pics"]
df = pd.read_csv("user_data.csv", names=header_list, skiprows=0, nrows=1000000)
df = df.drop(df.columns[[11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], axis=1)
"""""
df['num_friends'] = 0
df['num_expert'] = 0

for index, row in df.iterrows():

    array = row.friends.split(',')
    countFriends = len(array)
    df.num_friends[index] = countFriends

    if isinstance(row.expert, float):
        countExpert = 0
    else:
        array = row.expert.split(',')
        countExpert = len(array)
    df.num_expert[index] = countExpert
"""
df.to_csv('user_data_reduced.csv', mode='w', header=True)
