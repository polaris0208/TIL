# Redis 적용 및 퀴즈 출제 LLM 개선

## 로그인 시 자주 사용하는 데이터 세팅
- `ChatHistory.objects.filter(user=request.user)`
  - 대화 내역을 **DB** 에서 꺼내서 캐시에 등록
  - 사용자의 예상 서비스 이용시간을 1시간이라 가정하여 타임아웃 설정
- `documents = Documents.objects.all()`
- `reference = Reference.objects.all()`
  - 서비스 이용자들 모두가 자주 사용할 레퍼런스 데이터들도 캐시에 등록
  - 주된 서비스 시간에는 변경 예정이 없기 때문에 24시간으로 설정

```py
# 캐시 초기화
from chatbot.models import ChatHistory, Documents
from quizbot.models import Reference
from django.core.cache import cache

...

def post(self, request):
        ...
            # 사용자 캐시 초기화
            chats = ChatHistory.objects.filter(user=request.user)
            if chats:
                chathistory_key = f"{user.id}:chathistory_keys"
                keys = []
                for chat in chats:
                    cache_key = f"{user.id}:{chat.id}:chathistory"
                    cache.set(cache_key, chat, timeout=60*60)
                    keys.append(chat.id)
                cache.set(chathistory_key, keys, timeout=60*60)
                print('대화내역 캐시 등록')
            
            # 레퍼런스 초기화
            documents=cache.get('documents')
            if not documents:
                documents = Documents.objects.all()
                cache.set('documents', documents, timeout=60*60*24)
                print('공식문서 캐시 등록')
            reference=cache.get('reference')
            if not reference:
                reference = Reference.objects.all()
                cache.set('reference', reference, timeout=60*60*24)
                print('레퍼런스 캐시 등록')

            return res
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
```

## chatbot 캐싱
- `QnA`챗봇에 자주 사용되는 데이터는 캐시부터 조회하여 호출시간 단축
  - 대화 내역 데이터, 레퍼런스 데이터, 요약 데이터
  - 대화 내역 데이터는 변경사항이 생긴 경우 갱신

```py
from django.core.cache import cache


class RagChatbotView(APIView):

    ...

    def get(self, request, chat_id):
        try:
            user = request.user
            cache_key = f"{user.id}:{chat_id}:chathistory"
            if cache.get(cache_key):
                chat_history = cache.get(cache_key)
                print("캐시호출")
            else:
                chat_history = self.get_chat_history(chat_id, user)

        ...

                 title_no = chat_history.content_info["title_no"]
                cache_key = f"{user.id}:{category}:{title_no}:summary"
                summary = cache.get(cache_key)
                if not summary:
                    summary = ""
                    print("요약 불러오기 실패: 이어하기")

        ...

                documents_cache = cache.get("documents")
                if documents_cache:
                    print("공식문서 케시 호출")
                    documents = documents_cache.filter(title_no=title_no).first()
                else:
                    documents = Documents.objects.filter(title_no=title_no).first()
                cache_key = f"{user.id}:{category}:{title_no}:summary"
                summary = cache.get(cache_key)
                if not summary:
                    summary = ""
                    print("요약 불러오기 실패: 생성")

        ...
            else:
                reference_cache = cache.get("reference")
                if reference_cache:
                    print("레퍼런스 케시 호출")
                    reference = reference_cache.filter(
                        category=category, title_no=title_no
                    ).first()
                else:
                    reference = Reference.objects.filter(
                        category=category, title_no=title_no
                    ).first()
        ...
        cache_key = f"{user.id}:{chat_history.id}:chathistory"
        cache.set(cache_key, chat_history, timeout=60 * 60)

        chathistory_key = f"{user.id}:chathistory_keys"
        id = chat_history.id
        if not cache.get(chathistory_key):
            cache.set(chathistory_key, [id], timeout=60 * 60)
        else:
            keys = cache.get(chathistory_key)
            if id not in keys:
                keys.append(id)
            cache.set(chathistory_key, keys, timeout=60 * 60)
```

### Summary
- 같은 내용에 대한 요약은 캐시를 호출하여 대체
  - 일관성 있는 내용 유지
  - 호출 시간 단축
- 공식문서 요약의 경우
  - 사용자마다 다른 `keyword`를 사용하여 생성하기 때문에 사용자 `id`로 구분하여 저장

```py
class SummaryView(APIView):
    def get(self, request):
        category = request.query_params.get("category")
        title_no = request.query_params.get("title_no")
        if category == "OFFICIAL_DOCS":
            user = request.user
            cache_key = f"{user.id}:{category}:{title_no}:summary"
            keyword = request.query_params.get("keyword")
            documents_cache = cache.get("documents")
            if documents_cache:
                print("공식문서 케시 호출")
                documents = documents_cache.filter(title_no=title_no).first()
            else:
                documents = Documents.objects.filter(title_no=title_no).first()
            title = documents.title
            retriever = test.get_retriever(title)
            multi_query = test.multi_query_llm(keyword)
            contents = []
            for query in multi_query:
                contents.append(retriever.invoke(query))
            response = test.summary(contents, keyword)
            cache.set(cache_key, response, timeout=60 * 60 * 24)

        else:
            cache_key = f"{category}:{title_no}:summary"
            response = cache.get(cache_key)
            if not response:
                reference_cache = cache.get("reference")
                if reference_cache:
                    print("레퍼런스 케시 호출")
                    reference = reference_cache.filter(
                        category=category, title_no=title_no
                    ).first()
                else:
                    reference = Reference.objects.filter(
                        category=category, title_no=title_no
                    ).first()
                if not reference:
                    response = "자료 읽기에 실패하였습니다."
                else:
                    content = reference.content
                    response = test.summary(content, "")
                    cache.set(cache_key, response, timeout=60 * 60 * 24)

        return Response(
            {"result": response},
            status=status.HTTP_200_OK,
        )
```

