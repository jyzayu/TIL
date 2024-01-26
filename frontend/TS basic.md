JavaScript 런타임은 코드가 실행될 때 자신이 무엇을 해야 할지 결정하기 위하여 값의 타입, 즉 해당 값이 어떤 동작과 능력을 가지고 있는지를 확인합니다. 이것이 바로 TypeError가 암시하는 바입니다. 위 예시에서는 문자열인 "Hello World"가 함수로서 호출될 수 없다고 말하고 있는 것이죠.

일부 값들, 이를테면 string과 number과 같은 원시 타입의 값의 경우 typeof 연산자를 사용하면 각 값들의 타입을 실행 시점에 알 수 있습니다. 하지만 그 밖의 값들, 이를테면 함수값의 경우, 앞서 언급된 방식과 같이 해당 값의 타입을 실행 시점의 메커니즘은 존재하지 않습니다. 예를 들어, 아래와 같은 함수를 살펴보겠습니다.
```
function fn(x) {
  return x.flip();
}
```
위 코드를 보면, 인자로 전달된 객체가 호출 가능한 프로퍼티인 flip을 가져야만 위 함수가 잘 작동할 것이라는 것을 우리는 코드를 읽음으로써 알 수 있습니다. 하지만 JavaScript는 우리가 알고 있는 이러한 정보를 코드가 실행되는 동안 알지 못합니다. 순수 JavaScript에서 fn가 특정 값과 어떤 동작을 수행하는지 알 수 있는 유일한 방법은 호출하고 무슨 일이 벌어지는지 보는 것입니다. 이와 같은 동작은 코드 실행 전에 예측을 어렵게 만듭니다. 다시 말해 코드가 어떤 동작 결과를 보일지 코드를 작성하는 동안에는 알기 어렵습니다.

이런 측면에서 볼 때, 타입이란 어떤 값이 fn으로 전달될 수 있고, 어떤 값은 실행에 실패할 것임을 설명하는 개념입니다. JavaScript는 오직 동적 타입만을 제공하며, 코드를 실행해야만 어떤 일이 벌어지는지 비로소 확인할 수 있습니다.

이에 대한 대안은 정적 타입 시스템을 사용하여 코드가 실행되기 전에 코드에 대하여 예측하는 것입니다.


정적 타입 검사
코드 실행 전에 미리 타입을 검사하여 버그를 찾아낼 수 있으면 좋을 것입니다.
테스트를 하지 못할 수도 있고, 운 좋게 버그를 찾아도 리팩토링을 하면서 코드를 파헤치게 될 수 있습니다.

리가 작성한 프로그램에서 사용된 값들의 형태와 동작을 설명합니다. TypeScript와 같은 타입 검사기는 이 정보를 활용하여 프로그램이 제대로 작동하지 않을 때 우리에게 알려줍니다.
```
const message = "hello!";
 
message();
This expression is not callable.
  Type 'String' has no call signatures.
```

### 예외가 아닌 실행 실패
지금까지 런타임 오류에 대하여 다루었습니다. 이는 JavaScript 런타임이 무언가 이상하다고 우리에게 직접 말해주는 경우에 해당합니다. 이러한 오류는 예기치 못한 문제가 발생했을 때 JavaScript가 어떻게 대응해야 하는지 ECMAScript 명세에서 명시적인 절차를 제공하기 때문에 발생하는 것입니다.

예를 들어, 명세에 따르면 호출 가능하지 않은 것에 대하여 호출을 시도할 경우 오류가 발생합니다. 이는 “당연한 동작”처럼 들릴 수 있겠으나, 누군가는 객체에 존재하지 않는 프로퍼티에 접근을 시도했을 때에도 역시 오류를 던져야 한다고 생각할 수 있습니다. 하지만 그 대신 JavaScript는 전혀 다르게 반응하며 undefined를 반환합니다.
```
const user = {
  name: "Daniel",
  age: 26,
};
user.location; // undefined 를 반환
```

궁극적으로, 정적 타입 시스템은 어떤 코드가 오류를 발생시키지 않는 “유효한” JavaScript 코드일지라도, 정적 타입 시스템 내에서 오류로 간주되는 경우라면 이를 알려주어야 합니다. TypeScript에서는, 아래의 코드는 location이 정의되지 않았다는 오류를 발생시킵니다.

```
const user = {
  name: "Daniel",
  age: 26,
};
 
user.location;
Property 'location' does not exist on type '{ name: string; age: number; }'.
Try

```
비록 때로는 이로 인하여 표현의 유연성을 희생해야 하겠지만, 이렇게 함으로서 명시적인 버그는 아니지만 버그로 타당히 간주되는 경우를 잡아내는 데에 그 목적이 있습니다. 그리고 TypeScript는 이러한 겉으로 드러나지 않는 버그를 꽤 많이 잡아냅니다.

예를 들어, 오타,

const announcement = "Hello World!";
 
// 바로 보자마자 오타인지 아실 수 있나요?
announcement.toLocaleLowercase();
announcement.toLocalLowerCase();
 
// 아마 아래와 같이 적으려 했던 것이겠죠...
announcement.toLocaleLowerCase();
Try
호출되지 않은 함수,

function flipCoin() {
  // 본래 의도는 Math.random()
  return Math.random < 0.5;
Operator '<' cannot be applied to types '() => number' and 'number'.
}
Try
또는 기본적인 논리 오류 등이 있습니다.
