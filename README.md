# llmdriver

`llmdriver` is a Python package designed to automate interactions with large language model (LLM) user interfaces, such as ChatGPT, by simulating keyboard and mouse actions. This package is ideal for scenarios requiring repetitive, iterative prompt submissions and response retrievals from LLM-based interfaces.

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

## License

This project is licensed under the [MIT License](LICENSE).
