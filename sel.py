def sel(lnk):
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    import time
    driver_path = "chromedriver.exe"
    s=Service(driver_path)
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument('window-size=1920x1080')
    driver = webdriver.Chrome(service=s, options=option)
    ll=lnk
    driver.get(ll)
    time.sleep(10)
    html=driver.page_source

    p='"Sanskrit" data-text="'
    start_value=html.index(p)+22
    end_value=html.find('"', start_value)
    return html[start_value:end_value]
