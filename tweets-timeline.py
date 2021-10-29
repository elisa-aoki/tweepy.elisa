import tweepy

auth = tweepy.OAuthHandler("jEHAJFCNaJRgWDabd1Oyo8HHh", "4DvKKtW0k9gx0Ibv3EEKJEvcoeylzkc3aE09w3vuQkpzVNiYqs")
auth.set_access_token("61910822-zN7pBI5Vs4xtWEnRDyr78gP4SMLhrtnk7HdTUTFrk", "og5jwkJZf7BGUU1eu2pVrxtpq3D8xsxginiKnjI1FsBRA")

api = tweepy.API(auth)

timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")
