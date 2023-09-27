from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application



def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    # service = Service(executable_path=r'C:\Users\varsi\python-selenium-automation\chromedriver.exe')
    # context.driver = webdriver.Chrome(service=service)

    ### OTHER BROWSERS ###
    # service = Service(executable_path=r'C:\Users\varsi\python-selenium-automation\geckodriver.exe')
    # context.driver = webdriver.Firefox(service=service)
    # context.driver = webdriver.Safari()

    ### HEADLESS MODE ###
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # service = Service(executable_path=r'C:\Users\varsi\python-selenium-automation\chromedriver.exe')
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ### BROWSERSTACK ###
    bs_user = 'vladarsiriy_8uLida'
    bs_key = 'zm6PCPzbGTuRNMdyjo2L'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        'os': 'Windows',
        'osVersion': '10',
        'browserName': 'Firefox',
        'sessionName': scenario_name
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)


    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
