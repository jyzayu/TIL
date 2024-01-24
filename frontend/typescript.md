## 타입 추론 
TypeScript는 JavaScript 언어를 알고 있으며 대부분의 경우 타입을 생성해줄 것입니다. 예를 들어 변수를 생성하면서 동시에 특정 값에 할당하는 경우, TypeScript는 그 값을 해당 변수의 타입으로 사용할 것입니다.
```
let helloWorld = "Hello World";
```
기존 JS 코드에 타입을 명시하지 않고 값을 통해 helloWorld가 string 임을 알게 됩니다.


## 타입 정의하기 
JavaScript는 다양한 디자인 패턴을 가능하게 하는 동적 언어입니다. 몇몇 디자인 패턴은 자동으로 타입을 제공하기 힘들 수 있는데 (동적 프로그래밍을 사용하고 있을 것이기 때문에) 이러한 경우에 TypeScript는 TypeScript에게 타입이 무엇이 되어야 하는지 명시 가능한 JavaScript 언어의 확장을 지원합니다.

다음은 name: string과 id: number을 포함하는 추론 타입을 가진 객체를 생성하는 예제입니다.
```
const user = {
  name: "Hayes",
  id: 0,
};
```
이 객체의 형태를 명시적으로 나타내기 위해서는 interface 로 선언합니다.
```
interface User {
  name: string;
  id: number;
}
```
이제 변수 선언 뒤에 : TypeName의 구문을 사용해 JavaScript 객체가 새로운 interface의 형태를 따르고 있음을 선언할 수 있습니다.
```
interface User {
  name: string;
  id: number;
}
// ---cut---
const user: User = {
  name: "Hayes",
  id: 0,
};
```
해당 인터페이스에 맞지 않는 객체를 생성하면 TypeScript는 경고를 줍니다.
```
// @errors: 2322
interface User {
  name: string;
  id: number;
}
const user: User = {
  username: "Hayes",
  id: 0,
};
```
JavaScript는 클래스와 객체 지향 프로그래밍을 지원하기 때문에, TypeScript 또한 동일합니다. - 인터페이스는 클래스로도 선언할 수 있습니다.
```
interface User {
  name: string;
  id: number;
}
class UserAccount {
  name: string;
  id: number;
  constructor(name: string, id: number) {
    this.name = name;
    this.id = id;
  }
}
const user: User = new UserAccount("Murphy", 1);
```

인터페이스는 함수에서 매개변수와 리턴 값을 명시하는데 사용되기도 합니다.
```
// @noErrors
interface User {
  name: string;
  id: number;
}
// ---cut---
function getAdminUser(): User {
  //...
}
function deleteUser(user: User) {
  // ...
}
```

JavaScript에서 사용할 수 있는 적은 종류의 원시 타입이 이미 있습니다.
: boolean, bigint, null, number, string, symbol, object와 undefined는 인터페이스에서 사용할 수 있습니다. 
TypeScript는 몇 가지를 추가해 목록을 확장합니다. 예를 들어, 
any (무엇이든 허용합니다), 
unknown (이 타입을 사용하는 사람이 타입이 무엇인지 선언했는가를 확인하십시오),
never (이 타입은 발생될 수 없습니다) 
void (undefined를 리턴하거나 리턴 값이 없는 함수).

타입을 구축하기 위한 두 가지 구문이 있다는 것을 꽤 빠르게 알 수 있을 것입니다.: Interfaces and Types - interface를 우선적으로 사용하고 특정 기능이 필요할 때 type을 사용해야 합니다.








