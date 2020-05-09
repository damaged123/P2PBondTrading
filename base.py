from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

def crawl_Eight_Per_Cent():
    driver = webdriver.Chrome('/Users/kimsanghyun/Lets_Get_rich/ZZ_chromedriver/chromedriver')
    driver.implicitly_wait(3)
    driver.get('https://8percent.kr/user/login/')
    ## 아이디/비밀번호를 입력해준다.
    sleep(0.5)
    driver.find_element_by_name('email').send_keys("?????")
    sleep(0.5)
    driver.find_element_by_name('password').send_keys("?????")
    sleep(0.5)
    ## 로그인 버튼을 눌러주자.
    driver.find_element_by_xpath('//*[@id="submitbutton"]').click()

    # 8퍼센트 포크폴리오 분석
    driver.get('https://8percent.kr/my/investor/investments/')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    print("date in soup. 변수 soup를 활용하시오.")
    return soup 

'''
전체 파이프라인
crawl_investment_individual()는 인자가 비어 있을 함수이다. 개인신용 채권의 html데이터를 축출한다. soup = crawl_investment_individual()

    ListOfBonds(soup) 위 함수에서 html데이터에서 채권번호 데이터를 정재축출한다. name = ListOfBonds(soup)

        Get_individual_data(name, n) 위 함수에서 채권번호로 주소를 접근하고 html데이터를 축출한다. soup = Get_individual_data(name)

            get_NLB(soup) 위 함수에서 소득, 지출, 신용, 채무정보를 가져온다. test_text = get_NLB(soup)

                find_Income_index_in_string(test_text) 위 함수에서 소득정보를 정재한다. 근로소득자, 중기업...등 소득형태를 알아야 한다. "미정" Income = find_Income_index_in_string(test_text)

                find_Expense_index_in_string(test_text) 위 함수에서 지출정보를 정재한다. Expense = find_Expense_index_in_string(test_text)

                find_Credit_index_in_string(test_text) 위 함수에서 신용점수정보를 정재한다.  Credit = find_Credit_index_in_string(test_text)

                find_debt_index_in_string(test_text) 위 함수에서 채무유형을 축출한다. Dedts = find_debt_index_in_string(test_text)

                sum_of_debt(test_text)는 사용하는 함수가 아니다. 총 채무정보를 축출한다. "미정"

                sum_of_debt_inText(test_text)는 사용하는 함수가 아니다. 총 채무정보에서 채무사건 수만 축출한다. "미정"

                under_match(test_text) 부채유형에 따라 수의 리스트를 축출한다. "미정"

                get_missing_date(test_text) 부채유형의 합과 총 부채수의 합을 구한다. 누락된 채무정보를 알 수 있다. "미정"

                OverHead(test_text) 채권의 안정성을 지표화한다. 추산은 10년만기에 24%이율로 한다(문제는 신용대출은 이자가 높지만 부동산담보는 따로 추산할 필요가 있다. 추가 대출로 받게 될 이자를 미 반영했다.). OverHead = OverHead(test_text)

                find_P2P_debt(test_text) P2P 채무유형의 유무를 확인한다. 

                interestAndOverHead() 수익과 안정성을 비교한다. 

                    ???() 순수하게 안정적인 순서, 안정성대비 수익률 순서
                해드릴스 크롤링 방법
                http://blog.naver.com/PostView.nhn?blogId=baek2sm&logNo=221425659595&parentCategoryNo=&categoryNo=18&viewDate=&isShowPopularPosts=true&from=search

                ???() 엑셀파일로 출력한다. 
'''

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

#채권번호를 가져온다. 
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

def Get_individual_data(name, n): 
    '''
    채권번호를 활용한다. 주소
    '''
    from selenium import webdriver
    from bs4 import BeautifulSoup
    from time import sleep
    
    driver = webdriver.Chrome('/Users/kimsanghyun/Lets_Get_rich/ZZ_chromedriver/chromedriver')
    driver.implicitly_wait(3)
    sleep(0.5)
    
    # 채권심사를 위해 
    Bond_name = name[n][0:5] #현재 for문을 사용하지 않는다. 
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


def find_Income_index_in_string(test_text):
    want_list = test_text
    for n in range(len(want_list)):
        NullList = want_list[n].split()
        if len(NullList) > 0: # [] 리스트가 비어있는 경우
            if NullList[0] == "소득" and NullList[1] == "정보":
                Null1 = want_list[n].split()
                result = [Null1[5], Null1[-1]]

    return result

