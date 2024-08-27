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
        <img src="https://github.com/lokudadalla/NLP-with-Disaster-Tweet-Multi-Head-Attention/blob/0f4e7ec99335c5042da415a042ee6afd2b339f1d/images/1.png" alt="Model Architecture">
        <div class="caption">after preprocessing</div>
    </div>
    <p>

  </p>

  <div class="image-container">
        <img src="https://github.com/lokudadalla/NLP-with-Disaster-Tweet-Multi-Head-Attention/blob/0f4e7ec99335c5042da415a042ee6afd2b339f1d/images/2.png" alt="Model Architecture">
        <div class="caption">Tokenization</div>
    </div>

  <h2>Word Embedding with Word2Vec and Padding Sequences</h2>
    <p>
        Word embeddings are dense vector representations of words in a continuous vector space, capturing the semantic meaning of words. These embeddings are crucial for the neural network to understand the context and relationships between words. The script then converts the preprocessed text into sequences of word indices based on the Word2Vec model, preparing the data for input into the neural network.
        Since neural networks require input of fixed length, the script pads all sequences to match the length of the longest sequence in the dataset. This ensures uniform input size, which is necessary for training the model.
    </p>

   <div class="image-container">
        <img src="https://github.com/lokudadalla/NLP-with-Disaster-Tweet-Multi-Head-Attention/blob/0f4e7ec99335c5042da415a042ee6afd2b339f1d/images/3.png" alt="Model Architecture">
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
