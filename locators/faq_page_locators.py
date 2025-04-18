from selenium.webdriver.common.by import By

def question_locator(question_text):
    return (By.XPATH, f"//div[text()='{question_text}']")

def answer_locator(question_text):
    return (By.XPATH, f"//div[text()='{question_text}']/../following-sibling::div[@class='accordion__panel']/p")
