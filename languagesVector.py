import ngrams, operator, collections

#make a propbability list for one language
#source_file - file with plain text
def vector_of_language(source_file):
	opened_file =  open(source_file, encoding="utf-8")
	text = opened_file.read()

	unigram_probability = ngrams.probability(ngrams.count_ngrams(text,1))
	bigram_probability = ngrams.probability_of_bigram(ngrams.count_ngrams(text, 2))
	trigram_probability = ngrams.probability_of_trigram(ngrams.count_ngrams(text, 3))
	return [unigram_probability, bigram_probability, trigram_probability]

#count a score for sentence from vector of a language ~ probability for ngrams in the language (suma of logarithms)
def count_ngram_score(sentence, vector, n):
	score = 0
	ngrams_array = ngrams.make_ngrams(sentence, n)
	for ngram in ngrams_array:	
		if ngram in vector[n-1]:
			score += vector[n-1][ngram]
	return score

def add_language_vector(output_file, train_file):
	return
#n = number of kinds of ngrams (uni + bi + trigram = 3)
def recognize_language(sentence, vectors, n):
	scores = []
	for i in range(0,n):
		scores.append({})
		for language in vectors.keys():
			scores[i][language] = count_ngram_score(sentence, vectors[language], i+1)
	
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

czech = vector_of_language("cs/train-cs-10.txt")
#english = vector_of_language("en/train-en.txt")
#norwegian = vector_of_language("no/train-no.txt")
vectors = {"czech": czech}
print(recognize_language("ahoj, jak se máš", vectors, 3))

