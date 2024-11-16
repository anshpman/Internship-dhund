from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Configure WebDriver
chrome_options = Options()

# Mimic a real user by setting a user-agent
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

# Enable headless mode if needed
chrome_options.add_argument("--headless")  # Comment this out if you want to see the browser
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent detection as a bot

# Path to ChromeDriver
chrome_driver_path = r"C:\Users\elpid\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"  # Replace with your path

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the Naukri webpage
url = "https://www.naukri.com/internship-jobs-in-mumbai"
driver.get(url)

# Introduce a random delay to mimic human behavior
time.sleep(random.uniform(2, 5))  # Random delay between 2 and 5 seconds
# Define keywords for AI/ML roles (converted to lowercase for case-insensitive matching)
# Define keywords for AI/ML roles
keywords = [
    "data scientist", "machine learning engineer", "ai engineer", "data analyst", 
    "data engineer", "deep learning engineer", "data scientist intern", "ml engineer", 
    "ai researcher", "research scientist", "computer vision engineer", "natural language processing", 
    "nlp engineer", "data architect", "business intelligence", "statistical analyst", 
    "predictive modeler", "data science intern", "big data engineer", "data visualization", 
    "cloud data engineer", "data operations", "quantitative analyst", "analytics engineer", 
    "big data analyst", "mlops engineer", "artificial intelligence", "ai researcher", 
    "robotics engineer", "data mining", "quantitative data scientist", "data strategist", 
    "data consultant", "data science researcher", "ai developer", "data modeler", 
    "data wrangler", "data processing", "data science manager", "data science consultant", 
    "research analyst", "software engineer - machine learning", "business data analyst", 
    "data science specialist", "data science lead", "junior data scientist", "senior data scientist", 
    "data science expert", "machine learning scientist", "data mining engineer", 
    "ml research scientist", "data science trainer", "computer scientist", "cloud data scientist", 
    "data science director", "ai project manager", "ai solution architect", "data operations manager"
]


try:
    # Wait for the job listing container to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#listContainer"))
    )
    
    # Locate job elements
    job_elements = driver.find_elements(By.CSS_SELECTOR, ".styles_job-listing-container__OCfZC a")
    
    if not job_elements:
        print("No job elements found. Please check the CSS selectors or page content.")
    else:
        print("Extracting job details:")
        for element in job_elements:
            try:
                job_title = element.text.strip().lower()  # Normalize to lowercase
                job_link = element.get_attribute("href")
                
                # Check if the title contains any of the relevant keywords
                if any(keyword.lower() in job_title for keyword in keywords):
                    # Find the parent container for other job details
                    parent_div = element.find_element(By.XPATH, "./ancestor::div[contains(@class, 'styles_job-listing-container__OCfZC')]")
                    
                    # Extract company name, location, and salary
                    company_name = "N/A"
                    location = "N/A"
                    salary = "N/A"
                    
                    try:
                        company_name = parent_div.find_element(By.CSS_SELECTOR, "#listContainer > div.styles_job-listing-container__OCfZC > div > div:nth-child(7) > div > div.row2 > span > a.comp-name.mw-25").text.strip()
                    except:
                        pass
                    
                    try:
                        location = parent_div.find_element(By.CSS_SELECTOR, "#listContainer > div.styles_job-listing-container__OCfZC > div > div:nth-child(9) > div > div.row3 > div > span.loc-wrap.ver-line > span > span").text.strip()
                    except:
                        pass
                    
                    try:
                        salary = parent_div.find_element(By.CSS_SELECTOR, "#listContainer > div.styles_job-listing-container__OCfZC > div > div:nth-child(10) > div > div.row3 > div > span.sal-wrap.ver-line > span > span").text.strip()
                    except:
                        pass
                    
                    print(f"Job Title: {job_title}")
                    print(f"Company: {company_name}")
                    print(f"Location: {location}")
                    print(f"Salary: {salary}")
                    print(f"Job Link: {job_link}")
                    print("-" * 50)
            except Exception as inner_e:
                print(f"Error processing job entry: {inner_e}")

except Exception as e:
    print(f"An error occurred: {e}")
