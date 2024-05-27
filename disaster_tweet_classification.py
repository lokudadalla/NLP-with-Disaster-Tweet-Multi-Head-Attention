# -*- coding: utf-8 -*-
"""disaster tweet classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1L-LG28crAGaeDx5EZFV2NfR6h4o5VEpI
"""

import numpy as np
import pandas as pd
import os

train_df=pd.read_csv("/content/train.csv")
train_df

import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
nltk.download('stopwords')
nltk.download('punkt')
stemmer = PorterStemmer()
def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    stopwords_set = set(stopwords.words('english'))
    tokens = [stemmer.stem(word) for word in tokens if word not in stopwords_set]
    preprocessed_text = ' '.join(tokens)
    return preprocessed_text

def preprocess_text2(text):
    text = text.lower()
    tokens = word_tokenize(text)
    return tokens

from bs4 import BeautifulSoup
def clean_text(text):
    # Menghapus tag HTML
    text = BeautifulSoup(text, "html.parser").get_text()
    # Menghapus URL
    text = re.sub(r'http\S+', '', text)
    # Menghapus karakter non-ASCII kecuali titik
    text = re.sub(r'[^\x00-\x7F.]', ' ', text)
    # Menghapus karakter khusus kecuali titik
    text = re.sub(f'[{re.escape(string.punctuation.replace(".", ""))}]', '', text)
    # Menghapus angka yang terpisah
    text = re.sub(r'\b\d+\b', '', text)
    text = re.sub(r'\.{2,}', ' ', text)
    # Menghapus spasi ganda setelah titik
    text = re.sub(r'(?<=\.)\s+', ' ', text).strip()
    return text

clean_data=lambda text:clean_text(text)
train_df["clean_text"]=train_df["text"].apply(clean_data)

train_df

train_df.at[21,"text"]

train_df.at[21,"clean_text"]

preprocess_data=lambda text:preprocess_text(text)
train_df["text_prepro"]=train_df["clean_text"].apply(preprocess_data)

train_df

X=train_df.drop(["id","keyword","location","text","target","clean_text"],axis=1)
y=train_df["target"]

X

y

tokenized_documents=[preprocess_text2(doc) for doc in X["text_prepro"]]

len(tokenized_documents)

tokenized_documents[0],tokenized_documents[1]

from gensim.models import Word2Vec
ukuran_vektor=100
word2vec_model = Word2Vec(sentences=tokenized_documents,
                          min_count=1, vector_size=ukuran_vektor,sg=1)

word2vec_model

unique_words = len(word2vec_model.wv)
print("Unique_words:", unique_words)

all_words =word2vec_model.wv.index_to_key
print("first 20 model Word2Vec:")
for index, word in enumerate(all_words):
    if index < 20:
        print(f"{word} : {index}")
    else:
        break

sequences = [[word2vec_model.wv.key_to_index[word] for word in text]
             for text in [preprocess_text2(doc) for doc in train_df['text_prepro']]]

print(sequences)

max_length = max([len(seq) for seq in sequences])

print(max_length)

from keras.preprocessing.sequence import pad_sequences
padded_sequences = pad_sequences(sequences, maxlen=max_length, padding='post')

print(padded_sequences)

y=np.asarray(y)
y

from sklearn.model_selection import train_test_split
X_train,X_val,y_train,y_val=train_test_split(padded_sequences,y,
                    test_size=0.2,random_state=42, stratify=y)

embedding_matrix = np.zeros((len(word2vec_model.wv.key_to_index) + 1, word2vec_model.vector_size))

print(embedding_matrix)
print(embedding_matrix.shape)
print(len(word2vec_model.wv.key_to_index))

for word, i in word2vec_model.wv.key_to_index.items():
    embedding_vector = word2vec_model.wv[word]
    if embedding_vector is not None:
        embedding_matrix[i] = embedding_vector

print(embedding_matrix)

import tensorflow as tf
from tensorflow.keras.layers import Input, Embedding, Dense, MultiHeadAttention, GlobalMaxPooling1D, LayerNormalization, Dropout
from tensorflow.keras.initializers import Constant
from tensorflow.keras.regularizers import l2

