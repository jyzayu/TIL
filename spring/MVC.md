### MVC란
MVC는 Model, View, Controller의 약자이며, 각 레이어간 기능을 구분하는데 중점을 둔 디자인 패턴입니다.
Model은 데이터 관리 및 비즈니스 로직을 처리하는 부분이며, (DAO, DTO, Service 등)
View는 비즈니스 로직의 처리 결과를 통해 유저 인터페이스가 표현되는 구간입니다. (html, jsp, tymeleaf, mustache 등 화면을 구성하기도 하고, Rest API로 서버가 구현된다면 json 응답으로 구성되기도 한다.)
Controller는 사용자의 요청을 처리하고 Model과 View를 중개하는 역할을 합니다. Model과 View는 서로 연결되어 있지 않기 때문에 Controller가 사이에서 통신 매체가 되어줍니다.

### MVC 요청 처리 과정
![image](https://github.com/jyzayu/TIL/assets/55649979/b6aaad78-5a7e-4e02-95fb-fb91d0bbceda)
1. dispatcher servlet이 요청을 받습니다.
2. 요청URL을 갖고 핸들러 매핑이 요청을 처리할 handler를 찾습니다.
3. 찾은 handler 정보를 갖고 hadler Adapter 에게 요청 전달을 맡깁니다.
4. handler adapter가 해당 controller에 요청을 전달합니다.
5. handler에서 요청 처리하여 view name을 dispatcher servlet에게 데이터와 함께 전달합니다.
6. view name을 갖고 dispatcher servlet이 ViewResolver를 통해 view를 찾습니다.
7.  dispatcher servlet이 controller에서 데이터를 view에 추가합니다.
8. 클라이언트에게 데이터가 추가된 뷰를 응답합니다.

출처: https://dev-coco.tistory.com/163 [슬기로운 개발생활:티스토리]