# 지출 정보를 찾는 함수 
def find_Expense_index_in_string(test_text):
    want_list = test_text
    for n in range(len(want_list)):
        NullList = want_list[n].split()
        if len(NullList) > 0: # [] 리스트가 비어있는 경우
            if NullList[0] == "카드사용":
                Null1 = want_list[n].split('.') #그 줄을 리스트로 바꾸기
                Null2 = Null1[1].split()
                result = [Null2[0], Null2[4]]
    return result

# 신용정보만 추출하는 함수
def find_Credit_index_in_string(test_text):
    want_list = test_text
    for n in range(len(want_list)):
        NullList = want_list[n].split()
        if len(NullList) > 0: # [] 리스트가 비어있는 경우
            if NullList[0] == "신용" and NullList[1] == "정보": #해당 줄에 신용, 정보가 있을 때
                Null1 = want_list[n].split() #그 줄을 리스트로 바꾸기
                result = [Null1[-4], Null1[-1]]
    return result

# 부채정보를 찾는 함수 
def find_debt_index_in_string(test_text):
    want_list = test_text
    for n in range(len(want_list)):
        NullList = want_list[n].split()
        if len(NullList) > 0: # [] 리스트가 비어있는 경우
            if NullList[0] == "부채" and NullList[1] == "정보":
                getNum = []
                for i in range(len(NullList)):
                        if NullList[i] == "은행": #추산기준금리 COFIX+1%
                            getNum.append(i)
                        if NullList[i] == "저축은행": # 거액(1억 이상) 중금리
                            getNum.append(i)
                        if NullList[i] == "캐피탈": # 
                            getNum.append(i) 
                        if NullList[i] == "P2P": # 소액(3000만원 이하) 중급리
                            getNum.append(i)
                        if NullList[i] == "보험": # 소액(3000만원 이하) 중금리 신용 5등급 기준12%
                            getNum.append(i)
                        if NullList[i] == "학자금": # 2.2%
                            getNum.append(i)
                        if NullList[i] == "카드": # 소액 고금리
                            getNum.append(i)
                        if NullList[i] == "담보": # 추산기준금리 국민주택채권
                            getNum.append(i)
                        if NullList[i] == "현금서비스": #
                            getNum.append(i)
                        # 채무정보를 리스트로 반환
                        back_list = []
                        result = []
                        for n in getNum[::-1]:
                            if back_list == []:
                                result.append(NullList[n:])
                                back_list.append(n)
                            else:
                                result.append(NullList[n:back_list[-1]])
                                
                                back_list.append(n)
    return result

# 총부채정보
def sum_of_debt(test_text):
    return test_text[-1].split()
    

def sum_of_debt_inText(test_text):
    Null = sum_of_debt(test_text)[3].replace('(','')
    Null = Null.replace(')','')
    Null = Null.replace('건','')
    return Null

# 부채 유형 누락여부를 확인할 함수
def under_match(test_text):
    match = test_text
    result = []
    for n in range(len(match)):
        conv = match[n][1]
        conv = conv.replace('(','')
        conv = conv.replace(')','')
        result.append(int(conv))
    return result

def get_missing_date(test_text): #print를 반환하므로 데이터는 비어있다. 
    
    if sum(under_match(find_debt_index_in_string(test_text)))==int(sum_of_debt_inText(test_text)):
        print('누락 된 부채유형이 없음')
    else:
        print('누락된 채무유형이 있음') 

def OverHead(test_text): #24%최대 이자로 일률적으로 적용하며 10년 만기로 설정한다. 추산이자채무상환액 = 원금/12*10(10년만기균등상환)+원금*3%이자(이자비용+ 쿠션1%)
    #추가 대출금에 다한 반영X
    Income = find_Income_index_in_string(test_text)[0]
    Income = Income.replace('만원','')
    Income = Income.replace(',','')
    Income = int(Income)
    Expense = find_Expense_index_in_string(test_text)[0]
    Expense = Expense.replace('만원','')
    Expense = Expense.replace(',','')
    Expense = int(Expense)
    interest = sum_of_debt(test_text)[-1]
    interest = interest.replace('만원','')
    interest = interest.replace(',','')
    interest = int(interest)
    
    result = Income - (Expense+interest/120+interest*0.03)
    return result

def find_P2P_debt(test_text): #P2P채무가 있고 없는지를 알아낸다. 
    findText = find_debt_index_in_string(test_text)
    null = []
    for n in findText:
        for m in n:
            if m == 'P2P':
                null.append(1)
    if null == [1]:
        print('P2P채무 있음')
    else:
        print('P2P채무 없음')

def debt_Count(test_text):
    '''    
    findText = find_debt_index_in_string(test_text)
    null = []
    for n in findText:
        for m in n:
            if m == '저축은행':
                null.append(1)
    if null == [1]:
        
    else:
    '''

    pass

def interestAndOverHead():
    pass
