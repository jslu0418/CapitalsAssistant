import redis
import threading

ThreadLimits = 8
vocabListFile = open('./corncob_lowercase.txt')

vocabList = vocabListFile.readlines()

wordCount = len(vocabList)

redisDB = redis.StrictRedis(host='localhost', port=6379, db=0)

def exerciseSingleWord(word, depth):
    setName = word[0:depth]
    addItemName = word[0:depth+1]
    redisDB.sadd(setName, addItemName)
    if depth == len(word) - 1:
        redisDB.sadd(addItemName, '1')
        return

    exerciseSingleWord(word, depth+1)

def exerciseThread(index):
    tailFixValue = 0
    if wordCount % ThreadLimits > index:
        tailFixValue = 1

    for i in range(0, int(wordCount/ThreadLimits)+tailFixValue):
        exerciseSingleWord(vocabList[i * ThreadLimits + index].strip(), 1)


for j in range(0, ThreadLimits):
    t = threading.Thread(target=exerciseThread, args=(j,))
    t.daemon = True
    t.start()


t.join()
