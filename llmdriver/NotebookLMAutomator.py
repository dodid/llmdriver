import pyautogui as ui

from llmdriver.llmdriver import LLMAutomator


class NotebookLMAutomator(LLMAutomator):
    inputbox_data_uri = 'data:image/png;base64,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'
    copybtn_data_uri = 'data:image/png;base64,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'
    busysign_data_uri = 'data:image/png;base64,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'

    def __init__(self, silent: bool = False):
        super().__init__(silent=silent)

    def is_response_ready(self) -> bool:
        """Check if the response is ready by confirming the absence of the busy sign."""
        try:
            return ui.locateCenterOnScreen(self.busysign, confidence=0.5) is None
        except ui.ImageNotFoundException:
            return True
