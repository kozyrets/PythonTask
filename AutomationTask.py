from selene.support.shared import config, browser
from selene import have
from selene.support.shared.jquery_style import s

config.browser_name = 'chrome'
config.base_url = 'https://github.com/django/django'
config.timeout = 2

browser.open('/commits/master')

config.window_height = 1080
config.window_width = 1920

commit = browser.element(
    '//div[contains(@class,"js-navigation-container")]/div[1]//li[1]//a[contains(@class,"js-navigation-open")]') \
    .text
start = commit.index('#') + 1
end = commit.index('-', start) - 1
number = commit[start:end]

browser.open('/')
s('//div[contains(@class,"Box-header")]//span/a').should(have.text(number))
# print result if test Passed
print('Current commit as expected and = ' + number)
