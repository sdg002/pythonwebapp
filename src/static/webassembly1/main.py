import logging
import arrr
from pyscript import document, Event

logging.basicConfig(level=logging.DEBUG)


def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = arrr.translate(english)


def translate_english_submit(event: Event):
    event.preventDefault()
    logging.debug("Submit button clicked")
    input_text_element = document.querySelector("#english1")
    english = input_text_element.value
    logging.debug(f"Submit button clicked {english}")
    output_div = document.querySelector("#output1")
    output_div.innerText = arrr.translate(english)
    return True
