## Quiz LLM 리팩토링 
- Serializer 적용

### `serializers.py`

```python
from rest_framework import serializers
from .models import Quiz, Question, Choice

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ["id", "number", "content", "is_correct"]

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ["id", "number", "content", "code_snippets", "answer_type", "choices"]

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ["id", "title", "description", "questions"]

    def create(self, validated_data):
        questions_data = validated_data.pop("questions")
        quiz = Quiz.objects.create(**validated_data)

        for question_data in questions_data:
            choices_data = question_data.pop("choices")
            question = Question.objects.create(quiz=quiz, **question_data)

            for choice_data in choices_data:
                Choice.objects.create(question=question, **choice_data)

        return quiz
```

### `views.py`

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from .models import Quiz, Documents, Reference
from .serializers import QuizSerializer
import json

class QuizRequestView(APIView):
    def get(self, request):
        queryset = Quiz.objects.filter(user=request.user)
        serializer = QuizSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            category = request.data["category"]
            title_no = request.data.get("title_no", "")

            # Content 가져오기
            if category == "OFFICIAL_DOCS":
                keyword = request.data["keyword"]
                documents = cache.get("documents", None)
                if documents:
                    documents = documents.filter(title_no=title_no).first()
                else:
                    documents = Documents.objects.filter(title_no=title_no).first()

                if not documents:
                    return Response({"error": "문서를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

                retriever = get_retriever(documents.title)
                multi_query = multi_query_llm(keyword)
                contents = [retriever.invoke(query) for query in multi_query]
                content = summary(contents, keyword)

            elif category == "YOUTUBE":
                url = request.data["URL"]
                script = cache.get(url)
                if not script:
                    try:
                        script = YoutubeScript(url)
                        cache.set(url, script)
                    except:
                        return Response({"error": "URL 또는 영상길이를 확인해 주세요."}, status=status.HTTP_404_NOT_FOUND)
                content = script

            else:
                reference = cache.get("reference", None)
                if reference:
                    reference = reference.filter(category=category, title_no=title_no).first()
                else:
                    reference = Reference.objects.filter(category=category, title_no=title_no).first()

                if not reference:
                    return Response({"error": "Reference not found"}, status=status.HTTP_404_NOT_FOUND)
                
                content = reference.content

            # LLM으로 퀴즈 생성
            response = llm.quizz_chain(content, request.data)
            response_dict = json.loads(response)

            # 시리얼라이저를 사용해 저장
            quiz_data = {
                "user": request.user.id,
                "title": response_dict["title"],
                "description": response_dict["description"],
                "questions": response_dict["questions"],
            }

            serializer = QuizSerializer(data=quiz_data)
            if serializer.is_valid():
                quiz = serializer.save(user=request.user)
                return Response(
                    {"detail": "문제가 생성되었습니다.", "id": quiz.id, "questions": response_dict["questions"]},
                    status=status.HTTP_201_CREATED,
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Reference.DoesNotExist:
            return Response({"error": "Reference not found"}, status=status.HTTP_404_NOT_FOUND)
```

