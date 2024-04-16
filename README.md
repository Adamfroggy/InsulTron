# AIBOT - InsulTRon

AIBOT AKA InsulTron is a simple Python script that interacts with the OpenAI API to create a bot capable of generating sarcastic and rude responses to user prompts.

## Installation

1. Clone the repository:

    git clone https://github.com/yourusername/AIBOT.git


2. Install the required dependencies:

    pip install -r requirements.txt

3. Set up your OpenAI API key:

    - Create a `.env` file in the project directory.
    - Add your OpenAI API key to the `.env` file:

    - `OPENAI_API_KEY`=your_openai_api_key

# License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

# Citation

If you use or find inspiration from this project, please consider citing it using the provided [CITATION](CITATION) file.

## Usage

To use the AIBOT script, run the `main.py` file with Python:

[`python main.py`]
The script will prompt the user for input, and the bot will generate a response based on the input provided.

## Configuration

You can customize the behavior of the bot by modifying the parameters in the bot function within the main.py file. These parameters include the system prompt, temperature, max_tokens, and stop tokens used for generating responses.

## Experimentation

Feel free to experiment with different prompts and parameters to understand their impact on the bot's responses. You can adjust the system prompt, temperature, max_tokens, and stop tokens to achieve different behaviors.

## Refactoring

The bot function can be refactored into a class-based structure or further parameterized to make it more modular and reusable.

## Evaluation

Evaluate the performance of the bot in terms of coherence, relevance, and context-awareness. Test the bot with various prompts and scenarios to assess its capabilities and identify areas for improvement.

## Documentation

Document your design choices, implementation details, and observations in the README.md file to provide context and guidance for users and developers.