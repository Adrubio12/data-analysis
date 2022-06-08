import pandas as pd
from matplotlib import pyplot as plt
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
df = pd.read_csv("toronto_users.csv")

top_followers = df.nlargest(500,['followers'])
top_reviews = df.nlargest(500,['num_reviews'])

influencers = pd.merge(top_reviews, top_followers, how='inner', on=['user_id'])

influencers = influencers[influencers.followers_x > 500]
influencers = influencers.drop(['Unnamed: 0_x','Unnamed: 0_y','name_y','user_since_y','expert_y','friends_y','num_reviews_y','useful_y','fun_y','cool_y','followers_y','average_rating_y'], axis=1)
influencers = influencers.rename(columns={'name_x': 'name', 'num_reviews_x': 'num_reviews', 'user_since_x': 'user_since', 'useful_x': 'useful', 'fun_x': 'fun', 'cool_x': 'cool', 'expert_x': 'expert', 'friends_x': 'friends', 'followers_x': 'followers', 'average_rating_x': 'average_rating'})


influencers.to_csv('influencers.csv', mode='w', header=True)
