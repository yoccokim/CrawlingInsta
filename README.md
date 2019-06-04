Hello
==

"서울특별시 맛집 리스트 작성"을 목표로 시작한 작업이다.

Python의 Selenium을 이용하여 가상의 Chrome Browser로 인스타그램의 검색어에 따른 게시물들의 내용을 가져오는 Crawler를 구축했다. 
이후 수집한 정보들을 특수문자와 Emoji를 제거하고 한글 자연어 처리가 가능한 Soynlp로 토큰화 하였다.
토큰화한 결과물을 gensim 패키지를 활용해 Word2Vec 방법론을 적용했다.
학습시킨 word2vec 모델을 통해 검색어와 가장 비슷한(코사인 유사도가 큰) 단어를 추출했다.
마지막으로 임베딩한 단어 벡터들을 t-sne을 이용해 산점도로 시각화했다.

Example.zip
-----------

Crawler로 추출한 예제 Excel file.

Usage
-----

* 작성자는 Anconda를 통해 Python 3.7 버전을 이용하였으며 운영체제는 Windows 10 64bit.
1. 자신의 Chrome Version과 맞는 Chromedriver.exe 를 설치하여 Scripts 폴더에 위치시킨다. (이게 편함)
2. Crawler 사용을 위해 본문에서 사용한 모든 패키지들을 설치했는지 확인하고 설치 혹은 Update 한다.
3. ChromeDriver.exe의 경로를 정확히 입력한다.
4. 그 이후로는 패키지가 구동만 된다면 막히는 것 없이 사용할 수 있다.


Model
-----
처음 모델 학습을 하는 과정에서

```"c extension not loaded training will be slow" ```

수집한 단어 수에 비해 작업 시간이 너무 오래걸려 인터넷으로 비슷한 증상을 찾았고
gensim을 제거 후 재설치하고 update하는 것으로 해결했다.


Image
-----
![전처리](https://user-images.githubusercontent.com/49060963/58536754-69fef800-822c-11e9-8cbd-5e85795d22f1.JPG)
###### 신촌맛집, 이태원맛집, 제주도맛집의 게시물들을 특수문자와 Emoji 등을 제거 한 후 df의 모습


![단어유사도](https://user-images.githubusercontent.com/49060963/58534439-4d5fc180-8226-11e9-9400-429eb7b6486b.JPG)
###### 한국어 자연어 전처리 후 (soynlp) 단어간 유사성을 구해봄
###### X 를 인스타 검색어(예제에서는 신촌맛집, 이태원맛집, 제주도맛집)을 입력했고 Y는 모든 단어들의 집합


![시각화원본](https://user-images.githubusercontent.com/49060963/58534480-65374580-8226-11e9-93c1-a2bcbd4f0ae3.JPG)
###### Plot으로 t-SNE를 시각화 하였다.


![확대](https://user-images.githubusercontent.com/49060963/58534488-69fbf980-8226-11e9-8c59-b7b92cc683c4.JPG)
###### 여러 단어가 뭉쳐있는 부분을 확대한 Image.




End...
------
우리 팀원 모두 처음 해보는 공부이고 python 언어에 익숙치 않았기 때문에 코딩한 것이 굉장히 조잡하다.
양해 바라며 의도에 맞게 연구를 한 것이기를.... py 본문의 내용 대부분이 구글링을 통해 얻은 해답이었고 프로그래머즈에서 많은 도움을 받았다.
