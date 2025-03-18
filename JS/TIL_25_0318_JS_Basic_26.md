# Geolocation과 날씨 데이터 활용

## 개념 정리

- `navigator.geolocation`을 사용하여 사용자의 현재 위치(위도, 경도)를 가져올 수 있음.
- `getCurrentPosition(successCallback, errorCallback)` 함수 사용.
  - `successCallback`: 위치 정보를 성공적으로 가져왔을 때 실행할 함수.
  - `errorCallback`: 위치 정보를 가져오지 못했을 때 실행할 함수.
- 위치 정보가 제공되면 이를 OpenWeatherMap API와 같은 서비스와 연동하여 날씨 데이터를 가져올 수 있음.

## 코드 예시

```javascript
// 현재 위치 가져오기
navigator.geolocation.getCurrentPosition(onGeoSuccess, onGeoError);

function onGeoSuccess(position) {
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;
    console.log(`위도: ${lat}, 경도: ${lon}`);

    // 날씨 API 호출 예시
    const API_KEY = "YOUR_API_KEY";
    const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`;
    
    fetch(url)
        .then(response => response.json())
        .then(data => console.log(`현재 날씨: ${data.weather[0].description}, 온도: ${data.main.temp}°C`))
        .catch(error => console.error("날씨 정보를 가져오는 데 실패했습니다.", error));
}

function onGeoError() {
    alert("위치 정보를 가져올 수 없습니다.");
}
```

## 활용 방법

1. 브라우저에서 `navigator.geolocation.getCurrentPosition()`을 실행하여 위치 정보를 가져옴.
2. 성공적으로 위치 정보를 받으면 `latitude`, `longitude` 값을 추출.
3. OpenWeatherMap API에 해당 정보를 전달하여 날씨 데이터를 가져옴.
4. 콘솔 또는 화면에 날씨 정보를 출력하여 사용자에게 제공.

## 추가 참고 사항

- 위치 정보를 요청하면 브라우저에서 사용자에게 권한 요청 창이 표시됨.
- 사용자가 위치 정보를 차단하면 `onGeoError` 함수가 실행됨.
- OpenWeatherMap API를 사용하려면 사전 가입 및 API 키 발급 필요.