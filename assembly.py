import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

'''
검색어 설정: 기능에 따라 검색어를 분류한다.

crawl_ : 웹페이지에서 크롤
Filter_ : 크롤링한 데이터를 필터한다.
OutPut : 크롤링한 데이터를 스프레드 시트로 저장한다. 

MainPage : 모든 채권이 나온 페이지 https://8percent.kr/deals/채권번호
SubPage : 채권번호 https://8percent.kr/deals/채권번호

BondNum : 채권번호 
DebtData : 채무유형
DebtData_total : 총채무
DebtData_P2P : P2P채무

''' 



def crawl_MainPage(): # 개인 채권 홈페이지를 크롤링한다. 
    '''
    개인 채권 페이지를 크롤링한다. 
    https://8percent.kr/deals/individual
    html정보 전체를 가져온다. 
    '''

    #해드리스 상태 http://blog.naver.com/PostView.nhn?blogId=baek2sm&logNo=221425659595&parentCategoryNo=&categoryNo=18&viewDate=&isShowPopularPosts=true&from=search
    chrome_options = webdriver.ChromeOptions() #
    chrome_options.add_argument('--headless')
    #chrome_options.add_argument("--disable-gpu") # 보험  

    # 해드리스 탐지막기
    chrome_options.add_argument("???")

    # 웹드라이버 파일 주소
    driver = webdriver.Chrome('/Users/kimsanghyun/Lets_Get_rich/ZZ_chromedriver/chromedriver',chrome_options=chrome_options)
    driver.implicitly_wait(2)
    sleep(0.5)

    # 8퍼센트 포크폴리오 분석
    driver.get('https://8percent.kr/deals/individual')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    driver.quit()

    return soup #html의 자료를 축출한다.

# 변수항목
soup = crawl_MainPage()

# 함수항목
def Filter_BondNum(soup):
    '''
    채권번호를 가져오는 함수
    리스트형 데이터로 돌려준다
    밑에 #해시태그를 풀면 활용이 가능하다. 
    '''

    name =[]
    NumOfBonds = int((len(soup.body.find_all('span')[:])-9)/6)-2
    
    for n in range(NumOfBonds):
        name.append(str(soup.body.find_all('span')[9+n*6].text))
    return name

# 변수항목 
name = Filter_BondNum(soup) #soup = crawl_investment_individual()

# 함수항목
def crawl_SubPage(name, n): 
    '''
    채권번호를 활용한다. https://8percent.kr/deals/채권번호
    '''
    driver = webdriver.Chrome('/Users/kimsanghyun/Lets_Get_rich/ZZ_chromedriver/chromedriver')
    driver.implicitly_wait(3)
    sleep(0.5)
    
    Bond_name = name[n][0:5] 

    chrome_options = webdriver.ChromeOptions() #
    chrome_options.add_argument('--headless')
    #chrome_options.add_argument("--disable-gpu") # 보험  
    chrome_options.add_argument("???")
    driver = webdriver.Chrome('/Users/kimsanghyun/Lets_Get_rich/ZZ_chromedriver/chromedriver',chrome_options=chrome_options)
    driver.implicitly_wait(2)

    driver.get('https://8percent.kr/deals/' + str(Bond_name)) #
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    return soup


# 변수항목
#name = name[0:5] #개만 임시로 추출한다. 
#for n in range(len(name)): 
Subsoup = crawl_SubPage(name, 0) #in: name = Filter_BondNum(soup)

# 함수항목
def Filter_NL(soup): #1차 정제항목
    test_text=[]
    for n in range(len(soup.body.article.find_all('div'))):        
        test_text.append(str(soup.body.article.find_all('div')[n].text.replace('\n', '')))
    return test_text #채권페이지의 자연어를 축출한다.

