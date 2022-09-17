# Language Models

<p>
<a href="https://console.tiyaro.ai/explore/pierreguillou-bert-large-cased-squad-v1.1-portuguese"> <img src="https://tiyaro-public-docs.s3.us-west-2.amazonaws.com/assets/try_on_tiyaro_badge.svg"></a>
</p>
Repository of pre-trained Language Models and NLP models.

## NLP nas empresas | Como eu treinei um modelo T5 em português na tarefa QA no Google Colab
- Blog post: [NLP nas empresas | Como eu treinei um modelo T5 em português na tarefa QA no Google Colab](https://medium.com/@pierre_guillou/nlp-nas-empresas-como-eu-treinei-um-modelo-t5-em-portugu%C3%AAs-na-tarefa-qa-no-google-colab-e8eb0dc38894)
- Notebook: [Finetuning of the language model T5 base on a Question-Answering task (QA) with the dataset SQuAD 1.1 Portuguese](https://github.com/piegu/language-models/blob/master/HuggingFace_Notebook_t5_base_portuguese_vocab_question_answering_QA_squad_v11_pt.ipynb)
- [QA App](https://huggingface.co/spaces/pierreguillou/question-answering-portuguese-t5-base) in the Hugging Face Spaces

## NLP | Modelos e Web App para Reconhecimento de Entidade Nomeada (NER) no domínio jurídico brasileiro
- Blog post: [NLP | Modelos e Web App para Reconhecimento de Entidade Nomeada (NER) no domínio jurídico brasileiro](https://medium.com/@pierre_guillou/nlp-modelos-e-web-app-para-reconhecimento-de-entidade-nomeada-ner-no-dom%C3%ADnio-jur%C3%ADdico-b658db55edfb)
- [NER App](https://huggingface.co/spaces/pierreguillou/ner-bert-pt-lenerbr) in the Hugging Face Spaces

### Finetuning of the specialized version of the language model BERTimbau on a token classification task (NER) with the dataset LeNER-Br
- notebook: [HuggingFace_Notebook_token_classification_NER_LeNER_Br.ipynb](https://github.com/piegu/language-models/blob/master/HuggingFace_Notebook_token_classification_NER_LeNER_Br.ipynb) ([nbviewer of the notebook](https://nbviewer.org/github/piegu/language-models/blob/master/HuggingFace_Notebook_token_classification_NER_LeNER_Br.ipynb))
- [BERT base NER model in the legal domain in Portuguese (LeNER-Br)](https://huggingface.co/pierreguillou/ner-bert-base-cased-pt-lenerbr) in the Hugging Face model hub
- [BERT large NER model in the legal domain in Portuguese (LeNER-Br)](https://huggingface.co/pierreguillou/ner-bert-large-cased-pt-lenerbr) in the Hugging Face model hub

### Finetuning of the language model BERTimbau on LeNER-Br text files
- notebook: [Finetuning_language_model_BERtimbau_LeNER_Br.ipynb](https://github.com/piegu/language-models/blob/master/Finetuning_language_model_BERtimbau_LeNER_Br.ipynb) ([nbviewer of the notebook](https://nbviewer.org/github/piegu/language-models/blob/master/Finetuning_language_model_BERtimbau_LeNER_Br.ipynb))
- dataset: [pierreguillou/lener_br_finetuning_language_model](https://huggingface.co/datasets/pierreguillou/lener_br_finetuning_language_model)
- [BERT base Language modeling in the legal domain in Portuguese (LeNER-Br)](https://huggingface.co/pierreguillou/bert-base-cased-pt-lenerbr) in the Hugging Face model hub
- [BERT large Language modeling in the legal domain in Portuguese (LeNER-Br)](https://huggingface.co/pierreguillou/bert-large-cased-pt-lenerbr) in the Hugging Face model hub

## NLP nas empresas | Técnicas para acelerar modelos de Deep Learning para inferência em produção

- Blog post: [NLP nas empresas | Técnicas para acelerar modelos de Deep Learning para inferência em produção](https://medium.com/@pierre_guillou/nlp-nas-empresas-t%C3%A9cnicas-para-acelerar-modelos-de-deep-learning-para-infer%C3%AAncia-em-produ%C3%A7%C3%A3o-884acbf49f20)
- notebooks:
  - [fast_inference_transformers_on_CPU.ipynb](https://github.com/piegu/language-models/blob/master/fast_inference_transformers_on_CPU.ipynb) ([nbviewer](https://nbviewer.org/github/piegu/language-models/blob/master/fast_inference_transformers_on_CPU.ipynb?flush_cache=true))
  - [fast_inference_transformers_on_GPU.ipynb](https://github.com/piegu/language-models/blob/master/fast_inference_transformers_on_GPU.ipynb) ([nbviewer](https://nbviewer.org/github/piegu/language-models/blob/master/fast_inference_transformers_on_GPU.ipynb?flush_cache=true))

## NLP nas empresas | Reconhecimento de textos com Deep Learning em PDFs e imagens

- notebook [OCR_DeepLearning_Tesseract_DocTR_colab.ipynb](https://github.com/piegu/language-models/blob/master/OCR_DeepLearning_Tesseract_DocTR_colab.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/OCR_DeepLearning_Tesseract_DocTR_colab.ipynb?flush_cache=true))
- Blog post: [NLP nas empresas | Reconhecimento de textos com Deep Learning em PDFs e imagens](https://medium.com/@pierre_guillou/nlp-nas-empresas-reconhecimento-de-textos-com-deep-learning-em-pdfs-e-imagens-14d8b9e8d513)

## NLP nas empresas | Como criar um modelo BERT de Question-Answering (QA) de desempenho aprimorado com AdapterFusion?

- notebook [question_answering_adapter_fusion.ipynb](https://github.com/piegu/language-models/blob/master/adapters/question-answering/question_answering_adapter_fusion.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/adapters/question-answering/question_answering_adapter_fusion.ipynb?flush_cache=true)): finetuning a MLM (Masked Language Model) like BERT (base or large) with the library adapter-transformers on the Question Answering task (QA) with AdapterFusion
- Blog post: [NLP nas empresas | Como criar um modelo BERT de Question-Answering (QA) de desempenho aprimorado com AdapterFusion?](https://medium.com/@pierre_guillou/nlp-nas-empresas-como-criar-um-modelo-bert-de-question-answering-qa-de-desempenho-aprimorado-21b699326c82)

## NLP nas empresas | Como ajustar um modelo de linguagem natural como BERT para a tarefa de Question-Answering (QA) com um Adapter?

- notebooks [question_answering_adapter.ipynb](https://github.com/piegu/language-models/blob/master/adapters/question-answering/question_answering_adapter.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/adapters/question-answering/question_answering_adapter.ipynb?flush_cache=true)) and [question_answering_adapter_script.ipynb](https://github.com/piegu/language-models/blob/master/adapters/question-answering/question_answering_adapter_script.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/adapters/question-answering/question_answering_adapter_script.ipynb?flush_cache=true)): finetuning a MLM (Masked Language Model) like BERT (base or large) with the library adapter-transformers on the Question Answering task (QA)
- Blog post: [NLP nas empresas | Como ajustar um modelo de linguagem natural como BERT para a tarefa de Question-Answering (QA) com um Adapter?](https://medium.com/@pierre_guillou/nlp-nas-empresas-como-ajustar-um-modelo-de-linguagem-natural-como-bert-para-a-tarefa-de-b7d2e7553a01)

## NLP nas empresas | Como ajustar um modelo de linguagem natural como BERT para a tarefa de classificação de tokens (NER) com um Adapter?

- notebook [token_classification_adapter.ipynb](https://github.com/piegu/language-models/blob/master/adapters/token-classification/token_classification_adapter.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/adapters/token-classification/token_classification_adapter.ipynb)): finetuning a MLM (Masked Language Model) like BERT (base or large) with the library adapter-transformers on the Token Classification task (NER)
- Blog post: [NLP nas empresas | Como ajustar um modelo de linguagem natural como BERT para a tarefa de classificação de tokens (NER) com um Adapter?](https://medium.com/@pierre_guillou/nlp-nas-empresas-como-ajustar-um-modelo-de-linguagem-natural-como-bert-para-a-tarefa-de-9c6a704bf536)

## NLP nas empresas | Como ajustar um modelo de linguagem natural como BERT a um novo domínio linguístico com um Adapter?

- notebook [language_modeling_adapter.ipynb](https://github.com/piegu/language-models/blob/master/adapters/language-modeling/language_modeling_adapter.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/adapters/language-modeling/language_modeling_adapter.ipynb)): finetuning a MLM (Masked Language Model) like BERT (base or large) with the library adapter-transformers
- Blog post: [NLP nas empresas | Como ajustar um modelo de linguagem natural como BERT a um novo domínio linguístico com um Adapter?](https://medium.com/@pierre_guillou/nlp-nas-empresas-como-ajustar-um-modelo-de-linguagem-natural-como-bert-a-um-novo-dom%C3%ADnio-23752b73b185)

## NLP | Modelo de Question Answering em qualquer idioma baseado no BERT large (estudo de caso em português)

- notebook [question_answering_BERT_large_cased_squad_v11_pt.ipynb](https://github.com/piegu/language-models/blob/master/question_answering_BERT_large_cased_squad_v11_pt.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/question_answering_BERT_large_cased_squad_v11_pt.ipynb)): training code of a Portuguese BERT large cased QA (Question Answering), finetuned on SQUAD v1.1
- Blog post: [NLP | Como treinar um modelo de Question Answering em qualquer linguagem baseado no BERT large, melhorando o desempenho do modelo utilizando o BERT base? (estudo de caso em português)](https://medium.com/@pierre_guillou/nlp-como-treinar-um-modelo-de-question-answering-em-qualquer-linguagem-baseado-no-bert-large-1c899262dd96)
- Model in the Model Hub of Hugging Face: [Portuguese BERT large cased QA (Question Answering), finetuned on SQUAD v1.1](https://huggingface.co/pierreguillou/bert-large-cased-squad-v1.1-portuguese)

## NLP | How to add a domain-specific vocabulary (new tokens) to a subword tokenizer already trained like BERT WordPiece
**Summary**: In some cases, it may be crucial to enrich the vocabulary of an already trained natural language model with vocabulary from a specialized domain (medicine, law, etc.) in order to perform new tasks (classification, NER, summary, translation, etc.). While the Hugging Face library allows you to easily add new tokens to the vocabulary of an existing tokenizer like BERT WordPiece, those tokens must be whole words, not subwords. This article explains why and how to obtain these new tokens from a specialized corpus.
- notebook [nlp_how_to_add_a_domain_specific_vocabulary_new_tokens_to_a_subword_tokenizer_already_trained_like_BERT_WordPiece.ipynb](https://github.com/piegu/language-models/blob/master/nlp_how_to_add_a_domain_specific_vocabulary_new_tokens_to_a_subword_tokenizer_already_trained_like_BERT_WordPiece.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/nlp_how_to_add_a_domain_specific_vocabulary_new_tokens_to_a_subword_tokenizer_already_trained_like_BERT_WordPiece.ipynb)) ([notebook in colab](https://colab.research.google.com/drive/1Hlfv5wHbYW863c9MraDy9EBknIQf3uAr?usp=sharing))
- Blog post: [NLP | How to add a domain-specific vocabulary (new tokens) to a subword tokenizer already trained like BERT WordPiece](https://medium.com/@pierre_guillou/nlp-how-to-add-a-domain-specific-vocabulary-new-tokens-to-a-subword-tokenizer-already-trained-33ab15613a41)

## NLP | Modelo de Question Answering em qualquer idioma baseado no BERT base (estudo de caso em português)

- notebook [colab_question_answering_BERT_base_cased_squad_v11_pt.ipynb](https://github.com/piegu/language-models/blob/master/colab_question_answering_BERT_base_cased_squad_v11_pt.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/colab_question_answering_BERT_base_cased_squad_v11_pt.ipynb)): training code of a Portuguese BERT base cased QA (Question Answering), finetuned on SQUAD v1.1
- Blog post: [NLP | Modelo de Question Answering em qualquer idioma baseado no BERT base (estudo de caso em português)](https://medium.com/@pierre_guillou/nlp-modelo-de-question-answering-em-qualquer-idioma-baseado-no-bert-base-estudo-de-caso-em-12093d385e78)
- Model in the Model Hub of Hugging Face: [Portuguese BERT base cased QA (Question Answering), finetuned on SQUAD v1.1](https://huggingface.co/pierreguillou/bert-base-cased-squad-v1.1-portuguese)

## Portuguese

I trained 1 Portuguese Bidirectional Language Model (PBLM) with the [MultiFit](https://arxiv.org/pdf/1909.04761.pdf) configuration with 1 NVIDIA GPU v100 on [GCP](https://cloud.google.com).

**WARNING**: a Bidirectional LM model using the MultiFiT configuration is a good model to perform text classification but with only 46 millions of parameters, it is far from being a LM that can compete with [GPT-2](https://openai.com/blog/better-language-models/) or [BERT](https://arxiv.org/abs/1810.04805) in NLP tasks like text generation. This my next step ;-) 

**Note**: The training times shown in the tables on this page are the sum of the creation time of Fastai Databunch (forward and backward) and the training duration of the bidirectional model over 10 periods. The download time of the Wikipedia corpus and its preparation time are not counted.

### MultiFiT configuration (architecture 4 QRNN with 1550 hidden parameters by layer / tokenizer SentencePiece (15 000 tokens))
- notebook [lm3-portuguese.ipynb](https://github.com/piegu/language-models/blob/master/lm3-portuguese.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/lm3-portuguese.ipynb)): code used to train a Portuguese Bidirectional LM on a 100 millions corpus extrated from Wikipedia by using the [MultiFiT](https://arxiv.org/pdf/1909.04761.pdf) configuration.
- link to download pre-trained parameters and vocabulary in [models](https://github.com/piegu/language-models/tree/master/models)

| PBLM | accuracy | perplexity | training time |
| ------------- | ------------- | ------------- | ------------- |
| forward   | 39.68%  | 21.76  | 8h |
| backward  | 43.67%  | 22.16  | 8h |

- Applications:
  - notebook [lm3-portuguese-classifier-TCU-jurisprudencia.ipynb](https://github.com/piegu/language-models/blob/master/lm3-portuguese-classifier-TCU-jurisprudencia.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/lm3-portuguese-classifier-TCU-jurisprudencia.ipynb)): code used to fine-tune a Portuguese Bidirectional LM and a Text Classifier on "(reduzido) TCU jurisprudência" dataset.
  - notebook [lm3-portuguese-classifier-olist.ipynb](https://github.com/piegu/language-models/blob/master/lm3-portuguese-classifier-olist.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/lm3-portuguese-classifier-olist.ipynb)): code used to fine-tune a Portuguese Bidirectional LM and a Sentiment Classifier on "Brazilian E-Commerce Public Dataset by Olist" dataset. 

**[ WARNING ]** The code of this notebook [lm3-portuguese-classifier-olist.ipynb](https://github.com/piegu/language-models/blob/master/lm3-portuguese-classifier-olist.ipynb) must be updated in order to use the SentencePiece model and vocab already trained for the Portuguese Language Model in the notebook [lm3-portuguese.ipynb](https://github.com/piegu/language-models/blob/master/lm3-portuguese.ipynb) as it was done in the notebook [lm3-portuguese-classifier-TCU-jurisprudencia.ipynb](https://github.com/piegu/language-models/blob/master/lm3-portuguese-classifier-TCU-jurisprudencia.ipynb) (see explanations at the top of this notebook).
  
Here's an example of using the classifier to predict the category of a TCU legal text:

![Using the classifier to predict the category of TCU legal texts](https://miro.medium.com/max/6275/1*nKPnG0hJnTrW0xV-T1DQ9A.jpeg "Using the classifier to predict the category of TCU legal texts")

## French

I trained 3 French Bidirectional Language Models (FBLM) with 1 NVIDIA GPU v100 on [GCP](https://cloud.google.com) but **the best is the one trained with the [MultiFit](https://arxiv.org/pdf/1909.04761.pdf) configuration**.

| French Bidirectional Language Models (FBLM) | | accuracy | perplexity | training time |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| [MultiFiT with 4 QRNN + SentencePiece (15 000 tokens)](https://github.com/piegu/language-models/blob/master/lm3-french.ipynb) | forward   | 43.77%  | 16.09  | 8h40 |
| | backward  | 49.29%  | 16.58  | 8h10 | 
| [ULMFiT with 3 QRNN + SentencePiece (15 000 tokens)](https://github.com/piegu/language-models/blob/master/lm2-french.ipynb) | forward   | 40.99%  | 19.96  | 5h30 |
| | backward  | 47.19%  | 19.47  | 5h30 | 
| [ULMFiT with 3 AWD-LSTM + spaCy (60 000 tokens)](https://github.com/piegu/language-models/blob/master/lm-french.ipynb) | forward   | 36.44%  | 25.62  | 11h |
| | backward  | 42.65%  | 27.09  | 11h | 

### 1. MultiFiT configuration (architecture 4 QRNN with 1550 hidden parameters by layer / tokenizer SentencePiece (15 000 tokens))
- notebook [lm3-french.ipynb](https://github.com/piegu/language-models/blob/master/lm3-french.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/lm3-french.ipynb)): code used to train a French Bidirectional LM on a 100 millions corpus extrated from Wikipedia by using the [MultiFiT](https://arxiv.org/pdf/1909.04761.pdf) configuration.
- link to download pre-trained parameters and vocabulary in [models](https://github.com/piegu/language-models/tree/master/models)

| FBLM | accuracy | perplexity | training time |
| ------------- | ------------- | ------------- | ------------- |
| forward   | 43.77%  | 16.09  | 8h40 |
| backward  | 49.29%  | 16.58  | 8h10 | 

- Application: notebook [lm3-french-classifier-amazon.ipynb](https://github.com/piegu/language-models/blob/master/lm3-french-classifier-amazon.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/lm3-french-classifier-amazon.ipynb)): code used to fine-tune a French Bidirectional LM and a Sentiment Classifier on "French Amazon Customer Reviews" dataset.

Here's an example of using the classifier to predict the feeling of comments on an amazon product:

![Using the classifier to predict the feeling of comments on an amazon product](https://miro.medium.com/max/2630/1*HswVRzYjkFfom8BZLUWqjg.png "Using the classifier to predict the feeling of comments on an amazon product")

### 2. Architecture QRNN / tokenizer SentencePiece 
- notebook [lm2-french.ipynb](https://github.com/piegu/language-models/blob/master/lm2-french.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/lm2-french.ipynb)): code used to train a French Bidirectional LM on a 100 millions corpus extrated from Wikipedia
- link to download pre-trained parameters and vocabulary in [models](https://github.com/piegu/language-models/tree/master/models)

| FBLM | accuracy | perplexity | training time |
| ------------- | ------------- | ------------- | ------------- |
| forward   | 40.99%  | 19.96  | 5h30 |
| backward  | 47.19%  | 19.47  | 5h30 | 

- Application: notebook [lm2-french-classifier-amazon.ipynb](https://github.com/piegu/language-models/blob/master/lm2-french-classifier-amazon.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/lm2-french-classifier-amazon.ipynb)): code used to fine-tune a French Bidirectional LM and a Sentiment Classifier on "French Amazon Customer Reviews" dataset.

### 3. Architecture AWD-LSTM / tokenizer spaCy 
- notebook [lm-french.ipynb](https://github.com/piegu/language-models/blob/master/lm-french.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/lm-french.ipynb)): code used to train a French Bidirectional LM on a 100 millions corpus extrated from Wikipedia
- link to download pre-trained parameters and vocabulary in [models](https://github.com/piegu/language-models/tree/master/models)

| FBLM | accuracy | perplexity | training time |
| ------------- | ------------- | ------------- | ------------- |
| forward   | 36.44%  | 25.62  | 11h |
| backward  | 42.65%  | 27.09  | 11h | 

- Application: notebook [lm-french-classifier-amazon.ipynb](https://github.com/piegu/language-models/blob/master/lm-french-classifier-amazon.ipynb) ([nbviewer of the notebook](https://nbviewer.jupyter.org/github/piegu/language-models/blob/master/lm-french-classifier-amazon.ipynb)): code used to fine-tune a French Bidirectional LM and a Sentiment Classifier on "French Amazon Customer Reviews" dataset.
