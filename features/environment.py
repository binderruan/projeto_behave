from selenium import webdriver

def before_all(context):
    print("Começou")
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    context.driver = webdriver.Chrome(options=options)


def before_scenario(context, scenario):
    context.driver.maximize_window()
    context.driver.implicitly_wait(20)

def after_all(context):
    context.driver.quit()

