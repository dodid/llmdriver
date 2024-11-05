import base64
import os
import time
from abc import ABC, abstractmethod
from io import BytesIO

import pyautogui as ui
import pyperclip
from PIL import Image
from tqdm import tqdm


class PromptGenerator:
    def __iter__(self):
        pass

    def handle_response(self, response: str):
        print(response)


class LLMAutomator(ABC):
    inputbox_data_uri = ''
    copybtn_data_uri = ''
    busysign_data_uri = ''

    def __init__(self, silent: bool = False):
        self.silent = silent
        self.input_pos = None
        self.inputbox = Image.open(BytesIO(base64.b64decode(self.inputbox_data_uri.split(",")[1])))
        self.copybtn = Image.open(BytesIO(base64.b64decode(self.copybtn_data_uri.split(",")[1])))
        self.busysign = Image.open(BytesIO(base64.b64decode(self.busysign_data_uri.split(",")[1])))

    def is_prompt_sent(self) -> bool:
        """Check if the prompt has been sent successfully by verifying the presence of the input box."""
        try:
            return ui.locateCenterOnScreen(self.inputbox, confidence=0.9) is not None
        except ui.ImageNotFoundException:
            return False

    @abstractmethod
    def is_response_ready(self) -> bool:
        """Check if the response is ready by looking for the busy sign."""
        pass

    def say(self, text: str):
        if not self.silent:
            os.system(f"say {text}")
        else:
            time.sleep(1)

    def send_prompt(self, text: str):
        """Send the prompt and wait until it's confirmed to be sent."""
        self.say("Sending prompt")
        ui.click(self.input_pos.x // 2, self.input_pos.y // 2)
        pyperclip.copy(text)
        ui.hotkey('command', 'v')
        if self.is_prompt_sent():
            self.say("Prompt input not detected, stopping")
            exit(1)
        ui.click(self.input_pos.x // 2, self.input_pos.y // 2)
        ui.press('enter')
        time.sleep(1)
        while not self.is_prompt_sent():
            self.say("Prompt not sent, retrying")
            for _ in range(2):
                time.sleep(1)
        self.say("Prompt sent")

    def get_response(self) -> str:
        """Get the response from the interface once it's ready."""
        while not self.is_response_ready():
            self.say("Waiting for response")
            for _ in range(5):
                time.sleep(1)
        try:
            # find the last copy button
            box = list(ui.locateAllOnScreen(self.copybtn, confidence=0.8))[-1]
            ui.click((box.left + box.width // 2) // 2, (box.top + box.height // 2) // 2)
            return str(pyperclip.paste())
        except ui.ImageNotFoundException:
            self.say("Copy button not found, stopping")
            exit(1)

    def run(self, pg: 'PromptGenerator'):
        self.say("Bring up the chat window to start")
        self.say("3")
        self.say("2")
        self.say("1")
        try:
            self.input_pos = ui.locateCenterOnScreen(self.inputbox, confidence=0.9, minSearchTime=5)
            self.say("Ready")
        except ui.ImageNotFoundException:
            self.say("Input box not found, stopping")
            exit(1)
        for prompt in tqdm(pg, total=len(pg)):
            self.send_prompt(prompt)
            pg.handle_response(self.get_response())
        self.say("Done")


