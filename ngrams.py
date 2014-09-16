import collections
import math

def array_from_file(file_name):
	train_data = open(file_name, encoding="utf-8")
	return list(train_data.read())

#make unigrams from array of letters with the frequency
def make_unigrams(array_text):
	unigrams = collections.Counter(array_text)
	return unigrams

def make_bigrams(array_text):
	bigram_array = []
	for i in range(len(array_text) - 1):
		bigram_array.append((array_text[i],array_text[i+1]))
	bigrams = collections.Counter(bigram_array)
	return bigrams

def make_trigrams(array_text):
	trigram_array = []
	for i in range(len(array_text) - 2):
		trigram_array.append((array_text[i], array_text[i+1], array_text[i+2]))
	trigrams = collections.Counter(trigram_array)
	return trigrams

def make_ngrams(plain_text, n):
	ngram_array = []
	array_text = list(plain_text)
	for i in range(len(array_text) - n + 1):
		ngram = []
		for j in range(i,i+n):
			ngram.append((array_text[j]))
		ngram_array.append(tuple(ngram))
	return ngram_array

def count_ngrams(plain_text, n):
	ngram_array = make_ngrams(plain_text, n)
	ngrams = collections.Counter(ngram_array)
	return ngrams

#count the probability of unigrams, return logaritmus of probability to avoid small numbers
#probability = count of found / total count
def probability(unigrams):
	total = len(unigrams)
	unigram_probability = {}
	for the_unigram in unigrams:
		unigram_probability[the_unigram] = -math.log(unigrams[the_unigram]/total)
	return unigram_probability

#probability = count of certain bigram / total count bigrams with the same first letter
def probability_of_bigram(bigrams):
	bigram_probability = {}
	for the_bigram in bigrams:
		sum_of_frequency = 0
		for the_bigram2 in bigrams:
			if (the_bigram[0] == the_bigram2[0]):
				sum_of_frequency += bigrams[the_bigram2]
		bigram_probability[the_bigram] = -math.log(bigrams[the_bigram]/sum_of_frequency)	
	return bigram_probability		

#probability = count of certain trigram / total count of trigrams with the same first two letters
def probability_of_trigram(trigrams):
	trigram_probability = {}
	for the_trigram in trigrams:
		sum_of_frequency = 0
		for the_trigram2 in trigrams:
			if (the_trigram[0] == the_trigram2[0]) & (the_trigram[1] == the_trigram2[1]):
				sum_of_frequency += trigrams[the_trigram2]
		trigram_probability[the_trigram] = -math.log(trigrams[the_trigram]/sum_of_frequency)	
	return trigram_probability	
