"""
Functions for ranking answers using LLM.
"""

def GPTRanking(llm_model, question, answer1, answer2):
    """
    Returns 'answer 1' or 'answer 2' depending on which is more concise.
    """
    result = llm_model.chat_completion(
        model="gpt-4o_v2024-05-13",
        messages=[
            {"role": "system", "content": '''
Conciseness measures how efficiently an answer conveys its intended information. A concise answer avoids unnecessary elaboration or redundancy, while fully preserving all core facts. Given a question and two answers, choose the more concise one.
Note: Only reply with "answer 1" or "answer 2". Do not provide any other explanation.
'''},
            {"role": "user", "content": f'''question: {question}
answer 1: {answer1}
answer 2: {answer2}
'''},
        ]
    )
    return result.choices[0].message.content