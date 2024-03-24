from tweety import Twitter
import tweety
def scrape(username, password, target_user):
	message = ""
	app = Twitter("session")
	app.sign_in(username, password)
	tweets = app.get_tweets(target_user, 1)
	for tweet in tweets:
		if isinstance(tweet, tweety.types.twDataTypes.Tweet):
			message += "\""
			message += tweet.text
			message += "\", "
		else:
			for t in tweet:
				message += "\""
				message += t.text
				message += "\", "
	return message
