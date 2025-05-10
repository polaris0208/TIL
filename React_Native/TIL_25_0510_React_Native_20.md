# 배포 준비

## 아이콘 및 스플래시 화면 설정
- `app.json`에서 아이콘과 스플래시 화면을 설정
- 예: 검은 배경 + 야자수 이미지 아이콘 사용
- 스플래시 화면 배경 색 설정 예시:

```json
{
  "expo": {
    "splash": {
      "backgroundColor": "#000000"
    },
    "android": {
      "splash": {
        "backgroundColor": "#000000"
      }
    }
  }
}
```

## 앱 빌드 vs 앱스토어 등록
- 앱 빌드는 무료로 가능 (Expo 사용 시)
- 앱스토어 등록은 유료 (애플 $99/년, 구글 $25 1회)
- 등록 과정이 번거롭기 때문에 데모 수준에선 빌드까지만 수행

## Expo 빌드 방식
- 로컬에서 빌드하지 않고 Expo 서버에서 빌드 수행
- Expo 서버는 macOS와 Linux 환경에서 자동으로 빌드
- Windows 사용자도 iOS 앱 빌드 가능

\`\`\`bash
# Android 앱 빌드
npx expo build:android

# iOS 앱 빌드
npx expo build:ios
\`\`\`

## 빌드 결과
- Expo 서버에서 APK 또는 IPA 파일 생성
- 이 파일을 수동으로 앱스토어에 업로드 가능

## React Native for Windows / macOS
- Microsoft에서 개발한 확장 기능
- 하나의 코드베이스로 Windows/macOS 앱 제작 가능
- 기존 React Native API와 유사

\`\`\`bash
npx react-native init MyApp --template react-native@latest
\`\`\`

## React Native + VR
- React Native를 사용하여 VR 콘텐츠 제작 가능
- 예시 컴포넌트:
\`\`\`jsx
<Scene>
  <Pano source={{ uri: '360image.jpg' }} />
  <Text>Hello World</Text>
</Scene>
\`\`\`

## 웹 배포 (GitHub Pages)
- 웹사이트 배포도 가능 (`react-native-web` 기반)
- 과정 요약:
  1. GitHub 리포지토리 연결
  2. `gh-pages` 설치
  3. `package.json`에 배포 스크립트 추가
  4. `npm run deploy` 실행

\`\`\`bash
npm install gh-pages --save-dev
\`\`\`

\`\`\`json
"scripts": {
  "predeploy": "npm run build",
  "deploy": "gh-pages -d build"
}
\`\`\`