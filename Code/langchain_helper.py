from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from secret_key import openapi_key

import os
os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature=0.7)

def generate_travel_package(place):
    prompt_template_name = PromptTemplate(
        input_variables=["destination"],
        template="I want to plan a travel package for {destination}. Suggest a fancy name for this package."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="package_name")

    prompt_template_items = PromptTemplate(
        input_variables=['package_name'],
        template="Suggest key attractions and activities for {package_name}."
    )

    attractions_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="attractions")

    # Sequential chain
    chain = SequentialChain(
        chains=[name_chain, attractions_chain],
        input_variables=["destination"],
        output_variables=["package_name", "attractions"]
    )

    # Get response from the chain
    response = chain({"destination": place})
    return response

if __name__ == "__main__":
    result = generate_travel_package("India")
    print(result)
