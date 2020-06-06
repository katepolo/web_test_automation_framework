from selenium import webdriver


class WebdriverFactory:
    @staticmethod
    def get_webdriver(browser_name):
        if (browser_name == 'firefox'):
            return webdriver.Firefox()
        elif (browser_name == 'chrome'):
            return webdriver.Chrome('C:\\Users\\kpolo\\PycharmProjects\\chromedriver.exe')
        elif (browser_name == 'ie'):
            return webdriver.Ie()
        raise Exception("No such " + browser_name + " browser exists")