import redis
import sys
import re

def usage():
    print('Usage: python CapitalsAssistant.py [a-z]+')


if len(sys.argv) > 2:
    usage()
    sys.exit(-1)

if re.search(r'[^a-z]', sys.argv[1]):
    usage()
    sys.exit(-1)

availableLetters = list(sys.argv[1])
redisDB = redis.StrictRedis(host='localhost', port=6379, db=0)

wordGroup = set() # define a set for storing matched words.

def searchWord(curSetName, remainLetters):
    # if set's name is initial value, jump to the loop for extracting next letter
    if curSetName:
        # this specific combo of given letters cannot match any words in the redis.
        subSet = redisDB.scard(curSetName)
        if subSet == 0:
            return

        # updated: to prevent multiple words exist in the same route in the tree.
        if redisDB.sismember(curSetName, '1'):
            wordGroup.add(curSetName)
            if subSet == 1:
                return
    # extract another letter from the remain list.
    if len(remainLetters) > 0:
        for i in range(0, len(remainLetters)):
            letter = remainLetters[i]
            dupRemainLetters = remainLetters[:]
            dupRemainLetters.pop(i)
            searchWord(curSetName+letter, dupRemainLetters)


searchWord('', availableLetters)
wordList = list(wordGroup)
wordList.sort(key=lambda x:len(x))

# perhaps only printing 10 longest words is better than printing all words.
if len(wordList) > 9:
    print('\n'.join(wordList[-10:]))
else:
    print('\n'.join(wordList))
