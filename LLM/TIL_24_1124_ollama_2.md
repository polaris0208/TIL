# ollama 활용
> 로컬 환경에 맞는 모델 선택 및 활용

## 한국어 모델 활용

### 필요성
- `llama3.1, llama3.2` 한국어 사용시 불완전한 답변 생성
  - 한국어 모델로 파인튜닝된 모델 필요

```
하늘의 màu은 다양한 фактор에 의해 영향을 받습니다. 하늘은 주로.blue색을 띤다, 그러나 실제 하늘의 색상은 그에 따라 달라집니다.
```

### Hugging Face 탐색 [¶](https://huggingface.co)
- `EEVE-Korean-Instruct-10.8B-v1.0` [¶](https://huggingface.co/yanolja/EEVE-Korean-Instruct-10.8B-v1.0)
  - 야놀자에서 업스테이지 솔라 모델을 기반으로 개발
  - 높은 평가

- **Bllossom** [¶](https://huggingface.co/Bllossom)
  - `llama3, llama3.1, llama3.2` 한국어 튜닝 모델 제공
  - 언어학 자료 기반으로 튜닝 : 수학적 성능은 떨어지나 문장 생성 능력은 높음
  - 비교적 최신 업데이트 : 10일 ~ 5개월

### 모델 적용
- 모델 경로 셍성
  - `gguf` 파일 다운로드
  - `Modelfile` 작성 : 모델 설정 파일, `SYSTEM`에 모델 역할 부여
- `ollama create <사용할 이름> -f <모덾파일 경로>`

```
FROM model.gguf

TEMPLATE """{{- if .System }}
<s>{{ .System }}</s>
{{- end }}
<s>Human:
{{ .Prompt }}</s>
<s>Assistant:
"""

SYSTEM """A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions."""

PARAMETER stop <s>
PARAMETER stop </s>
```

### Bllossom 모델 테스트
- 메모리가 `EEVE` 모델을 사용하기에 부족
- 가벼운 모델로 지원하는 **Bllossom** 모델 선택
- `llama3` 기반 모델임에도 `llama3.1, 3.2` 모델에 비해 자연스러운 한국어 문장 구사
- 한국 관련 질문에도 더 적절한 답변 생성

```py
import langchain
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="bllossom3-Q4")

querry = ("하늘은 왜 파란색이야")
    
response = llm.invoke(querry)
print(response)

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("{topic} 친근한 말투로 초등학생도 이해할 수 있게 쉬운 말로 설명해줘.")

# 체인 생성
chain = prompt | llm | StrOutputParser()

# 간결성을 위해 응답은 터미널에 출력됩니다.
answer = chain.invoke({"topic": "하늘은 왜 파란색이야"})

print(answer)
```

```
# 단순 질문

하늘의 색은 주로 대기 중의 산소 분자와 물방울, 먼지 등이 일광을 흡수하고 반사하는 결과입니다. 하늘이 보이는 파란색은 대기의 산소 분자가 일광선을 흡수하는 특정 스펙트럼에서 나타나는 현상입니다. 이 스펙트럼의 파란색 부분이 우리에게 파란하늘을 보이게 만듭니다.

# 프롬프트 적용

하늘은 왜 파란색일까? 그건 대기 중에 있는 물방울들이 햇빛을 반사하면서 생기는 일이야. 우리가 보는 파란색은 사실 여러 가지 색이 섞여서 만들어진 거야. 대기 중에는 수증기가 있고, 이 수증기는 햇빛을 보고 다른 색을 반사해. 그 반사된 색들이 우리 눈에 들어오면 파란색으로 보인다! 그래서 하늘은 파란색이야!
```

## Embedding 모델

### 필요성
- 로컬 환경에서 무료로 사용 가능한 모델 필요

### `nomic-embed-text`
- 긴 문맥에서 텍스트를 효과적으로 임베딩
- `text-embedding-ada-002` 보다 향상된 성능
- `text-embedding3-small`과 비슷한 성능

### 테스트
- 현재 사용중인 `text-embedding-ada-002` 와 비교
- `nomic-embed-text` 모델이 유사한 정도를 더 잘 구별해서 임베딩
  - `text-embedding-ada-002`의 경우 유사한 문장과 그렇지 않은 문장의 유사도 점수에 큰 차이가 없음

```py
from langchain_ollama import OllamaEmbeddings

ollama_embeddings = OllamaEmbeddings(model="nomic-embed-text")

import os
import openai
from langchain_openai import OpenAIEmbeddings

openai.api_key = os.environ.get('NBCAMP_01')
openai_embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", api_key=openai.api_key)


import faiss
from langchain_community.vectorstores import FAISS 
from langchain_community.docstore.in_memory import InMemoryDocstore 


ollama_index = faiss.IndexFlatL2(len(ollama_embeddings.embed_query("hello world")))  
ollama_store = FAISS(
    embedding_function=ollama_embeddings,
    index=ollama_index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={}
)

openai_index = faiss.IndexFlatL2(len(openai_embeddings.embed_query("hello world")))  
openai_store = FAISS(
    embedding_function=openai_embeddings,
    index=openai_index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={}
)

from langchain_core.documents import Document

documents = [
    Document(page_content="이번 여름에 일본으로 여행을 가기로 했습니다. 도쿄에서의 멋진 여행을 기대하고 있습니다.", metadata={"source": "travel"}),
    Document(page_content="내년에 유럽을 여행하려고 계획 중입니다. 프랑스, 독일, 이탈리아를 방문할 예정입니다.", metadata={"source": "travel"}),
    Document(page_content="뉴욕에서의 여행은 매우 흥미로웠습니다. 센트럴 파크에서의 산책이 기억에 남아요.", metadata={"source": "travel"}),
    Document(page_content="이번 여름 방학에는 제주도로 여행을 갈 예정입니다. 바다와 자연을 만끽하고 싶어요.", metadata={"source": "travel"})
]

ollama_store.add_documents(documents=documents)
openai_store.add_documents(documents=documents)

ollama_results = ollama_store.similarity_search("여름 여행 계획", k=3)
for res in ollama_results:
    print(f"ollama_results \n {res.page_content} [{res.metadata}]")

openai_results = openai_store.similarity_search("여름 여행 계획", k=3)
for res in openai_results:
    print(f"openai_results \n {res.page_content} [{res.metadata}]")


ollama_results_with_scores = ollama_store.similarity_search_with_score("여름 여행 계획", k=3)
for res, score in ollama_results_with_scores:
    print(f"ollama_results [SIM={score:.3f}] {res.page_content} [{res.metadata}]")

openai_results_with_scores = openai_store.similarity_search_with_score("여름 여행 계획", k=3)
for res, score in openai_results_with_scores:
    print(f"openai_results [SIM={score:.3f}] {res.page_content} [{res.metadata}]")
```

```
ollama_results [SIM=0.298] 내년에 유럽을 여행하려고 계획 중입니다. 프랑스, 독일, 이탈리아를 방문할 예정입니다. [{'source': 'travel'}]
ollama_results [SIM=0.316] 이번 여름에 일본으로 여행을 가기로 했습니다. 도쿄에서의 멋진 여행을 기대하고 있습니다. [{'source': 'travel'}]
ollama_results [SIM=0.450] 이번 여름 방학에는 제주도로 여행을 갈 예정입니다. 바다와 자연을 만끽하고 싶어요. [{'source': 'travel'}]

openai_results [SIM=0.225] 이번 여름 방학에는 제주도로 여행을 갈 예정입니다. 바다와 자연을 만끽하고 싶어요. [{'source': 'travel'}]
openai_results [SIM=0.229] 이번 여름에 일본으로 여행을 가기로 했습니다. 도쿄에서의 멋진 여행을 기대하고 있습니다. [{'source': 'travel'}]
openai_results [SIM=0.253] 내년에 유럽을 여행하려고 계획 중입니다. 프랑스, 독일, 이탈리아를 방문할 예정입니다. [{'source': 'travel'}]
```