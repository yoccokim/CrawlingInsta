#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import csv
import time
import os
from selenium.webdriver.common.keys import Keys
import pandas as pd
import re 
import numpy as np
import pprint # 출력 깔끔하게 하는 모듈

options = webdriver.ChromeOptions() 
options.add_argument('headless')  #크롬 옵션인데 창 보이게 할지 안할지 , 안보이게 하고 싶으면 chrome_options=options 입력
options.add_argument("lang=ko_KR")


# In[2]:


import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import matplotlib as mpl  # plot  관련 모듈
from future.utils import iteritems
from collections import Counter
from sklearn.manifold import TSNE # T분포 확률적 임베딩 모듈
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer


# In[3]:


def wait(browser, sec):
    time.sleep(sec)
    browser.implicitly_wait(sec)
    
def ReEmoji(asd): # 한글과 띄어쓰기를 제외한 모든 부분을 제거
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+') 
    result = hangul.sub('', asd) 
    return result

def reMove(Fn):
    LA = [] # 해시태그 지우면서 띄우고, 그다음 하나씩 나누기
    for i in Fn['Post']:
        Fl = i.replace("#"," ")
        fl = Fl.split()
        LA.append(fl)
    LB = sum(LA, []) # 2중 리스트 지우기
    return LB

def re2list(맛집리스트):
    J = " ".join(맛집리스트)
    LC = ReEmoji(J)
    list_LC = LC.split()
    return list_LC


# In[3]:


driver_dir = 'C:\\Users\\John\\Anaconda3\\Scripts\\chromedriver'

A = []

query = input("* 검색어 입력: ")

times = int(input("* 게시물 개수 입력: "))
print("* 브라우저 실행 중...")
browser = webdriver.Chrome(driver_dir)
browser.get("https://www.instagram.com/explore/tags/{}".format(query))

wait(browser,2)

browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]').click()

wait(browser, 5)

name = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/h2/a').text
post = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/div[1]/ul/li[1]/div/div/div/span').text
post1 = post.replace('\n', ' ')
post2 = post1.replace('.', '')
Likes = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div/button/span').text
List = [name, post2, Likes]
A.append(List)
browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a').click()                       
wait(browser,2)

Tryyy = 0 
while Tryyy < times:
    try:
        name = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/h2/a').text
        post = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/div[1]/ul/li[1]/div/div/div/span').text
        post1 = post.replace('\n', ' ')
        post2 = post1.replace('.', '')
        Likes = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div/button/span').text
        List = [name, post2, Likes]
        A.append(List)
        browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()
        wait(browser,2)
        
        Tryyy= Tryyy + 1
        
    except:
        browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()
        wait(browser,1)
        

Col = ["Name", "Post", "Likes"]
df = pd.DataFrame.from_records(A, columns = Col)
dfX = df.drop_duplicates(['Name']) # 이름 중복 제거
dfY = dfX.drop_duplicates(['Post']) # 같은 글 중복 제거
Fn = pd.DataFrame.from_records(dfY, columns = Col) # 0번부터 재배열
Fn.to_excel(query + '.xlsx', sheet_name='sheet1') #excel 파일로 만들기


print("* 완료")


# In[16]:


A # Crawling 결과물, 동영상은 자동으로 걸러짐


# In[11]:


len(Fn)


# In[17]:


Col = ["Name", "Post", "Likes"]
df = pd.DataFrame.from_records(A, columns = Col)
df


# In[18]:


dfX = df.drop_duplicates(['Name']) # 이름 중복 제거
dfY = dfX.drop_duplicates(['Post']) # 같은 글 중복 제거
Fn = pd.DataFrame.from_records(dfY, columns = ["Name", "Post", "Likes"]) # 0번부터 재배열
Fn


# In[23]:


LA = [] # 해시태그 지우면서 띄우고, 그다음 하나씩 나누기
for i in Fn['Post']:
    Fl = i.replace("#"," ")
    fl = Fl.split()
    LA.append(fl)
LB = sum(LA, []) # 2중 리스트 지우기  이 스크립트는 함수 안될까봐 쫄려서 냅둠


# In[25]:


re2list(LB) == re2list(reMove(Fn)) # 잘 된건가 확인


# In[74]:


match_pattern=[] #처음 모델 학습 할 줄 몰랐을 때 빈도수 세기 위해서 만들었음.....ㅠㅠ
for item in list_LC:
    word = item.lower()
    match_pattern.append(word)

frequency={}
for word in match_pattern:
    count = frequency.get(word,0) # word가 처음 나왔을 경우 해당 단어에 대해 w1 : 0 이런 식으로 해줌
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
print(frequency_list)
frequency


# In[75]:


wordlist =[ item for item in frequency.keys() ]
wordlist
countlist = [ frequency[item] for item in frequency.keys() ]
countlist
newfreq={ 'word' : wordlist, 'count' : countlist}
#tc = pd.DataFrame.from_dict(newfreq)

