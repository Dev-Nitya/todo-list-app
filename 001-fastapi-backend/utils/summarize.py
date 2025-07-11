from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from utils.llm_initializer import llm

summarize_template_string = """Summarize the following text: {text}"""

prompt = PromptTemplate(
    input_variables=["text"],
    template=summarize_template_string
)

output_parser = StrOutputParser()
summarize_chain = prompt | llm | output_parser