https://www.nextree.co.kr/p6960/
https://velog.io/@moosou30/SOLID-SRP%EB%8B%A8%EC%9D%BC-%EC%B1%85%EC%9E%84-%EC%9B%90%EC%B9%99
### SRP단일 책임 원칙
- 1개의 클래스에 1개의 기능만 가지며 1개의 책임을 수행하는데 집중해야 한다는 원칙입니다. 
- 1 기능의 변경에서 다른 기능으로 연쇄반응을 막는 장점이 있습니다.
- 각 개체 간의 응집력이 있다면 병합이 순 작용의 수단이 되고 결합력이 있다면 분리가 순 작용의 수단
### OCP개방 폐쇄 원칙
- 구성요소(컴포넌트,클래스,모듈,함수)는 확장에는 열려있고, 변경에는 닫혀있어야 한다는 원칙입니다.
- 요구사항 변경이 발생해도, 기존 구성요소의 수정 없이 쉽게 확장해 재사용할 수 있어야한다는 뜻입니다.
- 재사용성을 높이는 법이며 추상화와 다형성으로 구현 가능합니다.
![image](https://github.com/jyzayu/TIL/assets/55649979/c6188aba-d17e-4e2e-8867-22a0f8ff2881)
- 악기가 추가 되면서 변경이 발생하는 부분을 추상화하여 분리했음을 확인할 수 있습니다.
- 코드의 수정을 최소화하여 결합도는 줄이고 응집도는 높이는 효과를 볼 수 있습니다.

### LSP리스코프 치환 법칙
- 서브타입은 언제나 기반 타입으로 교체할 수 있어야 한다는 원칙입니다.
- 서브 타입은 기반 타입이 약속한 규약(public 인터페이스, 메서드가 던지는 예외)를 지켜야 합니다.
- 상속은 구현상속(extends)이든 인터페이스 상속(implements)이든 다형성을 통한 확장성 획득을 목표로합니다.
- 다형성으로 인한 확장효과를 얻기 위해 서브클래스가 규약을 어겨서는 안 됩니다.
- 일반적으로 선언은 기반 클래스 생성은 구체 클래스로 대입하는 방법을 사용합니다.
- 결국 이 구조는 다형성을 통한 확장 원리인 OCP를 구성하는 구조가 됩니다.
- LSP는 규악을 준수하는 상속구조를 제공합니다.

### ISP 인터페이스 분리 원칙
- 한 클래스는 자신이 사용하지 않는 인터페이스는 구현하지 말아야 한다는 원칙입니다.
- 어떤 클래스가 다른 클래스에 종속될 때 가능한 최소한의 인터페이스만을 사용해야 합니다.
- 하나의 일반적인 인터페이스보다는 여러개의 ㅇ구체적인 인터페이스가 낫다라고 정의합니다.
- ISP는 인터페이스가 여러 책임 혹은 역할을 갖는 것을 인정합니다.
- SRP가 클래스 분리를 통해 변화 적응성을 획득하는 반면
- ISP는 인터페이스 분리를 통해 같은 목표에 도달합니다.

### DIP 의존 역전 원칙
- 하위 레벨 모듈의 변경이 상위 레벨 모듈의 변경을 요구하는 위계관계를 끊는 의미의 역전입니다.
- 추상을 매개로 메시지를 주고 받음으로써 관계를 최대한 느슨하게 만드는 원칙입니다.
- DIP 키워드는 "IOC", "훅 메소드", "확장성"입니다. 이 세가지 요소가 조합되어 복잡한
- 컴포넌트들의 관계를 단순화하고 컴포넌트 간 커뮤니케이션을 효율적이게 합니다.
- 
- 