tc = pd.DataFrame.from_records(newfreq, columns=['word','count']) # 칼럼 순서
tc = tc.sort_values(["count"], ascending=[False]) # 내림차순 정렬
tc
#tc['word'][tc['count']>=7] 이건 조건부 출력


# In[6]:


# 이건 껐다 켰는데 크롤 자료가 있다면 하단부터 시작


# In[4]:


신촌맛집 = pd.read_excel("신촌맛집.xlsx")
이태원맛집 = pd.read_excel("이태원맛집.xlsx")
제주도맛집 = pd.read_excel("제주도맛집.xlsx")

print(len(신촌맛집), len(이태원맛집), len(제주도맛집))


# In[5]:


del 이태원맛집["Likes"]
이태원맛집["Name"] = "이태원맛집"

del 제주도맛집["Likes"]
제주도맛집["Name"] = "제주도맛집"

del 신촌맛집["Likes"]
신촌맛집["Name"] = "신촌맛집"


# In[6]:


F_list = pd.DataFrame.from_records(신촌맛집.append(이태원맛집).append(제주도맛집))
F_list


# In[7]:


# pd 의 post 이모지를 한번에 제거하고 싶었음

def Noemoji(A):
    j = ReEmoji(A)
    return j


# In[8]:


j = []
for i in F_list["Post"]:
    z = ReEmoji(i)
    j.append(z)


# In[9]:


F_list["Post"] = j


# In[10]:


F_list # 이모지 지운 F_list


# In[11]:


from soynlp.word import WordExtractor # 언어는 soynlp, 띄어쓰기 기반 토큰화기 때문에 고유 명사 추출이 좀더 쉽다
from soynlp.tokenizer import LTokenizer
from gensim.models import Word2Vec
import gensim.models as g

Post_by_hashtag = F_list['Post'].tolist()
word_extractor = WordExtractor(min_frequency=10) # soynlp에서는 빈도수와 관련 된 parameter는 frequency로 통일
word_extractor.train(Post_by_hashtag)
word_scores = word_extractor.extract()

cohesion_scores = {word:score.cohesion_forward for word, score in word_scores.items()}
ltokenizer = LTokenizer(scores = cohesion_scores)
word2vec_corpus = [ltokenizer.tokenize(sent, remove_r=True) for sent in Post_by_hashtag]

Hashtag = F_list['Name'].tolist()

new_word2vec_corpus = []
for i in range(0, len(Post_by_hashtag)):
    k = word2vec_corpus[i]
    k.append(str(Hashtag[i]))
    new_word2vec_corpus.append(k) 

start_time = time.time()
model = Word2Vec(new_word2vec_corpus, size=300, window=10, min_count=10, workers=10, iter=25, sg=1)
model_name = 'By_soynlp'
model.save(model_name)

print("start_time", start_time)
print("--- %s seconds ---" %(time.time() - start_time))


# In[50]:


model = g.Word2Vec.load(model_name)
print(model.most_similar(positive='신촌맛집')) # 신촌맛집 = 인스타 검색어


# In[51]:


model = g.Word2Vec.load(model_name)
print(model.most_similar(positive='제주도맛집'))


# In[52]:


model = g.Word2Vec.load(model_name)
print(model.most_similar(positive='이태원맛집'))


# In[16]:


vocab = list(model.wv.vocab)
X = model[vocab]

print(len(X))
print(X[0][:10])
tsne = TSNE(n_components=2)

X_tsne = tsne.fit_transform(X[:500,:]) # 100개는 너무 적어서 일단 500개 


# In[17]:


Dim = pd.DataFrame(X_tsne, index=vocab[:500], columns=['x', 'y']) 
Dim.shape


# In[72]:


Dim.head(10)


# In[14]:


path = 'C:/Windows/Fonts/gulim.ttc'  # 굴림체 굳
fontprop = fm.FontProperties(fname=path, size=6) # 여기서 폰트 설정을 따로 해놔야 안깨짐
print(fontprop)
fm._rebuild()


# In[18]:


path = 'C:/Windows/Fonts/gulim.ttc'
plt.figure(figsize=(20,10))
fontprop = fm.FontProperties(fname=path, size=10)
plt.scatter(Dim['x'], Dim['y'], s = 20)
for word, pos in Dim.iterrows():
    plt.annotate(word, pos, fontProperties =fontprop)
    
plt.show()


# In[20]:


model.init_sims(replace=True) # 메모리 잡아먹지 말라고 종료


# In[21]:


from gensim.models import word2vec

print(word2vec.FAST_VERSION) ## will be slow.. 문제 확인차 버전 점검함


# In[19]:


#새창
get_ipython().run_line_magic('matplotlib', 'qt5')
path = 'C:/Windows/Fonts/gulim.ttc'
plt.figure(figsize=(20,10))
fontprop = fm.FontProperties(fname=path, size=10)
plt.scatter(Dim['x'], Dim['y'], s = 20)
for word, pos in Dim.iterrows():
    plt.annotate(word, pos, fontProperties =fontprop)
    
plt.show()


# In[ ]:




