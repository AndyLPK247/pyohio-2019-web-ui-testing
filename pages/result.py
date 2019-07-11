"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""


class DuckDuckGoResultPage:
  
  # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods

  def result_count_for_phrase(self, phrase):
    results = None   # TODO
    return len(results)
  
  def search_input_value(self):
    search_input = None   # TODO
    return search_input.text

  def title(self):
    return self.browser.title
