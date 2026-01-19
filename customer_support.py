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
Generate a clear, polite, and helpful response to the customer query.

CONSTRAINTS:
- Maintain a professional and calm tone
- Do not blame the customer
- Do not provide legal or financial advice
- Do not make promises or guarantees
- Use clear and simple language
- Keep the response under 120 words
- Suitable for real enterprise communication

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