# 변수항목
# ['신용 정보  ※ 최근 1년간 월별 KCB 점수 변화   KCB 등급 5등급 KCB 점수 733점 ', ' ※ 최근 1년간 월별 KCB 점수 변화   KCB 등급 5등급 KCB 점수 733점 ', ' ※ 최근 1년간 월별 KCB 점수 변화', '', '', '', '', '', '', '  KCB 등급 5등급 KCB 점수 733점 ', '소득 정보 월 평균 소득  575만원   소득형태 근로소득자 직장규모 코스피상장사 재직기간 19.3년', '카드사용 정보 월 평균 사용 금액    월 평균 사용 금액은 할부 등이 반영되지 않은, 과거 12개월 카드 총 이용금액을 단순평균한 금액입니다.  291만원   신용카드 총 한도  2,850만원 이용 카드개수 2장', '   월 평균 사용 금액은 할부 등이 반영되지 않은, 과거 12개월 카드 총 이용금액을 단순평균한 금액입니다.', '', '월 평균 사용 금액은 할부 등이 반영되지 않은, 과거 12개월 카드 총 이용금액을 단순평균한 금액입니다.', '월 평균 사용 금액은 할부 등이 반영되지 않은, 과거 12개월 카드 총 이용금액을 단순평균한 금액입니다.', '월 평균 사용 금액은 할부 등이 반영되지 않은, 과거 12개월 카드 총 이용금액을 단순평균한 금액입니다.', '부채 정보 보유 대출 7건 총 대출 잔액 3억 9,865만원 총 대출 잔액 (7건) 3억 9,865만원   대출잔액 / 약정금액 캐피탈 (2)            2,695만원          /                       2,960만원          은행 (1)            6,000만원          /                      정보없음          담보 (4)           3억 1,170만원          /                      정보없음          ', '보유 대출 7건 총 대출 잔액 3억 9,865만원', '보유 대출 7건', '총 대출 잔액 3억 9,865만원', '총 대출 잔액 (7건) 3억 9,865만원']
SubSoupText = Filter_NL(Subsoup) #Subsoup = crawl_SubPage(name, 0)

# 함수항목
def Filter_DebtData(test_text): # 과거함수명 find_debt_index_in_string [['담보', '(4)', '3억', '1,170만원', '/', '정보없음'], ['은행', '(1)', '6,000만원', '/', '정보없음'], ['캐피탈', '(2)', '2,695만원', '/', '2,960만원']]
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

# 변수항목
# [['은행', '(1)', '5,100만원', '/', '5,100만원'], ['담보', '(1)', '300만원', '/', '정보없음'], ['P2P', '(2)', '2,445만원', '/', '2,897만원']]
DebtData_List = Filter_DebtData(SubSoupText) #DebtData_List = Filter_DebtData(SubSoupText[1]) #여러개를 크롤링할 때


# 함수항목
def Filter_missing_DebtData(SubSoupText, DebtData_List):

    Null_List_2 = SubSoupText[-1].split()[3].replace('(','')
    Null_List_2 = Null_List_2.replace(')','')
    Null_List_2 = Null_List_2.replace('건','')
    print(Null_List_2)

    Null_List_1 = []
    for n in range(len(DebtData_List)):
        conv = DebtData_List[n][1]
        conv = conv.replace('(','')
        conv = conv.replace(')','')
        Null_List_1.append(int(conv))
        print(sum(Null_List_1))

    if Null_List_2 == sum(Null_List_1):
        return True
    else:
        return False

# 변수항목
# True / False
Filter_missing_DebtData(SubSoupText, DebtData_List)

# 함수항목
def Filter_P2P(test_text): #P2P채무가 있고 없는지를 알아낸다. 
    findText = Filter_DebtData(test_text)
    null = []
    for n in findText:
        for m in n:
            if m == 'P2P':
                null.append(1)
    if null == [1]:
        result = True #심사 거부 이유
        #print('P2P채무 있음')
    else:
        result = False
        #print('P2P채무 없음')
    
    return result

# 변수항목
# True / False
Filter_P2P(SubSoupText)

# 함수항목
def Filter_Income(test_text):
    want_list = test_text
    for n in range(len(want_list)):
        NullList = want_list[n].split()
        if len(NullList) > 0: # [] 리스트가 비어있는 경우
            if NullList[0] == "소득" and NullList[1] == "정보":
                Null1 = want_list[n].split()
                result = [Null1[5], Null1[-3], Null1[-1]]

    return result

# 변수항목
# ['575만원', '코스피상장사', '19.3년']
Income = Filter_Income(SubSoupText)

# 함수항목

