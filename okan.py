#!/usr/bin/env python
# coding: utf-8

# In[2]:


print(your_dataset.tail())


# In[3]:


your_dataset.isnull().sum()


# In[5]:


rows_with_null_response = your_dataset[your_dataset['Response'].isnull()]
print(rows_with_null_response)


# In[3]:


pip install nltk spacy transformers


# In[8]:


import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from keras.preprocessing.sequence import pad_sequences

# Download necessary NLTK data
nltk.download('punkt')

# Load your dataset from the file
df = pd.read_csv('C:/Users/ALABI ABIGAIL/Downloads/mental/train.csv')  # Replace with your actual file path

# Tokenize function using NLTK word_tokenize
def tokenize_text(text):
    return word_tokenize(text) if pd.notnull(text) else []

# Tokenize the text in specified columns
df['Context_Tokens'] = df['Context'].apply(tokenize_text)
df['Response_Tokens'] = df['Response'].apply(tokenize_text)

# Convert tokenized text to sentences
df['Context_Sentences'] = df['Context_Tokens'].apply(lambda x: ' '.join(x))
df['Response_Sentences'] = df['Response_Tokens'].apply(lambda x: ' '.join(x))

# Initialize CountVectorizer for BoW encoding
vectorizer = CountVectorizer()

# Fit the vectorizer on the entire dataset
vectorizer.fit(df['Context_Sentences'].tolist() + df['Response_Sentences'].tolist())

# Transform the tokenized text into BoW vectors
X_context = vectorizer.transform(df['Context_Sentences']).toarray()
X_response = vectorizer.transform(df['Response_Sentences']).toarray()

# Pad sequences to ensure uniform length
max_sequence_length = max(X_context.shape[1], X_response.shape[1])

X_context_padded = pad_sequences(X_context, maxlen=max_sequence_length, padding='post')
X_response_padded = pad_sequences(X_response, maxlen=max_sequence_length, padding='post')

# Example of sequence encoding
print("Original BoW Vector Shape:")
print(X_context.shape)

print("\nPadded BoW Vector Shape:")
print(X_context_padded.shape)

print("\nExample of Padded BoW Vector:")
print(X_context_padded[0])


# In[19]:


import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from keras.preprocessing.sequence import pad_sequences

# Download necessary NLTK data
nltk.download('punkt')

# Load your dataset from the file
df = pd.read_csv('C:/Users/ALABI ABIGAIL/Downloads/mental/train.csv')  # Replace with your actual file path

# Tokenize function using NLTK word_tokenize
def tokenize_text(text):
    return word_tokenize(text) if pd.notnull(text) else []

# Tokenize the text in specified columns
df['Context_Tokens'] = df['Context'].apply(tokenize_text)
df['Response_Tokens'] = df['Response'].apply(tokenize_text)

# Convert tokenized text to sentences
df['Context_Sentences'] = df['Context_Tokens'].apply(lambda x: ' '.join(x))
df['Response_Sentences'] = df['Response_Tokens'].apply(lambda x: ' '.join(x))

# Initialize CountVectorizer for BoW encoding
vectorizer = CountVectorizer()

# Fit the vectorizer on the entire dataset
vectorizer.fit(df['Context_Sentences'].tolist() + df['Response_Sentences'].tolist())

# Transform the tokenized text into BoW vectors
X_context = vectorizer.transform(df['Context_Sentences']).toarray()
X_response = vectorizer.transform(df['Response_Sentences']).toarray()

# Pad sequences to ensure uniform length
max_sequence_length = max(X_context.shape[1], X_response.shape[1])

X_context_padded = pad_sequences(X_context, maxlen=max_sequence_length, padding='post')
X_response_padded = pad_sequences(X_response, maxlen=max_sequence_length, padding='post')

# Add the padded vectors to the DataFrame for inspection
df['Context_BoW_Padded'] = list(X_context_padded)
df['Response_BoW_Padded'] = list(X_response_padded)

# Print the DataFrame with the padded BoW vectors
print(df[['Context', 'Response', 'Context_BoW_Padded', 'Response_BoW_Padded']])

# Optionally, print a subset for clearer view (e.g., first 5 rows)
print(df[['Context', 'Response', 'Context_BoW_Padded', 'Response_BoW_Padded']].head())


# In[7]:


pip install chardet


# In[ ]:


import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Download necessary NLTK data
nltk.download('punkt')

# Load and preprocess dataset
df = pd.read_excel('C:\\Users\\ALABI ABIGAIL\\abigail documents\\NLP_project\\train.xlsx')
df.dropna(inplace=True)  # Drop rows with missing values

# Convert all entries in 'Context' and 'Response' columns to strings
df['Context'] = df['Context'].astype(str)
df['Response'] = df['Response'].astype(str)

# Tokenization
df['Context_Tokens'] = df['Context'].apply(word_tokenize)
df['Response_Tokens'] = df['Response'].apply(word_tokenize)

# Join tokens back to sentences for vectorization
df['Context_Sentences'] = df['Context_Tokens'].apply(lambda x: ' '.join(x))
df['Response_Sentences'] = df['Response_Tokens'].apply(lambda x: ' '.join(x))

# Vectorization
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['Context_Sentences'])
y = df['Response_Sentences']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic Regression Model
log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(X_train, y_train)

# Predictions and Evaluation
y_pred = log_reg.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Function to get response for a given input
def get_response(user_input):
    user_input_tokenized = ' '.join(word_tokenize(user_input))
    user_input_vectorized = vectorizer.transform([user_input_tokenized])
    response = log_reg.predict(user_input_vectorized)
    return response[0]

# Get input from user and provide a response
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Exiting...")
        break
    response = get_response(user_input)
    print("Bot:", response)


# In[ ]:




