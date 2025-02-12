# Groq LLM Activity Suggestion App

This is a small Python application that allows you to interact with a Large Language Model (LLM) via the Groq API to get interesting ideas for activities. The app uses a simple Retrieval-Augmented Generation (RAG) approach to select the most relevant option from a "knowledge base" and then enriches the response using the LLM.

This project was a fun way to explore new concepts and experiment with Groq's API. Consider it a learning journey rather than a polished product!

The initial idea and base code were taken from [A beginner's guide to building a Retrieval Augmented Generation (RAG) application from scratch](https://learnbybuilding.ai/tutorials/rag-from-scratch).

The project has been significantly modified: a different LLM was integrated, the code was restructured, prompts, corpus and LLMs are easily modifiable.

## Features

- **Integration with Groq API**: Enables communication with the LLM to generate human-like and engaging responses.
- **Simple RAG**: Uses the Jaccard similarity coefficient to select the most relevant option from the knowledge base.
- **Managed via `uv`**: Easy management and running of the application using `uv`.

## Installation

1. Ensure you have Python 3.9 or higher installed.
2. Install the dependencies:
    `uv sync`
3. Make sure you have a Groq API key. Add it to the .env file:
```bash
    GROQ_API_KEY=your_api_key_here
```

## Usage

    Run the application using uv:

    `uv run --env-file=.env src/main.py`
    
    The program prompts you with the question.
    Share what you'd like to do and receive an enriched response from the LLM.

## Knowledge Base

The knowledge base consists of a collection of text files containing ideas and suggestions.
It's located at `data/ideas.txt` and each idea is placed on a new line.
The app uses the Jaccard similarity coefficient to select the most relevant option from this base.

## System prompt

System prompt is located at `data/system_prompt.txt` and it's used as a str-template.
`user_input` and `relevant_document` are used as variables for templating. User input is passed as is, relevant_document will be referring to one of the ideas in the corresponding file.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Credits

- https://console.groq.com/ - Simple yet powerful API for LLM inference
- https://learnbybuilding.ai/tutorials/rag-from-scratch - clear and concise explanation of basic idea behind RAG technique.