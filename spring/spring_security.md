### [ Spring Security ]
∘  Spring 기반의 애플리케이션의 보안(인증과 권한, 인가 등)을 담당하는 스프링 하위 프레임워크

∘  '인증'과 '권한'에 대한 부분을 Filter 흐름에 따라 처리

∘  Spring Security는 보안과 관련해서 체계적으로 많은 옵션을 제공해주기 때문에

개발자 입장에서는 일일이 보안관련 로직을 작성하지 않아도 된다는 장점이 있다.

### Spring Security사용하시면서 어려운 점이 없었나요?
Spring MVC와 Spring Security의 구조를 이해하지 못해서 어느 시점에 Security Filter와 DispatcherServlet이 동작하며 어떻게 Security Filter에 JWT를 처리하는지
### Filter와 Security Filter의 차이는 무엇인가요?
Filter와 Security Filter 모두 Servlet에 요청이 맵핑되기 전에 실행되는 필터(Filter)입니다.

둘다 동일한 Filter이지만 단순한 Filter는 서블릿 컨테이너에 직접 등록해서 사용하는 필터이고

Security Filter는 DelegatingFilterProxy가 서블릿 컨테이너에 Filter로 등록되어서 Filter 작업을 Security FilterChain으로 위임해서 실행되는 필터를 의미합니다.

### 인증 프로세스 간단히
1. Client가 요청을 보내면, Servlet Filter에 의해서 Security Filter로 작업이 위임되고 여러 Security Filter 중에서 JwtAuthenticationFilter에서 인증을 처리합니다.
2. JwtAuthenticationFilter는 Servlet 요청 객체에서 토큰을 가져와서 JwtTokenProvider가 해당 토큰을 검증해 토큰이 유효한지 검사합니다.
3. 토큰이 유효하다면 Authentication 객체를 만들고 AuthenticationManager를 사용할 필요 없이 직접 SecurityContextHolder에 접근해서 Authentication 객체를 저장합니다.
    
### spring security 인증 프로세스
1. 어플리케이션으로 http요청이 들어오면 AuthenticationFilter가 이 요청을 기반으로 인증되지 않은 UsernamePasswordAuthenticationToken(Authentication객체)을 만든다(isAuthenticated = false).
2. AuthenticationFilter에서 AuthenticationManager를 호출하여 Authentication객체에 대한 인증을 요청한다.
3. AuthenticationManager는 전달받은 Authentication객체를 인증할 수 있는 Provider를 찾아 인증을 요청한다.
4. 선택된 AuthenticationProvider는 Authentication객체에서 principal(username)을 추출하고 UserDetailsService에게 해당하는 사용자를 찾아달라고 요청한다.
5. UserDetailsService는 전달받은 principal(username)과 일치하는 사용자를 DB에서 찾고, UserDetails객체로 포장하여 AuthenticationProvider에게 돌려준다.
6. AuthenticationProvider는 UserDetails를 받아 인증을 수행하고, 인증에 성공하면 새로운 Authentication객체를 생성하여 AuthenticationManager에게 돌려준다(isAuthenticated = true).
7. AuthenticationManager는 인증된 Authentication객체를 가공하여 AuthenticationFilter로 돌려준다.
8. AuthenticationFilter는 인증된 Authentication객체를 SecurityContext로 감싸고 SecurityContextHolder에 저장한다.

위의 과정을 통해 인증에 성공한 Authentication객체는 SecurityContextHolder에 보관되고, 이후 필터에서 인가 프로세스를 처리할 때 사용된다.
