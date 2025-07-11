from langchain.prompts import PromptTemplate
from utils.llm_initializer import llm

write_poem_template_string = """Write a poem about the following topic: {topic}"""

prompt = PromptTemplate(
    input_variables=["topic"],
    template=write_poem_template_string
)

poem_chain = prompt | llm
