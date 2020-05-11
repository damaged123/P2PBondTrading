


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
            Nullver = Debts[n][2].replace('만원','')
            
            if len(Nullver) > 4:
                Nullver = Nullver.replace(',','')
                Nullver = int(Nullver)
                
                print('캐피탈')
                DebtWithInt = (Nullver*((1+(6+Credit*2)/100)**5))/(12*5)
                print(DebtWithInt)
                NullList.append(DebtWithInt)
                
            else:
                Nullver = int(Nullver)
                
                print('캐피탈')
                DebtWithInt = (Nullver*((1+(6+Credit*2)/100)**5))/(12*5)
                print(DebtWithInt)
                NullList.append(DebtWithInt)
            
        if Debts[n][0] == '저축은행': #5년 할부상환 6% 시작 2%가산
            Nullver = Debts[n][2].replace('만원','')
            if len(Nullver) > 4:
                Nullver = Nullver.replace(',','')
                Nullver = int(Nullver)
                
                print('저축은행')                
                DebtWithInt = (Nullver*((1+(6+Credit*2)/100)**5))/(12*5)
                print(DebtWithInt)
                NullList.append(DebtWithInt)
                
            else:
                Nullver = int(Nullver)
                
                print('저축은행')                
                DebtWithInt = (Nullver*((1+(6+Credit*2)/100)**5))/(12*5)
                print(DebtWithInt)
                NullList.append(DebtWithInt)
            
        if Debts[n][0] == 'P2P': #1년 만기
            Nullver = Debts[n][2].replace('만원','')
            if len(Nullver) > 4:
                Nullver = Nullver.replace(',','')
                Nullver = int(Nullver)
                
                print('P2P')
                DebtWithInt = (Nullver*((1+Credit*3/100)**1))/(12*1)
                print(DebtWithInt)
                NullList.append(DebtWithInt)
                
            else:
                Nullver = int(Nullver)
                
                print('P2P')
                DebtWithInt = (Nullver*((1+Credit*3/100)**1))/(12*1)
                print(DebtWithInt)
                NullList.append(DebtWithInt)

        # 소액 고금리
        if Debts[n][0] == '보험': #5년 할부상환 12% 시작 1.5%가산
            Nullver = Debts[n][2].replace('만원','')
            if len(Nullver) > 4:
                Nullver = Nullver.replace(',','')
                Nullver = int(Nullver)
                
                DebtWithInt = (Nullver*((1+(10.5+Credit*1.5)/100)**5))/(12*5)
                print('보험')
                print(DebtWithInt)
                NullList.append(DebtWithInt)
                
            else:
                Nullver = int(Nullver)
                
                DebtWithInt = (Nullver*((1+(10.5+Credit*1.5)/100)**5))/(12*5)
                print('보험')
                print(DebtWithInt)
                NullList.append(DebtWithInt)
            
        if Debts[n][0] == '카드': #5년 할부상환 12% 시작 1.5%가산
            Nullver = Debts[n][2].replace('만원','')
            if len(Nullver) > 4:
                Nullver = Nullver.replace(',','')
                Nullver = int(Nullver)
                
                DebtWithInt = (Nullver*((1+(10.5+Credit*1.5)/100)**5))/(12*5)
                print('카드')
                print(DebtWithInt)
                NullList.append(DebtWithInt)
                
            else:
                Nullver = int(Nullver)
                
                DebtWithInt = (Nullver*((1+(10.5+Credit*1.5)/100)**5))/(12*5)
                print('카드')
                print(DebtWithInt)
                NullList.append(DebtWithInt)
            
        if Debts[n][0] == '현금서비스': #5년 할부상환 12% 시작 1.5%가산
            Nullver = Debts[n][2].replace('만원','')
            if len(Nullver) > 4:
                Nullver = Nullver.replace(',','')
                Nullver = int(Nullver)
                
                DebtWithInt = (Nullver*((1+(10.5+Credit*1.5)/100)**5))/(12*5)
                print('현금서비스')
                print(DebtWithInt)
                NullList.append(DebtWithInt)
                
            else:
                Nullver = int(Nullver)
                
                DebtWithInt = (Nullver*((1+(10.5+Credit*1.5)/100)**5))/(12*5)
                print('현금서비스')
                print(DebtWithInt)
                NullList.append(DebtWithInt)
        
        # 고액 저금리
        if Debts[n][0] == '은행': #은행은 마이너스 통장 금리
            Nullver = Debts[n][2].replace('만원','')
            if len(Nullver) > 4:
                Nullver = Nullver.replace(',','')
                Nullver = int(Nullver)
                
                DebtWithInt = (Nullver*((1+Credit*3/(100))**10))/(12*10)
                print('은행')
                print(DebtWithInt)
                NullList.append(DebtWithInt)
                
            else:
                Nullver = int(Nullver)
                
                DebtWithInt = (Nullver*((1+Credit*3/(100))**10))/(12*10)
                print('은행')
                print(DebtWithInt)
                NullList.append(DebtWithInt)
            
        if Debts[n][0] == '담보': #부동산담보 부동산 담보는 신용등급 1로 가정
            Nullver = Debts[n][2].replace('만원','')
            if len(Nullver) > 4:
                Nullver = Nullver.replace(',','')
                Nullver = int(Nullver)
                
                DebtWithInt = (Nullver*((1+1*3/(100))**20))/(12*20)
                print('담보')
                print(DebtWithInt)
                NullList.append(DebtWithInt)
                
            else:
                Nullver = int(Nullver)
                
                DebtWithInt = (Nullver*((1+1*3/(100))**20))/(12*20)
                print('담보')
                print(DebtWithInt)
                NullList.append(DebtWithInt)
            
        if Debts[n][0] == '학자금': #부동산담보 부동산 담보는 신용등급 1로 가정
            Nullver = Debts[n][2].replace('만원','')
            Nullver = Debts[n][2].replace('만원','')
            if len(Nullver) > 4:
                Nullver = Nullver.replace(',','')
                Nullver = int(Nullver)
                
                DebtWithInt = (Nullver*((1+1*3/(100))**15))/(12*15)
                print('학자금')
                print(DebtWithInt)
                NullList.append(DebtWithInt)
                
            else:
                Nullver = int(Nullver)
                
                DebtWithInt = (Nullver*((1+1*3/(100))**15))/(12*15)
                print('학자금')
                print(DebtWithInt)
                NullList.append(DebtWithInt)
    
    return sum(NullList)

 



