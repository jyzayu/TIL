### 시스템 소프트웨어(운영체제)
컴퓨터 시스템의 전반적인 동작을 제어하고 조정하는 시스템 프로그램

하드웨어와 응용프로그램 간의 인터페이스 역할 수행

### 목적
1) 작업 기록 및 전반적인 동작 감독

2) 컴퓨터 자원(네트워크, 파일, 메모리 등)을 관리
- 다수 사용자에게 하드웨어 자원의 효율적 배분
- 멀티태스킹 지원
- 가상메모리 사용 : 실제 주기억장치보다 큰 영역 활용

### 새로운 운영 형태

- 사용자 편의성 : 명령어를 입력하고 이해하기 용이
• 상호 대화식 프로세싱


일괄처리 프로세싱(Batch processing)

• 처리할 프로그램을 원칙적으로 도착 순서에 따라 하나씩 실행 : FIFO(First-In First Out) 방식

- 최적화 환경 제공 : 효율적 제어 및 관리
- 시스템 효율성 : 기본 환경 제공 및 응용 소프트웨어 사용 가능
• 다중 프로그래밍

병렬처리 및 실시간 처리

병렬처리

• 하나의 프로그램을 여러 개의 작업으로 분할하여 몇 개의 CPU에 할당

→ 빠른 실행 결과 도출

• 다중 처리 (Multiprocessing)

: 여러 개의 프로그램을 여러 개의 CPU가 실행하여 전체적인 성능 향상

실시간처리

• 컴퓨터로 하여금 정해진 짧은 시간(거의 실시간) 내에 작업을 완료

예) 자율자동차의 경우 센서들을 통해서 들어오는 외부 세계의 데이터,

동영상의 비디오 부분과 오디오 부분의 실시간 처리

### 운영체제 구성
ㅁ감독프로그램
명령어 처리기
UNIX: shell
인터럽트 처리기

입출력제어기


### 운영체제 기능
사용자 인터페이스 지원
자원관리 (자원관리모듈 집합인 커널로) 프로세스,메모리,파일,장치관리
자원 스케줄링하여
메모리관리
파일관리
