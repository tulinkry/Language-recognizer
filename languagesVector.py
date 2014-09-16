import ngrams

#make a propbability list for one language
#source_file - file with plain text
def vector_of_language(source_file):
	opened_file =  open(source_file, encoding="utf-8")
	text = opened_file.read()

	unigram_probability = ngrams.probability(ngrams.count_ngrams(text,1))
	bigram_probability = ngrams.probability_of_bigram(ngrams.count_ngrams(text, 2))
	trigram_probability = ngrams.probability_of_trigram(ngrams.count_ngrams(text, 3))
	return [unigram_probability, bigram_probability, trigram_probability]


def count_unigram_score(sentence, vector):
	score = 0
	for letter in list(sentence):
		if letter in vector[0]:
			score += vector[0][letter]
	return score

#count a score for sentence from vector of a language ~ probability for ngrams in the language (suma of logarithms)
def count_ngram_score(sentence, vector, n):
	score = 0
	ngrams_array = ngrams.make_ngrams(sentence, n)
	for ngram in ngrams_array:
		
		if ngram in vector[n-1]:
			print(ngram)
			score += vector[n-1][ngram]
	return score

czech = vector_of_language("train_cs_500lines.txt")
english = vector_of_language("en/train-en.txt")
#norwegian = vector_of_language("no/train-no.txt")

print(count_ngram_score("ahoj, jak se máš", czech, 1))
print(count_ngram_score("ahoj, jak se máš", czech, 2))
print(count_ngram_score("ahoj, jak se máš", czech, 3))
print(count_ngram_score("ahoj, jak se máš", english, 1))
print(count_ngram_score("ahoj, jak se máš", english, 2))
print(count_ngram_score("ahoj, jak se máš", english, 3))
