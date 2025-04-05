## 셀레니움 기본 설정 & 테스트

### 현재 사용하는 프로필 정보 확인

- `chrome://version/` 접속하여 경로 확인 가능

### 프로필 충돌 방지

- 사용할 프로필이 열려 있는 경우 출동 발생
- 기존 프로필 종료를 위해 브라우저를 백그라운드에서 종료 처리

```py
import os
import time

os.system('killall "Google Chrome"')
time.sleep(2)
```

### 셀레니움 의존성 설정
- `pip install selenium`
-  필요한 라이브러리 불러오기

```py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
```

### 셀레니움 설정
- `Options()`
  - Chrome 실행을 위한 설정 객체를 생성
- `--headless`
  - 브라우저 UI 없이 백그라운드에서 실행
  - 서버 환경이나 자동화 테스트에 적합
- `user-data-dir=/Users/name/selenium_user_data`
  - 사용자 데이터(쿠키, 세션 등)를 저장하는 디렉터리를 지정
  - 로그인 상태 등을 유지
- `disable-blink-features=AutomationControlled`
  - 브라우저가 자동화 도구(봇)로 탐지되는 것을 방지
  - 사이트에서 Selenium 사용을 감지 방지
- `detach=True`
  - 스크립트가 종료되어도 브라우저 창이 닫히지 않도록 유지
- `excludeSwitches=["enable-logging"]`
  - DevTools 관련 경고 및 로그를 숨김

```py
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("user-data-dir=/Users/yeongung/selenium_user_data")
chrome_options.add_argument("disable-blink-features=AutomationControlled ")
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
```

### 드라이버 설정
- `service=Service(ChromeDriverManager().install()` : 사용하는 크롬에 맞는 드라이버 설치 후 실행

```py
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()
driver.get("https://polaris0208.github.io/")
```

### 원하는 데이터 추출
- `driver.find_elements` : 클래스명 기준으로 데이터 리스트 추출
- `soup.find_element` : 데이터 리스트에서 데이터 추출

```py
soup_list = driver.find_elements(By.CLASS_NAME, "post-preview")

with open("output.txt", "w", encoding="utf-8") as f:
    for soup in soup_list:
        entry = soup.find_element(By.CLASS_NAME, "post-entry")
        text = entry.text.strip()
        print(f"\n\n{text}")
        f.write(text + "\n\n")
```

### 자동화 프로그램(Mac)
- `Automator` 실행
- `셀 스트립트 실행` 선택
- 실행할 명령어 입력 후 저장
- 원하는 경로에 실행 아이콘 생성

```py
cd /Users/name/desktop/selenium
source venv/bin/activate

cd /Users/name/desktop/selenium
python3 main.py
```