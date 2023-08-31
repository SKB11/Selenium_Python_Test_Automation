# import pytest
# from selenium import webdriver

# @pytest.fixture(scope="class")
# def setup(request):
#     driver = webdriver.Chrome("executable_path=C:\\Program Files\\chromedriver-win64\\chromedriver.exe") # Replace with your driver path
#     request.cls.driver = driver
#     yield
#     driver.quit()

# @pytest.mark.usefixtures("setup")
# class BaseClass:
#     pass
import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="C:\\Program Files\\chromedriver-win64\\chromedriver.exe")
    request.cls.driver = driver
    yield
    driver.quit()

class BaseClass:
    pass
