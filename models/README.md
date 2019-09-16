# Models and vocabularies
Repository of links to download pre-trained parameters and vocabularies of pre-trained Language Models (architecture: [AWD-LSTM](https://github.com/salesforce/awd-lstm-lm)).

In a terminal, type `tar -xvzf filename.tgz` to extract the 2 files of the pre-trained Language Model ({lang} is the language symbol like fr for French):
- pre-trained parameters: {lang}_wt.pth
- vocabulary: {lang}_wt_vocab.pkl

For each Language Model, the link to the corresponding notebook is done. It allows to understand how the LM was trained and on which training corpus.

## French LM
- [french_lm.tgz](https://drive.google.com/file/d/1hIyWNZqWaRbce_f2VuqeYCJAUDenWe8v/view?usp=sharing) (157 Mo) | notebook [lm-french.ipynb](https://github.com/piegu/language-models/blob/master/lm-french.ipynb) | Training corpus: 100 millions tokens from French Wikipedia
