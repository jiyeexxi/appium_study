# 📱 Appium + Python 기반 Android 앱 자동화 (Android Studio 에뮬레이터 활용)

이 프로젝트는 **Appium**과 **Python**을 활용하여 **Android Studio 에뮬레이터**에서 모바일 앱을 자동화하는 프로젝트입니다.  
Android 디바이스 없이 **에뮬레이터(AVD)** 환경에서 UI 테스트를 수행할 수 있도록 구성되어 있습니다.

## 🚀 기능
- Android Studio 에뮬레이터(AVD) 기반 UI 자동화 테스트
- Appium을 활용한 Android 앱 UI 테스트
- Pytest를 통한 테스트 실행 및 리포트 생성
- GitHub Actions 또는 Jenkins를 활용한 CI/CD 연동 (추후 추가 예정)

## 📱 테스트 대상 앱
이 프로젝트에서 사용된 테스트 앱은 아래 링크에서 참고하였습니다.

🔗 [테스트 앱 제공 사이트](https://goddessbest-qa.tistory.com/263)

## 🛠️ 기술 스택
- **프로그래밍 언어:** Python
- **자동화 프레임워크:** Appium
- **테스트 러너:** Pytest
- **가상 디바이스:** Android Studio AVD (Emulator)
- **CI/CD:** GitHub Actions (예정)

## 📂 프로젝트 구조
.
├── README.md
└── appium_test.py


## 📑 테스트 케이스
앱을 분석한 뒤 자동화로 구현할 TC를 직접 작성하였습니다.

| **TC ID**  | **내용** | **사전조건** | **단계** | **예상결과** |
|------------| --- | --- | --- | --- |
| **TC_001** | `button_1` 버튼 선택 기능 확인 | 앱 메인 화면에 접근한 상태 | `button_1` 버튼 선택 | "button_1" → "touch!" 로 버튼 글자가 변경됨 |
| **TC_002** | `button_2` 버튼 선택 기능 확인 | 앱 메인 화면에 접근한 상태 | `button_2` 버튼 선택 | "button_2" 버튼 글자가 변경되지 않음 |
| **TC_003** | 텍스트박스에 문자 입력 기능 확인 | 앱 메인 화면에 접근한 상태 | 영어 입력 | 입력이 됨 |
|            |  |  | 숫자 입력 | 입력이 됨 |
|            |  |  | 한글 입력 | 입력이 되지 않음 |
|            |  |  | 띄어쓰기 입력 | 입력이 됨 |
|            |  |  | 특수문자 입력 | 입력이 됨 |
| **TC_004** | 텍스트박스에 공백만 입력 기능 확인 | 앱 메인 화면에 접근한 뒤 텍스트 박스에 문자가 입력되지 않은 상태 | 공백만 입력 | 입력이 됨 |
| **TC_005** | 체크박스 선택 기능 확인 | 앱 메인 화면에 접근한 상태 | 체크박스 선택 | 체크박스가 활성화됨 "unchecked" → "checked"로 글자가 변경됨 |
| **TC_006** | 토글 버튼 선택 기능 확인 | 앱 메인 화면에 접근한 상태 | 토글 버튼 선택 | 토글버튼이 활성화됨 |
| **TC_007** | `button_3` 버튼 선택 기능 확인 | 앱 메인 화면에 접근한 상태 | 하단으로 스크롤을 내림 | `button_3` 버튼이 존재함 |
|            |  |  | `button_3` 버튼 선택 | "button_2" 버튼 글자가 변경되지 않음 |
| **TC_008** | `home` 버튼 선택 시 초기화 기능 확인 | `button_1` 버튼이 선택된 상태 텍스트박스에 글자가 입력된 상태 체크박스와 토글 버튼이 활성화된 상태 | `home` 버튼 선택 | 화면이 초기화됨, 버튼 글자 및 입력 값 리셋 |
| **TC_009** | `my` 버튼 선택 기능 확인 | `button_1` 버튼이 선택된 상태 텍스트박스에 글자가 입력된 상태 체크박스와 토글 버튼이 활성화된 상태 | `my` 버튼 선택 | 컴포넌트 변경 없음, 상태 그대로 유지 |
| **TC_010** | `button_1`을 반복해서 클릭한 경우 문구가 변경되지 않는지 확인 | `button_1`의 문구는 "Click Me"로 초기화되어 있음 | `button_1`을 5번 이상 클릭 | 버튼 문구는 첫 번째 클릭 후 "touch!"로 변경되고, 이후 클릭에서는 문구가 변경되지 않는다. |
| **TC_011** | 텍스트박스에 아무런 입력 없이 엔터키를 눌렀을 때의 동작 확인 | 텍스트박스는 빈 상태이다. | 텍스트박스에 아무런 입력 없이 엔터키를 누른다. | 엔터키 입력 후 텍스트박스는 비어있고, 추가 동작 없이 빈 입력값으로 전송된다. |
| **TC_012** | 체크박스를 체크 후 다시 해제했을 때 문구가 "unchecked"로 변경되는지 확인 | 체크박스는 초기화되어 있고 문구는 "unchecked"로 설정되어 있다. | 체크박스를 체크한 후, 다시 해제한다. | 체크박스의 상태가 "checked"에서 "unchecked"로 변경되고, 문구도 "unchecked"로 변경된다. |
| **TC_013** | 토글 버튼을 클릭하여 "ON"과 "OFF"를 번갈아 가며 클릭 시 상태가 정상적으로 변경되는지 확인 | 토글 버튼은 "OFF" 상태로 초기화되어 있다. | 토글 버튼을 한 번 클릭하여 "ON" 상태로 만든 후, 다시 클릭하여 "OFF"로 만든다. | 첫 번째 클릭 후 "ON"으로 변경되고, 두 번째 클릭 후 "OFF"로 변경된다. |
