### HTTP 요청 메서드
HTTP는 요청 메서드를 정의하여, 주어진 리소스에 수행하길 원하는 행동을 나타냅니다. 

간혹 요청 메서드를 "HTTP 동사"라고 부르기도 합니다. 각각의 메서드는 서로 다른 의미를 구현하지만,

일부 기능은 메서드 집합 간에 서로 공유하기도 합니다. 이를테면 응답 메서드는 안전하거나, 캐시 가능하거나, 멱등성을 가질 수 있습니다.

게시판으로 예를 들자면, 글의 내용에 대한 목록을 보여주는 경우나, 글의 내용을 보는 경우는 Get에 해당합니다.
그리고 글의 내용을 저장하고, 수정할때에 Post를 사용하는 것이죠.

### Get
GET method는 클라이언트에서 서버로 어떠한 리소스로 부터 정보를 요청하기 위해 사용되는 메서드입니다.

좀 더 쉽게 말하자면, 데이터를 읽거나(Read), 검색(Retrieve)할 때에 사용되는 method라고 할 수 있겠네요.

GET은 요청을 전송할 때 URL 주소 끝에 파라미터로 포함되어 전송되며, 이 부분을 쿼리 스트링(QueryString) 이라고 부릅니다.

e.g.) www.example-url.com/resources?name1=송유현&name2=곽철용

위 예는 앞서 말한 쿼리스트링을 포함한 URL입니다. 파라미터인 name1과 name2를 통해 값을 전달받을 수 있습니다.
만약, 요청 파라미터가 여러 개이면 &로 연결합니다.

그리고 GET 요청은 오로지 데이터를 읽을 때만 사용되고 수정할 때는 사용하지 않습니다.
따라서 이런 이유로 사용하면 안전하다고 간주되죠. 즉, 데이터의 변형의 위험없이 사용할 수 있다는 뜻입니다.

### GET 요청 특징
- GET은 불필요한 요청을 제한하기 위해 요청이 캐시될 수 있습니다.
-  : GET을 통해 서버에 리소스를 요청할 때 웹 캐시가 요청을 가로채 서버로부터 리소스를 다시 다운로드하는 대신 리소스의 복사본을 반환한다.
-  HTTP 헤더에서 cache-control 헤더를 통해 캐시 옵션을 지정할 수 있다.

- 파라미터에 내용이 노출되기 때문에 민감한 데이터를 다룰 때 GET 요청을 사용해서는 안 됩니다.
- GET 요청은 브라우저 기록에 남습니다.
- GET 요청을 북마크에 추가할 수 있습니다.
- GET 요청에는 데이터 길이에 대한 제한이 있습니다.
- Get 요청은 성공시, 200(Ok) HTTP 응답 코드를 XML, JSON뿐만 아니라 여러 데이터(html, txt등..), 여러 형식의 데이터와 함께 반환합니다.
- GET 요청은 멱등(idempotent)합니다.



### Post
POSTmethod는 리소스를 생성/업데이트하기 위해 서버에 데이터를 보내는 데 사용됩니다.

GET과 달리 전송해야될 데이터를 HTTP 메세지의 Body에 담아서 전송합니다.
그리고 그 Body의 타입은 요청 헤더의 Content-Type에 요청 데이터의 타입을 표시 따라 결정 된다.
(POST로 요청을 보낼 때는 해야 합니다.)

HTTP 메세지의 Body는 길이의 제한없이 데이터를 전송할 수 있습니다. 그래서 POST 요청은 GET과 달리 대용량 데이터를 전송할 수 있는 이유도 이 때문입니다.


### Post 요청 특징
- POST 요청은 캐시되지 않습니다.
- POST 요청은 브라우저 기록에 남아 있지 않습니다.
- POST 요청을 북마크에 추가할 수 없습니다.
- POST 요청에는 데이터 길이에 대한 제한이 없습니다.
- Post 요청 중 자원 생성은 201(Created) HTTP 응답 코드를 반환합니다.
- Post 요청은 멱등(idempotent)하지 않습니다.
### GET, POST 차이
![image](https://github.com/jyzayu/TIL/assets/55649979/685de3fa-a16e-414a-b597-76038fc47bc6)


### (멱등성) (idempotent)
멱등성이란 연산을 여러 번 적용하더라도 결과가 달라지지 않는 성질(동일한 결과가 나오는 것)을 의미한다.

이에 따라 GET은 설계원칙에 따라 서버의 데이터나 상태를 변경시키지 않아야 멱등하기 때문에 주로 조회를 할 때에 사용해야합니다.

 POST는 서버의 상태나 데이터를 변경시킬 때 사용돼서 멱등하지 않습니다.

게시글을 쓰면 서버에 게시글이 저장이 되고, 게시글을 삭제하면 해당 데이터가 없어지는 등 POST로 요청을 하게 되면 서버의 무언가는 변경되도록 사용됩니다.

이처럼 POST는 생성, 수정, 삭제에 사용할 수 있지만, 생성에는 POST, 수정은 PUT 또는 PATCH, 삭제는 DELETE 가 더 용도에 맞는 메소드라고 할 수 있습니다.



### PUT DELETE 사용 이유?
GET과 POST 이외에도 PUT , DELETE 등을 적절히 사용하는게 좋은데 예를들어 봇의 경우에 사이트를 돌아다니면서 GET 요청을 날린다. 

이럴 때 DELETE 등을 GET으로 처리하면 봇에 의해 서버에 있는 리소스들이 삭제 되는 상황이 일어 날수 있다!

 POST는 데이터가 Body로 전송되고, 내용이 눈에 보이지 않아 GET보다 보안적인 면에서 안전하다고 생각할 수 있지만, 

 POST 요청도 크롬의 개발자 도구, Fiddler와 같은 툴로 요청 내용을 확인할 수 있기 때문에 민감한 데이터의 경우에는 반드시 암호화해 전송해야 합니다.

 POST는 생성, 수정, 삭제에 사용할 수 있지만, 생성에는 POST, 수정은 PUT 또는 PATCH, 삭제는 DELETE 가 더 용도에 맞는 메소드라고 할 수 있습니다.

