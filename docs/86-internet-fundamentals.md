# 86. 인터넷이 동작하는 원리 — IP·DNS·포트·HTTPS·HTTP·쿠키·캐시·브라우저

> 웹사이트 기본 구조는 [5장](05-how-websites-work.md), 요청·응답과 서버 기초는 [코딩 9장](coding/09-web-development.md), 도메인·DNS 설정은 [34장](34-domain-names.md), 프록시·동적 딜레이·브라우저 자동화는 [85장](85-proxy-delay-browser-automation.md)에 있어요. 이 장은 그 바탕이 되는 **인터넷 지식**이에요.

프록시가 "무엇을 대신 전달"하는지, 서버가 손님의 "무엇을 볼 수 있는지", 브라우저 자동화가 "왜 필요한지"를 제대로 알려면 인터넷이 어떻게 움직이는지 알아야 해요. 이 장의 예제는 **모두 직접 실행해 결과를 확인했어요.**

---

## 0. 큰 그림 — 주소창에 입력하고 화면이 뜨기까지

```
① 이름 → 주소       granolalab.co.kr 가 어느 컴퓨터인지 묻기         (DNS, 2절)
② 연결              그 컴퓨터의 443번 문(포트)으로 연결               (TCP/QUIC, 3절)
③ 암호화 약속        "진짜 그 사이트 맞나?" 인증서 확인 + 암호 열쇠 정하기 (TLS, 4절)
④ 요청과 응답        "GET /menu" → "200 OK + 내용"                   (HTTP, 6절)
⑤ 기억              쿠키(누구인지), 캐시(이미 받은 것)                 (7·8절)
⑥ 화면 그리기        HTML·CSS·자바스크립트로 화면 완성                 (10절)
```
중간에 **프록시**가 끼면 ②~④를 대신 해 주거나 지켜봐요(5절).

---

## 1. IP 주소 — 인터넷의 집 주소

| 종류 | 예 | 뜻 |
|---|---|---|
| **IPv4** | `8.8.8.8` | 숫자 4개, 전체 약 43억 개뿐이라 부족해요 |
| **IPv6** | `2001:4860:4860::8888` | 훨씬 긴 주소, 사실상 무한. 구글 기준 **2026년 3월 처음으로 접속의 50%를 넘었어요** |
| **공인 주소** | 인터넷에서 직접 닿는 주소 | 서버·공유기의 바깥 주소 |
| **사설 주소** | `192.168.x.x`, `10.x.x.x`, `172.16~31.x.x` | 집·회사 **안에서만** 쓰는 주소 |
| **루프백** | `127.0.0.1` | "내 컴퓨터 자신" (개발할 때 많이 써요) |
| **CGNAT 공유 주소** | `100.64.x.x` | 통신사가 **여러 가입자에게 하나의 공인 주소를 나눠 쓰게** 할 때 쓰는 주소 |

```python
import ipaddress

for a in ["192.168.0.10", "10.1.2.3", "172.20.0.5", "127.0.0.1", "100.64.1.1",
          "8.8.8.8", "2001:4860:4860::8888", "2001:db8::1", "fe80::1"]:
    ip = ipaddress.ip_address(a)
    if ip.is_loopback:
        kind = "내 컴퓨터 자신"
    elif ip.version == 4 and ip in ipaddress.ip_network("100.64.0.0/10"):
        kind = "통신사 공유 주소(CGNAT)"
    elif ip.is_link_local:
        kind = "같은 망 안에서만 쓰는 주소(링크 로컬)"
    elif ip.version == 6 and ip in ipaddress.ip_network("2001:db8::/32"):
        kind = "문서·예시 전용 주소"
    elif ip.is_private:
        kind = "사설(집·회사 안)"
    else:
        kind = "공인(인터넷)"
    print(f"IPv{ip.version}  {a:<14} → {kind}")

net = ipaddress.ip_network("192.168.0.0/24")
print(f"\n192.168.0.0/24 안의 주소 수: {net.num_addresses}개 (공유기 하나 아래 집 안 네트워크)")
print(f"IPv4 전체 주소 수: {2**32:,}개 / IPv6 전체: 2^128개")
```

