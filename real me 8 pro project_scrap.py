import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
page_num=input("Enter the page number")


Rating=[]
Review=[]
sentiment=[]   

for i in range(1,int(page_num)+1):
    
    url=("https://www.flipkart.com/realme-8-pro-illuminating-yellow-128-gb/product-reviews/itmaa9c73f5a987c?pid=MOBGYV98ESYUZZUK&lid=LSTMOBGYV98ESYUZZUKJK4O6X&marketplace=FLIPKART&page="+str(i))
    req=requests.get(url)
    
    content=BeautifulSoup(req.content,'html.parser')
    
    
    #fetching ratings
    rating=content.find_all('div',{"class":["_3LWZlK _1BLPMq","_3LWZlK _1rdVr6 _1BLPMq","_3LWZlK _32lA32 _1BLPMq"]})
    
    review=content.find_all('p',{"class":"_2-N8zT"})
    
    for i in rating:
        Rating.append(i.text)
        
    for j in review:
        Review.append(j.text)
    
for i in Rating:
    if (int(i)>2):
        sentiment.append('positive')
    else:
        sentiment.append('negative')
           
data={"Rating":Rating,"Review":Review,"Sentiment":sentiment}
df=pd.DataFrame(data)
print(df)
df.to_csv('Realme_8_pro_review .csv',index=False)