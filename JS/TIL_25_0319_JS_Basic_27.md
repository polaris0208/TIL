# OpenWeatherMap API

## 개념 정리
- API(응용 프로그램 인터페이스)는 외부 서버와 데이터를 주고받을 수 있도록 도와주는 인터페이스이다.
- OpenWeatherMap API를 사용하면 특정 지역의 날씨 데이터를 가져올 수 있다.
- API 요청 시 필요한 정보:
  - **API Key**: 인증을 위한 키 (개인 발급 필요)
  - **위도(latitude) 및 경도(longitude)**: 특정 위치의 날씨 데이터를 가져오기 위한 좌표
  - **요청 URL**: API 엔드포인트와 필요한 파라미터를 포함한 주소

## API 요청 방식
1. OpenWeatherMap API 문서를 참고하여 요청 형식을 확인한다.
2. 요청 URL을 작성한다.
3. JavaScript의 `fetch()` 함수를 이용하여 데이터를 요청한다.
4. 응답 데이터를 JSON 형식으로 변환하고 필요한 정보를 추출한다.
5. 화면에 데이터를 표시한다.

## API 요청 URL 예시
- `{위도}`: 가져오려는 지역의 위도 값
- `{경도}`: 가져오려는 지역의 경도 값
- `{API_KEY}`: 본인의 API 키 입력
- `units=metric`: 온도 단위를 섭씨(Celsius)로 설정

## 코드 예시

```javascript
const apiKey = "YOUR_API_KEY"; // 본인의 API 키 입력

navigator.geolocation.getCurrentPosition(position => {
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;
    
    const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${apiKey}&units=metric`;
    
    fetch(url)
        .then(response => response.json())
        .then(data => {
            console.log("날씨 데이터:", data);
            document.getElementById("weather").innerText = `${data.weather[0].main}, ${data.main.temp}°C`;
        })
        .catch(error => console.error("API 요청 실패:", error));
});
```

## 주요 기능 정리
- `navigator.geolocation.getCurrentPosition()`: 사용자의 현재 위치(위도, 경도) 가져오기
- `fetch(url)`: 지정된 URL로 API 요청 보내기
- `.then(response => response.json())`: 응답을 JSON 형식으로 변환
- `data.weather[0].main`: 날씨 상태 (예: Clouds, Clear 등)
- `data.main.temp`: 현재 온도 (섭씨)
- `document.getElementById("weather").innerText`: HTML에 날씨 정보 표시

## API 응답 예시(JSON)

```json
{
    "weather": [
        { "main": "Clouds", "description": "broken clouds" }
    ],
    "main": {
        "temp": 16,
        "humidity": 72,
        "pressure": 1013
    },
    "name": "Seoul",
    "sys": {
        "country": "KR"
    }
}
```

## 최종 결과
- 사용자의 현재 위치 기반 날씨 정보를 가져와 화면에 표시
- JavaScript `fetch()`와 `geolocation API`를 활용하여 비동기적으로 데이터를 요청
- API 요청에 필요한 정보(위도, 경도, API 키)를 동적으로 구성