# Models and vocabularies
Repository of links to download pre-trained parameters and vocabularies of **pre-trained Bidirectional Language Models**.

In a terminal, type `tar -xvzf filename.tgz` to extract the folder with 4 files of the pre-trained Bidirectional Language Model ({lang} is the language symbol like fr for French).

- Forward LM:
  - pre-trained parameters: {lang}_wt.pth
  - vocabulary: {lang}_wt_vocab.pkl
- Backward LM:
  - pre-trained parameters: {lang}_wt_bwd.pth
  - vocabulary: {lang}_wt_vocab_bwd.pkl

For each Language Model, the link to the corresponding notebook is done. It allows to understand how the LM was trained and on which training corpus.

## French Bidirectional LM

### architecture AWD-LSTM / tokenizer spaCy
- [fr_lm_awdlstm_spacy.tgz](https://drive.google.com/open?id=1CN6QqTxnTy_UHVTaIqc53mwSVpJJZtbN) (315 Mo) | notebook [lm-french.ipynb](https://github.com/piegu/language-models/blob/master/lm-french.ipynb) | Training corpus: 100 millions tokens from French Wikipedia

### architecture QRNN / tokenizer SentencePiece
- [fr_lm_qrnn_sp15.tgz](https://drive.google.com/open?id=1cAVj40tI9Q4RVrmn-AzF6dER8xTv1_zM) (200 Mo) | notebook [lm2-french.ipynb](https://github.com/piegu/language-models/blob/master/lm2-french.ipynb) | Training corpus: 100 millions tokens from French Wikipedia
