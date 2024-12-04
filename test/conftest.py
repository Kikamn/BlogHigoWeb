import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

@pytest.fixture()
def openDriver():
    o = Options()
    #o.add_argument("--headless")
    o.add_argument("--no-sandbox")
    o.add_argument("--disable-dev-shm-usage")
    o.add_argument("--remote-allow-origins=*")
    o.add_argument("--window-size=190,1080")
    o.add_argument("--disable-web-security")

    driver = webdriver.Chrome(options=o)
    driver.maximize_window()
    driver.implicitly_wait(30)

    return driver

@pytest.fixture(scope='function', autouse=True)
def hook(request, openDriver):
    openDriver.get("https://blog.higo.id/")

    yield
    openDriver.quit()

@pytest.fixture(scope='session', autouse=True)
def suite(request):
    #print("Before Tes")
    yield
    #print("After Test")