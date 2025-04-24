# React Native ScrollView와 관련 스타일 정리

- React Native에서는 웹 브라우저처럼 기본 스크롤 동작이 없다.  
  따라서 여러 항목을 스크롤하려면 `ScrollView` 컴포넌트를 사용해야 한다.

- `ScrollView`는 수직 또는 수평 스크롤이 가능하며, `horizontal` 속성을 사용하면 수평 스크롤이 가능하다.

- 스타일을 적용할 때는 `style` 대신 `contentContainerStyle` 속성을 사용해야 스크롤 영역에 스타일이 적용된다.

- `ScrollView`에 `flex` 속성을 주면 스크롤이 비활성화될 수 있다.  
  스크롤 영역은 화면보다 커야 하므로 `flex`를 제거해야 한다.

- 각 항목의 크기를 화면 크기에 맞추려면 `Dimensions` API를 사용하여 화면 너비/높이를 동적으로 구할 수 있다.
  ```js
  import { Dimensions } from 'react-native';
  const { width } = Dimensions.get('window');
  ```

- `pagingEnabled` 속성을 사용하면 스크롤이 페이지 단위로 동작해 부드럽고 직관적인 전환이 가능하다.

- 스크롤 인디케이터(스크롤바)는 `showsHorizontalScrollIndicator`, `showsVerticalScrollIndicator` 속성을 `false`로 설정하여 숨길 수 있다.

- `indicatorStyle` 속성으로 iOS에서 스크롤 인디케이터 색상을 변경할 수 있다. Android에서는 `persistentScrollbar` 등의 Android 전용 속성이 있다.

- 디버깅 시 기기를 흔들어 개발자 메뉴를 열고 `Element Inspector`를 사용할 수 있다.  
  이를 통해 요소의 크기, 마진, 패딩 등 UI 구성 요소 정보를 시각적으로 확인 가능하다.

- ScrollView는 유연하고 다양한 속성을 제공하지만, 문서를 참고하면서 필요한 속성만 익히는 것이 효율적이다.