def Filter_Expense(test_text):
    want_list = test_text
    for n in range(len(want_list)):
        NullList = want_list[n].split()
        if len(NullList) > 0: # [] 리스트가 비어있는 경우
            if NullList[0] == "카드사용":
                Null1 = want_list[n].split('.') #그 줄을 리스트로 바꾸기
                Null2 = Null1[1].split()
                result = [Null2[0], Null2[4]]
    return result

# 변수항목
# ['291만원', '2,850만원']
Expense = Filter_Expense(SubSoupText)

# 함수항목
def Filter_Credit(test_text):
    want_list = test_text
    for n in range(len(want_list)):
        NullList = want_list[n].split()
        if len(NullList) > 0: # [] 리스트가 비어있는 경우
            if NullList[0] == "신용" and NullList[1] == "정보": #해당 줄에 신용, 정보가 있을 때
                Null1 = want_list[n].split() #그 줄을 리스트로 바꾸기
                result = [Null1[-4], Null1[-1]]
    return result

# 변수항목
# ['6등급', '662점']
Credit = Filter_Credit(SubSoupText)

# 함수항목
def Filter_lonereq(soup): #대출신청 정보 계산
    '''
    세전 수익률, 상환기간, 모집금액(사람들이 넣은 돈), 대출금액(대출자가 모으고 싶은 돈)
    '''
    moneyList = []
    
    #soup.body.main.header.div

    profit = soup.body.main.header.div.find_all('p')[3].text #수익률
    profit = profit.replace('%', '')
    profit = float(profit)
    
    period = soup.body.main.header.div.find_all('p')[5].text #상환기간
    period = period.replace('개월', '')
    period = int(period)
    
    money = soup.body.main.header.div.find_all('p')[9].text #상환금액
    money_gathering  = money.split('\n')[1].replace(' ', '') #모집금액(사람들이 넣은 돈)
    money_gathering = int(money_gathering)
    
    money_gathered = money.split('\n')[3].replace(' ', '') #대출금액(대출자가 모으고 싶은 돈)
    money_gathered = money_gathered.replace(',', '')
    money_gathered = int(money_gathered)
    
    moneyList.append(profit) 
    moneyList.append(period) 
    moneyList.append(money_gathering) 
    moneyList.append(money_gathered) 
    return moneyList

# 변수항목
lonereq_List = Filter_lonereq(Subsoup)


# 함수항목