타입스크립트는 Java 같은 정적 타이핑 언어에 익숙한 사람에게 인기있습니다.
에러 감지, 프로그램과 더 좋은 소통?, 더 좋은 코드 완성도 등의 이점이 있습니다.
타입스크립트로 바로 넘어가기 전에 자바스크립트가 OOP언어와 다른 점을 아는 것이 흔한 위험을 피하고, 더 좋은 자바스크립트 코드를 작성하는데 도움이 됩니다.
자바스크립트 런타임 동작을 이해하기 위해 타입을 제외한 자바스크립트 을 먼저 학습하길 권장합니다. 실제 동작은 js와 다르지 않습니다. 
특정 런타임 동작(converting stirng to number, displaying alert, writing file to disc 을 어떻게 성취할지는 타입스크립트에서도 자바스크립트와 동일하게 동작합니다.

## 클래스 다시 생각하기
### 자유로운 함수와 데이터
oop언어에서 데이터와 기능은 클래스에 담도록 강제합니다. 하지만 자바스크립트에서는 클래스에 속하지 않고 데이터와 함수를 전달합니다. 이러한 유연성 있는 모델이 자바스크립트에서 선호됩니다.
### 정적 클래스
정적메서드 싱글턴 같은 것이 타입스크립트에서 필요하지 않습니다. 

### 타입스크립트 OOP 
타입스크립트에서 인터페이스, 상속, 정적 메서드 같은 패턴을 지원합니다. 클래스를 사용하기 원한다면 타입스크립트의 지원을 사용하여 더 효과적으로 만들 수 있습니다.

## 타입 다시 생각하기

이름으로 구체화된 타입 시스템 (Nominal Reified Type Systems)
이러한 타입의 정의는 특정한 이름을 갖고 클래스의 어딘가 존재하며, 명시적인 상속관계나 공통적으로 구현된 인터페이스가 없는 이상 두 클래스가 유사한 형태를 가졌다 해도 서로 대체하여 사용할 수 없습니다.
이러한 양상은 reified, nominal 타입 시스템을 설명합니다. 코드에서 사용한 타입은 런타임 시점에 존재하며, 타입은 구조가 아닌 선언을 통해 연관 지어집니다.

집합으로서의 타입
타입스크립트에서 타입을 무언가를 공유하는 값의 집합으로 생각합니다. 값은 여러개의 집합에 포함될 수 있습니다.
string, number 둘 다 담을 수 있는 것을 Java 에서 표현하기 어렵지만 집합으로 생각해보면 string | number 로 표현 가능합니다.

삭제된 구조적 타입 (Erased Structural Types)
TypeScript에서, 객체는 정확히 단일 타입이 아닙니다. 예를 들어 인터페이스를 만족하는 객체를 생성할 때,
둘 사이의 선언적인 관계가 없더라도 해당 인터페이스가 예상되는 곳에 해당 객체를 사용할 수 있습니다.

```
interface Pointlike {
  x: number;
  y: number;
}
interface Named {
  name: string;
}

function printPoint(point: Pointlike) {
  console.log("x = " + point.x + ", y = " + point.y);
}

function printName(x: Named) {
  console.log("Hello, " + x.name);
}

const obj = {
  x: 0,
  y: 0,
  name: "Origin",
};

printPoint(obj);
printName(obj);
```
obj 는 Pointlike로 선언되지 않았지만 숫자인 x,y 프로퍼티를 갖기 때문에 Pointlike로 사용될 수 있습니다.
Java의 명명된 타입으로의 특징과 다르다고 할 수 있을 것 같습니다.

obj는 Pointlike 타입이라는 것을 명시하지 않습니다.
typescript type system은 구체화되지 않아 Pointlike 타입임을 런타임에서 알 수 없습니다.
Java 타입의 구체화된 특징과 다르다고 할 수 있습니다

집합으로서의 타입 개념으로 obj는 Pointlike, Named 값 집합의 멤버라고 할 수 있습니다. type annotation에 맞는 개수의 프로퍼티를 갖고 있으므로? 

## Empty type
```
class Empty {}

function fn(arg: Empty) {
  // 무엇인가를 하나요?
}

// 오류는 없지만, '빈' 타입은 아니지 않나요?
fn({ k: 10 });
```
Empty에 있는 모든 프로퍼티를  {k:10} 이 갖는다고 할 수 있으므로 유효한 호출입니다.
최종적으로 명목적인 객체지향프로그래밍 언어와 매우 비슷하게 사용됩니다. 파생 클래스와 파생 클래스의 기본 사이의 자연스러운 하위 타입 관계가 파괴되기 때문에, 하위 클래스는 삭제할 수 없습니다. 
구조적 타입 시스템은 호환 가능한 유형의 속성을 갖는 측면에서 하위 타입을 설명하므로 위의 관계를 암시적으로 구별합니다


function greeter(person: string) {
  return "Hello, " + person;
}
 
let user = [0, 1, 2];
 
document.body.textContent = greeter(user);

type annotation 
person : string 형식으로 type annotatinon을 추가할 수 있습니다.
앞의 코드는 string parameter 에 number[] 을 넣으려 해서 에러가 발생합니다. 컴파일을 완료하고 greeter.js 파일은 생성됩니다. 
그러나 타입스크립트가 코드가 정상적으로 동작하지 않을 수 있다고 경고합니다.
