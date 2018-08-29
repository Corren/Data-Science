import json

filein = "merged.json"
fileout = "keywords.txt"

fin = open(filein, 'r')



tweets = []

for line in open(filein):
    try:
        tweets.append(json.loads(line))
    except:
        pass


print ("File Imported:", str(filein))
print ("# Tweets Imported:", len(tweets))


# create a new variable for a single tweets
tweet=tweets[0]

# pull out various data from the tweets

fin.close()

fout = open(fileout,'w')
for tweet in tweets:
    try:
        for hashtag in tweet['entities']['hashtags']:


            fout.write(hashtag['text'])
            fout.write('\n')
    except:
        pass


fout.close()
print("Done exporting")
