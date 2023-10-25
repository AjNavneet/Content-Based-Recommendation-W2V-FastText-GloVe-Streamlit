# Import necessary modules
from ML_Pipeline import preprocessing
from ML_Pipeline import recommendations
from ML_Pipeline import utils
import sys
import configparser

# Load parameters from the configuration file
config = configparser.RawConfigParser()
config.read('config.ini')
DATA_DIR = config.get('DATA', 'data_dir')

# Read the data
print("----Loading the data----")
df = utils.read_data(DATA_DIR)

# Data Preprocessing
print("----Data Preprocessing started----")
# Process the data and create unique_df and desc_list
unique_df, desc_list = preprocessing.process_data(df=df, col1='Description', col2='Product Name')

# Choose the similarity measure
val = int(input("Select the similarity measure\nCosine - 0\nManhattan - 1\nEuclidean - 2\nEnter your value: "))
if val == 0:
    distance = 'cosine'
elif val == 1:
    distance = 'manhattan'
elif val == 2:
    distance = 'euclidean'
else:
    sys.exit("Invalid option chosen")

# Choose the vectorizer
val1 = int(input("Select the algorithm for recommendation\nCount Vectorizer - 0\nTF-IDF Vectorizer - 1\nFastText Model - 2\nGloVe Model - 3\nWord2Vec Model - 4\nCo-occurrence Matrix - 5\nEnter your value: "))

if val1 == 0:
    model = 'count_vectorizer'
elif val1 == 1:
    model = 'tfidf_vec'
elif val1 == 2:
    model = 'fasttext_model'
elif val1 == 3:
    model = 'glove_model'
elif val1 == 4:
    model = 'word2vecModel'
elif val1 == 5:
    model = 'co-occurrence matrix'
else:
    sys.exit("Invalid option chosen")

# Get product recommendations
product_id = config.get('DATA', 'Product')
top_products = recommendations.get_recommendation(product_col='Product Name', product_id=product_id, df=unique_df, input=desc_list, vectorizer=model, similarity=distance, n=10)
