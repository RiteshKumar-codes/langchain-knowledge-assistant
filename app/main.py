
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


def main():
    load_dotenv()

    if not os.getenv("GOOGLE_API_KEY"):
        print("Error: GOOGLE_API_KEY is missing.")
        print("Add it to the .env file in the project root.")
        return

    try:
        model = ChatGoogleGenerativeAI(
            model="gemini-3.5-flash",
            temperature=0.2,
            max_tokens=1200
        )

        question = "Give me three beginner project ideas using LangChain."

        print("Question:", question)
        print("\nGenerating answer...\n")

        response = model.invoke(question)

        print("Answer:")

        if isinstance(response.content, str):
           print(response.content)
        else:
           for block in response.content:
            if block.get("type") == "text":
               print(block.get("text", ""))

        if response.usage_metadata:
            print("\nToken usage:")
            print(response.usage_metadata)

    except Exception as error:
        print(
            f"Model request failed: "
            f"{type(error).__name__}: {error}"
        )


if __name__ == "__main__":
    main()
