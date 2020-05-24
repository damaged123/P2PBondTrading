import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

'''
Top
검색어 설정: 기능에 따라 검색어를 분류한다.

crawl_ : 웹페이지에서 크롤
Filter_ : 크롤링한 데이터를 필터한다.
Calculate_ : 계산 기능을 하는 함수이다. 
OutPut : 크롤링한 데이터를 스프레드 시트로 저장한다. 

MainPage : 모든 채권이 나온 페이지 https://invest.lendit.co.kr/portfolio/0
SubPage : 채권번호 ???


''' 

def crawl_MainPage(): # 개인 채권 홈페이지를 크롤링한다. 
    '''
    기능: 개인 채권 페이지를 크롤링한다. https://invest.lendit.co.kr/portfolio/0
    인자: (인자가 없다)
    함수값: html정보를 리스트로 전체를 가져온다. 
    '''

    #해드리스 상태 http://blog.naver.com/PostView.nhn?blogId=baek2sm&logNo=221425659595&parentCategoryNo=&categoryNo=18&viewDate=&isShowPopularPosts=true&from=search
    chrome_options = webdriver.ChromeOptions() #
    chrome_options.add_argument('--headless')
    #chrome_options.add_argument("--disable-gpu") # 보험  

    # 해드리스 탐지막기
    chrome_options.add_argument("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36")

    # 웹드라이버 파일 주소
    driver = webdriver.Chrome('/Users/kimsanghyun/Lets_Get_rich/ZZ_chromedriver/chromedriver',chrome_options=chrome_options)
    driver.implicitly_wait(2)
    sleep(0.5)

    # 8퍼센트 포크폴리오 분석
    driver.get('https://invest.lendit.co.kr/portfolio/0')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    driver.quit()

    return soup #html의 자료를 축출한다.

def OutPut_spreadsheet(soup):
    '''
    testframe = pd.DataFrame({
        '채권번호':name, #name = Filter_BondNum(soup)
        '인정성지수':Null_SafeList, #SafeList = Calculate_OverHaed(Income, Expense, int_Cost, lonereq)
        '거절요건성립':Null_NDList #NDList = Calculate_lone_DN()
    })'''
    # [채권번호, 채권안정성, 투자요건]
    testframe = pd.DataFrame({
        'MainPage_All_html': soup
    })
    testframe.to_csv('/Users/kimsanghyun/Lets_Get_rich/aa_test_product/BondTrading/Runing_BondTrad/OutPut/BondData_2020_05_23.csv')
    return testframe

def RunAll():
    #soup = crawl_MainPage()
    result = crawl_MainPage()
    #result = OutPut_spreadsheet(soup)
    return result

print(RunAll())
