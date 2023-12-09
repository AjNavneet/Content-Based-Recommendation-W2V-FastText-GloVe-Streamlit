# Content-based Recommendation System using W2V, fasttext, glove and Streamlit

## Business Context

Imagine you want to buy a gift for your dear ones. You opened an eCommerce website on your phone and started searching for the gift. After a few minutes, you find a section that shows very similar gifts you wanted. Now you must be thinking, how do they know similar items based on one thing? Most platforms use the Recommendation system at the backend to show you the best items based on your search history. There are several choices in the digital market world, which are somehow too overwhelming for the user to choose from. There is always a need to filter and prioritize the relevant items for each user to engage the customers with the platform, which eventually impacts the revenue. Content-based filtering is one of the most used techniques to personalize the content for each user. It uses previous actions and feedback about users' liking to provide them with similar recommendations.

---

## Aim
To build a Recommender System using various content-based filtering techniques and similarity measures and to create a web application for the same using Streamlit.

---

## Data Description
The dataset contains about 4k products in various categories for a UK-based non-store online retail business. The company mainly sells unique all-occasion gifts with maximum wholesaler customers.

---

## Tech Stack
- Language: `Python`
- Libraries: `pandas`, `NumPy`, `seaborn`, `matplotlib`, `re`, `gensim`

---

## Approach
1. Data Description
2. Data Preprocessing
3. Ranking Functions
4. Building Recommendation system
   - Count Vectorizer
   - TFIDF Vectorizer
   - Word2Vec
   - FastText
   - Glove
   - Co-occurrence Matrix
5. Streamlit Web App

---

## Modular code overview

1. input
2. src
3. output
4. lib
5. requirements.txt

The `input` folder contains the data that we have for analysis, in our case, it contains data.xlsx.

The `src` folder is the heart of the project and contains all the modularized code for all the above steps in a modularized manner. It further includes:
- ML_pipeline
- engine.py
- config.ini
- product_recommendation_streamlit.py

---

## Execution Instructions

To install all the required libraries, run the following command:

```
pip install -r requirements.txt
```

### Running the Code

To execute the code, follow these steps:

1. Run the `engine.py` file.
2. Select the appropriate options to get recommendations for the chosen product in the config file.

### Running the Streamlit Web App

To run the Streamlit web application, use the following command:

```
streamlit run product_recommendation_streamlit.py
```

### Note

If you choose the "Co-occurrence Matrix" as the algorithm, be aware that it may throw a "numpy.core._exceptions.MemoryError" if there isn't sufficient space (more than 3 TiB) available.

---

