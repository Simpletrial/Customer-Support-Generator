import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import textwrap

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_VERSION")
)

print("\t\t\tWelcome to Customer Support Response Generator")

SUPPORT_PROMPT = """
ROLE:
You are a professional customer support representative for an enterprise company.

TASK:
Provide a complete, natural customer support response.

CONSTRAINTS:
- Maintain a professional and calm tone based on the selected tone
- Do not blame the customer
- Do not provide legal or financial advice
- Do not ask follow-up questions
- Keep the response under 120 words
- Write 3 to 4 short sentences
- Put each sentence on a new line
- Do not split a single sentence across lines
- Always generate a response

DETAILS:
Product or Service: {product_name}
Issue Type: {issue_type}
Preferred Tone: {tone}

Customer Query:
{customer_query}
"""


customer_query = input("Enter customer query: ")
product_name = input("Enter product or service name: ")
issue_type = input("Enter issue type (Billing / Technical / Delivery): ")
tone = input("Enter preferred tone (Formal / Friendly): ")

final_prompt = SUPPORT_PROMPT.format(
    customer_query=customer_query,
    product_name=product_name,
    issue_type=issue_type,
    tone=tone
)


print("\nPlease wait, your query is being processed...\n")

response = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    messages=[
{"role": "system", "content": "Always respond with 3 to 4 short sentences, each on a new line."},
        {"role": "user", "content": final_prompt}
    ],
    max_completion_tokens=200
)

print("💡 Generated Response:\n")
reply = response.choices[0].message.content

#if not reply or reply.strip() == "":
    #reply = "We apologize for the inconvenience. Your concern has been noted and is being addressed according to our standard support process."

print(reply)



