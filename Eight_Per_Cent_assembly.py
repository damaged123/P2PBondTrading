# -*- coding: utf-8 -*-
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

MainPage : 모든 채권이 나온 페이지 https://8percent.kr/deals/채권번호
SubPage : 채권번호 https://8percent.kr/deals/채권번호

BondNum : 채권번호 
DebtData : 채무유형
DebtData_total : 총채무
DebtData_P2P : P2P채무

lonereq: 채무자가 받고자 하는 대출정보이다. 
InterestCost : 이자비용을 추산한다. 
CF : 현금흐름
_OverHaed : 소득에서 지출과 이자비용 월상환액을 뺀 나머지이다. 
Bond_index : 채권의 안정성, 수익률, 현재가치를 반영한 지표이다.지표가 높을 수록 승인은 타당하다.

LND_ : DN함수에 인자로 사용할 변수
DN : 채출 요건을 다룬다. 다른 P2P 채무가 있는 경우이다. 소기업, 중기업 5년이하 경력, 코스피 상장사 3년이하 경력, 12년 이상의 경력이 있을 경우이다. OverHaed가 음수일 경우이다. 
''' 



def crawl_MainPage(): # 개인 채권 홈페이지를 크롤링한다. 
    '''
    기능: 개인 채권 페이지를 크롤링한다. https://8percent.kr/deals/individual
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
    driver.get('https://8percent.kr/deals/individual')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    driver.quit()

    return soup #html의 자료를 축출한다.

# 변수항목
# soup = crawl_MainPage()

# 함수항목
def Filter_BondNum(soup):
    '''
    기능: 채권번호를 가져오는 함수
    함수값: 리스트형 데이터로 돌려준다

    밑에 #해시태그를 풀면 활용이 가능하다. 
    '''

    name =[]
    NumOfBonds = int((len(soup.body.find_all('span')[:])-9)/6)-2
    
    for n in range(NumOfBonds):
        name.append(str(soup.body.find_all('span')[9+n*6].text))
    return name

# 변수항목 
# name = Filter_BondNum(soup) #soup = crawl_investment_individual()

# 함수항목
def crawl_SubPage(name, n): 
    '''
    인자: name = Filter_BondNum(soup)의 name은 채권번호이다. n은 채권리스트의 순서이다. 
    함수값: Subsoup이다. 채권의 html데이터를 리스트로 뽑는다.
    Subsoup = crawl_SubPage(name, 0)
    채권번호를 활용한다. https://8percent.kr/deals/채권번호
    '''
    driver = webdriver.Chrome('/Users/kimsanghyun/Lets_Get_rich/ZZ_chromedriver/chromedriver')
    driver.implicitly_wait(3)
    sleep(0.5)
    
    Bond_name = name[n][0:5] 

    chrome_options = webdriver.ChromeOptions() #
    chrome_options.add_argument('--headless')
    #chrome_options.add_argument("--disable-gpu") # 보험  
    chrome_options.add_argument("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36")
    driver = webdriver.Chrome('/Users/kimsanghyun/Lets_Get_rich/ZZ_chromedriver/chromedriver',chrome_options=chrome_options)
    driver.implicitly_wait(2)

    driver.get('https://8percent.kr/deals/' + str(Bond_name)) #
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    return soup


# 변수항목
#name = name[0:5] #개만 임시로 추출한다. 
'''for n in range(len(name)): 
    Subsoup = crawl_SubPage(name, n)''' #in: name = Filter_BondNum(soup)

# 함수항목
def Filter_NL(soup): #1차 정제항목
    test_text=[]
    for n in range(len(soup.body.article.find_all('div'))):        
        test_text.append(str(soup.body.article.find_all('div')[n].text.replace('\n', '')))
    return test_text #채권페이지의 자연어를 축출한다.

