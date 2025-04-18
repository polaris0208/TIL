# NLP Tools
> [¶ NLTK](#nltk)<br>
[¶ TextBlob](#textblob)<br>
[¶ POS-Tags](#pos-태그-목록)



- 자연어 분석을 위한 전처리 모듈 제공
- 전처리한 자연어 활용 모듈 제공

# NLTK
>**NLTK(Natural Language Toolkit)**
>>파이썬 기반 자연어 처리 라이브러리, 전처리, 분석, 분류 등 다목적 도구상자

## 주요 기능 
1. 텍스트 전처리 : 토큰화, 불용어 제거, 표제어 추출
2. 형태소 분석: 형태나 품사 분석 
3. 정서 분석: 긍정, 부정 등
4. **Corpus** 데이터 제공: 학습이나 실습용 텍스트 데이터 제공
  - 신문기사, 저작권이 만료된 문학작품 등
5. 분류 및 모델링: **NLPP** 기반 텍스트 분류작업 지원

## 설치
1. **NLTK** 설치 
- `pip install nltk`
2. **NLTK Data** 설치
- 기능을 활용하려면 해당 기능에 필요한 데이터 설치
- `'all'` 전체, 필요한 기능만 설치하려면 해당 데이터 이름으로 대치

```py 
import nltk
nltk.download('all')
```

### 데이터 관리
- **NLTK 데이터** 저장 경로 확인
```py
import nltk
print(nltk.data.path)  
```


## Corpus
- 말뭉치: 다양한 형식의 텍스트 데이터

### 주요 말뭉치
1. **Brown Corpus** : 뉴스, 소설, 과학, 논문 등
2. **Gutenberg Corpus** : 고전 문학
3. **Movie Review Corpus** : 영화 리뷰
- 정서 분석에 유용

```py
nltk.corpus.gutenberg.fileids()
emma_raw = nltk.corpus.gutenberg.raw("austen-emma.txt")
print(emma_raw[:1302])
#
[Emma by Jane Austen 1816]

VOLUME I

CHAPTER I


Emma Woodhouse, handsome, clever, and rich, with a comfortable home
and happy disposition, seemed to unite some of the best blessings
of existence; and had lived nearly twenty-one years in the world
with very little to distress or vex her......
```
## Dictionary
- 사전 자료
- `stopwords`: 불용어, `wordnet`: 영어 어휘 데이터베이스

### Wordnet
-  동의어(synonym), 반의어(antonym), 하위어(hyponym) 등 관계 분석

1. 동의어 정의

```py
import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')

syns = wordnet.synsets("wordnet")
print("동의어 및 정의:", syns[0].definition())  # 첫 번째 동의어의 정의 출력
#
동의어 및 정의: any of the machine-readable lexical databases modeled after the Princeton WordNet
```

2. 반의어 찾기
- 동의어를 찾기 `.lemmas()`
- 동의어를 바탕으로 반의어 찾기 `.antonyms()`
- 찾은 단어의 이름 출력 `.name()`

```py
import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')

# 'good'의 동의어, 반의어 가져오기
synonyms = wordnet.synsets('good')

# 동의어 찾기
synonym_list = set(lemma.name() for syn in synonyms for lemma in syn.lemmas())
print("동의어:", synonym_list)

# 반의어 찾기
antonym_list = set(ant.name() for syn in synonyms for lemma in syn.lemmas() for ant in lemma.antonyms())
print("반의어:", antonym_list)

#

동의어: {'undecomposed', 'proficient', 'safe', 'unspoiled', 'good', 'near', 'respectable', 'honest', 'adept', 'skillful', 'ripe', 'secure', 'beneficial', 'skilful', 'in_effect', 'dependable', 'full', 'serious', 'unspoilt', 'honorable', 'just', 'sound', 'upright', 'effective', 'thoroughly', 'right', 'trade_good', 'expert', 'commodity', 'estimable', 'well', 'soundly', 'practiced', 'dear', 'salutary', 'in_force', 'goodness'}
반의어: {'bad', 'ill', 'evilness', 'evil', 'badness'}
```

### Stopwords
- 불용어 사전
- 불용어: 의미 해석에 크게 영향이 없는 단어
- `.union()` : 추가
- `discard()` : 제거

```py
import nltk
from nltk.corpus import stopwords

# NLTK 불용어 다운로드
nltk.download('stopwords')

# 기본 불용어 리스트 가져오기
stop_words = set(stopwords.words('english'))

# 추가할 단어
additional_stopwords = {'example', 'test'}

# 기본 불용어에 추가
stop_words = stop_words.union(additional_stopwords)

# 제거할 단어
stop_words.discard('the')  # 'the'를 제거

# 예시
text = "This is an example test sentence."

# 단어 분리 및 불용어 제거
filtered_words = [word for word in text.lower().split() if word not in stop_words]
print("불용어 제거:", filtered_words)

#

불용어 제거: ['sentence.']
```

### CMU
- 단어별 발음 기호 제공

```py
from nltk.corpus import cmudict
nltk.download('cmudict')
```

## Regex
- **Regular Expression**

### 정규 표현식(Regex) 활용 구문 분석
- 구문 주조 정의에 대한 지식 필요

```py 
import nltk
from nltk import RegexpParser
from nltk.tokenize import word_tokenize
nltk.download('punkt')  # 단어 토큰화
nltk.download('averaged_perceptron_tagger')  # 품사 태깅

sentence = "The big brown fox quickly jumps over the lazy dog."
words = word_tokenize(sentence)
tagged = nltk.pos_tag(words) # 각 단어의 품사를 붙여줌

# 명사구(NP) 패턴을 정의
grammar = "NP: {<DT>?<JJ>*<NN>}"
# NP : 명사구
# ? : 0 또는 1
# JJ : 형용사
# * : 0개 이상
# NN : 명시
parser = RegexpParser(grammar) # 설정한 패턴에 맞게 분석
result = parser.parse(tagged)

# 결과 출력 
for subtree in result.subtrees():
    if subtree.label() == 'NP':
        print(subtree)
# 이미지 형태로 보고 싶으면 .draw()

(NP The/DT big/JJ brown/NN)
(NP the/DT lazy/JJ dog/NN)
```

### 정규표현식 활용 패턴 탐지

```py
import re

# 정규 표현식을 사용하여 이메일 주소 추출
text = "이메일 주소는 example@example.com 입니다."
email_pattern = r'\b\S+@\S+\b'
# email_pattern = r'\b\S+@\S+\.\S+\b'
# \b : 단어 경계
# \S : 공백이 아닌 문자 
# + : 하나 이상
# \. : . 
emails = re.findall(email_pattern, text)
print(emails)

#

['example@example.com']
```

## 자연어 처리
### Tokenize
#### 단어 토큰화
`from nltk.tokenize import word_tokenize`
- 구두점을 구분하지 않음
`from nltk.tokenize import WordPunctTokenizer`
- 구두점을 따로 분리
`from nltk.tokenize import RegexpTokenizer`
- 정규 표현식 적용 가능

```py
from nltk.tokenize import RegexpTokenizer
retokenize = RegexpTokenizer(r"[\w]+")
```

### 문장 토큰화
`from nltk.tokenize import sent_tokenize`
- 여러 개의 문장들로 부터 문장을 구분
- 마침표를 기준으로 구분하지 않음
  - ph.D 와 같은 단어가 등장해도 문장을 분리하지 않음
### Pos Tagging
- 품사 식별
  - PRP: 대명사
  - VBP: 현재형 동사
  - VBG: 동명사/현재분사
  - JJ: 형용사
  - NN: 명사

```py
from nltk import pos_tag
from nltk.tokenize import word_tokenize

# 예시 텍스트
text = "Modules in NLTK are very useful"

# 단어 토큰화 후 품사 태깅
tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)
print("품사 태깅:", pos_tags)
#

품사 태깅: [('Modules', 'NNS'), ('in', 'IN'), ('NLTK', 'NNP'), ('are', 'VBP'), ('very', 'RB'), ('useful', 'JJ')]
```

### NER
- **Named Entity Recognition**
- 개체명 인식
- `from nltk import ne_chunk`
[¶ POS-Tags](#pos-태그-목록)

```py
from nltk import ne_chunk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# 예시 텍스트
text = "Mr. Kim-Sang-Deok, who lives in Alaska."

# 단어 토큰화 및 품사 태깅
tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)

# 개체명 인식
named_entities = ne_chunk(pos_tags)
print("개체명 인식:", named_entities)

#

개체명 인식: (S
  (PERSON Mr./NNP)
  Kim-Sang-Deok/NNP
  ,/,
  who/WP
  lives/VBZ
  in/IN
  (GPE Alaska/NNP)
  ./.)
```

### Lemmatization
- `.stem()`: 어간 추출
- `.lemmatize()`: 표제어 추출

```py
from nltk.stem import PorterStemmer, WordNetLemmatizer

# 어간 추출기와 표제어 추출기
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# 예시 단어
words = ["Betty", "Botter", "Bought", "bitter", "Butter"]

# 어간 추출
stemmed_words = [stemmer.stem(word) for word in words]
print("어간 추출:", stemmed_words)

# 표제어 추출
lemmatized_words = [lemmatizer.lemmatize(word, pos='v') for word in words]  # 동사로 처리
print("표제어 추출:", lemmatized_words)

#

어간 추출: ['betty', 'botter', 'bought', 'bitter', 'butter']
표제어 추출: ['Betty', 'Botter', 'Bought', 'bitter', 'Butter']
```

### 감성 분석
- `SentimentIntensityAnalyzer` 사용
- `.lexicon.update(custom_lexicon)`: 단어 추가

```py
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# NLTK의 감정 사전 다운로드
nltk.download('vader_lexicon')

# 정서 분석기 초기화
sia = SentimentIntensityAnalyzer()

# 사용자 정의 단어 추가
custom_lexicon = {
    'lol': 3.0,
    'eww': -3.0,
    'skrrr': 4.0,
    'ewwwww': -4.0
}

# 사용자 정의 사전 적용
sia.lexicon.update(custom_lexicon)
```

```py
# 예시 텍스트
texts = [
    "lol!!! ",
    "disgusting ewwww",
    "nice scenery, skrrr",
    "astonishing",
    "nothing special."
]

# 사용자 정의 임계값
positive_threshold = 0.5
negative_threshold = -0.5

# 각 텍스트의 감정 점수 분석 및 분류
for text in texts:
    sentiment = sia.polarity_scores(text)
    compound_score = sentiment['compound']
    
    if compound_score >= positive_threshold:
        sentiment_label = "긍정적"
    elif compound_score <= negative_threshold:
        sentiment_label = "부정적"
    else:
        sentiment_label = "중립적"
    
    print(f"텍스트: '{text}' | 감정 점수: {sentiment} | 판별 결과: {sentiment_label}")

    #

텍스트: 'lol!!! ' | 감정 점수: {'neg': 0.0, 'neu': 0.0, 'pos': 1.0, 'compound': 0.7074} | 판별 결과: 긍정적
텍스트: 'disgusting ewwww' | 감정 점수: {'neg': 0.773, 'neu': 0.227, 'pos': 0.0, 'compound': -0.5267} | 판별 결과: 부정적
텍스트: 'nice scenery, skrrr' | 감정 점수: {'neg': 0.0, 'neu': 0.114, 'pos': 0.886, 'compound': 0.8316} | 판별 결과: 긍정적
텍스트: 'astonishing' | 감정 점수: {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0} | 판별 결과: 중립적
텍스트: 'nothing special.' | 감정 점수: {'neg': 0.693, 'neu': 0.307, 'pos': 0.0, 'compound': -0.3089} | 판별 결과: 중립적
```

### Text 클래스
- 문서 분서에 필요한 메서드 제공
- 토큰화 필요

```py
import nltk
nltk.corpus.gutenberg.fileids()
bible_raw = nltk.corpus.gutenberg.raw('bible-kjv.txt')
from nltk.tokenize import RegexpTokenizer
retokenize = RegexpTokenizer(r"[\w]+")
retokenize.tokenize(bible_raw)[0:4]

#

['The', 'King', 'James', 'Bible']
```

#### 클래스 생성

```py
from nltk import Text
text = Text(retokenize.tokenize(bible_raw))
```

#### 그래프 확인

- `text.plot(10)` # 빈도순 10개

![](/LLM/images/txt_plt.png)

- `text.dispersion_plot(['god', 'father', 'lord'])` : 사용된 위치

![](/LLM/images/dis_plt.png)

- `text.concordance("god")`:  해당 단어 앞 뒤 문맥

>Displaying 25 of 4472 matches:
s Called Genesis 1 1 In the beginning God created the heaven and the earth 1 2 
he face of the deep And the Spirit of God moved upon the face of the waters 1 3....

- `text.similar("god")`: 대신 사용된 횟수가 높은 단어들 

>them him it he israel thee me you and man david judah us i people
father jerusalem men that lord

- `text.common_contexts(["god", "he"])` : 두 단어의 공통 문맥

>and_said for_is for_hath which_hath that_hath whom_hath and_saw
that_is said_hath that_had and_spake which_had and_hath lord_will
and_made as_hath but_shall that_was lord_that lord_is

### FreqDist
- 빈도수 기반 통계
- **Text** 클래스 메서드로 추출
`fd = text.vocab()`
- `FreqDist` 클래스 선언

```py
from nltk import FreqDist
from nltk.tag import pos_tag

stopwords = ['LORD', 'God', 'Lord', 'Israel', 'Jerusalem', 'O', 'Egypt', 'Behold']
# 불필요한 단어 불용어로 설정 / 고유명사 중 이름이 아닌 것 제외
bible_tokens = pos_tag(retokenize.tokenize(bible_raw))
# 토큰화 및 품사태그 설정
names_list = [t[0] for t in bible_tokens if t[1] == "NNP" and t[0] not in stopwords]
# 태그를 조건으로 고유명사 추출
fd_names = FreqDist(names_list)
fd_names

#

FreqDist({'David': 1064, 'Jesus': 970, 'Judah': 813, 'Moses': 641, 'Thou': 579, 'Christ': 532, 'Saul': 419, 'Jacob': 374, 'Aaron': 349, 'GOD': 300, ...})
```

- `fd_names.N(), fd_names["Jesus"], fd_names.freq("Jesus")` : 전체, 출현 횟수, 확률

- `fd_names.most_common(5)`
> [('David', 1064),
 ('Jesus', 970),
 ('Judah', 813),
 ('Moses', 641),
 ('Thou', 579)]

 ### WordCloud 
 `from wordcloud import WordCloud`
```py
from wordcloud import WordCloud
import matplotlib.pyplot as plt

wc = WordCloud(width=1000, height=600, background_color="white", random_state=42)
plt.imshow(wc.generate_from_frequencies(fd_names))
plt.axis("off") # x,y 축 제거
plt.show()
```

![](/LLM/images/wc_plt.png)

[¶ TOP](#nlp-tools)

# TextBlob
- 텍스트 데이터 처리 라이브러리

## 주요 기능 

### 객체 생성

```py
from textblob import TextBlob
blob = TextBlob("How fun is it to be a baseball fan right now. Judge and Ohtani playing at the same time is amazing.")
```

### 품사 태깅

```py
blob.tags

#

[('How', 'WRB'),
 ('fun', 'NN'),
 ('is', 'VBZ'),
 ('it', 'PRP'),
 ('to', 'TO'),
 ('be', 'VB'),
 ('a', 'DT'),
 ('baseball', 'NN'),
 ('fan', 'NN'),
 ('right', 'RB'),
 ('now', 'RB'),
 ('Judge', 'NNP'),
 ('and', 'CC'),
 ('Ohtani', 'NNP'),
 ('playing', 'NN'),
 ('at', 'IN'),
 ('the', 'DT'),
 ('same', 'JJ'),
 ('time', 'NN'),
 ('is', 'VBZ'),
 ('amazing', 'JJ')]
```


### 명사구 추출
`blob.noun_phrases`

>WordList(['baseball fan', 'ohtani'])

### 감성 분석

```py
testimonial = TextBlob("How fun is it to be a baseball fan right now, Judge and Ohtani playing at the same time is amazing.")
testimonial.sentiment

#

Sentiment(polarity=0.29642857142857143, subjectivity=0.4401785714285714)

# 긍정-부정(-1.0 ~ 1.0)
testimonial.sentiment.polarity 
#
0.29642857142857143

# 객관적 (0.0 ~ 1.0)
testimonial.sentiment.subjectivity
#
0.4401785714285714
```

### NaiveBayesAnalyzer

```py
from textblob.sentiments import NaiveBayesAnalyzer
nb_blob = TextBlob(
  "How fun is it to be a baseball fan right now, Judge and Ohtani playing at the same time is amazing.",
analyzer=NaiveBayesAnalyzer())
nb_blob.sentiment
#
Sentiment(classification='pos', p_pos=0.7934866888790837, p_neg=0.20651331112091628)
```

### 토큰화 
- NLTK 보다 기능이 많지만 성능은 부족한 느낌
- `blob.words`
- `blob.sentences`


### 단수-복수

```py
# 단수화
blob.words.singularize() 
# 복수화 - 주의점 : 일괄적으로 s가 붙음
blob.words.pluralize()
```

### 표제어 추출

```py
from textblob import Word
w = Word('octopi')
w.lemmatize()
#
'octopus'

w = Word("went")
w.lemmatize("v")
#
'go'
```

### Wordnet 활용 

```py
from textblob import Word
from textblob.wordnet import VERB
word = Word("cat")
word.synsets
#
[Synset('cat.n.01'),
 Synset('guy.n.01'),
 Synset('cat.n.03'),
 Synset('kat.n.01'),
 Synset('cat-o'-nine-tails.n.01'),
 Synset('caterpillar.n.02'),
 Synset('big_cat.n.01'),
 Synset('computerized_tomography.n.01'),
 Synset('cat.v.01'),
 Synset('vomit.v.01')]
```

```py
Word("grooming").get_synsets(pos=VERB)
#
[Synset('prepare.v.05'), Synset('dress.v.15'), Synset('groom.v.03')]
```

```py
word.definitions
#
['feline mammal usually having thick soft fur and no ability to roar: domestic cats; wildcats',
 'an informal term for a youth or man'...'eject the contents of the stomach through the mouth']
```

### 철자 교정

```py
b = TextBlob("I havv goood speling!")
print(b.correct())
#
I have good spelling!

from textblob import Word
w = Word('falibility')
w.spellcheck()
#
[('fallibility', 1.0)]
```

### Count, Counts

```py
monty = TextBlob("We are no longer the Knights who say Ni. We are now the Knights who say Ekki ekki ekki PTANG.")
monty.word_counts['ekki'] # 대소문자 구분하지 않음
monty.words.count('ekki')
# 3
monty.words.count('ekki', case_sensitive=True) # 대소문자 구분
# 2
```

### 구문 분석

```py
b = TextBlob("And now for something completely different.")
print(b.parse())
#
And/CC/O/O now/RB/B-ADVP/O for/IN/B-PP/B-PNP something/NN/B-NP/I-PNP completely/RB/B-ADJP/O different/JJ/I-ADJP/O ././O/O
```

### 연속되는 리스트 생성

```py
blob = TextBlob("Now is better than never.")
blob.ngrams(n=3)
#
[WordList(['Now', 'is', 'better']),
 WordList(['is', 'better', 'than']), 
 WordList(['better', 'than', 'never'])]
```

## 분류 모델

### NaiveBayes 모델 
`from textblob.classifiers import NaiveBayesClassifier`

### 데이터 셋 준비
- csv 파일
- (문장, 그룹) 구조

```py
train = [
    ('I love this sandwich.', 'pos'),
    ('This is an amazing place!', 'pos'),
    ('I feel very good about these beers.', 'pos'),
    ('This is my best work.', 'pos'),
    ('What an awesome view', 'pos'),
    ('I do not like this restaurant', 'neg'),
    ('I am tired of this stuff.', 'neg'),
    ('I can’t deal with this', 'neg'),
    ('He is my sworn enemy!', 'neg'),
    ('My boss is horrible.', 'neg')
]

test = [
    ('The beer was good.', 'pos'),
    ('I do not enjoy my job', 'neg'),
    ('I ain’t feeling dandy today.', 'neg'),
    ('I feel amazing!', 'pos'),
    ('Gary is a friend of mine.', 'pos'),
    ('I can’t believe I’m doing this.', 'neg')
]
```

### 모델 학습
`cl = NaiveBayesClassifier(train)`

### 모델 적용
```py
cl.classify("an amazing library!")
#
'pos'

prob_dist = cl.prob_classify("This one's a doozy.")
print(prob_dist.max())  # 'pos'
print(round(prob_dist.prob("pos"), 2))  # 0.63
print(round(prob_dist.prob("neg"), 2))  # 0.37
#
pos
0.95
0.05
```

### textBlob 클래스 활용

```py
from textblob import TextBlob
blob = TextBlob("The beer is good. But the hangover is horrible.", classifier=cl)

for s in blob.sentences:
    print(s, s.classify())
#
The beer is good. pos
But the hangover is horrible. neg
```

### 평가, 분석
```
print(cl.accuracy(test))
#
0.8333333333333334

cl.show_informative_features(5)
#
Most Informative Features
          contains(this) = True              neg : pos    =      2.3 : 1.0
          contains(this) = False             pos : neg    =      1.8 : 1.0
          contains(This) = False             neg : pos    =      1.6 : 1.0
            contains(an) = False             neg : pos    =      1.6 : 1.0
             contains(I) = False             pos : neg    =      1.4 : 1.0
```

### 데이터 추가
```
new_data = [
    ('She is my best friend.', 'pos'),
    ("I'm happy to have a new friend.", 'pos'),
    ("Stay thirsty, my friend.", 'pos'),
    ("He ain't from around here.", 'neg')
]
cl.update(new_data)
```

[¶ TOP](#nlp-tools)

# POS 태그 목록:

- CC: 접속사 (coordinating conjunction)
- CD: 기수 (cardinal digit)
- DT: 한정사 (determiner)
- EX: 존재론적 "there" (예: "there is")
- FW: 외래어 (foreign word)
- IN: 전치사/종속접속사 (preposition/subordinating conjunction)
- JJ: 형용사 ('big')
- JJR: 비교급 형용사 ('bigger')
- JJS: 최상급 형용사 ('biggest')
- LS: 목록 표시기 (list marker) (예: 1))
- MD: 조동사 (modal) (예: could, will)
- NN: 단수 명사 ('desk')
- NNS: 복수 명사 ('desks')
- NNP: 단수 고유 명사 ('Harrison')
- NNPS: 복수 고유 명사 ('Americans')
- PDT: 선행 한정사 ('all the kids')
- POS: 소유격 접미사 (possessive ending) ('parent's')
- PRP: 인칭 대명사 (personal pronoun) (예: I, he, she)
- PRP$: 소유 대명사 (possessive pronoun) (예: my, his, hers)
- RB: 부사 (adverb) (예: very, silently)
- RBR: 비교급 부사 (adverb, comparative) (예: better)
- RBS: 최상급 부사 (adverb, superlative) (예: best)
- RP: 분리 접두사 (particle) (예: give up)
- TO: "to" (예: go 'to' the store)
- UH: 감탄사 (interjection) (예: errrrrrrrm)
- VB: 동사, 기본형 (verb, base form) (예: take)
- VBD: 동사, 과거형 (verb, past tense) (예: took)
- VBG: 동사, 현재 분사 (verb, gerund/present participle) (예: taking)
- VBN: 동사, 과거 분사 (verb, past participle) (예: taken)
- VBP: 동사, 단수 현재형 (verb, sing. present, non-3d) (예: take)
- VBZ: 동사, 3인칭 단수 현재형 (verb, 3rd person sing. present) (예: takes)
- WDT: 의문 한정사 (wh-determiner) (예: which)
- WP: 의문 대명사 (wh-pronoun) (예: who, what)
- WP$: 소유 의문 대명사 (possessive wh-pronoun) (예: whose)
- WRB: 의문 부사 (wh-adverb) (예: where, when)

[¶ TOP](#nlp-tools)