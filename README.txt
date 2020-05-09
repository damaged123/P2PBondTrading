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
