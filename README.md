# CapitalsAssistant
An auxiliary tool for iOS Game Capitals.


Thanks to http://www.mieliestronk.com/, I downloaded the vocabulary list from this site. Please notice that this is supposed to be a British Spelling list.


This script tries using as many combos of the given letters as possible to search in the redis. In the worst case, it may incur n! times match function (O(n!)). Every set in the redis has no more than 26 elements.

## MaintainExerciseSet
This program uses redis to store all words from the vocabulary list, for another program easily excluding impossible combos, every set's subset has all its ancestors. For example, smembers(a) would be [au, ai, ad, ..., at].
