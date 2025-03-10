# 단체 퀴즈 LLM 고도화

## 의존성 설치

```py
import os
import json
import openai
from pprint import pprint
from openai import OpenAI
from pydantic import BaseModel
from operator import itemgetter
from django.core.cache import cache


openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai.api_key)
```

## 캐시 확인 및 주제 생성
- 캐시 확인
  - 이미 생성된 주제가 있는지 확인
  - 생성된 주제 중 아직 사용되지 않은 주제 선택
- 주제 변경 : `programming algorithm` 
  - 단순 프로그래밍 지식보다 어려운 난이도의 문제 유도

```py
def chat_quiz():
    cache_key = "chat_quiz"
    subjects = cache.get(cache_key)
    selected_subject = ""
    if subjects:
        print("\n<--------------캐시 호출-------------->\n")
        subject_list = subjects["subjects"]
        for subject in subject_list:
            if subject["done"] == False:
                subject["done"] = True
                selected_subject = subject
                print("<--------------주제 선택--------------> \n")
                break

        if selected_subject:
            print("\n<--------------주제 선택/캐시 적용-------------->\n")
            cache.set(cache_key, subjects, timeout=60 * 60)
        else:
            subjects = None
            print("\n<--------------주제 모두 사용-------------->\n")

    if not subjects:
        print("\n<--------------캐시 없음/주제 모두 사용-------------->\n")

        # 주제, 난이도 생성 / 한시간에 12개 - 5분에 하나
        class Subject(BaseModel):
            subject: str
            difficulty: str
            done: bool  # 이미 사용된 주제는 false 처리

        class Subjects(BaseModel):
            subjects: list[Subject]

        prompt = f"""
        Make **30** 'Subject' about programming algorithm
        'difficulty' is Hard
        `done' is false
        """

        completion = client.beta.chat.completions.parse(
            model="gpt-4o",  # 조정 필요
            messages=[
                {"role": "system", "content": prompt},
            ],
            temperature=0.7,  # 조정 필요
            response_format=Subjects,
        )

        subject = completion.choices[0].message.parsed
        subject_json = json.dumps(subject.model_dump(), indent=2)
        subject_dict = json.loads(subject_json)
        print("<--------------주제 선택-------------->")
        subject_list = subject_dict["subjects"]
        for subject in subject_list:
            if subject["done"] == False:
                subject["done"] = True
                selected_subject = subject
                print("<--------------주제 선택-------------->")
                break
        cache.set(cache_key, subject_dict, timeout=60 * 60)
```

## 프롬프트 수정
- 문제 형태 규정
  - 개념 문제
  - 코드 문제
- 규칙 설정
  - 질문은 항상 끝에
  - 문제에 정답 포함하지 않도록 설정
  - 문제는 정답을 직접적으로 언급하지 않으면서도 상세하게 묘사
  - 디테일하고 실용적인 코드 예제를 포함
- 예시
  - 긍정적인 예시와 부정적인 예시 제공
  - 비교가 될 수 있도록 차이점을 부각


```py
    class ChatQuiz(BaseModel):
        description: str
        code_snippet: str
        answer: str

    prompt = f"""
            **only in korean**

            Generate question about topic.
            
            question type is "code-based problems" or "conceptual knowledge"

            <conceptual knowledge>
            description: ask concept or knowledge
            code_snippet: code example
            answer: short answer (maximum 1 word)
            </conceptual knowledge>

            <code-based problems>
            description: ask code to fill blank
            code_snippet: **only include code**
            answer: code
            </code-based problems>

            <topic>
            {selected_subject}
            </topic>

            <rule>
            located question in last sentence
            do not include answer in description and code_snippet.
            explain the concept and knowledge in detail without directly mentioning the answer or specific keywords
            Include a practical and detailed code example in code_snippet, excluding any references or annotations.
            </rule>

            <conceptual knowledge example>
            <positive example>
            description: "새로운 화폐가 생성되는 과정(조폐)에서, 생성자들(채굴자들)에게 "이것"을 강제하여 화폐의 가치와 보안을 보장합니다. 
                분산 네트워크에서는 조폐 과정에서 누가 얼마의 새 화폐를 받을지를 결정할 중앙 권력이 없기 때문에 모든 참여자들이 자동적으로 동의할 수 있는 방법이 필요합니다. 
                이때 일방향함수인 해시 함수가 계산(검산)하기는 쉽지만 역을 구하는 것(채굴)은 어렵다는 것에 착안하여, 모든 참여자가 해시 함수를 계산해서 가장 먼저 계산한 사람이 새 화폐를 받아가게 하는 것 입니다. 
                최초로 상업적 성공을 거둔 암호화폐 비트코인의 경우, 블록체인의 다음 블록을 캐기 위한 해시 함수의 입력값에 거래내역을 담은 블록체인의 최신값을 연동시켜서, 송금과 조폐 양 기능과 보안을 동시에 해결하였습니다.
                비트코인 블록체인에서 채택된 합의 알고리즘으로, 네트워크에 참여하는 노드(컴퓨터)들이 일정한 계산 작업을 수행하도록 설계된 시스템은 무엇일까요?"
            code_snippet :""
            answer: 작업증명
            </positive example>

            <negative example>
            description: "블록체인 합의 메커니즘에서 '작업 증명(Proof of Work)'의 주요 개념은 무엇인가요?"
            code_snippet:""
            answer: 작업증명
            </negtive example>
            </conceptual knowledge example>

            <code-based problems>
            <positive example>
            description: 해밍 거리(Hamming Distance) 계산 
                두 개의 이진 문자열(binaryA, binaryB)이 주어졌을 때, 두 문자열의 해밍 거리(Hamming Distance) 를 계산하는 프로그램입니다.
                해밍 거리는 두 이진 문자열에서 대응하는 비트가 서로 다른 위치의 개수를 의미합니다. 
                예를 들어, "10010"과 "110"이 있을 때, 이 두 문자열을 동일한 길이로 맞춘 뒤 각 비트를 비교하여 다른 비트의 개수를 세는 방식입니다.

                매개변수 설명:
                    binaryA (1 <= len(binaryA), len(binaryB) <= 100): 첫 번째 이진 문자열.
                    binaryB (1 <= len(binaryA), len(binaryB) <= 100): 두 번째 이진 문자열.
                문제 해결 과정:
                    먼저, 두 이진 문자열의 길이가 다르면 짧은 문자열에 앞에서 0을 추가하여 두 문자열의 길이를 맞추어야 합니다.
                    두 문자열이 같은 길이가 되면, 각 위치에서 두 문자열의 비트를 비교하여 값이 다를 경우 해밍 거리를 1씩 증가시킵니다.
                코드 설명:
                    func_a 함수는 주어진 이진 문자열을 length 길이에 맞게 앞부분에 0을 추가하는 함수입니다. 예를 들어, binaryB가 짧으면 앞에 0을 추가하여 두 문자열의 길이를 동일하게 만듭니다.
                    solution 함수는 두 이진 문자열을 같은 길이로 맞춘 후 각 비트를 비교합니다. 비트가 다르면 hamming_distance를 증가시킵니다.
                    binaryA = "10010"과 binaryB = "110"을 입력하면, binaryB는 "00110"으로 패딩되어 비교됩니다. 두 문자열에서 다른 비트는 2개이므로 해밍 거리는 2가 됩니다.
                시간 복잡도:
                    문자열의 길이가 최대 100이므로, func_a와 solution 함수 모두 시간 복잡도는 O(n)입니다.

                다음 작성된 코드 예시 속에서 빈칸에 들어갈 코드는 무엇일까요?
            code_snippet:
                def func_a(string, length):
                    padZero = ""
                    padSize = (--빈칸--)
                    for i in range(padSize):
                        padZero += "0"
                    return padZero + string

                def solution(binaryA, binaryB):
                    max_length = max(len(binaryA), len(binaryB))
                    binaryA = func_a(binaryA, max_length)
                    binaryB = func_a(binaryB, max_length)

                    hamming_distance = 0
                    for i in range(max_length):
                        if binaryA[i] != binaryB[i]:
                            hamming_distance += 1
                    return hamming_distance

                binaryA = "10010"
                binaryB = "110"
                ret = solution(binaryA, binaryB)

                print("solution 함수의 반환 값은", ret, "입니다.")
            answer: len(string)
            </positive example>

            <negative example>
            description : 해밍 거리(Hamming Distance) 계산
            code_snippet:
                def func_a(string, length):
                    padZero = ""
                    padSize = length - len(string)  # 패딩할 0의 개수를 계산
                    for i in range(padSize):
                        padZero += "0"
                    return padZero + string

                def solution(binaryA, binaryB):
                    max_length = max(len(binaryA), len(binaryB))  # 가장 긴 문자열 길이 구하기
                    binaryA = func_a(binaryA, max_length)  # 첫 번째 문자열을 길이에 맞게 패딩
                    binaryB = func_a(binaryB, max_length)  # 두 번째 문자열을 길이에 맞게 패딩

                    hamming_distance = 0  # 해밍 거리 초기화
                    for i in range(max_length):
                        if binaryA[i] != binaryB[i]:  # 두 비트가 다르면 해밍 거리 증가
                            hamming_distance += 1
                    return hamming_distance  # 최종 해밍 거리 반환

                # 테스트 예시
                binaryA = "10010"
                binaryB = "110"
                ret = solution(binaryA, binaryB)
                print("solution 함수의 반환 값은", ret, "입니다.")  # 예상 출력: 2
            answer: len(string)
            </negative example>
            </code-based problems>

            **only in korean**
            """
```

## 출력 필터링
- 문제에 정답이 포함되는 경우 빈칸으로 변환
- 코드스니펫 적용 

```py
    completion = client.beta.chat.completions.parse(
        model="gpt-4o",  # 조정 필요
        messages=[
            {"role": "system", "content": prompt},
        ],
        temperature=0.1,  # 조정 필요
        response_format=ChatQuiz,
    )

    quiz = completion.choices[0].message.parsed
    quiz_json = json.dumps(quiz.model_dump(), indent=2)
    quiz_dict = json.loads(quiz_json)
    answer = quiz_dict["answer"]
    description = quiz_dict["description"].replace(answer, "[__________]")
    code_snippet = quiz_dict["code_snippet"]
    if code_snippet:
        code_snippet = code_snippet.replace("```", "").replace(answer, "[__________]")
        question = f"[POP RIDDLE]\n{description}\n\n```\n{code_snippet}\n```"
    question = f"[POP RIDDLE]\n{description}\n\n{code_snippet}\n"
    pprint(question)

    return question, answer
```