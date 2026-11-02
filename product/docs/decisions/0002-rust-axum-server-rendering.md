# 0002. Rust(Axum) + 서버 렌더링 + Supabase + 도커 호스팅으로 만든다

- 상태: 채택 (2026-11-02)

## 배경
처음 제안은 Next.js + Supabase + Vercel이었다. 사용자가 개발 언어로 Rust를 원했다.

## 결정
- 서버: Rust + Axum(Tokio)
- 화면: 서버에서 HTML을 만들어 보낸다(Askama 템플릿). 처음엔 자바스크립트 없이 HTML 폼으로 동작
- 로그인·DB: Supabase(Auth + Postgres + RLS)는 그대로 — 2주차
- 배포: Vercel 대신 도커 컨테이너를 실행하는 호스팅(Fly.io·Render 등) — 2주차에 결정
- AI: Claude API를 서버에서 HTTP로 호출 — 3주차
- 1주차부터 테스트·CI(fmt·clippy·test)·상태 확인 주소·안전한 종료를 넣는다(81장)

## 결과
- 좋아지는 점: 빠르고 적은 자원으로 실행(호스팅 비용↓), 컴파일러가 많은 실수를 미리 잡음, 하나의 실행 파일로 배포가 단순
- 나빠지는 점: Rust는 배우기 어렵고 컴파일이 느림. AI 도구가 만든 Rust 코드도 컴파일 오류가 잦을 수 있다 → 작게 나눠 만들고 매번 cargo test
- Next.js용으로 쓰여 있던 설계(폴더 구조 등)는 Rust 구조로 바꿨다(03-architecture)
