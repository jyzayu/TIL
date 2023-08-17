## Web Server:

요청에 대한 응답으로 웹브라우저로 페이지(html css js)를 제공한다.


## Key points about web servers:

HTTP Protocol: 웹 브라우저와 통신을 위해 HTTP 프로토콜을 사용한다. 소켓을 SSL 프로토콜로 대체하여 HTTPS로 사용한다.

Static Content: 정적 컨텐츠 또는 적게 처리하여 응답하는 컨텐츠 제공에 유리하다.

Examples: Popular web servers include Apache, Nginx, Microsoft IIS (Internet Information Services), and LiteSpeed.

## Web Application Server (WAS):

A Web Application Server, often referred to as an Application Server, is a software framework specifically designed to host, manage, and execute web applications. Unlike web servers that mainly serve static content, WAS is responsible for handling dynamic content, business logic, and database interactions for web applications.

## Key points about Web Application Servers:

Dynamic Content: WAS는 동적 컨텐츠를 다룹니다. 사용자 입력, db query실행해 상호작용하고, 복잡한 비즈니스 로직을 처리하여 동적인 html또는 데이터를 응답합니다. 

Application Framework: WAS는 다양한 언어,프레임워크를 지원하고, 개발,배포,운영 도구와 런타임 환경을 제공합니다

Load Balancing: 많은 WAS는 다양한 서버에 걸쳐 들어오는 요청들을 분산시키는 로드 밸런싱 능력을 가져서 더 좋은 성능과 이용성을 보장한다.

Examples: Common Web Application Servers include Apache Tomcat, WildFly (formerly JBoss), IBM WebSphere, Microsoft ASP.NET, and Oracle WebLogic.


최근에는 서비스가 컨테이너로 패키징되고 Docker 및 Kubernetes와 같은 플랫폼을 사용하여 배포되는 컨테이너화 및 마이크로서비스 아키텍처도 증가했습니다.  
이로 인해 컨테이너화된 애플리케이션에 맞는 경량 서버 솔루션이 개발되었습니다. 

기술 환경은 빠르게 변할 수 있으며 시간이 지남에 따라 새로운 도구와 접근 방식이 나타날 수 있음을 기억하십시오. 웹 개발의 최신 동향과 모범 사례를 최신 상태로 유지하는 것이 중요합니다.