# 변수항목
# ['신용 정보  ※ 최근 1년간 월별 KCB 점수 변화   KCB 등급 5등급 KCB 점수 733점 ', ' ※ 최근 1년간 월별 KCB 점수 변화   KCB 등급 5등급 KCB 점수 733점 ', ' ※ 최근 1년간 월별 KCB 점수 변화', '', '', '', '', '', '', '  KCB 등급 5등급 KCB 점수 733점 ', '소득 정보 월 평균 소득  575만원   소득형태 근로소득자 직장규모 코스피상장사 재직기간 19.3년', '카드사용 정보 월 평균 사용 금액    월 평균 사용 금액은 할부 등이 반영되지 않은, 과거 12개월 카드 총 이용금액을 단순평균한 금액입니다.  291만원   신용카드 총 한도  2,850만원 이용 카드개수 2장', '   월 평균 사용 금액은 할부 등이 반영되지 않은, 과거 12개월 카드 총 이용금액을 단순평균한 금액입니다.', '', '월 평균 사용 금액은 할부 등이 반영되지 않은, 과거 12개월 카드 총 이용금액을 단순평균한 금액입니다.', '월 평균 사용 금액은 할부 등이 반영되지 않은, 과거 12개월 카드 총 이용금액을 단순평균한 금액입니다.', '월 평균 사용 금액은 할부 등이 반영되지 않은, 과거 12개월 카드 총 이용금액을 단순평균한 금액입니다.', '부채 정보 보유 대출 7건 총 대출 잔액 3억 9,865만원 총 대출 잔액 (7건) 3억 9,865만원   대출잔액 / 약정금액 캐피탈 (2)            2,695만원          /                       2,960만원          은행 (1)            6,000만원          /                      정보없음          담보 (4)           3억 1,170만원          /                      정보없음          ', '보유 대출 7건 총 대출 잔액 3억 9,865만원', '보유 대출 7건', '총 대출 잔액 3억 9,865만원', '총 대출 잔액 (7건) 3억 9,865만원']
# SubSoupText = Filter_NL(Subsoup) #Subsoup = crawl_SubPage(name, 0)

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
# DebtData_List = Filter_DebtData(SubSoupText) #DebtData_List = Filter_DebtData(SubSoupText[1]) #여러개를 크롤링할 때


# 함수항목
def Filter_missing_DebtData(SubSoupText, DebtData_List):

    Null_List_2 = SubSoupText[-1].split()[3].replace('(','')
    Null_List_2 = Null_List_2.replace(')','')
    Null_List_2 = Null_List_2.replace('건','')
    #print(Null_List_2)

    Null_List_1 = []
    for n in range(len(DebtData_List)):
        conv = DebtData_List[n][1]
        conv = conv.replace('(','')
        conv = conv.replace(')','')
        Null_List_1.append(int(conv))
        #print(sum(Null_List_1))

    if Null_List_2 == sum(Null_List_1):
        return True #누락 없음
    else:
        return False #누락이 있음

# 변수항목
# True / False
# LND_missing_Debt = Filter_missing_DebtData(SubSoupText, DebtData_List)

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
# LND_P2P = Filter_P2P(SubSoupText)

# 함수항목
def Filter_Income(test_text):
    want_list = test_text
    for n in range(len(want_list)):
        NullList = want_list[n].split()
        if len(NullList) > 0: # [] 리스트가 비어있는 경우
            if NullList[0] == "소득" and NullList[1] == "정보":
                Null1 = want_list[n].split()
                result = [Null1[5], Null1[-3], Null1[-1]]
            elif NullList[0] == "매출" and NullList[1] == "정보":
                Null1 = want_list[n].split()
                result = [Null1[5], Null1[-3], Null1[-1]]
    return result

# 변수항목
# ['575만원', '코스피상장사', '19.3년']
# Income = Filter_Income(SubSoupText)

# 함수항목
def Filter_Job(income):
    Cre = float(income[2].replace('년', ''))
    if income[1] == '공기업/공무원':
        result = True
        return result
    elif income[1] == '코스피상장사':
        if 3 <= Cre   and Cre <= 12:
            result = True
            return result

    elif income[1] == '중기업':
        if 5 <= Cre and Cre <= 12:
            result = True
            return result

    else:
        result = False
        #if income[1] == '소기업':
        return result

