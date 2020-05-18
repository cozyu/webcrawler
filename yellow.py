from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from bs4 import BeautifulSoup

#This example requires Selenium WebDriver 3.13 or newer
#outputdir="./"
#service_log_path = "{}/chromedriver.log".format(outputdir)
#service_args = ['--verbose']
#with webdriver.Chrome('/usr/bin/chromedriver',
#        service_args=service_args,
#        service_log_path=service_log_path) as driver:

url="https://ynpres1.xanterra.com/cgi-bin/lansaweb?procfun+rn+resnet+RES+funcparms+UP(A2560):;OSSUM0;070820;1;2;2;010;?/&_ga=2.230307156.919223959.1589666383-929081673.1589666383#"
path="/html/body/form/div[3]/div[1]/div[2]/div/article/div/div[2]/div[2]/div/div[2]/table[1]/tbody"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
dataList=[]
with webdriver.Chrome(chrome_options=chrome_options) as driver:
    wait = WebDriverWait(driver, 10)
    driver.get(url)
    html = driver.page_source # 페이지의 elements모두 가져오기
    tbody=driver.find_element_by_xpath(path)
    #text=driver.find_element(By.TAG_NAME,'div').get_attribute('innerHTML')
    dates=tbody.find_elements(By.CLASS_NAME,'date')
    for date in dates:
        #print(date.get_attribute('innerText').strip().split() )
        dataList.append(date.get_attribute('innerText').strip().split())
for data in dataList:
    if data[1]!='SOLD':
        day=int(data[0])
        if day>=8 and day <=13:
            print(data)
        
"""
    soup = BeautifulSoup(html, 'html.parser') # BeautifulSoup사용하기
    notices = soup.select('div.p_inr > div.p_info > a > span')
    for n in notices:
        print(n.text.strip())
    driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
    first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3>div")))
    print(first_result.get_attribute("textContent"))
"""

  

