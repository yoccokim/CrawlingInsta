Hello
==

"서울특별시 맛집 리스트 작성"을 목표로 시작한 작업입니다.
연구의 최초 목표는 위와 같았으나 정보 수집 후 전처리 된 단어의 
빈도를 계산하는 것에서 그치는 것이 아니라 더 나아가 한국어 자연어 처리를 통해 
토큰화 한 후 t-SNE 를 통해 시각화 하여 분석해봤습니다. 

Example.zip
-----------

인스타그램 크롤러를 통해 3가지 검색어에 대해서 추출한 Excel file 입니다.

Usage
-----

* 작성자는 Anconda를 통해 Python 3.7 버전을 이용하였으며 운영체제는 Windows 10 64bit 입니다.
1. 자신의 Chrome Version과 맞는 Chromedriver.exe 를 설치하여 Scripts 폴더에 위치시킨다. (이게 편함)
2. Crawler 사용을 위해 본문에서 사용한 모든 모듈을 설치했는지 확인하고 설치 혹은 Update 한다.
3. ChromeDriver.exe의 경로를 정확히 입력한다.
4. 그 이후로는 모듈이 구동이 되었다면 막히는 것 없이 사용할 수 있다.


Model
-----
처음 모델 학습을 하는 과정에서 
```"c extension not loaded training will be slow" ```
위와 같은 코드와 함께 적은 단어 수에 비해 작업 시간이 너무 오래걸려 비슷한 증상을 찾고
gensim을 제거 후 재설치 + Upgrade로 해결함.


Image
-----
![단어유사도](https://user-images.githubusercontent.com/49060963/58534439-4d5fc180-8226-11e9-9400-429eb7b6486b.JPG)
###### 한국어 자연어 전처리 후 (soynlp) 단어간 유사성을 구해봄
###### X 를 인스타 검색어(예제에서는 신촌맛집, 이태원맛집, 제주도맛집)을 입력했고 Y는 모든 단어들의 집합

![시각화원본](https://user-images.githubusercontent.com/49060963/58534480-65374580-8226-11e9-93c1-a2bcbd4f0ae3.JPG)
###### Plot으로 t-SNE를 시각화 하였다.

![확대](https://user-images.githubusercontent.com/49060963/58534488-69fbf980-8226-11e9-8c59-b7b92cc683c4.JPG)
###### 여러 단어가 뭉쳐있는 부분을 확대한 Image.




End...
------
우리 팀원 모두 처음 해보는 연구이고 (라고 쓰고 공부라고 읽는다) 아무도 python 언어에 익숙치 않았기 때문에 코딩한 것이 굉장히 조잡하다.
양해 바라며 의도에 맞게 연구를 한 것이기를.... py 본문의 내용 대부분이 구글링을 통해 얻은 해답이었고 프로그래머즈에서 많은 도움을 받았다.

