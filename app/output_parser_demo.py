
import os
import json

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import (
    StrOutputParser,
    JsonOutputParser,
)


def main():
    # 1. Load configuration from the project-root .env file.
    load_dotenv()

    # 2. Check for the Gemini API key.
    if not os.getenv("GOOGLE_API_KEY"):
        print("Error: GOOGLE_API_KEY is missing.")
        return

    try:
        # 3. Initialize the Gemini chat model.
        model = ChatGoogleGenerativeAI(
            model="gemini-3.5-flash",
            temperature=0.2,
            max_tokens=1000,
        )

        # 4. Demonstrate the plain-text output parser.
        text_prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                "You are a patient programming tutor."
            ),
            (
                "human",
                "Explain {topic} in three short bullet points."
            ),
        ])

        text_chain = text_prompt | model | StrOutputParser()

        text_answer = text_chain.invoke({
            "topic": "Python functions"
        })

        print("=== PLAIN TEXT OUTPUT ===")
        print(text_answer)
        print("Python type:", type(text_answer).__name__)

        # 5. Create a JSON output parser.
        json_parser = JsonOutputParser()

        # 6. Add the parser's formatting instructions to the prompt.
        json_prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                "You are a programming tutor. "
                "Return information about programming topics. "
                "Follow these output format instructions:\n"
                "{format_instructions}"
            ),
            (
                "human",
                "Give three beginner-friendly project ideas "
                "for {topic}. Each project must have a name "
                "and a short description."
            ),
        ])

        # 7. Connect the prompt, model, and parser.
        json_chain = json_prompt | model | json_parser

        # 8. Supply all required template variables.
        json_inputs = {
            "topic": "Python",
            "format_instructions": (
                json_parser.get_format_instructions()
            ),
        }

        # 9. Invoke the chain to get parsed Python data.
        result = json_chain.invoke(json_inputs)

        print("\n=== STRUCTURED JSON OUTPUT ===")
        print(json.dumps(result, indent=2, ensure_ascii=False))
        print("Python type:", type(result).__name__)

        # 10. Access individual fields.
        projects = result.get("projects", [])

        print("\n=== PROJECT NAMES ===")
        for project in projects:
            print("-", project.get("name", "Unnamed project"))

    except Exception as error:
        print(
            f"Request failed: {type(error).__name__}: {error}"
        )


if __name__ == "__main__":
    main()
