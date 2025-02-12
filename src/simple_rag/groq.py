from groq import Groq
from typing import Optional


class GroqClient:
    client: Groq
    system_prompt_template: str
    model: str = "deepseek-r1-distill-qwen-32b"

    def __init__(self, model: Optional[str] = None):
        # api_key must be set in env as GROQ_API_KEY
        self.client = Groq()
        self.model = model or self.model

    def set_system_prompt_template(self, template: str):
        self.system_prompt_template = template

    def prompt(self, user_input: str, relevant_document: str) -> str:
        system_prompt = self.system_prompt_template.format(
            user_input=user_input, relevant_document=relevant_document
        )

        chat_completion = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": f"The user input is: {user_input}",
                },
            ],
            model=self.model,
        )

        return chat_completion.choices[0].message.content