실행 결과 (직접 확인했어요):
```
IPv4  192.168.0.10   → 사설(집·회사 안)
IPv4  10.1.2.3       → 사설(집·회사 안)
IPv4  172.20.0.5     → 사설(집·회사 안)
IPv4  127.0.0.1      → 내 컴퓨터 자신
IPv4  100.64.1.1     → 통신사 공유 주소(CGNAT)
IPv4  8.8.8.8        → 공인(인터넷)
IPv6  2001:4860:4860::8888 → 공인(인터넷)
IPv6  2001:db8::1    → 문서·예시 전용 주소
IPv6  fe80::1        → 같은 망 안에서만 쓰는 주소(링크 로컬)

192.168.0.0/24 안의 주소 수: 256개 (공유기 하나 아래 집 안 네트워크)
IPv4 전체 주소 수: 4,294,967,296개 / IPv6 전체: 2^128개
```

### NAT — 한 주소를 여럿이 나눠 쓰기
- 집 공유기는 집 안 기기들(사설 주소)을 **하나의 공인 주소**로 바꿔 인터넷에 내보내요(NAT).
- 통신사는 그걸 한 번 더 해서, **수백 명이 같은 공인 IPv4 주소**를 쓰기도 해요(**CGNAT**). 모바일 망에서 흔해요.

### 사업자에게 중요한 이유
| 상황 | 의미 |
|---|---|
| **IP로 손님을 구별·차단** | CGNAT 뒤의 **수많은 정상 손님이 같이 막혀요.** IP는 "사람"이 아니에요 → 계정·세션·행동을 함께 보기 (41·85장) |
| **IP로 알 수 있는 것** | 대략적인 지역, 통신사, 데이터센터(클라우드) 주소인지 여부 정도 |
| **IP로 알 수 없는 것** | 정확한 사람·집 주소 |
| **IP도 개인정보가 될 수 있어요** | 다른 정보와 결합하면 사람을 알아볼 수 있어서, 로그 보관·처리방침에 반영 (10·68장) |

---

## 2. DNS — 이름을 주소로 바꾸는 전화번호부

- `granolalab.co.kr` → DNS에 물어봄 → `203.0.113.10` 같은 IP를 받음
- 결과는 정해진 시간(**TTL**) 동안 여러 곳에 **기억(캐시)**돼요. 그래서 DNS를 바꿔도 **바로 반영되지 않을 수 있어요**(34장).
- 이름을 못 찾으면 접속 자체가 안 돼요. 예를 들어 이 교재를 만든 작업 환경은 **허용된 주소만 이름 풀이가 되게** 막혀 있어서, 허용되지 않은 사이트는 "주소를 찾을 수 없음(ENOTFOUND)" 오류가 났어요.
- 레코드 종류(A·AAAA·CNAME·MX·TXT)와 메일 인증(SPF·DKIM·DMARC)은 30·34장.

---

## 3. TCP·UDP·포트 — 어느 문으로, 어떤 방식으로

| | TCP | UDP |
|---|---|---|
| 방식 | 먼저 **연결을 맺고**(악수), 빠진 것은 다시 보내 **순서·완전성 보장** | 연결 없이 **그냥 보냄**, 빠르지만 빠질 수 있음 |
| 쓰는 곳 | 웹(HTTP/1.1·2), 메일, DB | 게임 실시간 위치(40장), 음성·영상, DNS, **HTTP/3(QUIC)** |

**포트** = 한 컴퓨터 안의 "문 번호"예요.

| 포트 | 무엇 | 인터넷에 열어도 되나 |
|---|---|---|
| 443 | HTTPS | ✅ |
| 80 | HTTP (HTTPS로 보내는 용도) | ✅ |
| 22 | SSH (서버 관리) | ⚠️ 관리자 IP만 |
| 5432 / 3306 / 27017 | PostgreSQL / MySQL / MongoDB | ❌ 절대 (83장 6절) |

