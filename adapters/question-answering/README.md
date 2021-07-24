Notebooks and scripts for fine-tuning a Masked Language Model (MLM) like BERT (base or large) for a QA task by training adapters (library [adapter-transformers](https://github.com/Adapter-Hub/adapter-transformers)), not the embeddings and transformers layers of the MLM model.

To be able to run the notebook [question_answering_adapter_script.ipynb](https://github.com/piegu/language-models/blob/master/adapters/question-answering/question_answering_adapter_script.ipynb), you need to download in the same folder the 2 following files: [trainer_qa.py](https://github.com/Adapter-Hub/adapter-transformers/blob/master/examples/question-answering/trainer_qa.py), [utils_qa.py](https://github.com/Adapter-Hub/adapter-transformers/blob/master/examples/question-answering/utils_qa.py).

The [requirements.txt](https://github.com/Adapter-Hub/adapter-transformers/blob/master/examples/question-answering/requirements.txt) gives you the datasets version needed and here is the list of the libraries versions used in a virtual environment when we ran successfully notebooks and scripts of this folder:

- python: 3.8.10 (default, Jun  4 2021, 15:09:15) 
- Pytorch: 1.9.0
- adapter-transformers: 2.1.1
- HF transformers: 4.8.2
- tokenizers: 0.10.3
- datasets: 1.9.0
