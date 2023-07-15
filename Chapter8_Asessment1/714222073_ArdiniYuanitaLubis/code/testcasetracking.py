import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SystemTest(unittest.TestCase):
    def setUp(self):
        # Inisialisasi WebDriver
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Tambahkan penundaan waktu sebelum menutup WebDriver
        time.sleep(5)
        # Menutup WebDriver
        self.driver.quit()

    def test_search_google(self):
        # Membuka halaman web Google
        self.driver.get("https://www.posindonesia.co.id/en/tracking")  

        # Mencari elemen input pencarian menggunakan ID
        search_input = self.driver.find_element(By.ID, "resi")

        # Memasukkan kata kunci pencarian
        search_input.send_keys("P2111130018330")

        # Menekan tombol Enter untuk melakukan pencarian
        search_input.send_keys(Keys.ENTER)

        # Memastikan halaman hasil pencarian muncul
        search_results = self.driver.find_elements(By.XPATH, "//div[@class='g']")
        self.assertTrue(len(search_results) > 0, "Hasil pencarian ditemukan")


if __name__ == "__main__":
    unittest.main()
