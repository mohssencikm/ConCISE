"""
Functions for scoring answers using LLM and calculating compression ratios.
"""

def GPTSCORE(llm_model, answer):
    """
    Returns a conciseness score (0-10) for the given answer.
    """
    result = llm_model.chat_completion(
        model="gpt-4o_v2024-05-13",
        messages=[
            {"role": "system", "content": '''
Conciseness measures how efficiently an answer conveys its intended information. A 
concise answer avoids unnecessary elaboration or redundancy, while fully preserving 
all core facts. Given an answer, assign a score for conciseness in the range 0–10.
Note: Do not provide any other explanations and just give a number.
Do not bring back any summary or concise version of the answer. You task is to evaluate the level of 
Conciseness and your task is to bring back only one number.
answer: 
'''},
            {"role": "user", "content": answer},
        ]
    )
    return result.choices[0].message.content

def calculate_compression_ratio(original_length, summary_length):
    """
    Calculates the compression ratio given original and summary lengths.
    """
    if original_length == 0:
        return 0
    return 1 - ((original_length - summary_length) / original_length)