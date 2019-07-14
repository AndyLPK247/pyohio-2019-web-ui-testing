# pyohio-2019-web-ui-testing
This repository contains the companion project for the PyOhio 2019 *Hands-On Web UI Testing* tutorial.
If you are taking the tutorial, then please clone this repository and follow the instructions below.

## Project Setup

### System Prerequisites
You can complete this tutorial using any OS: Windows, macOS, Linux, etc.

This tutorial requires Python 3.6 or higher.
You can download the latest Python version from [Python.org](https://www.python.org/downloads/).

This tutorial also requires [pipenv](https://docs.pipenv.org/).
To install pipenv, run `pip install pipenv` from the command line.

You should also have a Python editor/IDE of your choice.
Good choices include [PyCharm](https://www.jetbrains.com/pycharm/)
and [Visual Studio Code](https://code.visualstudio.com/docs/languages/python).

For Web UI testing, you will need to install the latest version of [Google Chrome](https://www.google.com/chrome/).
You can use other browsers with Selenium WebDriver,
but the tutorial will use [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/) for finding Web element locators.
Make sure your version of Chrome is up-to-date.
You can update Chrome under *Help* > *About Google Chrome*.

You will also need the latest version of [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/).
ChromeDriver will act as a proxy between our test automation code and the Chrome browser instance.
Make sure the version of ChromeDriver matches the version of Chrome, or else problems may happen.
The ChromeDriver executable must also be on your [system path](https://en.wikipedia.org/wiki/PATH_(variable)).
Please ask if you need help with this configuration.

You will also need [Git](https://git-scm.com/) to copy this project code.
If you are new to Git, [try learning the basics](https://try.github.io/).

### Setup Instructions

1. Clone this repository.
2. Run `cd pyohio-2019-web-ui-testing` to enter the project.
3. Run `pipenv install` to install the dependencies.
4. Run `pipenv run python -m pytest` to verify that the framework can run tests.
5. Create a branch for your code changes. (See *Branching* below.)

### Branching

The `master` branch contains the code for the tutorial's starting point.
The project is basically empty in the `master` branch.

If you want to code along with the tutorial, then create a branch for your work off the `master` branch.
To create your own branch named `tutorial/develop`, run:

    > git checkout master
    > git branch tutorial/develop
    > git checkout tutorial/develop

The `example/*` branches contain the completed code for tutorial parts.
If you get stuck, you can always check the example code.

* `example/1-first-test`
* `example/2-page-objects`
* `example/3-webdriver-setup`
* `example/4-webdriver-calls`
* `example/develop` (main development branch for the examples)

## Tutorial Instructions

### Part 1: Writing Our First Test

*Time Estimate: 5 Minutes*

We should always write test *cases* before writing any test *code*.
Test cases are procedures that exercise behavior to verify goodness and identify badness.
Test code simply automates test cases.
Writing a test case first helps us form our thoughts well.

Consider the following test case:

```gherkin
Scenario: Basic DuckDuckGo Search
    Given the DuckDuckGo home page is displayed
    When the user searches for “panda”
    Then the search result title contains “panda”
    And the search result query is “panda”
    And the search result links pertain to “panda”
```

Let's implement this test using pytest.
Create a new file named `test_search.py` under the `tests` directory,
and add the following code:

```python
"""
These tests cover DuckDuckGo searches.
"""

def test_basic_duckduckgo_search():

    # Given the DuckDuckGo home page is displayed
    # TODO

    # When the user searches for "panda"
    # TODO

    # Then the search result title contains "panda"
    # TODO
    
    # And the search result query is "panda"
    # TODO
    
    # And the search result links pertain to "panda"
    # TODO

    raise Exception("Incomplete Test")
```

Adding comments to stub each step may seem trivial,
but it's a good first step when writing new test cases.
We can simply add code at each TODO line as we automate.
Once the test is completed, we will remove the exception at the end.
Also, note that pytest expects all test functions to begin with `test_`.

To avoid confusion when we run tests, let's remove the old placeholder test.
Delete `tests/test_fw.py`.

Rerun the tests using `pipenv run python -m pytest`.
The `test_basic_duckduckgo_search` should be the only test that runs,
and it should fail due to the "Incomplete Test" exception.

Finally, commit your code change. Part 1 is complete!

### Part 2: Defining Page Objects

*Time Estimate: 10 Minutes*

A **page object** is an object representing a Web page or component.
They have *locators* for finding elements,
as well as *interaction methods* that interact with the page under test.
Page objects make low-level Selenium WebDriver calls
so that tests can make short, readable calls instead of complex ones.

Since we have our test steps, we know what pages and elements our test needs.
There are two pages under test, each with a few interactions:

1. The DuckDuckGo search page
   * Load the page
   * Search a phrase
2. The DuckDuckGo results page
   * Get the results
   * Get the search query
   * Get the title

Understanding interactions with the Web app is more important than the code.
We can write stubs for page object classes as we figure out the interactions.

Create a new Python package named `pages`.
To do this create a directory under the root directory named `pages`.
Then, put a blank file in it named `__init__.py`.
The `pages` directory shoult *not* be under the `tests` directory.
Why? When using pytest, the `tests` folder should *not* be a package.

Create a new module named `pages/search.py` and add the following code
for the DuckDuckGo search page:

```python
"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""


class DuckDuckGoSearchPage:

  def load(self):
    # TODO
    pass

  def search(self, phrase):
    # TODO
    pass
```

Create another new module named `pages/result.py` and add the following code
for the DuckDuckGo result page:

```python
"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""


class DuckDuckGoResultPage:
  
  def result_count_for_phrase(self, phrase):
    # TODO
    return 0
  
  def search_input_value(self):
    # TODO
    return ""

  def title(self):
    # TODO
    return ""
```

Finally, update `test_basic_duckduckgo_search` in `tests/test_search.py`
with the following code:

```python
"""
These tests cover DuckDuckGo searches.
"""

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


def test_basic_duckduckgo_search():
  search_page = DuckDuckGoSearchPage()
  result_page = DuckDuckGoResultPage()
  PHRASE = "panda"
  
  # Given the DuckDuckGo home page is displayed
  search_page.load()

  # When the user searches for "panda"
  search_page.search(PHRASE)

  # Then the search result title contains "panda"
  assert PHRASE in result_page.title()
  
  # And the search result query is "panda"
  assert PHRASE == result_page.search_input_value()
  
  # And the search result links pertain to "panda"
  assert result_page.result_count_for_phrase(PHRASE) > 0

  # TODO: Remove this exception once the test is complete
  raise Exception("Incomplete Test")
```

Notice how we are able to write all the test steps using page object calls and assertions.
We also kept the step comments so the code is well-documented.
Even though we haven't made any Selenium WebDriver calls, our test case function is nearly complete!
Our code is readable and understandable.
It delivers clear testing value.

Rerun the test using `pipenv run python -m pytest`.
The test should fail again, but this time, it should fail on one of the assertions.
Then, commit your latest code changes. Part 2 is now complete!

### Part 3: Setting Up Selenium WebDriver

*Time Estimate: 10 Minutes*

[Selenium WebDriver](https://www.seleniumhq.org/projects/webdriver/)
is a tool for automating Web UI interactions with live browsers.
It works with several popular programming languages and browser types.

The Selenium WebDriver package for Python is named `selenium`.
Run `pipenv install selenium` to install it for our project.

Every test should use its own WebDriver instance.
This keeps things simple and safe.
The best way to set up the WebDriver instance is using a
[pytest fixture](https://docs.pytest.org/en/latest/fixture.html).
Fixtures are basically setup and cleanup functions.
As a best practice, they should be placed in a `conftest.py` module so they can be used by any test.

Create a new file named `tests/conftest.py` and add the following code:

```python
"""
This module contains shared fixtures.
"""

import pytest
import selenium.webdriver


@pytest.fixture
def browser():

  # Initialize the ChromeDriver instance
  b = selenium.webdriver.Chrome()

  # Make its calls wait up to 10 seconds for elements to appear
  b.implicitly_wait(10)

  # Return the WebDriver instance for the setup
  yield b

  # Quit the WebDriver instance for the cleanup
  b.quit()
```

Our fixture uses Chrome as the browser.
Other browser types could be used.
Real-world projects often read browser choice from a config file here.

The implicit wait will make sure WebDriver calls wait for elements to appear before sending calls to them.
10 seconds should be reasonable for our test project's needs.
For larger projects, however, setting explicit waits is a better practice
because different calls need different wait times.
Read more about implicit versus explicit waits [here](https://selenium-python.readthedocs.io/waits.html).

The `yield` statement makes the `browser` fixture a generator.
The first iteration will do the "setup" steps,
while the second iteration will do the "cleanup" steps.
Always make sure to *quit* the WebDriver instance as part of cleanup,
or else zombie processes might lock system resources!

Now, update `test_basic_duckduckgo_search` in `tests/test_search.py` to call the new fixture:

```python
def test_basic_duckduckgo_search(browser):
  search_page = DuckDuckGoSearchPage(browser)
  result_page = DuckDuckGoResultPage(browser)
  # ...
```

Every page object needs a reference to the WebDriver instance.
Update the page object classes to have `__init__` methods.

In `pages/search.py`:

```python
class DuckDuckGoSearchPage:

  def __init__(self, browser):
    self.browser = browser

  # ...
```

And in `pages/result.py`:

```python
class DuckDuckGoResultPage:
  
  def __init__(self, browser):
    self.browser = browser

  # ...
```

Rerun the test using `pipenv run python -m pytest` to test the fixture.
Even though the test should still fail,
Chrome should briefly pop up for a few seconds while the test is running.
Make sure Chrome quits once the test is done.
Then, commit your latest code changes.
Part 3 is now complete!

### Part 4: Making WebDriver Calls

*Time Estimate: 15 Minutes*

Now we can implement all the page object methods using WebDriver calls.
The [WebDriver API for Python](https://selenium-python.readthedocs.io/api.html)
documents all WebDriver calls.
If you aren't sure how to do something, look it up.
WebDriver can do anything a user can do on a Web page!

Let's start with `DuckDuckGoSearchPage`.
The `load` method is a one-line WebDriver call,
but it's good practice to make the URL a class variable:

```python
URL = 'https://www.duckduckgo.com'

def load(self):
  self.browser.get(self.URL)
```

The `search` method is a bit more complex because it interacts with an element.
We need to use a *locator* to find the search input element,
and then we need to *send keys* to type the search phrase into the element.

First, import some key pieces from the `selenium` package:

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
```

Then, write a locator for the search input element.
If we inspect the page's HTML, we can see that the search element has a "name" attribute set to "q".
Therefore, we can use the `By.NAME` locator to find the element like this:

```python
SEARCH_INPUT = (By.NAME, 'q')
```

It's good practice to write locators as page object class variables.
That way, the locator can be reused by multiple page object methods.
It is also good to write them as tuples - and we will see why next.

The `search` method needs two parts: finding the element and sending the keystrokes:

```python
def search(self, phrase):
  search_input = self.browser.find_element(*self.SEARCH_INPUT)
  search_input.send_keys(phrase + Keys.RETURN)
```

The `find_element` method will return the first element found by the locator.
Notice how the locator uses the `*` operator to expand the tuple into arguments.
The `selenium` package offers specific locator type methods (like `find_element_by_name`),
but using the generic `find_element` method with argument expansion is better practice.
If the locator type must be changed due to Web page updates,
then the `find_elements` call would not need to be changed.

The `send_keys` call sends the search phrase passed into the `search` method.
This means that the page object can search any phrase!
The addition of `Keys.RETURN` will send the ENTER/RETURN key as well,
which will submit the input value to perform the search and load the results page.

The full code for `pages/search.py` should look like this:

```python
"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoSearchPage:

  # URL

  URL = 'https://www.duckduckgo.com'

  # Locators

  SEARCH_INPUT = (By.NAME, 'q')

  # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods

  def load(self):
    self.browser.get(self.URL)

  def search(self, phrase):
    search_input = self.browser.find_element(*self.SEARCH_INPUT)
    search_input.send_keys(phrase + Keys.RETURN)
```

Now, let's do `DuckDuckGoResultPage`.
The `title` method is the easiest one because it just returns a property value:

```python
def title(self):
  return self.browser.title
```

The `search_input_value` method is similar to the `search` method from `DuckDuckGoSearchPage`,
but instead of sending a command, it asks for state from the page.
Thankfully, it uses the same locator.
(The "value" attribute contains the text a user types into an "input" element.)

```python
from selenium.webdriver.common.by import By

SEARCH_INPUT = (By.NAME, 'q')

def search_input_value(self):
  search_input = self.browser.find_element(*self.SEARCH_INPUT)
  return search_input.get_attribute('value')
```

The `result_count_for_phrase` method is the most complex.
The test must verify that the result page displays links relating to the search phrase.
This method should find all result links that contain the search phrase in their display texts.
Then, it should return the count.
The test asserts that the count is greater than zero.
This assertion may seem weak because it could allow some results to be unrelated to the phrase,
but it is good enough for the nature of a basic search test.
(A more rigorous test could and should more carefully cover search result goodness.)

How can we write a locator that finds elements based on text?
We can use XPath:

```python
@classmethod
def PHRASE_RESULTS(cls, phrase):
  xpath = f"//div[@id='links']//*[contains(text(), '{phrase}')]"
  return (By.XPATH, xpath)
```

`PHRASE_RESULT` is a method because the phrase is a parameter for the XPath.
It still returns a tuple so that it can work like other locators.

The `result_count_for_phrase` method uses it like this:

```python
def result_count_for_phrase(self, phrase):
  results = self.browser.find_elements(*self.PHRASE_RESULTS(phrase))
  return len(results)
```

The full code for `pages/result.py` should look like this:

```python
"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""

from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:
  
  # Locators

  SEARCH_INPUT = (By.NAME, 'q')

  @classmethod
  def PHRASE_RESULTS(cls, phrase):
    xpath = f"//div[@id='links']//*[contains(text(), '{phrase}')]"
    return (By.XPATH, xpath)

  # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods

  def result_count_for_phrase(self, phrase):
    results = self.browser.find_elements(*self.PHRASE_RESULTS(phrase))
    return len(results)
  
  def search_input_value(self):
    search_input = self.browser.find_element(*self.SEARCH_INPUT)
    return search_input.get_attribute('value')

  def title(self):
    return self.browser.title
```

Finally, remove the "incomplete" exception from `tests/test_search.py`.
That module's code should look like this:

```python
"""
These tests cover DuckDuckGo searches.
"""

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


def test_basic_duckduckgo_search(browser):
  search_page = DuckDuckGoSearchPage(browser)
  result_page = DuckDuckGoResultPage(browser)
  PHRASE = "panda"

  # Given the DuckDuckGo home page is displayed
  search_page.load()

  # When the user searches for "panda"
  search_page.search(PHRASE)

  # Then the search result title contains "panda"
  assert PHRASE in result_page.title()
  
  # And the search result query is "panda"
  assert PHRASE == result_page.search_input_value()
  
  # And the search result links pertain to "panda"
  assert result_page.result_count_for_phrase(PHRASE) > 0
```

Rerun the test using `pipenv run python -m pytest`.
Now, finally, it should run to completion and pass!
The test will take a few second to run because it must wait for page loads.
Chrome should pop up and automatically go though all test steps.
Try not to interfere with the browser as the test runs.
Make sure pytest doesn't report any failures when it completes.

Congrats! You have completed the guided part of this tutorial!

## Independent Exercises

TBD
