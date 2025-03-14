# 사용자 입력 자료 기능 추가 - Youtube

## LLM
- 사용자가 입력한 **URL** 에서 **Video ID** 추출
- **Video ID**를 통해 해당 영상의 스크립트를 가져옴
  - 없는 경우 음성을 바탕을 자동 생성된 스크립트가 추출됨
- 스크립트에서 중요한 사건 또는 인물 정보, 개념, 수치 추출
- 부자연스럽게 생성된 문자나 문장 전처리 및 불필요한 문자-기호 제거
- 불건전한 내용이 포함될 경우에는 경고 메시지와 사유 반환

```py
def get_video_id(url):
    # ?:v= 기본 구조
    # \/ 축소형
    # {11} 11자 구조
    video_id_pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
    match = re.search(video_id_pattern, url)
    if match:
        return match.group(1)
    return None


def get_script(video_id):
    # 텍스트, 시작 시점, 자막 지속시간 딕셔너리 구조
    subtitle = ""
    transcription = YouTubeTranscriptApi.get_transcript(
        video_id, languages=["ko", "en", "en-US"]
    )
    for content in transcription:
        subtitle += f"{content['text']} \n"
    return subtitle


def extract_script(url):
    id = get_video_id(url)
    subtitle = get_script(id)
    return subtitle


# 30분 미만 영상
# Convert a conversation or speech into an informational document like a research paper,
def YoutubeScript(url):
    class YoutubeScript(BaseModel):
        title: str
        context: str
        content: str
        inappropriate: bool

    script = extract_script(url)

    prompt = f"""
            only use korean
            if english, translate to korean
            You are an editing expert. 
            Analyze the given script's topic and content, correcting any typos, altered expressions, or inappropriate word usage. 
            Join broken sentences together, and correct or revise any cut-off or misspelled words or expressions based on the context.
            remove unnecessary symbols like escape
            Include the following fields:

    
            title: Provide a title that best represents the overall content.
            context: itemization format, include specific figures like number, and name or keywords
            content: preprocessed content
            

            If the content is inappropriate (e.g., obscene, overly violent, or explicitly offensive), 
            set inappropriate to true. 
            In that case, 
            the title should be "Inappropriate Content," 
            the context should explain why it is inappropriate, 
            and the content field should contain a detailed explanation of the reasons.

            <script>
            {script}
            </script>
            """
    # 퀴즈 데이터를 구조화하여 응답 받기
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini-2024-07-18",
        messages=[
            {"role": "system", "content": prompt},
        ],
        temperature=0.1,
        response_format=YoutubeScript,
    )

    # 응답 데이터
    query = completion.choices[0].message.parsed

    # JSON 형태로 추출
    query_json = json.dumps(query.model_dump(), indent=2)
    query_dict = json.loads(query_json)

    # 결과 출력
    return query_dict
```

## 퀴즈 생성
- 영상 내용을 바탕으로 퀴즈 생성
- 같은 영상을 사용할 것에 대비하여 내용을 캐시에 저장

```py
class QuizRequestView(APIView):
    ...
    def post(self, request):
        try:
            ...
            elif category == "YOUTUBE":
                url = request.data["URL"]
                cache_key = url
                script = cache.get(cache_key)
                content = script
                if not script:
                    try:
                        content = YoutubeScript(url)
                        script = cache.set(cache_key, content)
                    except:
                        return Response(
                            {"error": "URL 또는 영상길이를 확인해 주세요."},
                            status=status.HTTP_404_NOT_FOUND,
                        )
      ...
```

## QnA
- 영상 내용을 컨텍스트로 사용
  - 영상에 대한 질문이나, 데이터 종합, 추출 등의 요청에 대응
- 컨텍스트 토큰 수를 고려하여 30분에서 1시간의 영상 분량이 적절
  - 초과할 경우 오류 발생
  - 안내 메시지 출력

```py
class RagChatbotView(APIView):

    ...
    def post(self, request, chat_id=False):
            ...
            elif category == "YOUTUBE":
                url = request.data["URL"]
                cache_key = url
                script = cache.get(cache_key)
                content = script
                if not script:
                    try:
                        content = llm.YoutubeScript(url)
                        script = cache.set(cache_key, content)
                    except:
                        return Response(
                            {"error": "URL 또는 영상길이를 확인해 주세요."},
                            status=status.HTTP_404_NOT_FOUND,
                        )
                result = llm.QnA_chain(content, memory, user_input)
            else:
                content = chat_history.content
                result = llm.QnA_chain(content, memory, user_input)

            ...

            elif category == "YOUTUBE":
                url = request.data["URL"]
                cache_key = url
                script = cache.get(cache_key)
                content = script
                if not script:
                    try:
                        content = llm.YoutubeScript(url)
                        script = cache.set(cache_key, content)
                    except:
                        return Response(
                            {"error": "URL 또는 영상길이를 확인해 주세요."},
                            status=status.HTTP_404_NOT_FOUND,
                        )
                memory = ""
                result = llm.QnA_chain(content, memory, user_input)
                content_info = {"category": category, "title_no": title_no}
                memory = [{"SYSTEM": "init conversation"}]
            ...
```