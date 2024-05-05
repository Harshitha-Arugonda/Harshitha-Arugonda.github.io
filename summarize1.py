import os
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx

# Initialize NLTK
nltk.download('punkt')
nltk.download('stopwords')

def read_text_from_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text

# Define the path to the recognized text file
recognized_text_file_path = os.path.join("output_texts", "recognized_text.txt")

# Read the recognized text from the file
recognized_text = read_text_from_file(recognized_text_file_path)

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text.lower())
    filtered_text = [word for word in word_tokens if word.isalnum() and word not in stop_words]
    return ' '.join(filtered_text)

def generate_summary(text, num_sentences=3):
    sentences = sent_tokenize(text)
    preprocessed_sentences = [preprocess_text(sentence) for sentence in sentences]
    
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(preprocessed_sentences)
    
    sentence_similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_matrix)
    scores = nx.pagerank(sentence_similarity_graph)
    ranked_sentences = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)
    
    summary = [ranked_sentences[i][1] for i in range(num_sentences)]
    return ' '.join(summary)

# Generate summary from the recognized text
summary = generate_summary(recognized_text, num_sentences=3)
print("Summary:", summary)
