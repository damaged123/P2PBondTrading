from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

# 소득 정보를 찾는 함수
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
        result = True
        print('누락 된 부채유형이 없음')
    else:
        result = False #분석 중단이유
        print('누락된 채무유형이 있음') 

    return result

def find_P2P_debt(test_text): #P2P채무가 있고 없는지를 알아낸다. 
    findText = find_debt_index_in_string(test_text)
    null = []
    for n in findText:
        for m in n:
            if m == 'P2P':
                null.append(1)
    if null == [1]:
        result = True #심사 거부 이유
        print('P2P채무 있음')
    else:
        result = False
        print('P2P채무 없음')
    
    return result

#대출신청 정보 계산
def lonereq(soup):
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

def NetIncome(test_text): #24%최대 이자로 일률적으로 적용하며 10년 만기로 설정한다. 추산이자채무상환액 = 원금/12*10(10년만기균등상환)+원금*3%이자(이자비용+ 쿠션1%)
    #추가 대출금에 다한 반영X
    '''
    '''
    Income = find_Income_index_in_string(test_text)[0]
    Income = Income.replace('만원','')
    Income = Income.replace(',','')
    Income = int(Income)
    Expense = find_Expense_index_in_string(test_text)[0]
    Expense = Expense.replace('만원','')
    Expense = Expense.replace(',','')
    Expense = int(Expense)
    
    result = Income - (Expense)
    return result

#OverHead

#Test
'''if __name__ == "__main__":
    NetIncome()'''