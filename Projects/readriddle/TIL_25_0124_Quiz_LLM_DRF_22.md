# 단체 퀴즈 LLM 고도화 -2

## 문제 : 문제 본문에 정답을 포함하는 문제 지속 발생

### 방안: 생성된 퀴즈를 필터링하는 모델 추가
- 정답 또는 정답과 비슷한 표현을 필터링

```py
    class Filter(BaseModel):
        description: str
        code_snippet: str

    prompt_2 = f"""
    answer과 description에, code_snippet을 화인한 후
    description에 모든 answer 또는 비슷한 표현을 (       ) 으로 변경한 뒤 description 반환
    code_snippet에서 answer 과 동일한 표현을 (       ) 으로 변경 뒤 code_snippet 반환

    <code_snippet>
    {code_snippet}
    </code_snippet>

    <description>
    {description}
    </description>

    <answer>
    {answer}
    </answer>
    """

    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",  # 조정 필요
        messages=[
            {"role": "system", "content": prompt_2},
        ],
        temperature=0.1,  # 조정 필요
        response_format=Filter,
    )
    filtered = completion.choices[0].message.parsed
    filtered_json = json.dumps(filtered.model_dump(), indent=2)
    filtered_dict = json.loads(filtered_json)
    description = filtered_dict["description"]
    code_snippet = filtered_dict["code_snippet"]
```

## 문제 : 문제가 고르게 출제되지 않고, 어떤 답변을 원하는지 명확하게 표현하지 않음

### 방안 1 : 문제 출제 비율을 설정

```py
    ...
    prompt = f"""
            **only in korean**

            Generate question about topic.
            
            question type is "code-based problems" or "conceptual knowledge"

            <conceptual knowledge>
            description: ask concept or knowledge
            code_snippet: code example
            answer: short answer (maximum 1 word)
            spawn Probability: 20%
            </conceptual knowledge>

            <code-based problems>
            description: ask the result of code execution. Do not include example in description.
            code_snippet: **only include code**
            answer: the result of code execution
            spawn Probability: 80%
            </code-based problems>

            <topic>
            {selected_subject}
            </topic>
    ...
```

### 방안 2 : 문제 유형을 한정
- `다음 작성된 코드를 실행했을 때 나오는 결과값 'answer' 는 무엇일까요?`