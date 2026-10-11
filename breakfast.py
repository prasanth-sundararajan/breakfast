from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

# Exact instructions to follow the formatting constraints
prompt = (
    "Provide exactly 5 healthy breakfast ideas. "
    "Format as a numbered list from 1 to 5, exactly one line per idea, "
    "with no preamble, introduction, or concluding remarks."
)

reply = llm.invoke(prompt)

# Print ONLY the text content, not the object
print(reply.content)