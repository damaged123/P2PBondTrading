from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

def Get_individual_data(name, n): 

    '''
    채권번호를 활용한다. 주소
    '''

    
    driver = webdriver.Chrome('/Users/kimsanghyun/Lets_Get_rich/ZZ_chromedriver/chromedriver')
    driver.implicitly_wait(3)
    sleep(0.5)
    
    # 채권심사를 위해 
    Bond_name = name[n][0:5] #현재 for문을 사용하지 않는다. 

    chrome_options = webdriver.ChromeOptions() #
    chrome_options.add_argument('headless')
    options = webdriver.ChromeOptions()
    options.add_argument("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36")
    driver = webdriver.Chrome('/Users/kimsanghyun/Lets_Get_rich/ZZ_chromedriver/chromedriver',chrome_options=options)
    driver.implicitly_wait(2)

    # 8퍼센트 포크폴리오 분석
    driver.get('https://8percent.kr/deals/' + str(Bond_name)) #
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    # individual화면으로 돌아가기
    
    # driver.get('https://8percent.kr/deals/individual')
    return soup

def get_NLB(soup): #
    test_text=[]
    for n in range(len(soup.body.article.find_all('div'))):
        test_text.append(str(soup.body.article.find_all('div')[n].text.replace('\n', '')))
    return test_text #채권페이지의 자연어를 축출한다.
