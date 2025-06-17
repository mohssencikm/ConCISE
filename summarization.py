"""
Functions for generating summaries and pruned versions of answers.
"""

def make_summary(llm_model, answer):
    """
    Generates abstractive, extractive, and pruned summaries for the given answer.
    Returns a tuple: (abstractive, extractive, pruned)
    """
    result = llm_model.chat_completion(
        model="bedrock-claude-3-sonnet",
        messages=[
            {"role": "system", "content": '''
Given a question-answer pair, generate three versions of the answer using the following techniques:
1. Abstractive Summary: Create a paraphrased summary that captures the main ideas using new phrasing.
2. Extractive Summary: Select and present the most relevant sentences directly from the original text.
3. Pruned Text: Produce a minimalist version of the original text by removing all non-essential words while preserving the core meaning.
Output your results just as follows and do not provide any other explanations:

1- Summary (abstractive summary); no need to mention this title
2- Summary (extractive summary); no need to mention this title
3- sentence with removed words; no need to mention this title
'''},
            {"role": "user", "content": answer},
        ]
    )
    content = result.choices[0].message.content
    parts = content.split('\n\n')
    # Remove numbering if present
    abstractive = parts[0].replace('1- ', '').strip() if len(parts) > 0 else ''
    extractive = parts[1].replace('2- ', '').strip() if len(parts) > 1 else ''
    pruned = parts[2].replace('3- ', '').strip() if len(parts) > 2 else ''
    return abstractive, extractive, pruned