# 변수항목
# LND_Job = Filter_Job(Income)

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
# Expense = Filter_Expense(SubSoupText)

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
# Credit = Filter_Credit(SubSoupText)


# 함수항목
def Filter_lonereq(soup): #대출신청 정보 계산
    '''
    세전 수익률, 상환기간, 모집금액(사람들이 넣은 돈), 대출금액(대출자가 모으고 싶은 돈)
    '''
    moneyList = []
    
    def str_to_float(strInBond):
        if len(strInBond) > 4:
            strInBond = strInBond.replace(',', '')
            strInBond = float(strInBond)
            return strInBond
        else:
            strInBond = float(strInBond)
            return strInBond

    profit = soup.body.main.header.div.find_all('p')[3].text #수익률
    profit = profit.replace('%', '')
    profit = float(profit)
    
    period = soup.body.main.header.div.find_all('p')[5].text #상환기간
    period = period.replace('개월', '')
    period = int(period)
    
    money = soup.body.main.header.div.find_all('p')[9].text #상환금액

    money_gathering  = money.split('\n')[1].replace(' ', '') #모집금액(사람들이 넣은 돈)
    money_gathering = str_to_float(money_gathering)
    
    money_gathered = money.split('\n')[3].replace(' ', '') #대출금액(대출자가 모으고 싶은 돈)
    money_gathered = str_to_float(money_gathered)
    
    moneyList.append(profit) 
    moneyList.append(period) 
    moneyList.append(money_gathering) 
    moneyList.append(money_gathered) 
    return moneyList

# 변수항목
# lonereq_List = Filter_lonereq(Subsoup)


# 함수항목
def Calculate_InterestCost(Debts, Credit):
    '''
    Debts = Filter_DebtData(test_text)
    Credit = Filter_Credit(test_text)

    인자: 채무유형, 신용정보
    함수값: 매월 할부상환할 원금과 이자비용
    '''

    # 신용등급 문자열 > 수
    Credit = Credit[0].replace('등급','')
    Credit = int(Credit[0])
    
    def MIR(Pv, r, n):  # 함수안에 함수 월 할부상환함수(Monthly_installment_repayment MIR)
        return (Pv*((1+r/100)**n))/(12*n)

    def handling_MIR(Debts, r, n):
        if Debts[2][-1] == '억': #1억 1000만원 
            Million100 = Debts[2].replace('억','')
            Million100 = float(Million100)

            Million10 = Debts[3].replace('만원','')
            if len(Million10) > 4: #(,)를 처리하기 위해 
                Million10 = float(Million10.replace(',',''))
                Nullver = Million100*10000 + Million10
                return MIR(Nullver, r, n)

            else:
                Million10 = float(Million10)
                Nullver = Million100*10000 + Million10
                return MIR(Nullver, r, n)

        elif Debts[2][-2] == '억' and Debts[2][-1] == '원': #1억원
            Million100 = float(Debts[2].replace('억원',''))
            Nullver = Million100*10000
            return MIR(Nullver, r, n)

        else:
            Nullver = Debts[2].replace('만원','')
            if len(Nullver) > 4:
                Nullver = float(Nullver.replace(',',''))
                return MIR(Nullver, r, n)
                
            else:
                Nullver = float(Nullver)
                return MIR(Nullver, r, n)

    # 월 할부상환
    NullList = []
    for n in range(len(Debts)):
        
        #중액 중금리
        if Debts[n][0] == '캐피탈': #5년 할부상환 6% 시작 2%가산
            r = 6 + 2*Credit
            D = 5
            NullList.append(handling_MIR(Debts[n], r, D))
            
        if Debts[n][0] == '저축은행': #5년 할부상환 6% 시작 2%가산
            r = 6 + 2*Credit
            D = 5
            NullList.append(handling_MIR(Debts[n], r, D))        
            
        if Debts[n][0] == 'P2P': #1년 할부상환 12% 시작 1.5%가산
            r = 6 + 2*Credit
            D = 1
            NullList.append(handling_MIR(Debts[n], r, D))    

        # 소액 고금리
        if Debts[n][0] == '보험': #5년 할부상환 12% 시작 1.5%가산
            r = 12 + Credit*1.5
            D = 5
            NullList.append(handling_MIR(Debts[n], r, D))    
            
        if Debts[n][0] == '카드': #5년 할부상환 12% 시작 1.5%가산
            r = 12 + Credit*1.5
            D = 5
            NullList.append(handling_MIR(Debts[n], r, D))    
            
        if Debts[n][0] == '현금서비스': #5년 할부상환 12% 시작 1.5%가산
            r = 12 + Credit*1.5
            D = 5
            NullList.append(handling_MIR(Debts[n], r, D))    

        # 고액 저금리
        if Debts[n][0] == '은행': #은행은 마이너스 통장 금리 
            r = 0 + Credit*3
            D = 10
            NullList.append(handling_MIR(Debts[n], r, D))             
            
        if Debts[n][0] == '담보': #부동산담보 부동산 담보는 신용등급 1로 가정 (Nullver*((1+1*3/(100))**15))/(12*15)
            r = 3
            D = 15
            NullList.append(handling_MIR(Debts[n], r, D)) 
            
        if Debts[n][0] == '학자금': #부동산담보 부동산 담보는 신용등급 1로 가정 (Nullver*((1+1*2.25/(100))**15))/(12*10)
            r = 2.25
            D = 10
            NullList.append(handling_MIR(Debts[n], r, D)) 
    
    return sum(NullList)

