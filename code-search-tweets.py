import tweepy

auth = tweepy.OAuthHandler("jEHAJFCNaJRgWDabd1Oyo8HHh", "4DvKKtW0k9gx0Ibv3EEKJEvcoeylzkc3aE09w3vuQkpzVNiYqs")
auth.set_access_token("61910822-zN7pBI5Vs4xtWEnRDyr78gP4SMLhrtnk7HdTUTFrk", "og5jwkJZf7BGUU1eu2pVrxtpq3D8xsxginiKnjI1FsBRA")

api = tweepy.API(auth)

for tweet in api.search(q="Home Office", lang="en", rpp=10):
    print(f"{tweet.user.name}:{tweet.text}")
