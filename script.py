import pandas as pd
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time,keyboard


# Load codes and IDs from excel file
file_path = r"code.xlsx"  
df = pd.read_excel(file_path)

codes,ids = [],[]

for index, row in df.iterrows():
    if not pd.isna(row['Code']):
        codes.append(row['Code'])
    if not pd.isna(row['ID']): 
        ids.append(str(row['ID'])[:-2]) 

# Open Chrome
driver = webdriver.Chrome()

# Navigate to the form
driver.get("https://giftcode.vnggames.com/vn/redeem/452") 

time.sleep(2)  # Wait for page to load


code_text_box = driver.find_element(By.XPATH, "//input[@placeholder='Nhập thông tin code']")
dropdown = driver.find_element(By.XPATH, "//input[@placeholder='Chọn server']")
dropdown.click()
option = driver.find_element(By.XPATH, "//div[text()='S258-Phương Thổ']")
option.click()

id_text_box = driver.find_element(By.XPATH, "//input[@placeholder='Chọn nhân vật / Nhập ID nhân vật']")

for code in codes:
    for id in ids:
        code_text_box.clear()
        code_text_box.send_keys(str(code))

        id_text_box.click() 

        pyautogui.press("tab")
        pyautogui.press("enter")
        id_text_box.send_keys(str(id))
        
        keyboard.wait("enter")
        

# Close browser
driver.quit()