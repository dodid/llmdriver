# llmdriver

`llmdriver` is a Python package designed to automate interactions with large language model (LLM) user interfaces, such as ChatGPT, by simulating keyboard and mouse actions. This package is ideal for scenarios requiring repetitive, iterative prompt submissions and response retrievals from LLM-based interfaces. **It works on Mac only**.

## Features

- **Automated Prompt Submission**: Streamline sending prompts to LLM interfaces.
- **Response Handling**: Capture and process responses for further analysis or storage.
- **Customizable Prompt Generation**: Define and manage prompt flows tailored to specific interactions.

## Installation

The package can be installed from source using `pip`:

```bash
$ git clone https://github.com/dodid/llmdriver.git
$ cd llmdriver
$ pip install .
```

## Usage

It uses image matching to locate buttons and text fields on the UI. Only the light theme is supported. Ensure the chat window has a white background before proceeding.

Below is an example of how to use the `ChatGPTAutomator` class to get responses for multiple prompts.

```python
from llmdriver import ChatGPTAutomator, PromptGenerator

# Initialize the automator
automator = ChatGPTAutomator()

# Define a custom prompt generator by inheriting PromptGenerator
class MyPromptGenerator(PromptGenerator):
    def __iter__(self):
        yield "Hello, ChatGPT!"
        yield "How are you today?"

    def handle_response(self, response: str):
        print("Response:", response)

# Instantiate and run with the custom prompt generator
pg = MyPromptGenerator()
automator.run(pg)
```

For a more comprehensive example, check out [apigen.py on GitHub](https://github.com/dodid/ibwebapi/blob/main/tools/apigen.py).

## License

This project is licensed under the [MIT License](LICENSE).
