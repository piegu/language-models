# Language Models
Repository of pre-trained Language Models.

## Portuguese

I trained 1 Portuguese Bidirectional Language Model with the [MultiFit](https://arxiv.org/pdf/1909.04761.pdf) configuration.

### MultiFiT configuration (architecture 4 QRNN with 1550 hidden parameters by layer / tokenizer SentencePiece (15 000 tokens))
- notebook [lm3-portuguese.ipynb](https://github.com/piegu/language-models/blob/master/lm3-portuguese.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/lm3-portuguese.ipynb)): code used to train a Portuguese Bidirectional LM on a 100 millions corpus extrated from Wikipedia by using the [MultiFiT](https://arxiv.org/pdf/1909.04761.pdf) configuration.
- link to download pre-trained parameters and vocabulary in [models](https://github.com/piegu/language-models/tree/master/models)

**forward Portuguese LM**: (accuracy) 39.68% | (perplexity) 21.76

**backward Portuguese LM**:(accuracy) 43.67% | (perplexity) 22.16

## French

I trained 3 French Bidirectional Language Models but the best is the one trained with the [MultiFit](https://arxiv.org/pdf/1909.04761.pdf) configuration.

### 1. MultiFiT configuration (architecture 4 QRNN with 1550 hidden parameters by layer / tokenizer SentencePiece (15 000 tokens))
- notebook [lm3-french.ipynb](https://github.com/piegu/language-models/blob/master/lm3-french.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/lm3-french.ipynb)): code used to train a French Bidirectional LM on a 100 millions corpus extrated from Wikipedia by using the [MultiFiT](https://arxiv.org/pdf/1909.04761.pdf) configuration.
- link to download pre-trained parameters and vocabulary in [models](https://github.com/piegu/language-models/tree/master/models)

**forward French LM**: (accuracy) 43.77% and (perplexity) 16.09

**backward French LM**: (accuracy) 49.29% and (perplexity) 16.58

### 2. Architecture QRNN / tokenizer SentencePiece 
- notebook [lm2-french.ipynb](https://github.com/piegu/language-models/blob/master/lm2-french.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/lm2-french.ipynb)): code used to train a French Bidirectional LM on a 100 millions corpus extrated from Wikipedia
- link to download pre-trained parameters and vocabulary in [models](https://github.com/piegu/language-models/tree/master/models)
- notebook [lm2-french-classifier-amazon.ipynb](https://github.com/piegu/language-models/blob/master/lm2-french-classifier-amazon.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/lm2-french-classifier-amazon.ipynb)): code used to fine-tune a French Bidirectional LM and a Sentiment Classifier on "French Amazon Customer Reviews" dataset.

**forward French LM**: (accuracy) 40.99% and (perplexity) 19.96

**backward French LM**: (accuracy) 47.19% and (perplexity) 19.47

### 3. Architecture AWD-LSTM / tokenizer spaCy 
- notebook [lm-french.ipynb](https://github.com/piegu/language-models/blob/master/lm-french.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/lm-french.ipynb)): code used to train a French Bidirectional LM on a 100 millions corpus extrated from Wikipedia
- link to download pre-trained parameters and vocabulary in [models](https://github.com/piegu/language-models/tree/master/models)
- notebook [lm-french-classifier-amazon.ipynb](htps://github.com/piegu/language-models/blob/master/lm-french-classifier-amazon.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/lm-french-classifier-amazon.ipynb)): code used to fine-tune a French Bidirectional LM and a Sentiment Classifier on "French Amazon Customer Reviews" dataset.

**forward French LM**: (accuracy) 36.44% and (perplexity) 25.62

**backward French LM**: (accuracy) 42.65% and (perplexity) 27.09
