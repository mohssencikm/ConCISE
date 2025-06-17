"""
Functions for generating verbose versions of answers.
"""

def make_verbose_version(llm_model, answer):
    """
    Generates a verbose version of the given answer using the LLM.
    """
    result = llm_model.chat_completion(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": '''
You are a language model that verbosely rewrites answers without changing their meaning.
You will be given an original concise answer. Your task is to rewrite it in a verbose manner while preserving all its facts and meaning. Do NOT add any new information that isn’t in the original answer, and do not omit any details. Keep all names, dates, and specific terms exactly the same as in the original. The goal is to make the answer much longer by being redundant and extremely detailed, without altering the truthfulness or intent of the content.

Guidelines for the verbose answer:
- Use a redundant, elaborative writing style. You should significantly expand on the original text (aim for at least 2× the word count of the original or more).
- You may rephrase key points in multiple ways, add clarifications of what terms or statements mean, and insert filler phrases that reinforce the same points. It should sound like a very detailed explanation of the original answer.
- Do not introduce new facts, examples, or any content that isn’t derived from the original answer. The core facts must remain identical.
- Ensure the verbose answer remains coherent and on-topic, even if it repeats itself. It should be clear that it addresses the same question as the original.
- The verbose answer should NOT contain any extra explanations from you, for instance, do not use "here is the verbose version...", or "sure here is the results", or "Here is a verbose rewriting of the original answer:" and so on. It only contains the verbose version of the original answer.
Now, perform the task on the given answer:'''},
            {"role": "user", "content": answer},
        ]
    )
    return result.choices[0].message.content
