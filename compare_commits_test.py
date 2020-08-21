from selene.support.shared import config, browser
from selene import have, query
from selene.support.shared.jquery_style import s
import ReadParam as Param
from ReadParam import get_param_value


def test_last_commit():
    # Getting Excel file to read parameters
    Param.file_path = './Param.xlsx'
    Param.sheet_name = 'Python'

    # Setting Up browser config
    config.browser_name = get_param_value('BROWSER')
    config.base_url = get_param_value('BASE_URL')
    config.timeout = 2

    # Opening page with commits
    browser.open(get_param_value('COMMIT_URL'))

    # config.window_height = 768
    # config.window_width = 1024

    # Getting text from last commit
    commit = browser.element(
        '//div[contains(@class,"js-navigation-container")]/div[1]//li[1]//p/a') \
        .get(query.attribute('innerText'))

    # Not all commits have their numbers
    if commit.find('#') != -1:
        start = commit.index('#') + 1
        end = commit.index('-', start) - 1
        # Getting current number of last commit
        number = commit[start:end]
        commit = number

    # Opening base URL
    browser.open('/')
    # Comparing commits
    s('//div[@class="Box mb-3"]/div[contains(@class,"Box-header")]//span/a').should(have.text(commit))
    print('Current commit as expected: ' + commit)
