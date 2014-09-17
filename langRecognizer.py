import ngrams, operator, collections, langVector, sys

#HOW TO IMPROVE: use collections.OrderedDict (pro záznam skóre)
#TODO: shoda u určení jazyků
#TODO: váhy! - viz HOW TO IMROVE


#count a score for sentence from vector of a language ~ probability for ngrams in the language (suma of logarithms)
def count_ngram_score(sentence, vector, n):
	score = 0
	ngrams_array = ngrams.make_ngrams(sentence, n)
	for ngram in ngrams_array:	
		if ngram in vector[n-1]:
			score += vector[n-1][ngram]
	return score

#n = number of kinds of ngrams (uni + bi + trigram = 3)
def recognize_language(sentence, vectors, n):
	scores = []
	for i in range(0,n):
		scores.append({})
		for language in vectors.keys():
			scores[i][language] = count_ngram_score(sentence, vectors[language], i+1)

	#result for uni/bi/trigrams - 0 ~ uni etc.
	result = []
	for i in range(0,n):
		#find the language with largest score for i-gram
		result.append(max(scores[i].items(), key=operator.itemgetter(1))[0])
	counted_result = collections.Counter(result)
	#find the languge which is mostly appeared - dořešit váhy!!!
	language = max(counted_result.items(), key=operator.itemgetter(1))[0]
	probability = counted_result[language] / sum(counted_result.values())
	return language, probability


vectors = langVector.load_vector("language_vector.p")

if len(sys.argv) < 2:
	sentence = input("Your sentence: ")
else:
	sentence = sys.argv[1]
print(recognize_language(sentence, vectors, 3))