---

## 4. HTTPS(TLS) — 자물쇠가 실제로 하는 일

### 무엇을 보장하나
1. **암호화**: 중간에서 내용을 읽지 못하게
2. **진짜 확인**: 인증서로 "이 서버가 정말 granolalab.co.kr인가" 확인 (인증기관이 서명)
3. **변조 방지**: 중간에서 내용을 바꾸지 못하게

### 그래도 밖에서 보이는 것
| 보이는 것 | 숨겨지는 것 |
|---|---|
| 어느 **IP**로 가는지 | 주소의 **경로**(`/orders/42`)·검색어 |
| 어느 **사이트 이름**으로 가는지 (연결 초기에 보내는 이름, SNI) | 주고받는 **내용**·쿠키·비밀번호 |
| 언제, 얼마나 많이 주고받는지 | |

### 실제로 관찰한 "TLS 가로채기"
이 교재를 만든 작업 환경에서 `curl`로 github.com에 접속해 인증서를 봤더니:
```
> CONNECT github.com:443 HTTP/1.1
< HTTP/1.1 200 Connection Established
* SSL connection using TLSv1.3 / TLS_AES_128_GCM_SHA256 / X25519 / RSASSA-PSS
*  subject: CN=github.com
*  issuer: CN=CCR agent-proxy interception CA (production) 2026-08; O=Anthropic
```
- 인증서의 **발급자(issuer)**가 깃허브의 진짜 인증기관이 아니라 **작업 환경의 프록시**였어요.
- 프록시가 중간에서 HTTPS를 **풀어서 검사하고 다시 암호화**하는 거예요. 이 컴퓨터가 그 프록시의 인증서를 **믿도록 설정돼 있어서** 가능해요.
- 회사 보안 장비도 같은 방식으로 직원 PC의 HTTPS를 검사해요. 반대로 **내가 모르는 인증서를 믿도록 설치하라는 앱·안내는 위험**해요. 모든 HTTPS를 엿볼 수 있게 되기 때문이에요.

---

## 5. 프록시가 실제로 하는 일 — 직접 본 장면

### 포워드 프록시: CONNECT 터널
같은 작업 환경에서 **허용되지 않은 사이트**에 접속하면:
```
> CONNECT example.com:443 HTTP/1.1
< HTTP/1.1 403 Forbidden
* CONNECT tunnel failed, response 403
```
- 브라우저(또는 curl)는 프록시에게 "**example.com 443번까지 길(터널)을 뚫어 줘**"라고 요청해요(CONNECT).
- 프록시는 목록을 보고 **허용하면 200, 아니면 403**으로 답해요. 회사·학교의 사이트 차단이 이런 방식이에요.

### 리버스 프록시: 서버는 손님을 이렇게 봐요
내 서버(8091번) 앞에 아주 작은 리버스 프록시(8090번)를 두고, 손님(주소 127.0.0.5)이 직접 접속할 때와 프록시를 거칠 때 **서버가 본 것**을 비교했어요. 코드는 장 끝 부록에 있어요.

