import tweepy, time, sys, json
import random
from wordnik import *

apiUrl = 'http://api.wordnik.com/v4'
apiKey = 'bce4c40918f100d53800f0c13c80038c5eb6382fc33a34167'
client = swagger.ApiClient(apiKey, apiUrl)

consumer_key = "8Ja8DGfD1yeTxtARhgkDQ38iK"
consumer_secret = "OsWr77zSBhDmc3Trpbctk3gxPeWHmPL1cb3GdG37sf3fI8TbmU"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
access_token = "3295331221-iezkh8Q9hns6adMOEL9BlYUZmPnKxQndl2BO6LL"
access_token_secret = "mQrLLaKYV7KdxVO1b0L6pMJXhIqGBYtakfP8HpsOEth7W"
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
		
	
def tweet(message):
	api.update_status(status=message)
					

wordApi = WordApi.WordApi(client)


def randphrase():
		# Generates a random endcap
		endcaps = ["huh", "well then", "yessir", "you betcha", "and dont forget it", "mmhmm", ";)", ";/", "hmm", "*wink*", "RT if u agree", "fav if u agree", "speaking of kelis", "yup", "*nod*", ":/", "mmm", "friend", "buddy", "old pal", "forget it" ]
		rand_endcap = random.choice(endcaps)
		return rand_endcap
	
def randopener():
		# Generates a random greeting
		openers = ["oh", "hi", "yo", "*stretch*", "*blink*", "oh dear", "#pp2", "anna kendrick", "oh look", "*curtsy*", "*takes a bow*", ]
		rand_opener = random.choice(openers)
		return rand_opener
	
def syn(Word):
		# Returns a synonyms of Word
		input.word = Word
		input.limitPerRelationshipType = 10
		input.relationshipTypes = 'synonym'
		synonym = wordApi.getRelatedWords(input)
		return synonym
		
	
def rhyme(word):
		#returns a random rhyme
		relatedWordslist = wordApi.getRelatedWords(word, relationshipTypes='rhyme')
		relatedWords = relatedWordslist[0].words
		relatedWord = random.choice(relatedWords)
		return relatedWord

def search(query):
		results = api.search(q=query)
		return results[0]
	
word='journalist'
rhyme = rhyme(word)
end = randphrase()
start = randopener()


sentence = "HELLO DID YOU KNOW " + word + " rhymes with " + rhyme + " " + end


tweet(sentence)

exit()