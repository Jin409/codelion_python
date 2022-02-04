import requests
from bs4 import BeautifulSoup
url = "https://datalab.naver.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text,'html.parser')

dates =  soup.findAll("span","title_cell")
results = soup.findAll("span","title")
cnt = 0
for i in range(len(dates)-2):
    print(dates[i].get_text(),"의 실시간 급상승 검색어입니다.")
    n=1
    for j in range(cnt,cnt+10):
        print(n,"위 : ",results[j].get_text())
        n+=1
    print("\n")
    cnt+=10