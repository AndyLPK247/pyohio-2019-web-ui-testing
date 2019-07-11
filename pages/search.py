"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

from selenium.webdriver.common.keys import Keys


class DuckDuckGoSearchPage:
  URL = 'https://www.duckduckgo.com'

  # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods

  def load(self):
    self.browser.get(self.URL)

  def search(self, phrase):
    search_input = None   # TODO
    search_input.send_keys(phrase + Keys.RETURN)
