
# LangChain Knowledge Assistant Architecture

## Current Learning Stage

Day 2 — LLM and model-provider fundamentals.

## Initial Model Integration

- Framework: LangChain
- Provider: Google Gemini API
- Integration: langchain-google-genai
- Credential: GOOGLE_API_KEY environment variable

## Initial Request Flow

User input -> LangChain chat model -> Gemini API -> Model response

## Planned RAG Request Flow

User question -> Retriever -> Relevant document passages
-> Prompt and context -> Chat model -> Answer with sources

## Security

- Never commit .env files.
- Keep API keys out of source code.
- Use environment variables for local configuration.
- Validate uploaded documents before processing.
