import Eight_Per_Cent
import pandas as pd
'''
def OverHead(test_text, soup):
    gain = NetIncome(test_text)

    Debts = find_debt_index_in_string(test_text)

    Credit = find_Credit_index_in_string(test_text)

    soup = crawl_investment_individual()

    lose = Debt_Calculation(Debts, Credit) + (lonereq(soup)[-1]*(1+lonereq(soup)[0]/100))/lonereq(soup)[1]

    result = gain - lose

    return result'''

def RunAll():
    #GetFromMainPage에서 가져올 것들
    soup = Eight_Per_Cent.GetFromMainPage.crawl_investment_individual() #신용채권 메인페이지를 들어간다.
    name = Eight_Per_Cent.GetFromMainPage.ListOfBonds(soup) #채권번호를 추출한다. 

    #GetFromSubPage에서 가져올 것들
    soup = Eight_Per_Cent.GetFromSub.Get_individual_data(name, 0) #name리스트의 인덱스를 인자로 활용한다. 나중에 for문에 활용한다. 
    souptext = Eight_Per_Cent.GetFromSub.get_NLB(soup)
    
    #FilterFromSubPage
    Income = Eight_Per_Cent.FilterFromSubPage.find_Income_index_in_string(souptext)
    Expense = Eight_Per_Cent.FilterFromSubPage.find_Expense_index_in_string(souptext)
    Credit = Eight_Per_Cent.FilterFromSubPage.find_Credit_index_in_string(souptext)
    Debts = Eight_Per_Cent.FilterFromSubPage.find_debt_index_in_string(souptext)

    #필수 정보 확인(채무유형 누락, 타사 P2P 이용)
    Eight_Per_Cent.FilterFromSubPage.get_missing_date(souptext)
    Eight_Per_Cent.FilterFromSubPage.find_P2P_debt(souptext)

    Cost_of_Interest = Eight_Per_Cent.Debt_Calculation.InterestCost(Debts,Credit) #Debt_Calculation.py모듈인식 불가

    Eight_Per_Cent.FilterFromSubPage.lonereq(souptext)

    '''result = Eight_Per_Cent.Base_Eight_Per_Cent.OverHead(souptext, soup)'''
    print(Income)
    print(Expense)
    print(InterestCost)
    pass



def excel():
    soup = Eight_Per_Cent.GetFromMainPage.crawl_investment_individual()
    name = Eight_Per_Cent.GetFromMainPage.ListOfBonds(soup) #채권번호를 추출한다. 
    testframe = pd.DataFrame({'채권번호':name}) #지수화하고 번호옆 옆에 표시하기

    #일단 내보내는 법. 파일 주소랑 이름
    testframe.to_csv('Users/kimsanghyun/Lets_Getrich/aa_test_product/BondTrading/BondsData_2020_05_11.csv',  index = False, header = True)
    return testframe


'''
testframe = pd.DataFrame({'채권번호':[10000,20000,34103, 51324],
'채권이자':[4,8,12,21],
'투자가능액':[1000,1200,3100, 200]})
#일단 내보내는 법
testframe.to_csv('BondsData.csv') #파일 주소랑 이름
'''

#RunAll()
#excel()

import os
print(os.getcwd())
