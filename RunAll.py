import Eight_Per_Cent
import GetFromMainPage
import GetFromSub
import FilterFromSubPage
import Base_Eight_Per_Cent
import Debt_Calculation

def RunAll():
    #GetFromMainPage에서 가져올 것들
    soup = GetFromMainPage.crawl_investment_individual()
    name = GetFromMainPage.ListOfBonds(soup)

    #GetFromSubPage에서 가져올 것들
    soup = GetFromSub.Get_individual_data(name, 0)
    souptext = GetFromSub.get_NLB(soup)
    
    #FilterFromSubPage
    Income = FilterFromSubPage.find_Income_index_in_string(souptext)
    Expense = FilterFromSubPage.find_Expense_index_in_string(souptext)
    Credit = FilterFromSubPage.find_Credit_index_in_string(souptext)
    Debts = FilterFromSubPage.find_debt_index_in_string(souptext)

    #필수 정보 확인(채무유형 누락, 타사 P2P 이용)
    FilterFromSubPage.get_missing_date(souptext)
    FilterFromSubPage.find_P2P_debt(souptext)

    InterestCost = Debt_Calculation.Debt_Calculation(Debts,Credit) #Debt_Calculation.py모듈인식 불가

    FilterFromSubPage.lonereq(souptext)

    result = Base_Eight_Per_Cent.OverHead(souptext, soup)
    print(Income)
    print(Expense)
    print(InterestCost)
    return result



def exle():
    '''
    엑셀로 뽑자
    '''
    pass

RunAll()
