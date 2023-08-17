HTTPS 통신을 적용하기 위해 NGINX에 대한 이해가 필요했다. 

## NGINX란?
Nginx는 WS(Web Server)의 일종이다. 주로 정적 컨텐츠를 제공하거나 ReverseProxy, LoadBalancer의 역할을 한다.

Nginx는 로드 밸런스 처리에 특화된 웹 서버 프로그램이다.  
Nginx를 서버 앞 단에 두어 Express가 사용하는 실제 포트를 숨기고 Nginx의 80번 포트를 통해 Reverse proxing 함으로써 보안 이슈를 방지하고,  
Nginx의 여러 기능도 사용할 수 있다.

Reverse proxy란 사용자가 실제 서버의 정보를 알지 못하게 함을 의미한다.  
사용자들이 서버에 요청한 내용을 리버스 프록시가 배후의 서버에서 응답 데이터를 받아와 다시 사용자에게 전송한다..
![image](https://github.com/jyzayu/TIL/assets/55649979/91074404-eeb6-4e0c-b70c-5a4cd1afaa36)

## NGINX의 등장 배경
NGINX 등장이전 Apache가 웹서버로써의 높은 인기를 가졌다. 잘 사용되던 Apache 웹서버는 어느순간 어떠한 문제를 가져왔다. Apache의 요청처리 메커니즘과 함께 어떠한 문제를 가져왔는지 살펴보자.
![image](https://github.com/jyzayu/TIL/assets/55649979/a97bff25-d6e1-4e74-8d9d-dc6194bddd3f)

초기의 Apache는 그림과 같이 요청(Request)이 들어올 떄 마다 새로운 Process를 생성하여 네트워크 연결을 하고 요청을 처리했다.(이러한 처리방식을 prefork라고 함)

그런데, 2000년에 접어 들고 인터넷 트래픽이 증가하면서 아파치의 요청 처리방식은 C10K 문제를 가져왔다.

C10K 문제란 Connection 10000 Problem의 줄임말로 웹서버가 1만개의 동시 Connection을 처리하기 어렵다는 의미이다.

## 동시 Connection
![image](https://github.com/jyzayu/TIL/assets/55649979/c98bca4c-4a1f-4ae8-a080-a1a419e519af)

웹서버는 클라이언트로 부터 요청이 들어오면 Connection을 생성하고 유지한다. 그리고 그림과 같이 클라이언트는 생성된 Connection을 통해 또다른 요청을 서버에게 전달한다.

이렇게 Connection 하나로 여러 요청을 처리하는 이유는 다음과 같다. 클라이언트와 서버는 Connection을 생성하는데 여러가지 절차가 필요하다. 그래서 매 요청마다 Connection을 생성하는것은 비효율적이고 느렸다.

비효율성을 해결하기 위해 사람들은 이미 만들어진 Connection이 있다면 이를 활용하여 요청을 보내고자 하였다.

이렇게 유지되는 Connection들을 동시 Connection이라고 한다.

💡 여담으로 HTTP 프로토콜 Header부분의 Keep-Alive가 바로 Connection을 얼마나 유지할 것인지에 대한 통신 규약이다.

## 이때, Apache 서버는 C10K문제를 가져왔다.
![image](https://github.com/jyzayu/TIL/assets/55649979/5eff5265-d4dc-4eb6-abbe-3bb9e3bb30b3)

그림과 같이 Apache서버는 요청이 들어올 때 마다, Process를 생성했는데 요청이 만단위를 넘어가면서 어느순간 부터 요청에 대한 Connection을 생성하지 못한것이다.

이러한 문제를 가져온 원인은 다음과 같았다.

메모리 부족 Apache서버는 Connection이 생성될 때마다 Process를 생성해야했는데 동시에 유지해야할 Connection이 많아지면서 유지해야할 Process가 증가했고 메모리 부족을 발생시켰다.
CPU 과부하 또한, 실행중인 Process가 많아지면서 CPU는 Process를 처리 할 때, 컨텍스트 스위칭을 굉장히 많이해야했다. 그래서 CPU의 부하가 증가했다.
결국, 수많은 동시 커넥션을 처리하기엔 Apache의 요청 처리구조는 부적합했다.

그래서 Apache의 단점을 보완하기 위해 2004년 NGINX가 등장했다.


## NGINX의 요청 처리 방식
![image](https://github.com/jyzayu/TIL/assets/55649979/fb3a3b83-6ec2-4774-82a8-acb96a816e17)

NGINX는 MasterProcess를 통해 설정 파일을 읽고 WorkerProcess와 같은 자식 Process 3종류를 생성한다. (cache loader, cache manager가 있음)

그리고 생성된 WorkerProcess는 요청이 들어오면 Connection을 형성하고 요청을 처리한다. 요청에 따라서 매번 Process를 생성하던 Apache와 달리, NGINX는 MasterProcess에 따라 WorkerProcess를 생성하고 고정된 개수의 WorkerProcess 들이 요청을 처리한다.

이렇게 고정된 Process의 개수로 요청을 처리하기 위해 NGINX는 Event-Driven 방식으로 요청을 처리한다.

## Event-Driven이란?
NGINX는 형성된 Connection에 아무런 요청이 없으면 새로운 요청에 대한 Connection을 형성하여 요청을 처리한다.  
또는 이미 만들어진 다른 Connection으로부터 요청을 처리한다. Nginx에서의 Conneciton 형성, Connection 제거, 새로운 요청 처리를 Event라고 부른다.  
또한, Event를 비동기 방식으로 처리하는 것을 Event-Driven이라고 한다.



![image](https://github.com/jyzayu/TIL/assets/55649979/ba70cf35-699e-4e00-855b-d8cd2c90f064)

NGINX는 그림과 같이 큐형태의 저장소에 Event들을 담아 WorkerProcess가 순차적으로 작업을 처리한다.


## NGINX의 Apache의 차이점
Apache는 동기방식으로 하나의 Connection이 끝날 때 까지 Process를 유지했다.

반면, NGINX는 고정된 WokerProcess를 생성하고 Event가 발생 할 때마다 요청을 처리하는 비동기 Event-Driven 방식을 사용한다는 것이 차이점이다.

보통 WorkerProcess는 CPU의 코어 개수만큼 생성하는것이 일반적이라고 한다. (이유: 컨텍스트 스위칭 회수를 최소하 하기 위함.)


## NGINX의 장점
NGINX는 Apache에 비해 성능 측면에서 두가지 장점이있다.

처리할수 있는 동시 커넥션 개수가 훨씬 많다.
동일한 개수의 커넥션 처리 속도가 더 빠르다.
이러한 장점을 가지고 오는 이유를 마지막으로 정리해보자.

고정된 Process 개수 만을 사용하기에 Process 생성 비용이 없다.
또한, Process 개수가 제한되어 CPU의 부담이 줄어든다. (컨텍스트 스위칭이 적어지기 때문)
비동기 방식이기에 Process가 쉬지않고 일을 할 수 있다.

NGINX 활용 방법
도입부에서 이야기햇듯이 NGINX는 정적파일처리, 리버스 프록시, 로드밸런서의 역할로써 WAS의 부담을 줄여주는 역할로 다양하게 활용 할 수 있다.
