# CapitalsAssistant
An auxiliary tool for iOS Game Capitals. (Tested at python 3.5.1, redis 3.2.8)


Thanks to http://www.mieliestronk.com/, I downloaded the vocabulary list from this site. Please notice that this is supposed to be a British Spelling list.


This script tries using as many combos of the given letters as possible to search in the redis. In the worst case, it may incur n! times match function (O(n!)). Every set in the redis has no more than 26 elements.

## How to use it
### Firstly, clone the repository.
    git clone https://github.com/jslu0418/CapitalsAssistant.git

### Download the vocabulary list to the repository's root menu.
    wget http://www.mieliestronk.com/corncob_lowercase.txt


### Make sure you've installed the redis-server and it is running and listening on 6379.

### Building vocab. tree.
    python Maintainexerciseset.py

### Last step.
    python CapitalsAssistant.py abcdefg...


## MaintainExerciseSet
This program uses redis to store all words from the vocabulary list, for another program easily excluding impossible combos, every set's subset has all its ancestors. For example, smembers(a) would be [au, ai, ad, ..., at].