def InterestCost(Debts, Credit):
    '''
    Debts = find_debt_index_in_string(test_text)
    Credit = Eight_Per_Cent.find_Credit_index_in_string(test_text)
    
    기준 공식
    intr = Credit*3
    Cap*((1 + intr/100)**n)/(12*n)
    '''

    # 신용등급 문자열 > 수
    Credit = Credit[0].replace('등급','')
    Credit = int(Credit[0])
    
    # 월 할부상환
    NullList = []
    for n in range(len(Debts)):
        
        #중액 중금리
        if Debts[n][0] == '캐피탈': #5년 할부상환 6% 시작 2%가산
            if Debts[n][2][-1] == '억': #억일 때 
                Million100 = Debts[n][2].replace('억','')
                Million100 = int(Million100)

                Million10 = Debts[n][3].replace('만원','') # [2] > [3] 인덱스 변경
                if len(Million10) > 4:
                    Million10 = Million10.replace(',','')
                    Million10 = int(Million10)

                    Nullver = Million100*10000 + Million10
                    DebtWithInt = (Nullver*((1+(6+Credit*2)/100)**5))/(12*5)
                    NullList.append(DebtWithInt)  
                else:
                    Million10 = int(Million10)
                    Nullver = Million100*10000 + Million10
                    DebtWithInt = (Nullver*((1+(6+Credit*2)/100)**5))/(12*5)
                    NullList.append(DebtWithInt) 
            else:
                Nullver = Debts[n][2].replace('만원','')
                if len(Nullver) > 4:
                    Nullver = Nullver.replace(',','')
                    Nullver = int(Nullver)
                    
                    DebtWithInt = (Nullver*((1+(6+Credit*2)/100)**5))/(12*5)
                    NullList.append(DebtWithInt)
                    
                else:
                    Nullver = int(Nullver)
                    
                    DebtWithInt = (Nullver*((1+(6+Credit*2)/100)**5))/(12*5)
                    NullList.append(DebtWithInt)
            
        if Debts[n][0] == '저축은행': #5년 할부상환 6% 시작 2%가산
            if Debts[n][2][-1] == '억': #억일 때 
                Million100 = Debts[n][2].replace('억','')
                Million100 = int(Million100)

                Million10 = Debts[n][3].replace('만원','') # [2] > [3] 인덱스 변경
                if len(Million10) > 4:
                    Million10 = Million10.replace(',','')
                    Million10 = int(Million10)

                    Nullver = Million100*10000 + Million10
                    DebtWithInt = (Nullver*((1+(6+Credit*2)/100)**5))/(12*5)
                    NullList.append(DebtWithInt)  
                else:
                    Million10 = int(Million10)
                    Nullver = Million100*10000 + Million10
                    DebtWithInt = (Nullver*((1+(6+Credit*2)/100)**5))/(12*5)
                    NullList.append(DebtWithInt) 
            else:
                Nullver = Debts[n][2].replace('만원','')
                if len(Nullver) > 4:
                    Nullver = Nullver.replace(',','')
                    Nullver = int(Nullver)
                            
                    DebtWithInt = (Nullver*((1+(6+Credit*2)/100)**5))/(12*5)
                    NullList.append(DebtWithInt)    
                else:
                    Nullver = int(Nullver)    
                    DebtWithInt = (Nullver*((1+(6+Credit*2)/100)**5))/(12*5)
                    NullList.append(DebtWithInt)
            
        if Debts[n][0] == 'P2P': #1년 할부상환 12% 시작 1.5%가산
            if Debts[n][2][-1] == '억': #억일 때 
                Million100 = Debts[n][2].replace('억','')
                Million100 = int(Million100)

                Million10 = Debts[n][3].replace('만원','') # [2] > [3] 인덱스 변경
                if len(Million10) > 4:
                    Million10 = Million10.replace(',','')
                    Million10 = int(Million10)

                    Nullver = Million100*10000 + Million10
                    DebtWithInt = (Nullver*((1+Credit*3/100)**1))/(12*1)
                    NullList.append(DebtWithInt)  
                else:
                    Million10 = int(Million10)
                    Nullver = Million100*10000 + Million10
                    DebtWithInt = (Nullver*((1+Credit*3/100)**1))/(12*1)
                    NullList.append(DebtWithInt) 
            else:
                Nullver = Debts[n][2].replace('만원','')
                if len(Nullver) > 4:
                    Nullver = Nullver.replace(',','')
                    Nullver = int(Nullver)
                    DebtWithInt = (Nullver*((1+Credit*3/100)**1))/(12*1)
                    NullList.append(DebtWithInt)
                    
                else:
                    Nullver = int(Nullver)
                    DebtWithInt = (Nullver*((1+Credit*3/100)**1))/(12*1)
                    NullList.append(DebtWithInt)

        # 소액 고금리
        if Debts[n][0] == '보험': #5년 할부상환 12% 시작 1.5%가산
            if Debts[n][2][-1] == '억': #억일 때 
                Million100 = Debts[n][2].replace('억','')
                Million100 = int(Million100)

                Million10 = Debts[n][3].replace('만원','') # [2] > [3] 인덱스 변경
                if len(Million10) > 4:
                    Million10 = Million10.replace(',','')
                    Million10 = int(Million10)

                    Nullver = Million100*10000 + Million10
                    DebtWithInt = (Nullver*((1+(10.5+Credit*1.5)/100)**5))/(12*5)
                    NullList.append(DebtWithInt)  
                else:
                    Million10 = int(Million10)
                    Nullver = Million100*10000 + Million10
                    DebtWithInt = (Nullver*((1+(10.5+Credit*1.5)/100)**5))/(12*5)
                    NullList.append(DebtWithInt)    
            else:
                Nullver = Debts[n][2].replace('만원','')
                if len(Nullver) > 4:
                    Nullver = Nullver.replace(',','')
                    Nullver = int(Nullver)
                    
                    DebtWithInt = (Nullver*((1+(10.5+Credit*1.5)/100)**5))/(12*5)
                    NullList.append(DebtWithInt)
                    
                else:
                    Nullver = int(Nullver)
                    
                    DebtWithInt = (Nullver*((1+(10.5+Credit*1.5)/100)**5))/(12*5)
                    NullList.append(DebtWithInt)
            
        if Debts[n][0] == '카드': #5년 할부상환 12% 시작 1.5%가산
            if Debts[n][2][-1] == '억': #억일 때 
                Million100 = Debts[n][2].replace('억','')
                Million100 = int(Million100)

                Million10 = Debts[n][3].replace('만원','') # [2] > [3] 인덱스 변경
                if len(Million10) > 4:
                    Million10 = Million10.replace(',','')
                    Million10 = int(Million10)

                    Nullver = Million100*10000 + Million10
                    DebtWithInt = (Nullver*((1+(10.5+Credit*1.5)/100)**5))/(12*5)
                    NullList.append(DebtWithInt)  
                else:
                    Million10 = int(Million10)
                    Nullver = Million100*10000 + Million10
                    DebtWithInt = (Nullver*((1+(10.5+Credit*1.5)/100)**5))/(12*5)
                    NullList.append(DebtWithInt)        
            else:
                Nullver = Debts[n][2].replace('만원','')
                if len(Nullver) > 4:
                    Nullver = Nullver.replace(',','')
                    Nullver = int(Nullver)
                    DebtWithInt = (Nullver*((1+(10.5+Credit*1.5)/100)**5))/(12*5)
                    NullList.append(DebtWithInt)
                    
                else:
                    Nullver = int(Nullver)
                    DebtWithInt = (Nullver*((1+(10.5+Credit*1.5)/100)**5))/(12*5)
                    NullList.append(DebtWithInt)
            
        if Debts[n][0] == '현금서비스': #5년 할부상환 12% 시작 1.5%가산
            if Debts[n][2][-1] == '억': #억일 때 
                Million100 = Debts[n][2].replace('억','')
                Million100 = int(Million100)

                Million10 = Debts[n][3].replace('만원','') # [2] > [3] 인덱스 변경
                if len(Million10) > 4:
                    Million10 = Million10.replace(',','')
                    Million10 = int(Million10)
                    Nullver = Million100*10000 + Million10
                    DebtWithInt = (Nullver*((1+(10.5+Credit*1.5)/100)**5))/(12*5)
                    NullList.append(DebtWithInt)
                else:
                    Nullver = int(Million10)
                    DebtWithInt = (Nullver*((1+(10.5+Credit*1.5)/100)**5))/(12*5)
                    NullList.append(DebtWithInt)
            else:
                Nullver = Debts[n][2].replace('만원','')
                if len(Nullver) > 4:
                    Nullver = Nullver.replace(',','')
                    Nullver = int(Nullver)
                    DebtWithInt = (Nullver*((1+(10.5+Credit*1.5)/100)**5))/(12*5)
                    NullList.append(DebtWithInt)
                    
                else:
                    Nullver = int(Nullver)
                    Nullver = Million100*10000 + Million10
                    DebtWithInt = (Nullver*((1+(10.5+Credit*1.5)/100)**5))/(12*5)
                    NullList.append(DebtWithInt)
        
        # 고액 저금리
        if Debts[n][0] == '은행': #은행은 마이너스 통장 금리
            
            if Debts[n][2][-1] == '억': #억일 때 
                Million100 = Debts[n][2].replace('억','')
                Million100 = int(Million100)

                Million10 = Debts[n][3].replace('만원','') # [2] > [3] 인덱스 변경
                if len(Million10) > 4:
                    Million10 = Million10.replace(',','')
                    Million10 = int(Million10)
                    Nullver = Million100*10000 + Million10
                    DebtWithInt = (Nullver*((1+Credit*3/(100))**10))/(12*10)
                    NullList.append(DebtWithInt)
                else:
                    Million10 = int(Million10)
                    Nullver = Million100*10000 + Million10
                    DebtWithInt = (Nullver*((1+Credit*3/(100))**10))/(12*10)
                    NullList.append(DebtWithInt)
            else:
                Nullver = Debts[n][2].replace('만원','')
                if len(Nullver) > 4:
                    Nullver = Nullver.replace(',','')
                    Nullver = int(Nullver)
                    
                    DebtWithInt = (Nullver*((1+Credit*3/(100))**10))/(12*10)
                    NullList.append(DebtWithInt)
                else:
                    Nullver = int(Nullver)
                    
                    DebtWithInt = (Nullver*((1+Credit*3/(100))**10))/(12*10)
                    NullList.append(DebtWithInt)
            
        if Debts[n][0] == '담보': #부동산담보 부동산 담보는 신용등급 1로 가정
            if Debts[n][2][-1] == '억': #억일 때 
                Million100 = Debts[n][2].replace('억','')
                Million100 = int(Million100)
                Million10 = Debts[n][3].replace('만원','') # [2] > [3] 인덱스 변경
                if len(Million10) > 4:
                    Million10 = Million10.replace(',','')
                    Million10 = int(Million10)

                    Nullver = Million100*10000 + Million10
                    DebtWithInt = (Nullver*((1+1*3/(100))**15))/(12*15)
                    NullList.append(DebtWithInt)
                else:
                    Million10 = int(Million10)
                    Nullver = Million100*10000 + Million10
                    DebtWithInt = (Nullver*((1+1*3/(100))**15))/(12*15)
                    NullList.append(DebtWithInt)

            else: #억으로 시작하지 않아 기존 함수 유지
                Nullver = Debts[n][2].replace('만원','')
                if len(Nullver) > 4:
                    Nullver = Nullver.replace(',','')
                    Nullver = int(Nullver)
                    DebtWithInt = (Nullver*((1+1*3/(100))**15))/(12*15)
                    NullList.append(DebtWithInt)
                    
                else:
                    Nullver = int(Nullver)
                    DebtWithInt = (Nullver*((1+1*3/(100))**15))/(12*15)
                    NullList.append(DebtWithInt)
            
        if Debts[n][0] == '학자금': #부동산담보 부동산 담보는 신용등급 1로 가정
            if Debts[n][2][-1] == '억': #억일 때 
                Million100 = Debts[n][2].replace('억','')
                Million100 = int(Million100)
                
                Million10 = Debts[n][3].replace('만원','') # Debts[n][2] > Debts[n][3] 인덱스 변경
                if len(Million10) > 4:
                    Million10 = Million10.replace(',','')
                    Million10 = int(Million10)
                    Nullver = Million100*10000 + Million10
                    DebtWithInt = (Nullver*((1+1*2.25/(100))**15))/(12*10)
                    NullList.append(DebtWithInt)
                else:
                    Million10 = int(Million10)
                    Nullver = Million100*10000 + Million10
                    DebtWithInt = (Nullver*((1+1*2.25/(100))**15))/(12*10)
                    NullList.append(DebtWithInt)
            else: #억으로 시작하지 않아 기존 함수 유지
                Nullver = Debts[n][2].replace('만원','')
                if len(Nullver) > 4:
                    Nullver = Nullver.replace(',','')
                    Nullver = int(Nullver)
                    DebtWithInt = (Nullver*((1+1*2.25/(100))**15))/(12*10)
                    NullList.append(DebtWithInt)
                else:
                    Nullver = int(Nullver)
                    DebtWithInt = (Nullver*((1+1*2.25/(100))**15))/(12*10)
                    NullList.append(DebtWithInt)
    
    return sum(NullList)

# 변수항목
Cost_of_Interest = InterestCost(DebtData_List, Credit)

# 함수항목
def OverHead():
    pass

# 함수항목
def Bond_index():
    pass

# 함수항목
def Bond_req_ND(): #거절요건
    pass

# 함수항목
'''def OutPut_spreadsheet(채권번호, 채권지수, 채권안정성, 거절요건성립):

    #name = Filter_BondNum(soup) #채권번호
    #index = Bond_index() #채권지수
    #OverHead_List = OverHead()
    #Lone_ND = Bond_req_ND()
    
    testframe = pd.DataFrame({
        '채권번호':name,
        '안정성대비수익지수':range(len(name)),
        '인정성지수':OverHead_List,
    })
    # [채권번호, 채권지수, 채권안정성, 투자요건]
    return testframe'''

