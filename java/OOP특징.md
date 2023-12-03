OOP 4가지 특징
1. 캡슐화 
- 클래스 내의 연관된 속성과 함수를 하나의 캡슐로 묶어 외부로부터 접근을 최소화하는 것을 의미합니다.
- 정보를 직접 외부에 노출하지 않고 필요에 따라 접근할 수 있는 인터페이스를 제공합니다.
-  클래스의 캡슐화는 public, static, private, protected와 같은 접근제한자를 통해 구현할 수 있다.
- public: 하위 클래스와 인스턴스에서 접근 가능.
- static: 클래스와 외부에서 접근 가능. 인스턴스에서는 접근 불가
- private: 클래스 본인만 접근 가능, 하위 클래스, 인스턴스 접근 불가
- protected: 클래스 본인, 하위 클래스에서 접근 가능, 인스턴스 접근 불가

```
public poor, boil, seasoning 
-> private poor boil() seasoning()
public cook {  seasoning(boil(poor()));}
```
- public이었던 Pharmacist의 메소드들을 모두 private으로 변경했다. 그리고 이들을 모두 실행하는 public 메소드 operate를 새로 생성했다.
- Patient에서는 Pharmacist의 opreate 메소드만 접근 가능하다. 하지만, opreate에서 Pharmacist에서 접근해야하는 기능들은 모두 접근할 수 있다.
- 즉, Pharmacist  측면에서는 Patient에 operate 메소드만 노출시키고, 그 외 메소드들은 감춘 것이다. 즉, 데이터 은닉과 데이터 보호를 실현한 것이다.
- 아울러, 코드적으로도 Pharmacist의 변경사항이 생기면, 해당 Class 변경해주면 된다. 유지보수의 용이성이 개선된 것이다.

2. 상속
- 기존에 구현한 클래스를 재사용하여 같은 속성과 기능을 갖는 하위 클래스를 구현하는 것을 의미합니다.
3. 추상화
- 객체들의 공통적인 속성과 기능을 모아 정의하고 이에 기반하여 객체로 구현하는 것입니다.
- 구체적인 개념이 아닌 추상적인 개념에 의존해야 설계를 유연하게 변경할 수 있습니다.
- 공통적인 특징을 정의하는 데 프로그래밍적으로 활용되는 개념이 abstract class와 interface입니다.
```
abstract class SportsTeam
class SoccerTeam extends SportsTeam
class BaseballTeam extends SportsTeam
class A {
  private final SportsTeam sportsTeam;   - soccerTeam or BaseballTeam 유연하게 변경 가능
}
```
- abstract class와 interface의 차이는 다음 글에서 다룬다.
4. 다형성
- 어떤 객체의 속성이나 기능이 상황에 따라 여러 형태로 변할 수 있다는 것을 의미합니다.
- 다형성 구현 예시로 상속/구현 상황에서 메서드 오버라이딩/오버로딩이 있습니다.

https://coldpresso.tistory.com/15#:~:text=%2D%20%EC%B6%94%EC%83%81%ED%99%94%EB%9E%80%20%EC%9C%84%EC%97%90%EC%84%9C%20%EC%96%B8%EA%B8%89%ED%95%9C,%EA%B5%AC%ED%98%84%ED%95%98%EB%8A%94%20%EA%B2%83%EC%9D%84%20%EC%9D%98%EB%AF%B8%ED%95%9C%EB%8B%A4.
