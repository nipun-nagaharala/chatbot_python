from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file  

print(os.environ.get("OPENAI_API_KEY"))  # Print the API key to verify it's loaded correctly

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

client = OpenAI(api_key=OPENAI_API_KEY)

while True:
    question = input("Enter your question: ")
        if question != "bye":

            response = client.chat.completions.create(
                model="gpt-4o-mini", 
                max_tokens=50,  
                n=1, #number of responses
                temperature=0.7,
                messages=[
                    {"role": "user", "content": question}
                ] 
                )

            print(response)

            for choice in response.choices:
                print("AI : {choice.message.content}")
            else:
                print("AI : Goodbye!")
                break
