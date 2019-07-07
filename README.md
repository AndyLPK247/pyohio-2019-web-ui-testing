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
* `example/3-webdriver-calls`
* `example/4-locators`
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

To avoid confusion when we run tests, let's remove the old placeholder test.
Delete `tests/test_fw.py`.

Rerun the tests using `pipenv run python -m pytest`.
The `test_basic_duckduckgo_search` should be the only test that runs,
and it should fail due to the "Incomplete Test" exception.

Finally, commit your code change. Part 1 is complete!

### Part 2: Defining Page Objects

TBD

### Part 3: Making Selenium WebDriver Calls

TBD

### Part 4: Writing Element Locators

TBD