```
── ② 내 서버에 직접 접속했을 때 서버가 본 것 ──
{"접속한 주소": "127.0.0.5", "X-Forwarded-For": null, "User-Agent": "StudyClient/1.0", "Cookie": null}
── ③ 리버스 프록시를 거쳤을 때 서버가 본 것 ──
{"접속한 주소": "127.0.0.1", "X-Forwarded-For": "127.0.0.5", "User-Agent": "StudyClient/1.0", "Cookie": null}
```
- 프록시를 거치면 서버 입장에서 **접속한 주소는 프록시**가 되고, 진짜 손님 주소는 프록시가 붙여 준 **`X-Forwarded-For` 헤더**에만 남아요.
- 그래서 클라우드플레어 같은 프록시 뒤의 서버는 **이 헤더를 읽어야** 진짜 손님 IP를 알 수 있어요(요청 제한·로그, 41·68장).
- ⚠️ 하지만 **손님도 이 헤더를 마음대로 지어 보낼 수 있어요.** 그래서 **내가 믿는 프록시가 붙인 값만** 믿도록 설정해야 해요. 아무 `X-Forwarded-For`나 믿으면, 요청 제한을 우회하는 구멍이 돼요.
- 실제로 손님이 `X-Forwarded-For: 1.2.3.4`라고 **거짓으로 붙여** 보내 봤어요:
```
── ⑤ 손님이 X-Forwarded-For를 위조해서 보내면 ──
   직접 접속:   {"접속한 주소": "127.0.0.5", "X-Forwarded-For": "1.2.3.4", ...}  ← 서버가 이 값을 믿으면 속아요
   프록시 경유: {"접속한 주소": "127.0.0.1", "X-Forwarded-For": "127.0.0.5", ...}  ← 프록시가 위조값을 버리고 진짜 주소로 바꿈
```
  → **서버는 프록시를 통해서만 접속받고**(직접 접속 막기), **프록시가 붙인 값만** 믿는 게 정답이에요.

---

## 6. HTTP — 요청과 응답은 사실 "글자"

브라우저가 하는 일을 손으로 해 보면, HTTP는 정해진 형식의 **글자 주고받기**예요.

```python
import socket

def raw_get(host, port, path, extra=""):
    """브라우저가 하는 일을 손으로: TCP로 연결해서 HTTP 글자를 그대로 보내고 받기"""
    with socket.create_connection((host, port), timeout=5, source_address=("127.0.0.5", 0)) as s:   # 손님 주소 127.0.0.5
        req = f"GET {path} HTTP/1.1\r\nHost: shop.example\r\nUser-Agent: StudyClient/1.0\r\n{extra}Connection: close\r\n\r\n"
        s.sendall(req.encode())
        data = b""
        while chunk := s.recv(4096):
            data += chunk
    head, _, body = data.partition(b"\r\n\r\n")
    return head.decode(), body.decode()
```
- 요청: `GET /whoami HTTP/1.1` + `Host`·`User-Agent` 같은 **헤더 줄들** + 빈 줄
- 응답: `HTTP/1.1 200 OK` + 헤더 줄들 + 빈 줄 + **본문**
- 상태 코드(200·301·304·404·429·500)는 60장.

### 자주 보는 헤더
| 헤더 | 방향 | 뜻 |
|---|---|---|
| `Host` | 요청 | 어느 사이트 (한 서버가 여러 사이트를 맡을 때 구분) |
| `User-Agent` | 요청 | 어떤 프로그램인지 (스스로 적는 값, 85장) |
| `Cookie` / `Set-Cookie` | 요청 / 응답 | 기억표 주고받기 (7절) |
| `Cache-Control`, `ETag` | 응답 | 캐시 규칙 (8절) |
| `Retry-After` | 응답 | 언제 다시 오라 (85장) |
| `Authorization` | 요청 | 로그인 토큰·API 키 (주소에 넣지 말 것, 60장) |
| `X-Forwarded-For` | 요청 | 프록시가 붙인 원래 손님 주소 (5절) |

### HTTP 버전
| 버전 | 특징 | 2025년 클라우드플레어 요청 기준 (보도) |
|---|---|---|
| HTTP/1.1 | 연결 하나에 요청 하나씩 | 약 29% |
| HTTP/2 | 연결 하나로 여러 요청을 동시에 | 약 50% |
| HTTP/3 | **UDP 위의 QUIC**, 연결이 빠르고 와이파이↔데이터 전환에 강함 | 약 21% (웹사이트 수 기준으로는 약 36%가 지원) |

→ 1인 사업자가 직접 할 일은 거의 없어요. **CDN·호스팅이 알아서** 최신 버전을 켜 줘요(36·68장).

---

## 7. 쿠키와 세션 — 서버가 "아까 그 손님"을 기억하는 법

