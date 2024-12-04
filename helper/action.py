
def element_click(openDriver, pom):
    openDriver.find_element(pom[0], pom[1]).click()

def validate_is_display(openDriver, pom):
    openDriver.find_element(pom[0], pom[1]).is_displayed()

def element_input(openDriver, pom, text):
    openDriver.find_element(pom[0], pom[1]).send_keys(text)