# 변수항목
# Cost_of_Interest = Calculate_InterestCost(DebtData_List, Credit)


#함수항목
def Filter_CF(SubSoup): 
    '''
    기능: 채권 현금흐름의 현재가치를 추산한다.
    인자: Subsoup = crawl_SubPage(name, 0)의 Subsoup이다. 
    함수값: [매월 받는 현금흐름, 일시상환하는 현금흐름, 총 현금흐름의 합]
    현금흐름 기준 할인율은 1.3으로 설정한다.
    
    '''
    CF_Soup = SubSoup.html.body.find_all('p')[14].text
    CF_Soup = CF_Soup.split(' ')
    def Pv(Fv, r, n):
        return Fv/((1+r/100)**n)

    def flowList(flow, Last, r, n):
        flowList = []
        for n in range(1, 12):
            flowList.append(Pv(flow/n, r/n, n))
        return [flow, Last, sum(flowList) + Pv(Last, r, 1)]

    if CF_Soup[-3] == '만기일시상환' and CF_Soup[-5] == '원리금균등,':
        
        if len(CF_Soup[-4]) > 4:
            CF_Soup[-4] = CF_Soup[-4].replace('만원은','')
            Last = float(CF_Soup[-4].replace(',',''))
            CF_Soup[-6] = CF_Soup[-6].replace('만원은','')
            flow = float(CF_Soup[-6].replace(',',''))
            return flowList(flow, Last, 1.3, 12)
        else: 
            Last = float(CF_Soup[-4].replace('만원은',''))
            flow = float(CF_Soup[-6].replace('만원은',''))

            return flowList(flow, Last, 1.3, 12)
    else:
        return False

# 변수항목
# CF_List = Filter_CF(Subsoup)

# 함수항목
def Calculate_OverHaed(Income, Expense, int_Cost, lonereq):
    def Fv(Pv, r, n):
        return Pv*((1+r/100)**n)

    Nullvar1 = Income[0].replace('만원','')
    Nullvar2 = Expense[0].replace('만원','')
    Nullvar3 = Fv(lonereq[-1], lonereq[1], 1)/12 #이번 대출을 통한 월균등 상환액

    if len(Nullvar1) > 4:
        Nullvar1 = float(Nullvar1.replace(',',''))
    else:
        Nullvar1 = float(Nullvar1)
    if len(Nullvar2) > 4:
        Nullvar2 = float(Nullvar2.replace(',',''))
    else:
        Nullvar2 = float(Nullvar2)

    return Nullvar1 - (Nullvar2 + int_Cost + Nullvar3)


