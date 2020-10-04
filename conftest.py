import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language with '--language=language_name' parameter, e.g., '--language=es'")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    language = request.config.getoption("language")
    browser = None
    languages = ["ar", "ca", "cs", "da", "de", "en", "el", "es", "fi", "fr", "it",
                 "ko", "nl", "pl", "pt", "pt-br", "ro", "ru", "sk", "uk", "zh-hans"]
    if language and language in languages:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        print(f"\nStarting browser for testing purposes with {language} language...")
        browser = webdriver.Chrome(options=options)
        yield browser
        print("\nQuitting browser...")
    else:
        raise pytest.UsageError(f"\n--language should be indicated! List of supported languages:"
                                f"\n{languages}")
    browser.quit()
