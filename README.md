# Language Models
Repository of pre-trained Language Models.

**WARNING**: a Bidirectional LM model using the MultiFiT configuration is a good model to perform text classification but with only 46 millions of parameters, it is far from being a LM that can gan compete with [GPT-2](https://openai.com/blog/better-language-models/) or [BERT](https://arxiv.org/abs/1810.04805) in NLP tasks like text generation. This my next step ;-) 

**Note**: the traning times given below are the sum of fastai Databunch creation + model training on 10 epochs.

## Portuguese

I trained 1 Portuguese Bidirectional Language Model with the [MultiFit](https://arxiv.org/pdf/1909.04761.pdf) configuration.

### MultiFiT configuration (architecture 4 QRNN with 1550 hidden parameters by layer / tokenizer SentencePiece (15 000 tokens))
- notebook [lm3-portuguese.ipynb](https://github.com/piegu/language-models/blob/master/lm3-portuguese.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/lm3-portuguese.ipynb)): code used to train a Portuguese Bidirectional LM on a 100 millions corpus extrated from Wikipedia by using the [MultiFiT](https://arxiv.org/pdf/1909.04761.pdf) configuration.
- link to download pre-trained parameters and vocabulary in [models](https://github.com/piegu/language-models/tree/master/models)
- Training with 1 NVIDIA GPU v100 on [GCP](https://cloud.google.com)

| | accuracy | perplexity | training time |
| ------------- | ------------- | ------------- | ------------- |
| forward   | 39.68%  | 21.76  | 8h |
| backward  | 43.67%  | 22.16  | 8h |

## French

I trained 3 French Bidirectional Language Models but the best is the one trained with the [MultiFit](https://arxiv.org/pdf/1909.04761.pdf) configuration.

### 1. MultiFiT configuration (architecture 4 QRNN with 1550 hidden parameters by layer / tokenizer SentencePiece (15 000 tokens))
- notebook [lm3-french.ipynb](https://github.com/piegu/language-models/blob/master/lm3-french.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/lm3-french.ipynb)): code used to train a French Bidirectional LM on a 100 millions corpus extrated from Wikipedia by using the [MultiFiT](https://arxiv.org/pdf/1909.04761.pdf) configuration.
- link to download pre-trained parameters and vocabulary in [models](https://github.com/piegu/language-models/tree/master/models)
- notebook [lm3-french-classifier-amazon.ipynb](https://github.com/piegu/language-models/blob/master/lm3-french-classifier-amazon.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/lm3-french-classifier-amazon.ipynb)): code used to fine-tune a French Bidirectional LM and a Sentiment Classifier on "French Amazon Customer Reviews" dataset.
- Training with 1 NVIDIA GPU v100 on [GCP](https://cloud.google.com)

| | accuracy | perplexity | training time |
| ------------- | ------------- | ------------- | ------------- |
| forward   | 43.77%  | 16.09  | 8h40 |
| backward  | 49.29%  | 16.58  | 8h10 | 

### 2. Architecture QRNN / tokenizer SentencePiece 
- notebook [lm2-french.ipynb](https://github.com/piegu/language-models/blob/master/lm2-french.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/lm2-french.ipynb)): code used to train a French Bidirectional LM on a 100 millions corpus extrated from Wikipedia
- link to download pre-trained parameters and vocabulary in [models](https://github.com/piegu/language-models/tree/master/models)
- notebook [lm2-french-classifier-amazon.ipynb](https://github.com/piegu/language-models/blob/master/lm2-french-classifier-amazon.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/lm2-french-classifier-amazon.ipynb)): code used to fine-tune a French Bidirectional LM and a Sentiment Classifier on "French Amazon Customer Reviews" dataset.
- Training with 1 NVIDIA GPU v100 on [GCP](https://cloud.google.com)

| | accuracy | perplexity | training time |
| ------------- | ------------- | ------------- | ------------- |
| forward   | 40.99%  | 19.96  | 5h30 |
| backward  | 47.19%  | 19.47  | 5h30 | 

### 3. Architecture AWD-LSTM / tokenizer spaCy 
- notebook [lm-french.ipynb](https://github.com/piegu/language-models/blob/master/lm-french.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/lm-french.ipynb)): code used to train a French Bidirectional LM on a 100 millions corpus extrated from Wikipedia
- link to download pre-trained parameters and vocabulary in [models](https://github.com/piegu/language-models/tree/master/models)
- notebook [lm-french-classifier-amazon.ipynb](htps://github.com/piegu/language-models/blob/master/lm-french-classifier-amazon.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/lm-french-classifier-amazon.ipynb)): code used to fine-tune a French Bidirectional LM and a Sentiment Classifier on "French Amazon Customer Reviews" dataset.

| | accuracy | perplexity | training time |
| ------------- | ------------- | ------------- | ------------- |
| forward   | 36.44%  | 25.62  | 11h |
| backward  | 42.65%  | 27.09  | 11h | 
