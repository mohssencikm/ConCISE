🧠 ConCISE: A Reference-Free Metric for Measuring Conciseness of LLM Responses
ConCISE is a novel LLM-based metric designed to automatically evaluate the conciseness of language model outputs. Unlike traditional metrics, ConCISE assesses how succinctly an answer conveys information without sacrificing its key meaning—entirely without needing gold references.

This project provides a complete and reproducible pipeline to:

Generate verbose and concise versions of LLM answers

Evaluate conciseness via LLM-based summarization and redundancy detection

Compare ConCISE against human annotations and baselines (like BERTScore, GPTScore, and answer length)

Compute correlation with human ratings and evaluate pairwise agreement

📝 This project accompanies our resource paper submission to CIKM 2025.




🔧 **Project Structure**

ConCISE/
│
├── __init__.py

├── api.py               # LLM wrapper and API call manager

├── verbose.py           # Verbose version generation

├── summarization.py     # Summarization and word-pruning operations

├── scoring.py           # LLM-based scoring functions and compression ratio

├── ranking.py           # Pairwise ranking using LLM

├── evaluation.py        # Spearman, Kendall correlation calculations

├── utils.py             # Helper functions (e.g. word counting)


🚀 **Getting Started**
1. Install Dependencies
You need:

Python 3.8+

A working OpenAI or Anthropic API key (e.g., for GPT-4 or Claude)

```python
openai, pandas, scipy

pip install openai pandas scipy
```



2. Initialize Your LLM Model
```python
from openai import OpenAI
from genrait_conciseness.api import LLMModelWrapper

client = OpenAI(api_key="your-key-here")
llm_model = LLMModelWrapper(client)
```



🧪 **Core Functionality**
Generate Verbose Answers
```python
from genrait_conciseness.verbose import make_verbose_version

verbose = make_verbose_version(llm_model, original_answer)
```



**Generate Summaries & Pruned Text**
```python
from genrait_conciseness.summarization import make_summary

abstractive, extractive, pruned = make_summary(llm_model, original_answer)
```



**Compute Conciseness Score (GPT)**
```python
from genrait_conciseness.scoring import GPTSCORE

score = GPTSCORE(llm_model, original_answer)
```


**Rank Answers by Conciseness**
```python
from genrait_conciseness.ranking import GPTRanking

better = GPTRanking(llm_model, question, answer1, answer2)  # returns "answer 1" or "answer 2"
```


**Correlation with Human Ratings**
```python
from genrait_conciseness.evaluation import spearman_corr, kendall_corr

rho, p_val = spearman_corr(human_scores, concise_scores)
```


📊 **Example Pipeline**
```python
import pandas as pd
from genrait_conciseness.api import LLMModelWrapper
from genrait_conciseness.verbose import make_verbose_version
from genrait_conciseness.scoring import GPTSCORE
from genrait_conciseness.utils import count_words

# **Load dataset**
df = pd.read_csv("your_data.csv")

# **Generate verbose answers**
df["verbose"] = df["answer"].apply(lambda x: make_verbose_version(llm_model, x))

# **Score answers**
df["score"] = df["answer"].apply(lambda x: GPTSCORE(llm_model, x))
```


📁 **Dataset**
The code is designed to work with WikiEval, but can easily be adapted for any question-answer dataset with at least:

question

answer


🪪 **License**
This project is licensed under the MIT License. See the LICENSE file for more details.

🙏 **Acknowledgements**
This work is inspired by recent developments in LLM evaluation such as:

RAGAS (arXiv:2309.15217)

CRScore (NAACL 2025)



