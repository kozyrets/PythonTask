from selene.support.shared import config, browser
from selene import have
from selene.support.shared.jquery_style import s

config.browser_name = 'chrome'
config.base_url = 'https://github.com/django/django'
config.timeout = 2

browser.open('/commits/master')

# config.window_height = 768
# config.window_width = 1024

# getting text from last commit
commit = browser.element(
    '//div[contains(@class,"js-navigation-container")]/div[1]//li[1]') \
    .get_attribute('innerText')
# not all commits have their numbers
if commit.find('#') != -1:
    start = commit.index('#') + 1
    end = commit.index('-', start) - 1
    # getting current number of last commit
    number = commit[start:end]
    commit = number

browser.open('/')
# comparing commits
s('//div[@class="Box mb-3"]/div[contains(@class,"Box-header")]').should(have.text(commit))
print('Current commit as expected: ' + commit)
