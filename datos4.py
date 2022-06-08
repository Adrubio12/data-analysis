import pandas as pd

header_list = ["review_id", "user_id", "business_id", "rating", "useful", "fun", "cool", "description", "date"]
df = pd.read_csv("toronto_reviews.csv", names=header_list)
bs = pd.read_csv("influencers.csv")
influencer_reviews = df.loc[df['user_id'].isin(bs.user_id)]

influencer_reviews.to_csv('influencer_reviews.csv', mode='w', header=True)