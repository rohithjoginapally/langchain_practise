from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain_openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')

# Check if the API key was loaded correctly
if api_key is None:
    raise ValueError("API key not found. Ensure that the .env file is correctly configured and located.")

# Set the API key for OpenAI
os.environ['OPENAI_API_KEY'] = api_key



llm = OpenAI(temperature = 0.6)

def generate_restaurant_name_and_items(cuisine):
    
    # Creating Restaurant Name Chain
    prompt_template_restaurant_name = PromptTemplate(
        input_variables= cuisine,
        template= 'I want to open an {cuisine} Restaurant in Boston, Massachusetts. Can you help me with a quirky name?'
    )

    name_chain = LLMChain(llm = llm, prompt = prompt_template_restaurant_name, output_key= "restaurant_name")

    # Creating Menu Items Chain
    prompt_template_items = PromptTemplate(
        input_variables= ['restaurant_name'],
        template= 'Suggest some menu items for {restaurant_name}. Return it as a Comma Seperated list'
    )

    food_items_chain = LLMChain(llm = llm, prompt = prompt_template_items,output_key= "menu_items")

    chain = SequentialChain(
        chains = [name_chain, food_items_chain],
        input_variables = ["cuisine"],
        output_variables = ['restaurant_name', 'menu_items']
    )

    response = chain(cuisine)
    
    return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Indian"))
