프로토콜은 많은 기능들을 포함하는 매우 크고 복잡한 시스템
복잡함을 단순화하도록 나누어 구현(계층화)
어느 계층의 기능만을 바꾸더라도 전체 기능을 바꾸는데 용이
컴퓨터 네트워크 프로토콜은 이러한 계층화 구조를 가짐

### OSI 참조 모델
• 다양한 종류의 컴퓨터 시스템간 통신을 가능하게
하는 네트워크 시스템 설계를 위한 계층 구조
• 서로 연관된 7개의 계층으로 이루어짐

### TCP/IP 모델
• OSI 이전에 개발
• 5개의 계층으로 이루어짐
• 인터넷에서 사용되고 있는 프로토콜 스택

![image](https://github.com/jyzayu/TIL/assets/55649979/fa67ed92-a6a3-41e0-947c-27bbd15c691f)

### 인터넷 구조의 특성
1. 느슨한 계층화 구조를 가짐
- 인터넷 프로토콜에서는 엄격한 구조화를 요구하지 않음
- 특정 기능들이 한 곳 이상의 계층에서 구현됨
(예) 흐름 제어, 에러 제어 기능이 제2계층과 제4계층에 존재
2.  위 계층과 아래 계층 간의 규정과 계층간의 규정을 만족해야 함

 3. 네트워크 계층에서 주로 인터넷 프로토콜 IP 사용
- 하부 네트워크 구조에서는 이더넷, FDDI, ATM 등의
여러 가지 서로 다른 네트워크 기술을 사용 할 수 있음

### • 프로토콜 각 계층마다 고유의 PDU를 사용
4 계층 - 세그먼트(Segment)
3 계층 - 데이터그램(Datagram)
2 계층 - 프레임(Frame)

![image](https://github.com/jyzayu/TIL/assets/55649979/d28bde68-5700-4ee8-8493-1380c624f352)
## OSI 7계층의 기본 기능들
### 물리 계층(Physical Layer)
• OSI 참조 모델에서 가장 하위 계층
• 매체를 통해 데이터를 전송에 필요한 기능들을 수행
• 각 네트워크 장비의 인터페이스에 관한 사항, 데이터의
표현 및 처리 절차 등 기술

[ 기능 ]
• 매체의 물리적 특성
- 꼬임 2중선, 동축케이블, 광섬유 등의 매체를 통한
인터페이스 특성 등을 규정
• 비트의 동기화
- 송신자와 수신자 간의 비트 동기화를 위한 클럭에 대해 규정
• 데이터의 전송 속도
- 초당 전송되어지는 데이터의 양을 규정
• 물리적 접속 형태
- 링크를 통한 컴퓨팅 장비의 접속 형태에 대해 규정
- 구성 형태 : 스타형, 버스형, 링형 등
• 전송 모드
- 두 노드 간 데이터를 전송하는 방식 기술
- 방식 : 단방향 모드, 반이중 전송, 전이중 전송 등

### 데이터 링크 계층(Data Link Layer)
• 직접 연결된 두 노드 간의 신뢰성 있는 전송 목적
• 상위 계층(네트워크 계층)으로부터 데이터그램을
받음 → 목적지 노드와 송신 노드 등의 주소, 다른
제어 정보를 포함하는 헤더와 데이터그램의 뒤에
꼬리를 덧붙여 프레임을 생성

데이터 링크 계층(Data Link Layer)
[ 기능 ]
• 물리 주소 지정
- 스테이션이 물리 계층의 링크에 직접 연결 → 프레임
전송할 때 송신 스테이션과 수신 스테이션을 구분하기
위해 각 스테이션 마다 고유 주소 부여
• 프레임 구성
- 네트워크 계층으로부터 받은 데이터그램에 물리 주소
등을 포함한 헤더를 첨가하여 프레임 구성
• 오류 제어
- 프레임이 물리 매체를 통하여 전송할 때 잡음 등의
영향으로 에러 발생 혹은 프레임 손실 발생 가능
→ 발생한 비트 에러 검출, 정정, 손실된 프레임에
대한 재전송 등의 오류 제어 기능 수행

데이터 링크 계층(Data Link Layer)
[ 기능 ]
• 흐름 제어(Flow Control)
- 전송 스테이션이 수신 스테이션에서의 처리 능력 이상으로
데이터를 전송하지 못하도록 하는 기능
- 이 기능을 수행하기 위해 수신 스테이션의 여유 버퍼 크기에
대한 정보를 송신 스테이션으로 보내주는 메커니즘 필요

![image](https://github.com/jyzayu/TIL/assets/55649979/dc12e1ce-8506-4c7a-bc00-b15fbe1a795d)

데이터 링크 계층(Data Link Layer)
[ 기능 ]
• 매체 접근제어
- 여러 전송 호스트들이 하나의 통신 매체를 공유하여
데이터를 전송하려고 할 때, 데이터 전송 호스트의
순서를 정해 매체를 사용하도록 하는 기능
- 임의의 접근 방법, 스케줄링에 의한 접근 방법 등

### 네트워크 계층(Network Layer)
• 제 3계층
• 필요에 따라 노드와 노드 간의 전송을 위한 연결 설정 및 해지 기능 담당

[ 기능 ]
• 라우팅(routing) 기능
- 전송 호스트에서 목적지 호스트가 속한 네트워크로 가는 가장 좋은 경로를 선택하는 것
- 각 라우터는 라우팅 테이블(목적지 호스트까지 경로 정보 입력)을 가지고 있음
- 패킷의 헤더에 있는 목적지 주소를 보고 라우팅 테이블을 참조하여 가장 좋은 경로 선택

• 순방향 전송 기능
- 라우팅 기능으로부터 가장 좋은 경로를 결정한 후에,
결정된 좋은 경로를 라우팅 테이블에 저장
- 수신된 목적지 주소를 라우팅 테이블에서 찾아 해당
출력 포트로 패킷을 전달

###  전송 계층(Transport Layer)
• 세션 계층과 네트워크 계층 사이에 위치
• 종간(end-to-end) 통신을 지원

[ 기능 ]
• 분할과 재조립(Segment&Reassembly)
- 분할(segment) : 상위 계층(응용계층)에서 받은 데이터를 세그먼트
(segment)라 불리는 패킷으로 잘라서 하위 계층
(네트워크 계층)으로 전달하는 것
→ 전송 노드에서 동작
- 수신 호스트에서는 네트워크 계층에서 받은 패킷을 다시 데이터
메시지로 재조립(reassembly)하여 상위 계층에 전달하는 기능 수행
→ 수신 노드에서 동작
![image](https://github.com/jyzayu/TIL/assets/55649979/394451c4-f706-4c0f-9b94-6c01fa827a09)

• 에러 제어(Error Control)
- 에러 : 통신 링크 상에서 패킷이 전송될 때 신호의 왜곡, 간섭,
네트워크의 혼잡 등으로 인한 패킷 손실이 발생하는 것
* 이진수 값 “0→1”, “1→0” 수신되는 경우,
패킷이 전송 노드에서 네트워크를 통해 수신 노드로 전송 되는 경우
- 전송 노드와 수신 노드 사이에 이루어짐

• 흐름 제어(Flow Control)
- 전송 노드와 수신 노드 종단 간의 호스트 간에 이루어 짐
- 송신 노드가 데이터를 전송할 때 수신자가 처리할 수 있는
이상의 데이터를 보내지 않는 것을 기본으로 함

• 혼잡 제어(Congestion Control)
혼잡:
- 초기에는 라우터 버퍼에 수신한 패킷을 저장하여 처리
→ 지연(delay) 증가
- 지속된 혼잡 발생
→ 라우터의 버퍼가 full
→ 이상 패킷을 수신할 수 없음
→ 전송된 패킷은 라우터의 버퍼에 들어가지 못하고 손실(loss)
- 혼잡: 네트워크의 라우터가 처리할 수 있는 능력 이상으로 패킷을 수신하는 경우 발생

### 세션 계층(Session Layer)
• 전송 호스트와 수신 호스트 사이에서 동작하는
특정 한 쌍의 프로세스들 간의 세션이라 부르는
연결을 확립하고 유지하며 동기화를 제공하는
기능 수행

 동기화
데이터 유니트를 전송 계층으로 전달하기 위한
순서를 결정하고 데이터에 대한 중간 점검 및
복구를 위한 동기 제공

 대화제어
두 호스트 간의 대화를 지원하는데 일방 전송,
반이중 전송 혹은 전이중 전송 등을 결정함

 반이중(half duplexing) 전송
송신자와 수신자 간 양방향 통신이나 한 번에
한 방향씩만 전송

 전이중(full duplexing) 전송
송신자와 수신자 간 양방향 통신이나 동시에
양방향으로 전송

### 표현 계층(Presentation Layer)
• 사용자가 통신하거나 참조할 수 있도록 정보를 표현하는 기능 수행
• 전송되는 메시지에 표현된 문법 내용을 양단의 프로세스가 해석하는
기능 제공
• 전송 노드가 전달하려는 의미(semantic)를 수신 프로세서가 정확히
이해할 수 있도록 함
• 코드 간의 변환 및 여러 표준 간의 데이터 형식을 정의

 암호화
- 비밀성을 제공하거나 보내는 데이터의 효율적인
전송을 위하여 암호화(encryption)함
- 받은 데이터를 복호화(decryption)로 변환
- 
 압축
- 효율적이고 안정된 데이터 전송을 수행하기
위해 데이터의 양을 줄여 보냄
- 멀티미디어 데이터 전송에 매우 필요
  
 변환
- 수신 호스트에서 데이터 형식을 해석할 수
있도록 미리 정의된 형식으로 변환
- 수신자가 이해할 수 있는 형식으로 변환

### 응용 계층(Application Layer)
• 네트워크 응용을 위한 하나의 구성 요소
• 다음과 같은 일들을 정의
- 교환되는 메시지의 타입
- 여러 메시지 타입들의 구문과 의미
- 메시지를 클라이언트와 서버 사이에
언제, 어떻게 전송하고 응답할 것인가?

대부분 RFCs (Request For Comments)에 규정
HTTP, FTP, SMTP, SNMP, DNS,
