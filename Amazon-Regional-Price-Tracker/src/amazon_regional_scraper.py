from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
import time
from datetime import date
import datetime

# -----------------------------
# CONFIGURATION
# -----------------------------
TARGET_PINCODE = ""  # ENTER YOUR TARGET PINCODE (e.g., "560068" for Bangalore)
PRODUCT_ASINS = []   # ADD YOUR ASIN LIST HERE (e.g., ["B07X3HVQQ4", "B0BCSVTZNT"])

# -----------------------------
# CHANGE PINCODE FUNCTION
# -----------------------------
def change_pincode(driver, pincode):
    """
    Simulates a user changing their delivery location on Amazon.in.
    This is crucial for seeing regional pricing and Buybox winners.
    """
    if not pincode:
        print("No pincode provided. Skipping location change.")
        return

    driver.get("https://www.amazon.in/")
    wait = WebDriverWait(driver, 10)

    try:
        # Click the location button
        location_button = wait.until(EC.element_to_be_clickable((By.ID, "nav-global-location-popover-link")))
        location_button.click()
        time.sleep(2)

        # Enter the new pincode
        pincode_input = wait.until(EC.presence_of_element_located((By.ID, "GLUXZipUpdateInput")))
        pincode_input.clear()
        pincode_input.send_keys(pincode)
        time.sleep(1)

        # Submit
        apply_button = driver.find_element(By.ID, "GLUXZipUpdate")
        apply_button.click()
        time.sleep(2)

        # Handle confirm/continue button if it appears
        try:
            continue_button = driver.find_element(By.CSS_SELECTOR, "span.a-button-inner > input.a-button-input")
            continue_button.click()
        except:
            pass

        time.sleep(3)
        print(f"Pincode successfully set to: {pincode}")

    except Exception as e:
        print(f"Error changing pincode to {pincode}: {e}")

# -----------------------------
# MAIN SCRAPER LOGIC
# -----------------------------
def run_scraper():
    if not PRODUCT_ASINS:
        print("ASIN list is empty. Please add ASINs to the PRODUCT_ASINS list.")
        return

    chrome_options = Options()
    
    # Standard stable configuration
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # TROUBLESHOOTING: If you encounter hardware acceleration issues or crashes, 
    # you can try adding these flags:
    # chrome_options.add_argument('--enable-unsafe-webgpu')
    # chrome_options.add_argument('--enable-unsafe-swiftshader')

    today_date = date.today().strftime('%Y-%m-%d')
    excel = openpyxl.Workbook()
    sheet = excel.active
    sheet.title = f"PriceReport_{today_date}"
    
    # Output Columns: ASIN, Price, Buybox Winner, Deal Tags
    sheet.append(['ASIN', 'Price', 'Buybox Winner', 'Deal Tags'])

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Set regional context (Bangalore, Delhi, etc.)
        change_pincode(driver, TARGET_PINCODE)

        base_url = "https://www.amazon.in/dp/"

        for asin in PRODUCT_ASINS:
            print(f"Scraping ASIN: {asin}")
            driver.get(f"{base_url}{asin}")
            time.sleep(3)

            # Check for Availability
            try:
                checker_tag = driver.find_element(By.CSS_SELECTOR, 'span.a-size-medium.a-color-success')
                is_unavailable = 'currently unavailable' in checker_tag.text.strip().lower()
            except:
                is_unavailable = False

            if is_unavailable:
                sheet.append([asin, 0, "Currently unavailable", "N/A"])
            else:
                try:
                    price = driver.find_element(By.CLASS_NAME, 'a-price-whole').text
                    
                    try:
                        buybox = driver.find_element(By.ID, 'sellerProfileTriggerId').text
                    except:
                        buybox = "Amazon"

                    try:
                        sticker_tag = driver.find_element(By.ID, 'dealBadgeSupportingText').text
                    except:
                        sticker_tag = "No tag"

                    sheet.append([asin, price, buybox, sticker_tag])
                except Exception as e:
                    print(f"Error retrieving data for {asin}: {e}")
                    sheet.append([asin, "Error", "Error", "Error"])

    except Exception as e:
        print(f"Critical Error: {e}")
    finally:
        output_file = f'Amazon_Regional_Report_{today_date}.xlsx'
        excel.save(output_file)
        print(f"Report saved successfully to: {output_file}")
        driver.quit()

if __name__ == "__main__":
    run_scraper()
