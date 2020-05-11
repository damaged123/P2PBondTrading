from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

def ListOfBonds(soup):
    '''
    채권번호를 가져오는 함수
    리스트형 데이터로 돌려준다
    밑에 #해시태그를 풀면 활용이 가능하다. 
    '''
    name =[]
    #requered_capital =[]
    #invested_capital = []
    #classification = []
    
    NumOfBonds = int((len(soup.body.find_all('span')[:])-9)/6)-2
    
    for n in range(NumOfBonds):
        name.append(str(soup.body.find_all('span')[9+n*6].text))
        #classification.append(str(soup.body.find_all('span')[10+n*6].text))
        #invested_capital.append(str(soup.body.find_all('span')[11+n*6].text))
        #requered_capital.append(str(soup.body.find_all('span')[12+n*6].text))
    return name
    
def crawl_investment_individual(): # 개인 채권 홈페이지를 크롤링한다. 
    '''
    개인 채권 페이지를 크롤링한다. 
    https://8percent.kr/deals/individual
    html정보 전체를 가져온다. 
    '''

    #해드리스 상태 http://blog.naver.com/PostView.nhn?blogId=baek2sm&logNo=221425659595&parentCategoryNo=&categoryNo=18&viewDate=&isShowPopularPosts=true&from=search
    chrome_options = webdriver.ChromeOptions() #
    chrome_options.add_argument('headless')
    options = webdriver.ChromeOptions()

    # options.add_argument("--disable-gpu") # 보험

    # 해드리스 탐지막기
    options.add_argument("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36")

    # 웹드라이버 파일 주소
    driver = webdriver.Chrome('/Users/kimsanghyun/Lets_Get_rich/ZZ_chromedriver/chromedriver',chrome_options=options)
    driver.implicitly_wait(2)
    sleep(0.5)


    # 8퍼센트 포크폴리오 분석
    driver.get('https://8percent.kr/deals/individual')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    driver.quit()

    print("date in soup. 변수 soup를 활용하시오.")
    return soup #html의 자료를 축출한다.