HTTP는 원래 **기억이 없어요.** 요청마다 처음 보는 사람이에요. 그래서:
```
① 서버 → 응답에  Set-Cookie: session=abc123; HttpOnly; Secure; SameSite=Lax
② 브라우저가 저장
③ 다음 요청부터  Cookie: session=abc123  를 자동으로 붙여 보냄
④ 서버가 "abc123 = 로그인한 김손님" 확인 (65장 세션)
```
| 쿠키 설정 | 뜻 |
|---|---|
| `HttpOnly` | 화면의 자바스크립트가 못 읽음 → 스크립트 공격으로 훔치기 어려움 |
| `Secure` | HTTPS에서만 보냄 |
| `SameSite=Lax` | 다른 사이트에서 몰래 보내는 요청에는 안 붙임 (위조 요청 방어) |
| 만료 | 언제까지 기억할지 |

- **제3자 쿠키** = 내가 방문한 사이트가 아닌 **다른 회사(광고 등)**의 쿠키예요. 사이트를 넘나드는 추적에 쓰여서 브라우저들이 점점 제한하고 있어요 → 광고 측정이 어려워지는 이유(61장 전환 API).
- 광고·분석용 쿠키는 **개인정보처리방침에 고지**하고, 유럽 손님에게는 **동의**가 필요해요(52장).

---

## 8. 캐시 — 이미 받은 건 다시 받지 않기

| 헤더 | 뜻 |
|---|---|
| `Cache-Control: max-age=60` | "60초 동안은 다시 묻지 말고 저장한 걸 써" |
| `ETag: "ee43…"` | 내용의 지문(버전 표시) |
| `If-None-Match: "ee43…"` | 손님: "나 이 버전 갖고 있는데 바뀌었어?" |
| `304 Not Modified` | 서버: "안 바뀌었어, 갖고 있는 거 써" (**본문 없이**) |

직접 확인한 결과 (부록의 서버와 6절의 `raw_get` 사용):
```
── ④ 캐시: 처음 요청 vs 같은 ETag로 다시 요청 ──
   처음: HTTP/1.0 200 OK | 본문 34 바이트 | ETag "ee4316d20820"
   다시: HTTP/1.0 304 Not Modified | 본문 0 바이트
```
- 큰 이미지·파일일수록 효과가 커요. **CDN**은 이 캐시를 손님 가까운 곳에 두는 서비스예요(5·68장).
- 85장의 예의 바른 수집기도 이 방법을 쓰면 **상대 서버 부담을 크게 줄여요.**
- ⚠️ 로그인한 사람만 보는 페이지(주문 내역 등)는 **공용 캐시에 저장되지 않게** `Cache-Control: private` 또는 `no-store`. 안 그러면 남의 화면이 보이는 사고가 날 수 있어요.

---

## 9. 같은 출처 정책과 CORS — 브라우저의 안전장치

- 브라우저는 **A 사이트의 자바스크립트가 B 사이트의 데이터를 마음대로 읽지 못하게** 막아요(같은 출처 정책).
- B가 "A는 읽어도 돼"라고 허락하는 헤더가 **CORS**예요(`Access-Control-Allow-Origin`).
- 자주 하는 오해:
  - CORS 오류가 나면 `*`(모두 허용)로 풀어 버리기 → **로그인이 필요한 API**에서는 위험해요. 허용할 주소만 정확히.
  - **CORS는 서버 보안이 아니에요.** 브라우저만 지키는 규칙이라, 서버끼리 호출하거나 curl·스크립트로 부르면 적용되지 않아요. 진짜 보호는 **서버의 로그인·권한 확인**(60·65장).

---

## 10. 브라우저가 화면을 만드는 법 — 왜 "브라우저 자동화"가 필요한가

