import twitter

api = twitter.Api(
    consumer_key='LSnYD9PVZaL7B6CfKUMBRJNjr',
    consumer_secret='PfX8XvkxffnyTIRHYb5CsWn7JrbqoJaW7qq64RQnCsOPkNlr6k',
    access_token_key='929862495745007617-CCPgOz9Mdv1fIQc5YMqJg5XF9xD3tMw',
    access_token_secret='1GKGWFPdVnfZWMWZg6m4Fg1foCeys4nkWqNKe1OStNgpG',
    tweet_mode='extended')

statuses = api.GetUserTimeline(2414818604)
# # print(statuses[1].text)
# for status in statuses:
#     print(status.full_text)
#     if status.retweeted_status:
#         print("RT: " + status.retweeted_status.full_text)
#     print("\n")

stream = api.GetStreamFilter(track="proxy")
stream.
