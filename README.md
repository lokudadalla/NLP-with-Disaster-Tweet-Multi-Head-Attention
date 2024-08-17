# NLP-with-Disaster-Tweet-Multi-Head-Attention

<!DOCTYPE html>
<html lang="en">
<body>
    <h2>Data Preprocessing and Tokenization</h2>
    <p>
        The data is stored in a DataFrame called <code>train_df</code>. The text data is then cleaned using various NLP techniques. HTML tags and URLs are removed, non-ASCII characters and special characters are filtered out, and isolated numbers are deleted. This process ensures that the text data is standardized and free from unnecessary noise, making it suitable for further analysis.
        After cleaning the text, the script tokenizes the text, which involves splitting it into individual words or tokens. Stop words, which are common words like "the" and "and" that do not add significant meaning, are removed. The remaining words are then stemmed using the Porter Stemmer algorithm, which reduces words to their root form. This step helps in normalizing the text data by converting different forms of a word into a single representation, making it easier for the model to process.
    </p>

   <div class="image-container">
        <img src="https://private-user-images.githubusercontent.com/133969661/334141706-f782f01c-1b15-4f00-92cb-b006d9bd91f2.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjM5MTAwNzEsIm5iZiI6MTcyMzkwOTc3MSwicGF0aCI6Ii8xMzM5Njk2NjEvMzM0MTQxNzA2LWY3ODJmMDFjLTFiMTUtNGYwMC05MmNiLWIwMDZkOWJkOTFmMi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwODE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDgxN1QxNTQ5MzFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00MzM5NDA4ZjA1MmZmZTc5MmQ1ZjNjMGU0YzljNGY3ODhjZWMyZDE1OTIzYjliZTNjNGZjNWI2OWFlZmE0YTg0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.DUSs3jjkSlmAXhqocgv-KWzgXkYYaND9pa0gXex-B_Q" alt="Model Architecture">
        <div class="caption">after preprocessing</div>
    </div>
    <p>

  </p>

  <div class="image-container">
        <img src="https://private-user-images.githubusercontent.com/133969661/334141755-e162d2ce-da7e-4e40-bc6d-acea0233a928.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjM5MTAwNzEsIm5iZiI6MTcyMzkwOTc3MSwicGF0aCI6Ii8xMzM5Njk2NjEvMzM0MTQxNzU1LWUxNjJkMmNlLWRhN2UtNGU0MC1iYzZkLWFjZWEwMjMzYTkyOC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwODE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDgxN1QxNTQ5MzFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hYmQxODA5MTFjZDA0ZWI4MmMzMjk1ZDYwZDI4NGRkZmNmYzNlNWJhZjdlMzhhZjg2NmU3YzVkOGM5Y2IxOGNmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.I2uDnE1wIsEDAXzp6r2RzcH1cKywIs7NW0bZ9n1UeYE" alt="Model Architecture">
        <div class="caption">Tokenization</div>
    </div>

  <h2>Word Embedding with Word2Vec and Padding Sequences</h2>
    <p>
        Word embeddings are dense vector representations of words in a continuous vector space, capturing the semantic meaning of words. These embeddings are crucial for the neural network to understand the context and relationships between words. The script then converts the preprocessed text into sequences of word indices based on the Word2Vec model, preparing the data for input into the neural network.
        Since neural networks require input of fixed length, the script pads all sequences to match the length of the longest sequence in the dataset. This ensures uniform input size, which is necessary for training the model.
    </p>

   <div class="image-container">
        <img src="https://private-user-images.githubusercontent.com/133969661/334141765-fe1f4538-2f79-4ebb-b57a-3e2da6951c78.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjM5MTAwNzEsIm5iZiI6MTcyMzkwOTc3MSwicGF0aCI6Ii8xMzM5Njk2NjEvMzM0MTQxNzY1LWZlMWY0NTM4LTJmNzktNGViYi1iNTdhLTNlMmRhNjk1MWM3OC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwODE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDgxN1QxNTQ5MzFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04OGU2YjAwYzM2Y2ViYzY4M2UxNzViYjFhM2RkYjE5MjQ2OGNiZTljNTk2NzhmMzM5MjRhNzZlMDVlODRmNmMyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.7zNmq6EYBcUjORd8b6nKqNuE2d5tIxRMaNAkbC5cu30" alt="Model Architecture">
        <div class="caption">after padding sequence</div>
    </div>

  <h2>Building, Training, and Evaluating the Model</h2>
    <p>
        The function creates an input layer and an embedding layer, followed by multi-head attention layers, which allow the model to focus on different parts of the input sequence simultaneously. This is crucial for capturing contextual relationships in the text. Layer normalization and fully connected layers with dropout and L2 regularization are added to enhance generalization and prevent overfitting. The model is finalized with a global max pooling layer and a dense output layer with a softmax activation function, suitable for classification tasks. Training is performed with early stopping to avoid overfitting, using the training set for learning and the validation set for performance evaluation.
    </p>
<h2>Resources</h2>
<p>
        For more information about multi-head attention and its applications in neural networks, you can visit this
        <a href="https://arxiv.org/pdf/1706.03762v7" target="_blank">paper on Attention Is All You Need</a>. This paper introduces the concept of multi-head attention and explains how it improves the model's ability to focus on different parts of the input sequence simultaneously.
</p>
<p>
    <a href="https://storrs.io/multihead-attention/" target="_blank">multi-head attention 1</a>
</p>
<p>
     <a href="https://storrs.io/attention/" target="_blank">multi-head attention 2</a>
</p>

    
</body>
</html>
