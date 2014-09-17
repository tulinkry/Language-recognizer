import ngrams, operator, collections, langVector

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
	print(scores)	
	#result for uni/bi/trigrams - 0 ~ uni etc.
	#vyřešit - shoda u určení jazyků, váhy
	result = []
	for i in range(0,n):
		#find the language with largest score for i-gram
		result.append(max(scores[i].items(), key=operator.itemgetter(1))[0])
	counted_result = collections.Counter(result)
	#find the languge which is mostly appeared - dořešit váhy!!!
	language = max(counted_result.items(), key=operator.itemgetter(1))[0]
	probability = counted_result[language] / sum(counted_result.values())
	return language, probability




#langVector.add_language_vector("czech", "cs/train-cs-100.txt", "language_vector.p")
#langVector.add_language_vector("norwegian", "no/train-no.txt", "language_vector.p")
#langVector.add_language_vector("english", "en/train-en.txt", "language_vector.p")

vectors = langVector.load_vector("language_vector.p")
#czech = vector_of_language("cs/train-cs-10.txt")
#english = vector_of_language("en/train-en.txt")
#norwegian = vector_of_language("no/train-no.txt")
#vectors = {"czech": czech}
print(recognize_language("ahoj, jak se máš", vectors, 3))
print(recognize_language("I like måte, hyggilig", vectors, 3))