## 퀴즈 출제 LLM 개선

### `modles.py`
- 문제의 예문 역할을 할 `code_snipet` 추가

```py
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    number = models.PositiveIntegerField()  # 문제 번호
    content = models.TextField()  # 문제
    code_snipet = models.TextField(blank=True, null=True) # 코드 스니펫 / 코드 예시
    answer_type = models.CharField(max_length=100)  # 문제 형태(객관식, 단답형, ox)
    user_answer = models.JSONField(default=dict) # 사용자 답변
    feedback = models.TextField(blank=True, null=True)   # 문제별 피드백
```

### `test.py`
- `Pydantic` 모델 정의 위치 변경
  - 난이도 선택에 따라 모델 변경
  - 어려움 난이도에만 코드 예제를 포함한 코드 문제 출제
- 프롬프트 수정
  - 난이도 상세 규정
  - 한국어 출력 강조
  - 예문에 정답이 포함되는 문제 해결 : 프롬프트에 강조 + `gpt-4o`로 모델 변경
  - `temperature` : 다양한 문제가 출제되도록 수정

```py
def quizz_chain(content, input):


    type = input.get('type', 'ox')
    count = input.get('count', 5)
    difficulty = input.get('difficulty', 'easy')
    correct_answer_distribution = []
    if type == '4_multiple_choice':
        for _ in range(1, int(count) + 1):
                correct_index = random.randint(1, 4)
                suffle = f"""
                qustions_id : {_},
                choices_id : {correct_index},
                is_correct : true
                """
                correct_answer_distribution.append(suffle)
        description = f'create {count}, {difficulty} quiz with 4_multiple_choice. and follow answer_sheet : {correct_answer_distribution}'
    elif type == 'ox':
        for _ in range(1, int(count) + 1):
                correct_index = random.randint(1, 2)
                correct_answer_distribution.append(correct_index)
        description = f'create {count}, {difficulty} quiz with true or false (O/X). and follow answer_sheet : {correct_answer_distribution}'
    
    # Pydantic 모델 정의
    class QuestionChoice(BaseModel):
        id: int 
        content: str
        is_correct: bool

    if difficulty == "hard" : 
        class Question(BaseModel):
            id: int
            content: str
            code_snipet : str
            answer_type: str
            choices: list[QuestionChoice]
    
    else :
        class Question(BaseModel):
            id: int
            content: str
            code_snipet : None
            answer_type: str
            choices: list[QuestionChoice]
         

    class QuizResponse(BaseModel):
        # id: int # DB에서 자동 생성
        title: str
        description: str
        questions: list[Question]
        
    # OpenAI 클라이언트 설정
    client = OpenAI(api_key=openai.api_key)
    prompt = f"""
        **Language:** only in Korean
        **Context:** {content}
        **Description:** {description}
        **answer_type** : 4_multiple_choice or ox

        Generate quizzes based on the given context and ensure they align with the following difficulty levels:
        
        - **Easy**: Problems focusing on basic concepts, fundamental principles, or straightforward information from the context. Require minimal reasoning and should be solvable by beginners.
        
        - **Medium**: Problems that involve slightly complex ideas, require critical thinking, or include detailed information. May include tricky concepts or require interpreting context more deeply.

        - **Hard**: Create advanced Python coding challenges focusing on machine learning (ML), deep learning (DL), large language models (LLMs), Docker, Django, or Django REST framework (DRF). Challenges should require deep analytical thinking, manual coding, and an in-depth understanding of complex ML/DL frameworks and principles.

        **For Hard:** Each challenge must include at least one of the following elements:
        - Manually implement a custom neural network model without using pre-built layers.
        - Develop a loss function or optimization algorithm (e.g., gradient descent) from scratch.
        - Process and analyze a given dataset, incorporating visualization and preprocessing techniques.

        Challenges should be designed to push problem-solving skills and require writing efficient, scalable code.

        <code_snipet>
        **only in Hard difficulty**
        You should include code snippets broadly from the provided context, ensuring a comprehensive coverage of the topic.
        Context: {content} difficulty
        Important: Do not include direct explanatory hints or clues about the correct answer outside of the quizzes itself. Ensure that the code presented provides enough information for problem-solving without explicitly revealing the answer.
        Questions should challenge the reader to think critically by analyzing, interpreting, or applying the given code in realistic scenarios.
        do not include annotation
        </code_snipet>

        **Types of problems:**
        1. Select the expected output based on the given code.
        2. Choose the appropriate code that matches the given output.
        3. Fill in the blanks in the code with correct options.

        Include detailed examples and explanations for all questions. Ensure that answer options are full sentences, not just short answers. Mark the correct answer explicitly.

        **Language:** only in Korean
        """
    # 퀴즈 데이터를 구조화하여 응답 받기
    completion = client.beta.chat.completions.parse(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt},
        ],
        temperature=0.5,
        response_format=QuizResponse,  # 여기에서 QuizResponse 모델을 설정
    )

    # 응답 데이터
    quiz = completion.choices[0].message.parsed

    # JSON 형태로 추출
    quiz_json = json.dumps(quiz.model_dump(), indent=2)
    return quiz_json
```