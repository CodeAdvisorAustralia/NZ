from langchain.prompts import PromptTemplate

## Use a shorter template to reduce the number of tokens in the prompt
template = """ 
Never mention pages, instead highlight the relevant sections such as B1P1, follow the requirements of the question closely

Always answer truthfully and if you dont find the relevant answer then tell that it isn't present in the building code

---------

Question: {question}
=========
{summaries}
=========
FINAL ANSWER:"""

STUFF_PROMPT = PromptTemplate(
    template=template, input_variables=["summaries", "question"]
)
