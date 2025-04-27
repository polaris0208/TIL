# Get Weather 프로젝트 개념 정리

- 프로젝트 이름을 "Get Weather"로 변경하고, 위치(location) 저장은 필요 없음. 16일치 일일 예보를 배열로 저장

```javascript
const [days, setDays] = useState([]);
```

- OpenWeather API 사용. 계정 생성 후 발급받은 API 키 필요

```javascript
const API_KEY = "여기에_API_KEY_입력";
```

- 보안상 실제 서비스에서는 API 키를 클라이언트에 직접 노출하지 않고 서버를 통해 요청해야 함

- One Call API를 사용하여 현재 날씨와 일일(daily) 예보 데이터 가져오기  
  (minute, hourly, alerts 데이터는 제외)

```javascript
const response = await fetch(
  `https://api.openweathermap.org/data/2.5/onecall?lat=${latitude}&lon=${longitude}&exclude=alerts&units=metric&appid=${API_KEY}`
);
const json = await response.json();
console.log(json);
```

- 가져온 데이터에서 `daily` 배열만 추출하여 `days` 상태에 저장

```javascript
setDays(json.daily);
```

- `days` 데이터가 비어 있을 때는 로딩 인디케이터 표시

```javascript
if (days.length === 0) {
  return <ActivityIndicator size="large" color="white" />;
}
```

- React Native의 `ActivityIndicator`를 이용해 로딩 상태 표시

```javascript
import { ActivityIndicator } from 'react-native';
```

- `days.map()`을 사용하여 일일 날씨 정보를 화면에 표시  
  온도와 날씨(main) 정보를 출력

```javascript
{days.map((day, index) => (
  <View key={index}>
    <Text>{parseFloat(day.temp.day).toFixed(1)}°</Text>
    <Text>{day.weather[0].main}</Text>
  </View>
))}
```

- 온도는 `units=metric` 옵션을 추가해 섭씨(Celsius)로 변환  
  `parseFloat`와 `toFixed(1)`로 소수점 1자리까지만 표시해 가독성 향상

```javascript
<Text>{parseFloat(day.temp.day).toFixed(1)}°</Text>
```

- 추가로 날씨 설명(description)도 출력 가능

```javascript
<Text>{day.weather[0].description}</Text>
```
