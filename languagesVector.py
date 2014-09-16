import ngrams

#make a propbability list for one language
#source_file - file with plain text
def vector_of_language(source_file):
	letters = ngrams.array_from_file(source_file)
	unigram_probability = ngrams.probability(ngrams.make_unigrams(letters))
	bigram_probability = ngrams.probability_of_bigram(ngrams.make_bigrams(letters))
	trigram_probability = ngrams.probability_of_trigram(ngrams.make_trigrams(letters))
	
	return [unigram_probability, bigram_probability, trigram_probability]

def count_unigram_score(sentence, vector):
	score = 0
	for letter in list(sentence):
		if letter in vector[0]:
			score += vector[0][letter]
	return score

def count_bigram_score(sentence, vector):
	score = 0
	

czech = vector_of_language("train_cs_500lines.txt")
#english = vector_of_language("en/train-en.txt")
#norwegian = vector_of_language("no/train-no.txt")

print(count_unigram_score("ahoj, jak se máš", czech))	
