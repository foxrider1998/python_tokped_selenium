from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Membuat objek browser
options = webdriver.ChromeOptions()
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=options)

# Menunjuk ke website Tokopedia
driver.get("https://www.tokopedia.com/")
# Menunggu halaman selesai dimuat
time.sleep(1)




# Mencari elemen input search dan mengetikkan kata kunci "smartphone"
search_input =driver.find_element(By.XPATH, '//*[@id="header-main-wrapper"]/div[2]/div[2]/div[1]/div/div/div/input')
search_input.send_keys("smartphone")
search_input.send_keys(Keys.RETURN)

for i in range(10):
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(2)


# Menunggu halaman selesai dimuat
time.sleep(2)

# Mendapatkan jumlah produk
elements_with_same_class = driver.find_elements(By.CSS_SELECTOR, ".css-12sieg3")
print("Jumlah item yang ditampilkan:", len(elements_with_same_class))

# Menutup browser
driver.quit()
