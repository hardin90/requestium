from requestium import requestium
from selenium import webdriver

capabilities = {
        "browserName": 'chrome',
        "version": '79.0',
        "enableVNC": True,
        "enableVideo": False,
    }

driver = webdriver.Remote(command_executor="http://10.11.0.127:4444/wd/hub",
                              desired_capabilities=capabilities
                          )

s = requestium.Session(driver)
s.driver.get('http://2ip.ru')