def build_transformer_model(max_length, vocab_size, embedding_dim, num_heads, ff_dim, num_classes):
    inputs = Input(shape=(max_length,))
    embedding = Embedding(input_dim=vocab_size, output_dim=embedding_dim)(inputs)
    x = Dropout(0.5)(embedding)
    multi_head_attention = MultiHeadAttention(num_heads=num_heads, key_dim=embedding_dim)
    x = multi_head_attention(query=x, value=x, key=x)
    x = LayerNormalization()(x)
    ff_network = Dense(ff_dim, activation='relu', kernel_regularizer=l2(0.01))(x)
    ff_network = Dense(embedding_dim, kernel_regularizer=l2(0.01))(ff_network)
    x = x + ff_network
    x = LayerNormalization()(x)
    x = GlobalMaxPooling1D()(x)
    x = Dropout(0.5)(x)
    outputs = Dense(num_classes, activation='softmax')(x)
    model = tf.keras.Model(inputs=inputs, outputs=outputs)
    return model

max_length = max_length
vocab_size = embedding_matrix.shape[0]
embedding_dim = embedding_matrix.shape[1]
num_heads = 8
ff_dim = 256
num_classes = 2
model = build_transformer_model(max_length, vocab_size, embedding_dim, num_heads, ff_dim, num_classes)

from keras.optimizers import Adam
optimizer = Adam(learning_rate=0.001)
model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy',
                                                      metrics=['accuracy'])

from keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='val_loss', patience=10,
                                     restore_best_weights=True)

history = model.fit(X_train, y_train, epochs=20, batch_size=10,
                    validation_data=(X_val, y_val), callbacks=[early_stopping])

loss, accuracy = model.evaluate(X_val, y_val, verbose=0)
print(f'loss: {loss:.2f}')
print(f'Accuracy: {accuracy*100:.2f}%')

embedding_layer = model.layers[1]
embedding_weights = embedding_layer.get_weights()[0]
print(embedding_weights)
if len(embedding_layer.get_weights()) > 1:
    embedding_bias = embedding_layer.get_weights()[1]
    print("Vector Bias:")
    print(embedding_bias)

import matplotlib.pyplot as plt
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='val')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()

accuracy = history.history['accuracy']
val_accuracy = history.history['val_accuracy']
plt.plot(accuracy, label='Training Accuracy')
plt.plot(val_accuracy, label='Validation Accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

model.summary()

from sklearn.metrics import classification_report
y_pred = model.predict(X_val)
y_pred_classes = np.argmax(y_pred, axis=1)
report = classification_report(y_val, y_pred_classes)
print("Classification Report:")
print(report)

from sklearn.metrics import confusion_matrix
import seaborn as sns
cm = confusion_matrix(y_val, y_pred_classes)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()

# Load the test data
test_df = pd.read_csv('/content/test.csv')

# Clean the text data
test_df["clean_text"] = test_df["text"].apply(clean_data)

# Preprocess the text data
test_df["text_prepro"] = test_df["clean_text"].apply(preprocess_data)

# Convert the preprocessed text into sequences
test_sequences = [[word2vec_model.wv.key_to_index[word] for word in preprocess_text2(doc) if word in word2vec_model.wv.key_to_index]
                  for doc in test_df['text_prepro']]

# Pad the sequences to the same length as the training data
test_padded_sequences = pad_sequences(test_sequences, maxlen=max_length, padding='post')

print(test_padded_sequences)

# Make predictions on the test data
predictions = model.predict(test_padded_sequences)

# Convert predictions to class labels (if necessary)
predicted_classes = np.argmax(predictions, axis=1)
print(predicted_classes)

# Save predictions to a CSV file
submission_df = pd.DataFrame({'id': test_df['id'],'text': test_df['text'], 'target': predicted_classes})
submission_df.to_csv('/content/predictions.csv', index=False)

print("Predictions saved to /content/predictions.csv")