# 변수항목
'''SafeList = Calculate_OverHaed(Income, Expense, Cost_of_Interest, lonereq_List)
Null_SafeList = []
Null_SafeList.append(SafeList)'''


# 함수항목
def Calculate_lone_DN(LND_missing_Debt, LND_P2P, LND_Job): 
    '''
    기능: 대출 거절 사유를 표시한다. 
    인자: 
    함수값: 
    [True, True, True] #대출허가
    [True, False, True] #대출불허 P2P채무존재
    [True, True, False] #대출불허 직업요건 불충족
    '''
    Null_ND = []
    if LND_missing_Debt == True: #누락이 없는 경우(허가 요건)
        Null_ND.append(True)
    else:
        Null_ND.append(False)

    if LND_P2P == True: #P2P채무있음(불허 요건)
        Null_ND.append(False)
    else:
        Null_ND.append(True)

    if LND_Job == True: #허가 요건
        Null_ND.append(True)
    else:
        Null_ND.append(False)
    return Null_ND

#변수항목
'''NDList = Calculate_lone_DN()
Null_NDList = []
Null_NDList.append(NDList)'''

# 함수항목
def OutPut_spreadsheet(name, Null_SafeList, Null_NDList):

    testframe = pd.DataFrame({
        '채권번호':name, #name = Filter_BondNum(soup)
        '인정성지수':Null_SafeList, #SafeList = Calculate_OverHaed(Income, Expense, int_Cost, lonereq)
        '거절요건성립':Null_NDList #NDList = Calculate_lone_DN()
    })
    # [채권번호, 채권안정성, 투자요건]
    testframe.to_csv('/Users/kimsanghyun/Lets_Get_rich/aa_test_product/BondTrading/Runing_BondTrad/OutPut/BondData_2020_05_20.csv',  index = False, header = True)
    return testframe

def RunAll():
    '''
            if n == -2: # Null 버그픽스 
            Null_SafeList.append(False)
            Null_NDList.append(False)
            pass
        elif n == -1: # 28 31233호 AttributeError: 'NoneType' object has no attribute 'find_all'
            Null_SafeList.append(False)
            Null_NDList.append(False)   
            pass
    '''
    soup = crawl_MainPage()
    name = Filter_BondNum(soup)

    Null_SafeList = []
    Null_NDList = []
    for n in range(len(name)): 
        print(n)
        print(name[n])
        try:
            Subsoup = crawl_SubPage(name, n)
            SubSoupText = Filter_NL(Subsoup)
            DebtData_List = Filter_DebtData(SubSoupText)
            LND_missing_Debt = Filter_missing_DebtData(SubSoupText, DebtData_List)
            LND_P2P = Filter_P2P(SubSoupText)
            Income = Filter_Income(SubSoupText)
            LND_Job = Filter_Job(Income)
            Expense = Filter_Expense(SubSoupText)
            Credit = Filter_Credit(SubSoupText)
            lonereq_List = Filter_lonereq(Subsoup)

            Cost_of_Interest = Calculate_InterestCost(DebtData_List, Credit)
            #CF_List = Filter_CF(Subsoup)
            SafeList = Calculate_OverHaed(Income, Expense, Cost_of_Interest, lonereq_List)
            Null_SafeList.append(SafeList)
            NDList = Calculate_lone_DN(LND_missing_Debt, LND_P2P, LND_Job)
            Null_NDList.append(NDList)
        except AttributeError:
            print('AttributeError')
            Null_SafeList.append(False)
            Null_NDList.append(False)   
            
    OutPut_spreadsheet(name, Null_SafeList, Null_NDList)

RunAll()
#Bot