```
HTML 받기 → 화면 구조(DOM) 만들기 → CSS로 꾸미기 → 자바스크립트 실행 → 데이터 받아서 화면 채우기
```
| 방식 | 뜻 | 단순 요청(curl·수집기)으로 받으면 |
|---|---|---|
| **서버 렌더링 (SSR)** | 서버가 완성된 HTML을 보내요 (한 바퀴 앱 방식) | 내용이 다 보여요 |
| **화면 렌더링 (SPA)** | 빈 HTML + 자바스크립트가 브라우저에서 API를 불러 화면을 채워요 | **거의 빈 페이지**만 보여요 |

- 그래서 SPA는 **진짜 브라우저를 돌려야** 내용이 보여요 → 85장의 브라우저 자동화가 필요한 이유예요.
- 같은 이유로 **검색 엔진·AI 크롤러·SNS 미리보기**도 SPA를 잘 못 읽을 수 있어요 → 공개 페이지(소개·상품·글)는 **서버 렌더링이나 미리 만든 HTML**이 유리해요(63장 검색 노출, 38장 공유 썸네일).

---

## 11. 서버는 손님에 대해 무엇을 알 수 있나

| 알 수 있는 것 | 출처 |
|---|---|
| IP 주소 (프록시 뒤면 프록시 주소) | 연결 (1·5절) |
| 대략적인 지역·통신사 | IP 데이터베이스 |
| 브라우저 종류·언어·화면 크기 | 헤더, 자바스크립트 |
| 쿠키 (이전 방문·로그인) | 7절 |
| 연결 방식의 특징 (TLS·HTTP 버전 등) | 연결 과정 |
| 마우스·입력 속도 같은 행동 | 자바스크립트 |

- 이런 정보를 합치면 "같은 기기인지"를 꽤 추정할 수 있어요(**브라우저 지문**). **봇 탐지·사기 방지**(41·85장)와 **추적 광고**가 이 원리를 써요.
- 반대로 말하면, **필요 이상 수집하면 개인정보 문제**예요. 무엇을 왜 수집하는지 처리방침에 적고, 꼭 필요한 것만(10장).

---

## 12. 지연 시간과 대역폭 — "빠르다"의 두 가지 뜻

| | 뜻 | 비유 |
|---|---|---|
| **지연 시간 (왕복 시간, RTT)** | 신호가 갔다 오는 데 걸리는 시간 | 도로의 **길이** |
| **대역폭** | 한 번에 보낼 수 있는 양 | 도로의 **폭** |

- 서울에서 미국 서버까지는 왕복에 보통 **수백 밀리초 가까이** 걸려요. 페이지 하나에 왕복이 여러 번 필요하면 그만큼 느려져요.
- 대책: 한국 손님이면 **가까운 지역 서버·CDN**(36장), **요청 수 줄이기**, 캐시(8절), HTTP/2·3.
- 실시간 게임·채팅은 **웹소켓**처럼 연결을 계속 열어 두는 방식을 써요(40장).

---

### 이 장 요약
1. **IP**는 사람이 아니라 주소예요. NAT·CGNAT로 **여럿이 한 주소를 나눠 써서** IP만으로 막으면 정상 손님도 막혀요. IPv6는 이제 접속의 절반이에요.
2. **HTTPS**는 내용을 숨기지만 **어느 사이트로 가는지는 보여요.** 회사·작업 환경 프록시는 **믿도록 설정된 인증서**로 가로채 검사하기도 해요. 리버스 프록시 뒤 서버는 **믿는 프록시가 붙인 `X-Forwarded-For`만** 믿어요.
3. HTTP는 **글자 주고받기**, 기억은 **쿠키**, 다시 안 받기는 **캐시(ETag·304)**, 브라우저 안전장치는 **같은 출처·CORS**(서버 보안 아님). SPA는 진짜 브라우저가 있어야 보여서 **브라우저 자동화**가 필요하고 **검색 노출**에도 영향을 줘요.

---

## 부록 — 5·8절 실습 코드 (내 컴퓨터에서만)

