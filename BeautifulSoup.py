from bs4 import BeautifulSoup
import requests
import json
import time

# time.sleep(6 * 3600)

with open('DataDump_Rating.json', 'r') as file:
    content = file.read()
    parsed = json.loads(content)
# print(parsed)

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'cookie': 'CONSENT=YES+NL.en+20150921-01-1; ANID=AHWqTUk2eQsk2nrxU72YW_4xBwqgFy9K-xXEye7AnUTbKCQZ17Cxf9UiT2ocP7d9; HSID=AJ2w3KmyWNRW3RGcy; SSID=AqVJ5qRHQCpf_vO-Q; APISID=Avv22LEpuM_nHlV7/AnNjuyosCN8toPhGL; SAPISID=IMLwsWCKXeZDqHan/A_USwDqQdSuC804rr; __Secure-3PAPISID=IMLwsWCKXeZDqHan/A_USwDqQdSuC804rr; SID=9gdONeUdF6I1SbhNDodo1XrC9bPGGvwWPBjX4CV6K1d1Cr_pxzvmLgK1KbQwxyxpHbSLPw.; __Secure-3PSID=9gdONeUdF6I1SbhNDodo1XrC9bPGGvwWPBjX4CV6K1d1Cr_pFAHEMNEJCh53Ce0HcnYaJg.; GSP=LM=1622975508:S=nW-wFyJsHz3YuwMh; SEARCH_SAMESITE=CgQI5JIB; 1P_JAR=2021-06-10-22; NID=216=HqcvIRTR1ppo-hpqYP-p-BCEiUSWcys6o_icSUhjvjJd8IYTf5fMD6-V41ZVVUPWpXtamFVZL-DbwgjJX3oejBvB7YE6Xv4C5fMJxsrjSSZIv5DEpk7aoND-f9IQnv8eGQHhpr2A0ZK_HarXr_S-N3EsGuUT-D00i5MvkrMCq4vw6hUXhuiWoQNGb5dM15acKJYDpgPi6XafsNlXkaXfj-0kG9Apt7Wn-bhtG6-vQ8rbNmp25WszR6PORQm6maIMrsjkgLR3RV8G80ZueHYcRgaFcIG5Q7yXV8JWPz-1kPLGZxqNkXqTm75OhXhi_-YU4NZd_3uPPjKbBB_ZiXtzC8gGheYTmhE6H6TXY-29; SIDCC=AJi4QfFZRFnRT01_J3nLQ0tTMK6DkxlehLrfgIPPdzeP3x4UH5QybjC666ean2O4UaXm65mq5yI; __Secure-3PSIDCC=AJi4QfEFk1icTI2WdHxgl1qeQEV1AvgOTNgvaU8UPDxpXucVrI19oTsiLwpXY2egJ1bqPz7zb6yd',
}

def find(firstname, middlename, lastname, inst):
    inst = map_inst(inst)
    to_search = f'{firstname} {middlename} {lastname} {inst}'.replace(' ', '+')
    url = f'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q={to_search}&btnG='
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.content, 'lxml')

    for item in soup.find(id='gs_res_ccl_mid'):
        if str(item) == ' ':
            continue
        # print(item)
        # for child in item.children:
        #     print(child)
        children = item.children
        next(children)
        table = next(children)
        str_table = str(table)
        idx = str_table.find('Cited by')
        citations = str_table[idx+9:-24]
        try:
            print(int(citations))
            return int(citations)
        except:
            print(f'this guy sucky sucky big time :( => {firstname} {lastname}')
            return None

def map_inst(s):
    if s == 'University of California Berkeley':
        return 'UC Berkeley'
    if s == 'smth':
        return 'smth else'
    return s


import os
os.remove('results.json')
with open('results.json', 'x') as file:
    file.write('[]')

scores = []
for prof in parsed:
    print(f'lets look at {prof["tFname"]} {prof["tMiddlename"]} {prof["tLname"]} who works dilligently at {prof["institution_name"]}')
    score = find(prof['tFname'], prof['tMiddlename'], prof['tLname'], prof['institution_name'])

    with open('results.json', 'w+') as file:
        filecontent = file.read()
        scores.append({
            'first_name': prof['tFname'],
            'middle_name': prof['tMiddlename'],
            'last_name': prof['tLname'],
            'institution_name': prof['institution_name'],
            "score": score,
        })
        file.write(json.dumps(scores, indent=4))


# find('David', '', 'Torres', 'Universidad de Los Andes')

