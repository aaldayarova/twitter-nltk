from nltk.corpus import twitter_samples
from nltk.tag import pos_tag_sents

#Importing positive tweets as lines
tweets = twitter_samples.strings('positive_tweets.json')

#Splitting each line of a tweet into 'tokens' or parts
tweets_tokens = twitter_samples.tokenized('positive_tweets.json')

#POS-ing each token as a part of speech (noun, adj., etc.)
#JJ = adjective, NN = singular noun, NNS = plural nouns
tweets_tagged = pos_tag_sents(tweets_tokens)

#Counting each POS type
JJ_count = 0
NN_count = 0

for tweet in tweets_tagged:
    for pair in tweet:
        tag = pair[1]
        if tag == 'JJ':
            JJ_count += 1
        elif tag == 'NN':
            NN_count += 1

#Reporting number of nouns and adjectives in our corpus
print('The number of adjectives is ', JJ_count)
print('The number of nouns is ', NN_count)
#Reported number of adjectives is 6092
#Reported number of nouns is 13181
 