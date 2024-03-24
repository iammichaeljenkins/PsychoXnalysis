import scraper
import ai
import re

def main():
	print("This program gives a psychological analysis of a twitter user based on their first page of tweets.")
	print("In order to access twitter your username and password are needed (Beware twitter web client has rate limits and abusing this program can lead to a read_only twitter account)")
	username = input("Username: ")
	password = input("Password: ")
	while True:
		print("Type \"stop\" to exit the program")
		target_user = input("Enter the user you would like to analyze: ")
		if target_user == "stop":
			return 0
		try:
			message = scraper.scrape(username, password, target_user)
		except Exception as e:
			print(f"The scraping process encountered an error. Make sure the username you provided corresponds to an account. Error: {e}")
			continue
		message = re.sub(' +', ' ', message)
		print("Successfully scraped tweets. Analysis may take some time...")
		try:
			response = ai.AI(message)
		except Exception as e:
			print(f"The AI ran into an error. Make sure you have the required dependencies. Error: {e}")
			continue
		print(response)

if __name__ == "__main__":
    main()
