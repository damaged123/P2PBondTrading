import baseForEight_Per_Cent

soup = baseForEight_Per_Cent.crawl_investment_individual()
name = ListOfBonds(soup)
soup = Get_individual_data(name)
test_text = get_NLB(soup)

find_P2P_debt(test_text) #부울 함수 True일 때 대출 거부
get_missing_date(test_text) #True일 때 작업정지

Income = find_Income_index_in_string(test_text)
Expense = find_Expense_index_in_string(test_text)
Credit = find_Credit_index_in_string(test_text)
Debts = find_debt_index_in_string(test_text)

Debt_Calculation(Debts, Credit)
OverHead(Income, Expense, Debt_Calculation(Debts, Credit))

