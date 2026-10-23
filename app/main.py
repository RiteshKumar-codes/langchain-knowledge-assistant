
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate


def main():
    # 1. Load environment variables from .env.
    load_dotenv()

    # 2. Check that the API key exists.
    if not os.getenv("GOOGLE_API_KEY"):
        print("Error: GOOGLE_API_KEY is missing.")
        print("Add it to the .env file in the project root.")
        return

    try:
        # 3. Create the Gemini chat model.
        model = ChatGoogleGenerativeAI(
            model="gemini-3.5-flash",
            temperature=0.2,
            max_tokens=400,
        )

        # 4. Define a reusable chat prompt.
        prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                "You are a patient programming tutor. "
                "Explain concepts in {level} language. "
                "Use a definition, a practical example, and "
                "a short summary."
            ),
            (
                "human",
                "Explain {topic}. "
                "Include a simple code example if relevant."
            ),
        ])

        # 5. Provide values for the prompt variables.
        inputs = {
            "level": "beginner-friendly",
            "topic": "Python functions",
        }

        # 6. Inspect the formatted prompt before calling Gemini.
        formatted_prompt = prompt.invoke(inputs)
        print("Formatted messages:")
        for message in formatted_prompt.messages:
            print(f"\n{message.type.upper()}:")
            print(message.content)

        # 7. Connect the prompt to the model.
        chain = prompt | model

        # 8. Invoke the chain with the input values.
        response = chain.invoke(inputs)

        # 9. Print the model's answer.
        print("\n--- Gemini's Answer ---")
        print(response.content)

        # 10. Print token usage when available.
        if response.usage_metadata:
            print("\nToken usage:")
            print(response.usage_metadata)

    except Exception as error:
        print(
            f"Request failed: "
            f"{type(error).__name__}: {error}"
        )


if __name__ == "__main__":
    main()
