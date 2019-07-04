# pyohio-2019-web-ui-testing
PyOhio 2019: Hands-On Web UI Testing Tutorial

## System Prerequisites
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

## Setup Instructions

1. Clone this repository.
2. Run `cd pyohio-2019-web-ui-testing` to enter the project.
3. Run `pipenv install` to install the dependencies.
4. Run `pipenv run python -m pytest` to verify that the framework can run tests.
5. Create a branch for your code changes. (See *Branching* below.)

## Branching

The `master` branch contains the code for the tutorial's starting point.
The project is basically empty in the `master` branch.

The `example/*` branches contain the completed code for each tutorial chapter.
The name and number of each branch corresponds to the chapter.
If you get stuck, you can always check the example code.
The `example/develop` branch is the main development branch for the examples.

If you want to code along with the tutorial, then create a branch for your work off the `master` branch.
To create your own branch named `tutorial/develop`, run:

    > git checkout master
    > git branch tutorial/develop
    > git checkout tutorial/develop
