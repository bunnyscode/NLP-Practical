import random
import re
from collections import defaultdict

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

def build_bigram_model(corpus):
    words = corpus.split()
    bigram_model = defaultdict(list)
    
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        bigram_model[current_word].append(next_word)
    
    return bigram_model

def predict_next_word(bigram_model, current_word):
    if current_word in bigram_model:
        possible_next_words = bigram_model[current_word]
        return random.choice(possible_next_words)
    else:
        return None

def main():
    corpus_file = "corpus.txt"
    with open(corpus_file, 'r') as file:
        corpus_text = file.read()
    
    preprocessed_corpus = preprocess_text(corpus_text)
    bigram_model = build_bigram_model(preprocessed_corpus)
    
    seed_word = input("Enter a starting word: ").lower()
    
    while seed_word != 'exit':
        next_word = predict_next_word(bigram_model, seed_word)
        if next_word:
            print("Predicted next word:", next_word)
        else:
            print("Word not found in corpus.")
        
        seed_word = input("Enter a starting word: ").lower()

if __name__ == "__main__":
    main()
