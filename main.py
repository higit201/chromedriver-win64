from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# ✅ Paths (update these)
chrome_binary_path = r"C:\Users\dellb\Downloads\chrome-win64\chrome.exe"
chromedriver_path = r"C:\Users\dellb\Downloads\chromedriver-win64\chromedriver.exe"

# ✅ Set Chrome options
options = Options()
options.binary_location = chrome_binary_path

# 🔒 Safe settings to prevent crash
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugging-port=9222")

# Optional: Run headless if you don’t need UI
# options.add_argument("--headless=new")

# ✅ Launch ChromeDriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

# ✅ Test
driver.get("https://www.google.com")
print(driver.title)
driver.quit()