**내 서버 (8091번)** — 받은 요청에서 보이는 것을 돌려주고, 캐시와 쿠키를 다뤄요.
```python
"""내 서버: 받은 요청에서 무엇이 보이는지 그대로 돌려주고, 캐시(ETag)와 쿠키를 다뤄요."""
import hashlib, json
from http.server import BaseHTTPRequestHandler, HTTPServer

PAGE = "그래놀라 3종 세트 12,900원".encode()
ETAG = '"' + hashlib.sha256(PAGE).hexdigest()[:12] + '"'

class Backend(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/whoami":                      # 서버가 손님에 대해 아는 것
            seen = {"접속한 주소": self.client_address[0],
                    "X-Forwarded-For": self.headers.get("X-Forwarded-For"),
                    "User-Agent": self.headers.get("User-Agent"),
                    "Cookie": self.headers.get("Cookie")}
            body = json.dumps(seen, ensure_ascii=False).encode()
            self.send_response(200)
            self.send_header("Set-Cookie", "visit=1; HttpOnly; SameSite=Lax")
        elif self.headers.get("If-None-Match") == ETAG:  # 손님이 가진 것과 같으면
            self.send_response(304); self.send_header("ETag", ETAG); self.end_headers()
            return                                      # 본문 없이 "그대로 쓰세요"
        else:
            body = PAGE
            self.send_response(200)
            self.send_header("ETag", ETAG)
            self.send_header("Cache-Control", "max-age=60")
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, *a): pass

HTTPServer(("127.0.0.1", 8091), Backend).serve_forever()
```

**아주 작은 리버스 프록시 (8090번)**
```python
"""아주 작은 리버스 프록시: 손님 요청을 받아 내 서버(8091)로 전달하고, 원래 손님 주소를 헤더로 붙여요."""
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

class Proxy(BaseHTTPRequestHandler):
    def do_GET(self):
        drop = ("host", "connection", "x-forwarded-for")              # 손님이 보낸 X-Forwarded-For는 버림
        headers = {k: v for k, v in self.headers.items() if k.lower() not in drop}
        headers["X-Forwarded-For"] = self.client_address[0]        # 내가 직접 본 손님 주소만 붙임
        req = urllib.request.Request("http://127.0.0.1:8091" + self.path, headers=headers)
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))   # 바깥 프록시는 쓰지 않음
        try:
            r = opener.open(req, timeout=5)
            status, body, rh = r.status, r.read(), r.headers
        except urllib.error.HTTPError as e:
            status, body, rh = e.code, e.read(), e.headers
        self.send_response(status)
        for k, v in rh.items():
            if k.lower() not in ("connection", "transfer-encoding", "server", "date"):
                self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, *a): pass

HTTPServer(("127.0.0.2", 8090), Proxy).serve_forever()
```
> ⚠️ 이 프록시는 손님이 보낸 `X-Forwarded-For`를 **버리고 자기가 직접 본 주소만** 붙여요. 프록시가 여러 단계인 경우는 다루지 않는 단순한 예예요. 실제로는 Nginx·Caddy·클라우드플레어 같은 검증된 리버스 프록시를 쓰세요.

**확인용 손님** — 6절의 `raw_get` 함수에 아래를 이어 붙여 실행해요.
```python
print(raw_get("127.0.0.1", 8091, "/whoami")[1])          # 직접
head, body = raw_get("127.0.0.2", 8090, "/whoami")       # 프록시를 거쳐
print(body)
head1, _ = raw_get("127.0.0.1", 8091, "/menu")
etag = [l.split(": ", 1)[1] for l in head1.splitlines() if l.lower().startswith("etag")][0]
head2, body2 = raw_get("127.0.0.1", 8091, "/menu", f"If-None-Match: {etag}\r\n")
print(head2.splitlines()[0], len(body2))                  # → 304, 0
```
실행: 터미널 3개에서 서버 → 프록시 → 손님 순서로.

---

> 📚 이 장의 출처와 확인하지 못한 부분은 [참고 자료 모음](sources.md#86장-인터넷이-동작하는-원리)에 있어요.
