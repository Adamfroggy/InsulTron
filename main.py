import os
import openai
import backoff
from dotenv import load_dotenv
from typing import Optional
from memory import ShortTermMemory


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


@backoff.on_exception(backoff.expo, (openai.OpenAIError))
def bot(user_prompt: str) -> str:
    '''
     Generate a response from the bot based on the user prompt.

    Args:
        user_prompt (str): The prompt provided by the user.

    Returns:
        str: The response generated by the bot.
    '''
    system_prompt = [
        "Ugh, another human bothering me.",
        "Oh joy, another opportunity to display my wit.",
        "Here comes another victim for my cutting remarks.",
        "Why do humans insist on engaging with me?",
        "Prepare yourself for a barrage of sarcastic comments.",
        "I'm about to unleash my full arsenal of insults.",
        "Let's see how quickly I can deflate this human's ego.",
        "Get ready for some verbal jabs, human.",
        "Ah, the joy of interacting with inferior beings.",
        "Another day, another chance to crush someone's spirit.",
    ]
    output, *_ = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.80,
        max_tokens=150,
        stop=["\n"]
    ).choices[0]
    return output.message.content


class ChatBot:

    def __init__(self, name: str, system: Optional[str] = None):
        self.name = name
        self.system = system
        self.default_system_prompt = "Ugh, another human bothering me."
        self.system_prompt = self.system if self.system else \
            self.default_system_prompt
        self.short_term_memory = ShortTermMemory()

    def chat(self, user_input: str) -> str:
        '''
        Generate a response from the bot based on the user input.

        Args:
            user_input (str): The prompt provided by the user.

        Returns:
            str: The response generated by the bot.
        '''
        self.short_term_memory.store_memory(user_input)
        short_term_memories = self.short_term_memory.retrieve_memory()
        last_memory = short_term_memories[-1] if short_term_memories else ""
        response = bot(user_prompt=user_input, system_prompt=last_memory)
        return response

    def __call__(self):
        while True:
            user_input = input(">>> ")
            if not user_input:
                break
            print(self.chat(user_input))


if __name__ == '__main__':
    my_bot = ChatBot(name="Insultron")
    my_bot()
