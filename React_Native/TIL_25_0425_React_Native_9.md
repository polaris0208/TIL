# Geolocation 개념과 expo-location 주요 기능

## Geolocation

**Geolocation**은 사용자의 위치(위도, 경도 등)를 추적하거나 위치 정보를 얻는 기술로 모바일 앱에서는 위치 기반 서비스(예: 지도, 날씨, 배달 등)에 필수적으로 사용

**expo-location**은 Expo에서 제공하는 위치 정보 관리 라이브러리로, React Native 앱에서 위치 권한 요청, 현재 위치 조회, 위치 추적, 역지오코딩 등 다양한 위치 관련 기능을 제공


## 주요 기능 요약

- **위치 권한 요청**: 앱이 위치 정보를 사용하기 전에 사용자에게 권한을 요청
- **현재 위치 가져오기**: 사용자의 현재 위도, 경도 정보를 얻
- **역지오코딩(Reverse Geocoding)**: 위도, 경도 좌표를 주소, 도시명 등으로 변환
- **위치 추적(Watch Position)**: 사용자가 이동할 때마다 위치를 실시간으로 추적
- **Geofencing**: 사용자가 특정 지역에 들어가거나 나갈 때 이벤트를 발생시


## 주요 코드 흐름 및 예시

아래는 expo-location의 주요 기능을 사용하는 React Native 코드 예시

```javascript
import React, { useState, useEffect } from 'react';
import { Text, View, Button, Alert } from 'react-native';
import * as Location from 'expo-location';

export default function App() {
  const [location, setLocation] = useState(null);
  const [address, setAddress] = useState(null);
  const [errorMsg, setErrorMsg] = useState(null);

  // 권한 요청 및 현재 위치 가져오기
  useEffect(() => {
    (async () => {
      let { status } = await Location.requestForegroundPermissionsAsync();
      if (status !== 'granted') {
        setErrorMsg('위치 권한이 거부되었습니다.');
        Alert.alert('권한 거부', '앱 사용을 위해 위치 권한이 필요합니다.');
        return;
      }
      let loc = await Location.getCurrentPositionAsync({});
      setLocation(loc);

      // 역지오코딩: 위도, 경도 → 주소
      let addr = await Location.reverseGeocodeAsync({
        latitude: loc.coords.latitude,
        longitude: loc.coords.longitude,
      });
      setAddress(addr);
    })();
  }, []);

  // 위치 추적 (watchPositionAsync)
  const startWatching = async () => {
    await Location.watchPositionAsync(
      { accuracy: Location.Accuracy.High, distanceInterval: 1 },
      (loc) => {
        setLocation(loc);
      }
    );
  };

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>위치 정보:</Text>
      {location && (
        <>
          <Text>위도: {location.coords.latitude}</Text>
          <Text>경도: {location.coords.longitude}</Text>
        </>
      )}
      {address && (
        <>
          <Text>도시: {address.city}</Text>
          <Text>주소: {address.street} {address.name}</Text>
        </>
      )}
      {errorMsg && <Text>{errorMsg}</Text>}
      <Button title="위치 추적 시작" onPress={startWatching} />
    </View>
  );
}
```


## 주요 함수 설명

- **Location.requestForegroundPermissionsAsync()**: 위치 권한 요청
- **Location.getCurrentPositionAsync()**: 현재 위치의 위도, 경도 정보 반환
- **Location.reverseGeocodeAsync({ latitude, longitude })**: 위도, 경도를 주소 정보로 변환
- **Location.watchPositionAsync(options, callback)**: 사용자가 이동할 때마다 위치를 실시간으로 추적