'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = 'hRfHrwVFDiWgnO40QIq5xoFuc'
MY_CONSUMER_SECRET = '4HuGYqGxLnmM1DV6WTIewwxXiEFIIpXubynKInuzIEeU6ca7yl'
MY_ACCESS_TOKEN_KEY = '882084141533102080-wHANZCYoMAqrXwOFr2ki2eGWt6aKVZF'
MY_ACCESS_TOKEN_SECRET = '3l5KWFhZNyUh8rnANZA6Qg0wkroI9dDgt6h6dgNflCnVZ'

SOURCE_ACCOUNTS = ["rachgarb"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 2 #How often do you want this to run? 1/8 times?
ORDER = 3 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = Flase #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API. You can use the included testcorpus.txt, if needed.
TWEET_ACCOUNT = "rachelgarbot" #The name of the account you're tweeting to.
