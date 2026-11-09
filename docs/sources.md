# 참고 자료와 확인이 필요한 부분

이 자료를 만들 때 조사한 **출처**와, 조사 중 **직접 확인하지 못한 부분**을 장별로 모았어요.

- 조사 시점: **2026년 10월**
- 법 원문 사이트(국가법령정보센터, law.go.kr)는 조사 환경에서 접속이 막혀 있어서 **한 번도 열어 보지 못했어요.** 그래서 법 관련 내용은 정부 보도자료, 기사, 법률사무소·업체 해설을 바탕으로 썼어요.
- 아래 출처 중 상당수는 공식 문서가 아니라 **기사·블로그·업체 안내**예요. 실제로 사업을 시작하거나 설정을 바꿀 때는 꼭 **공식 사이트**에서 다시 확인하세요.

### 공식 확인처 모음
| 무엇 | 어디서 |
|---|---|
| 법 원문 | 국가법령정보센터 (law.go.kr) |
| 사업자등록·세금 | 국세청 홈택스 |
| 통신판매업 신고·인허가 검색 | 정부24, 관할 시·군·구청 |
| 개인정보 | 개인정보보호위원회, 개인정보 포털 (privacy.go.kr) |
| 전자상거래·광고 표시 | 공정거래위원회 |
| 게임 등급분류 | 게임물관리위원회 |
| AI 기본법 | 과학기술정보통신부 |
| 메일 설정 값 | 내가 쓰는 메일 서비스(구글 워크스페이스 등)의 공식 도움말 |

---

## 1~15장 (기본 운영)

### 7장 업데이트와 배포
- [블루-그린 vs 카나리 배포 (Unleash)](https://www.getunleash.io/blog/blue-green-deployment-vs-canary-release)
- [배포 전략 비교 (Educative)](https://educative.io/blog/blue-green-deployment-vs-canary-release)
- [배포 전략 설명 (Gravitee)](https://www.gravitee.io/deployment-strategies.html)

### 8장 백업과 복구
- [3-2-1 백업 규칙 (Seagate)](https://www.seagate.com/blog/3-2-1-backup-best-practices)
- [3-2-1 백업 규칙 (Rubrik)](https://www.rubrik.com/insights/understanding-the-3-2-1-backup-rule)
- [DB 백업 모범 사례 (DEV)](https://dev.to/dean_dautovich/13-postgresql-backup-best-practices-for-developers-and-dbas-3oi5)

### 2·3·11장 수익과 지표 (MRR, LTV, CAC 등)
- [SaaS 지표 설명 (Orb)](https://www.withorb.com/blog/saas-metrics)
- [SaaS 지표 설명 (Monetizely)](https://www.getmonetizely.com/articles/saas-pricing-metrics-101-arr-mrr-ltv-churn-amp-other-key-kpis-explained)

### 10장 보안과 법
- [통신판매업 신고 면제 기준 합리화 (정책브리핑)](https://www.korea.kr/briefing/pressReleaseView.do?newsId=156061292)
- [공정거래위원회 입법·행정예고](https://www.ftc.go.kr/www/selectBbsNttView.do?pageUnit=10&pageIndex=24&searchCnd=all&key=193&bordCd=105&nttSn=10853)
- [통신판매업 신고 면제 기준 정리 (thecheck)](https://thecheck.co.kr/mail-order-business-report-exemption/)
- [웹사이트 법적 준수사항 (Hostragons)](https://www.hostragons.com/ko/블로그/웹사이트-개설-시-필수-법적-준수사항과-개인정보보호법-가이드/)

**⚠️ 확인하지 못한 것**
- **통신판매업 신고 면제 기준**: "직전 연도 거래 50회 미만 또는 간이과세자"라는 자료와, 간이과세자 면제가 없어졌다는 예전 보도자료가 서로 달랐어요. 고시 원문은 확인하지 못했어요.
- **개인정보 유출 신고 기한(72시간)**, 거래 기록 보관 기간(5년 등), 간이과세 기준 금액은 원래 알던 내용을 바탕으로 썼고, 이번 조사에서 원문으로 확인하지는 못했어요.

---

## 16~21장 (여러 가지 사이트 사업)

### 16장 커뮤니티
- [불법촬영물 조치 의무 대상 (뉴스토마토)](https://newstomato.com/ReadNews.aspx?no=985589)
- [n번방 방지법 설명 (경향신문)](https://www.khan.co.kr/article/202112131643001)
- [임시조치 30일 (로톡)](https://www.lawtalk.co.kr/posts/177280)
- [게시글 관리와 임시조치 (Nepla)](https://www.nepla.ai/wiki/it-%EC%A0%95%EB%B3%B4-%EB%B0%A9%EC%86%A1%ED%86%B5%EC%8B%A0/%EC%9D%B8%ED%84%B0%EB%84%B7-%EB%B0%A9%EC%86%A1-%ED%86%B5%EC%8B%A0/%EC%A0%95%EB%B3%B4%ED%86%B5%EC%8B%A0%EB%A7%9D%EB%B2%95-%EC%83%81-%ED%94%8C%EB%9E%AB%ED%8F%BC-%EC%9A%B4%EC%98%81%EC%9E%90%EC%9D%98-%EA%B2%8C%EC%8B%9C%EA%B8%80-%EA%B4%80%EB%A6%AC-%EB%B0%A9%EB%B2%95-g6w93mqxnojp)

### 17장 정보 사이트
- [구글 스팸 정책 공식 안내 (2024년 3월)](https://developers.google.com/search/blog/2024/03/core-update-spam-policies)
- [AI 요약과 클릭률 하락 (Press Gazette)](https://pressgazette.co.uk/media-audience-and-business-data/google-ai-overviews-publishers-report-clickthroughs-authoritas-report/)
- [Pew 조사 정리 (VideoWeek)](https://videoweek.com/2025/07/23/pew-research-demonstrates-sharp-impact-of-ai-overviews-on-publisher-search-traffic/)

### 18장 트래픽 수익
- [AdSense 정산 방식 변경 (9to5Google)](https://9to5google.com/2023/11/02/google-adsense-payments-2024/)
- [AdSense 노출 기준 정산 (MediaPost)](https://www.mediapost.com/publications/article/390753/google-adsense-moves-payment-to-per-impression.html)

### 19장 로또·예측 사이트
- [로또 예측 사이트 피해·금감원 경고 (YTN)](https://www.ytn.co.kr/_ln/0103_202511121830302794)
- [로또 예측 사이트 92개 운영, 607억 원 편취 (경기일보)](https://kyeonggi.com/article/20220815580213)
- ["로또 공 무게" 사기 실형 (헤럴드경제)](https://www.heraldk.com/article/2026022302210023495)
- ["당첨 번호 알려준다" 400억 편취 징역 12년 (한국경제)](https://www.hankyung.com/amp/2025103038677)

### 20장 게임 사이트
- [확률형 아이템 확률 공개 의무화 (아주경제)](https://www.ajunews.com/view/20240102104711033)
- [영세 게임사 예외 (세계일보)](https://www.segye.com/newsView/20231113512094)
- [웹보드게임 규제 (문화체육관광부)](https://www.mcst.go.kr/site/s_notice/press/pressView.jsp?pSeq=9297)

**⚠️ 확인하지 못한 것**
- **내 웹사이트에서 직접 게임을 서비스할 때 등급분류를 받아야 하는지**(비영리·소규모 예외 기준)는 확실한 자료를 찾지 못했어요.
- 불법촬영물 조치 의무 사업자 수는 자료마다 달랐어요(83개 / 90여 개).
- AdSense 게시자 몫(약 68%)은 구글 발표를 전한 기사 기준이에요.

---

## 22~29장 (더 넓은 분류)

### 23장 오픈마켓 셀러·구매대행
- [구매대행 세금 (흠택스)](https://www.heumtax.com/contents/posts/buying-agency-tax)
- [KC 미인증 직구 금지 철회 (KED Global)](https://amp.kedglobal.com/newsAmp/ked202405190002)

### 24장 크리에이터
- [유튜브 수익 조건·2027년 변경 보도 (Tubefilter)](https://www.tubefilter.com/?p=193559)
- [쇼츠 수익 배분 (Stack Influence)](https://stackinfluence.com/blog/youtube-shorts-monetization)

### 25장 모바일 앱
- [앱 마켓 수수료 비교 (SplitMetrics)](https://splitmetrics.com/blog/google-play-apple-app-store-fees/)
- [애플 스몰 비즈니스 프로그램 (Appbot)](https://appbot.co/blog/app-developers-apple-google-small-business-programs/)

### 27장 매칭·중개 플랫폼
- [인력 중개 사업 유의사항 (Nepla)](https://www.nepla.ai/wiki/기업과-소비자/공정거래/o2o-서비스-플랫폼을-통한-인력-중개-사업-추진-시-유의사항-rv5n72qv38zm)
- [무등록 직업소개 사례 (로윈)](https://www.lawwin.co.kr/cases/7262)

### 28장 AI 서비스
- [AI 기본법 해설 (신앤김)](https://www.shinkim.com/kor/media/newsletter/3114)
- [AI 기본법 대응 (SK AX)](https://www.skax.co.kr/insight/trend/3666)
- [외부 AI를 쓰는 회사도 적용 대상 (헬프미)](https://www.help-me.kr/blog/article/korea-ai-act-2026-compliance-guide/)

### 29장 규제 업종
- [콘택트렌즈 판매 규정 (데일리안)](https://www.dailian.co.kr/news/view/119179)
- [쿠팡 판매 안전 가이드](https://www.coupang.com/np/safety/guide)

**⚠️ 확인하지 못한 것**
- **담배·주류의 온라인 판매 제한**, **투자 리딩방 규제 변경(2024년)** 은 근거 조항까지 찾지 못해서 원래 알던 내용을 "~로 알려져 있어요"라고 적었어요.
- **유튜브 수익 조건**과 **앱 마켓 수수료**는 공식 페이지가 아니라 해설 기사에서 확인한 숫자예요. 유튜브는 2027년 2월부터 신규 신청 기준이 올라간다는 보도도 있었어요.
- **해외 직구 면세 한도**와 KC 인증 관련 기준은 개편 논의가 있어 확정하지 못했어요.

---

## 30~31장 (문의·광고 받기)

### 30장 문의 창구와 이메일
- [Gmail·Yahoo 대량 발송 규칙 (Close)](https://help.close.com/technical-support/email-deliverability/requirements-for-bulk-email-senders)
- [Gmail·Yahoo 대량 발송 규칙 (Warmy)](https://www.warmy.io/guides/google-yahoo-sender-requirements/)
- [Gmail·Yahoo 대량 발송 규칙 (Bird)](https://bird.com/en-de/docs/knowledge-base/deliverability/gmail-yahoo-requirements)
- [구글 워크스페이스 MX 설정 (WebDogs)](https://guides.webdogs.com/workspace-mx-records/)
- [구글 워크스페이스 SPF 기록 (intoDNS)](https://intodns.ai/citations/google-workspace-spf-record)
- [광고 문자 규칙 (솔라피)](https://solapi.com/guides/sms-ad-guide)
- [마케팅 수신동의 (비즈고)](https://blog.bizgo.io/?p=3380)
- [정보통신망법 제50조 (korea.legal)](https://korea.legal/wiki/%ec%a0%95%eb%b3%b4%ed%86%b5%ec%8b%a0%eb%a7%9d-%ec%9d%b4%ec%9a%a9%ec%b4%89%ec%a7%84-%eb%b0%8f-%ec%a0%95%eb%b3%b4%eb%b3%b4%ed%98%b8-%eb%93%b1%ec%97%90-%ea%b4%80%ed%95%9c-%eb%b2%95-21/)
- [청소년보호책임자 기준 (뉴시스)](https://www.newsis.com/view/NISX20241107_0002950324)

**⚠️ 확인하지 못한 것**
- **광고 메일 법(정보통신망법 제50조)** 의 세부 규칙은 해설 자료로만 확인했어요. **야간 시간대(오후 9시~오전 8시)** 는 원래 알던 내용이라 "흔히 그렇게 안내된다"고 적었어요.
- **청소년보호책임자** 지정 기준 중 하루 평균 이용자 10만 명은 확인했지만, **매출 기준**은 찾지 못했어요.
- **Gmail 대량 발송 규칙(하루 약 5,000통, 스팸 신고율 0.3%)** 과 **구글 메일 MX 값**은 공식 페이지가 아니라 메일 업체들의 안내에서 확인했어요.

---

## 32~33장 (마케팅 실전과 사례)

### 32장 채널별 실전
- [인스타그램 2025 알고리즘 신호 (Social Media Today)](https://www.socialmediatoday.com/news/instagram-shares-algorithm-insights-2025/738034/)
- [인스타그램 도달 핵심 요인 (Social Samosa)](https://www.socialsamosa.com/news-2/instagram-reveals-key-factors-for-boosting-reach-8646916)
- [인스타그램 해시태그 5개 제한 (BetaNews)](https://betanews.com/2025/12/19/instagram-puts-a-limit-on-hashtag-usage/)
- [인스타그램 해시태그 제한 (Siècle Digital)](https://siecledigital.fr/2025/12/22/instagram-enterre-les-hashtags-a-rallonge/)
- [메타 광고 예산·학습 기준 (원포인트)](https://1point.kr/blog/insights/instagram-ad-budget-floor/)
- [메타 광고 전환 50건 (AMPM)](https://inside.ampm.co.kr/insight/60829)
- [메타 광고 첫 예산 (AMPM)](https://inside.ampm.co.kr/insight/12023)
- [네이버 플레이스·체험단 실전 (아이보스)](https://www.i-boss.co.kr/ab-6141-62818)
- [가게 마케팅 실전 전략 (토스플레이스)](https://tossplace.com/story/marketing_5tips)
- [당근 광고 안내 (아이보스, 대행사 글)](https://www.i-boss.co.kr/ab-2987-547041)
- [스레드 국내 이용자 증가 (MTN)](https://news.mtn.co.kr/news-detail/2026091016192841238)
- [스레드 국내 이용 분석 (나스미디어)](https://library.nasmedia.co.kr/file/b6ee19fd7275d4ccb7809cfabc2db0fc)

### 33장 실제 사례
- 배달의민족: [뉴시스](https://www.newsis.com/view/NISX20210218_0001344250), [브런치 정리](https://brunch.co.kr/@you486me/112)
- 당근: [바이라인네트워크](https://byline.network/2024/04/22-327/), [비즈한국](https://www.bizhankook.com/bk/article/20970)
- 무신사: [헤럴드경제](https://biz.heraldcorp.com/article/10409496), [피플와이 뉴스레터](https://maily.so/peoplewhy/posts/d5ryw2k1z1w)
- 오늘의집: [한국경제](https://www.hankyung.com/amp/2022081039351), [이코노미스트](https://economist.co.kr/article/view/ecn202304230001)
- 글로시에: [Entrepreneur](https://www.entrepreneur.com/article/249328), [Harvard Digital Initiative](https://d3.harvard.edu/platform-digit/submission/glossier-a-direct-to-consumer-beauty-disruptor/)
- 모닝 브루: [SparkLoop](https://sparkloop.app/blog/the-secrets-behind-morning-brews-growth-to-2-million-newsletter-subscribers-6), [Referral Rock](https://referralrock.com/blog/morning-brew-referral-program/)
- 드롭박스: [Prefinery](https://prefinery.com/blog/dropbox-referral-program-3900percent-growth-study/), [Referral Rock](https://referralrock.com/blog/dropbox-referral-program/)
- 워들: [위키백과](https://en.wikipedia.org/wiki/Wordle), [TechCrunch](https://techcrunch.com/2022/05/04/wordle-new-york-times-user-growth)
- 어몽어스: [PC Gamer](https://pcgamer.com/how-among-us-became-so-popular), [CNBC](https://www.cnbc.com/2020/10/14/how-among-us-became-a-mega-hit-thanks-to-amazon-twitch.html)
- 듀오링고: [Adweek](https://www.adweek.com/brand-marketing/duolingo-duo-owl-marketing-strategy/), [Digiday](https://digiday.com/marketing/how-duolingo-is-using-its-unhinged-content-with-duo-the-owl-to-make-people-laugh-on-tiktok/)
- 피터 레벨스: [Favikon](https://favikon.com/blog/who-is-levelsio)
- 에어비앤비: [Andrew Chen](https://andrewchen.com/how-to-be-a-growth-hacker-an-airbnbcraigslist-case-study/), [Boston University BHR](https://www.bu.edu/bhr/2016/01/08/the-making-of-airbnb)

**⚠️ 확인하지 못한 것**
- **인스타그램 해시태그 5개 제한**은 여러 매체 보도로 확인했지만, 인스타그램 공식 발표 원문은 직접 보지 못했어요. 3개라고 쓴 매체도 있었어요.
- **메타 광고 "7일에 50회" 학습 기준과 예산 계산식**은 국내 광고 대행사들의 안내예요. 메타 공식 도움말로는 확인하지 못했어요.
- **당근 광고 최소 금액**은 대행사 글만 찾았고, 공식 금액은 확인하지 못했어요.
- **스레드 국내 이용자 수**는 조사마다 540만~820만 명으로 차이가 컸어요.
- **사례 속 숫자**(무신사 시작 연도 2001/2002, 오늘의집 커머스 시작 2016/2017, 모닝 브루·드롭박스·듀오링고 성장 수치)는 출처마다 조금씩 달라요. 대부분 회사 공식 자료가 아니라 기사·분석 글이에요.

---

## 34~35장 (도메인 이름 · 업계 지식)

### 34장 도메인 이름
- [.com 도매가 인상 발표 (Domain Name Wire)](https://domainnamewire.com/2026/04/23/breaking-verisign-raising-wholesale-com-prices/)
- [.com 가격 인상 설명 (Openprovider)](https://www.openprovider.com/blog/com-price-increase-domain-resellers)
- [도메인 만료 단계 (DNSimple)](https://support.dnsimple.com/articles/domain-expiration-reference/)
- [도메인 만료 안내 (ICANN 블로그)](https://www.icann.org/news/blog/do-you-have-a-domain-name-here-s-what-you-need-to-know-part-5)
- [.kr 도메인 안내 (GoDaddy)](https://godaddy.com/help/about-kr-domains-19996)
- [.kr 소개 (ICANNWiki)](https://icannwiki.org/.kr)
- [UDRP 한국어 (WIPO)](https://www.wipo.int/amc/ko/domains/gtld/udrp/index.html)
- [UDRP 정책 한국어 (ICANN)](https://www.icann.org/en/contracted-parties/consensus-policies/uniform-domain-name-dispute-resolution-policy/uniform-domain-name-dispute-resolution-policy-01-01-2020-ko)
- [도메인이름 부정 차용 (Nepla)](https://www.nepla.ai/wiki/%EC%A7%80%EC%8B%9D%EC%9E%AC%EC%82%B0/%EB%B6%80%EC%A0%95%EA%B2%BD%EC%9F%81/%EB%8F%84%EB%A9%94%EC%9D%B8%EC%9D%B4%EB%A6%84-%EB%B6%80%EC%A0%95%EC%B0%A8%EC%9A%A9-mo59y6j3581v)

### 35장 업계 지식
- [정기결제(빌링) 이해하기 (토스페이먼츠)](https://www.tosspayments.com/blog/articles/34411)
- [PG 정산 구조 (고도몰)](https://www.godo.co.kr/main/blog/23/payment-gateway-calculate-sattlement-1091)
- [결제수단별 결제 프로세스 (아이보스)](https://www.i-boss.co.kr/ab-74668-4300)
- [3PL·풀필먼트 차이 (아임웹)](https://imweb.me/blog?idx=519)
- [풀필먼트 업계 인터뷰 (바이라인네트워크)](https://byline.network/2019/10/14-75/)
- [RTB 실시간 경매 (DI매거진)](https://ditoday.com/?p=12517)
- [서드파티 쿠키 제한의 영향 (DI매거진)](https://ditoday.com/?p=54024)
- [Bounded Context (Martin Fowler)](https://martinfowler.com/bliki/BoundedContext.html)
- [Domain-Driven Design (Devopedia)](https://devopedia.org/domain-driven-design)

**⚠️ 확인하지 못한 것**
- **.kr 등록 자격**: 국내 주소가 필요하다는 안내와 해외에서도 대리 등록이 된다는 안내가 섞여 있었어요. KISA 공식 안내는 직접 보지 못했어요.
- **도메인 만료 단계별 기간(약 45일·30일·5일)과 60일 이전 제한**은 주로 gTLD 기준이고, 등록 업체 안내 위주로 확인했어요. .kr은 다를 수 있어요.
- **인터넷주소분쟁조정위원회**의 현재 절차·수수료는 찾지 못했어요.
- **크롬 서드파티 쿠키 정책**의 최신 상태는 이번 조사에서 확인하지 못해서, "여러 번 바뀌었다"고만 적었어요.
- **PG사별 정산 주기(D+N 일수)** 는 계약마다 달라서 숫자를 적지 않았어요.

---

## 36~38장 (호스팅 · 보안 · 출시 전 체크리스트)

### 36장 서버·호스팅
- [무료 호스팅 요금제 비교 (Flavio Copes)](https://flaviocopes.com/hosting-free-tiers.md)
- [Vercel 무료 vs Pro (Fencode)](https://www.fencode.dev/en/blog/vercel-free-vs-pro-2026-official-limits-pricing)
- [호스팅 무료 요금제 비교 (AgentDeals)](https://agentdeals.dev/hosting-free-tier-comparison-2026)
- [개인정보 국외이전 (ITWiki, ISMS-P 기준)](https://itwiki.kr/w/ISMS-P_%EC%9D%B8%EC%A6%9D_%EA%B8%B0%EC%A4%80_3.3.4.%EA%B0%9C%EC%9D%B8%EC%A0%95%EB%B3%B4%EC%9D%98_%EA%B5%AD%EC%99%B8%EC%9D%B4%EC%A0%84)
- [개인정보보호법 시행령 개정 (법률신문)](https://www.lawtimes.co.kr/news/189930)

### 37장 보안
- [OWASP Top 10 2025 공식](https://owasp.org/Top10/2025/0x00_2025-Introduction/)
- [OWASP Top 10 2025 보도 (The Register)](https://www.theregister.com/2025/11/11/new_owasp_top_ten_broken/)
- [OWASP 2025 변경점 (Qualys)](https://blog.qualys.com/qualys-insights/2026/06/15/what-changed-in-owasp-top-10-2025-and-recommendations-for-each-category)
- [개인정보의 안전성 확보조치 기준 (위키독스 정리)](https://wikidocs.net/264634)
- [안전성 확보조치 기준 안내서 공개 (보안뉴스)](https://m.boannews.com/html/detail.html?idx=133982)

### 38장 출시 전 체크리스트
- [스크롤과 주목도 (Nielsen Norman Group)](https://www.nngroup.com/articles/scrolling-and-attention/)
- [제목 링크 가이드 (Google Search Central)](https://developers.google.com/search/docs/appearance/title-link)
- [제목·설명 도움말 발표 (Search Engine Land)](https://searchengineland.com/google-publishes-new-help-documents-on-controlling-titles-and-descriptions-in-search-375057)
- [robots.txt 소개 (Google Search Central)](https://developers.google.com/search/docs/advanced/robots)
- [코어 웹 바이탈 기준 (web.dev)](https://web.dev/articles/defining-core-web-vitals-thresholds)
- [HowTo·FAQ 리치 결과 축소 (Search Engine Land)](https://searchengineland.com/google-reduces-the-visibility-of-howto-and-faq-rich-results-in-search-430452)
- [FAQ 리치 결과 중단 보도 (Search Engine Journal)](https://www.searchenginejournal.com/google-drops-faq-rich-results/574429/)
- [카카오 스크랩(미리보기) 체크리스트 (카카오 데브톡)](https://devtalk.kakao.com/t/scrap-url/116202)
- [카카오 스크랩 캐시 삭제 (카카오 데브톡)](https://devtalk.kakao.com/t/topic/33298)
- [GA4 추천 이벤트 (Google 도움말)](https://support.google.com/analytics/answer/9267735)
- [GA4 핵심 이벤트 (PPC Land)](https://ppc.land/key-event/)
- [네이버 서치어드바이저 등록 (인블로그)](https://inblog.ai/ko/docs/seo-tutorial-domain-setup/registering-with-naver-search-advisor)

**⚠️ 확인하지 못한 것**
- **무료 요금제 조건**(Vercel 비상업 제한, Netlify·Cloudflare 상업 허용 등)은 비교 기사 기준이에요. 각 회사 약관 원문은 보지 못했어요.
- **해외 클라우드 서울 리전 사용 시 국외 이전 해당 여부**는 자료에서 직접 다루지 않아 "사례마다 다를 수 있다"고만 적었어요.
- **OWASP 2025의 A06·A07 항목 이름**은 검색 결과가 아니라 기존 지식으로 채웠어요. 공식 페이지에서 확인하세요.
- **안전성 확보조치 기준**: 접속기록 보관(원칙 1년, 조건부 2년)은 확인했지만, 관리자 2단계 인증 의무 등 세부 조문은 확인하지 못해 요약으로만 적었어요. "이용자 접속기록 3개월"이라는 다른 보도도 있었어요.
- **FAQ 리치 결과 2026년 완전 중단**은 SEO 업계 보도 기준이고, 구글 공식 공지는 직접 보지 못했어요.
- **OG 이미지 권장 크기**: 1200×630은 업계에서 흔히 쓰는 값이고, 카카오 공식 문서로는 확인하지 못했어요(카카오 포럼엔 800×400 안내).
- **meta keywords를 구글이 쓰지 않는다**는 내용과 **명도 대비 4.5:1(WCAG)** 은 이번 조사에서 새로 확인하지 않은 기존 지식이에요.
- **네이버 서치어드바이저** 세부 절차는 공식 도움말이 아니라 2차 자료로 확인했어요.

---

## 39~41장 (결제 연동 · 멀티플레이 서버 · 어뷰징)

### 39장 결제 연동과 정산
- [결제 요청·인증·승인 흐름 (토스페이먼츠 블로그)](https://www.tosspayments.com/blog/articles/54253)
- [토스페이먼츠 결제 연동하기 (토스페이먼츠 벨로그)](https://velog.io/@tosspayments/토스페이먼츠-결제-연동하기)
- [PG 계약 절차 (포트원)](https://blog.portone.io/pg_onboarding_process/)
- [포트원 FAQ](https://blog.portone.io/faq_portonepg/)
- [웹훅 멱등성·재시도 (Inquir)](https://inquir.org/blog/idempotency-making-webhooks-and-jobs-safe-to-retry)
- [Stripe 웹훅 운영 사례 (Alex Cloudstar)](https://alexcloudstar.com/blog/stripe-webhooks-production-2026/)
- [판매대금 20일 내 정산·50% 별도관리 (뉴시스)](https://www.newsis.com/view/NISX20241018_0002924933)
- [정산기한 논의 (유니콘팩토리)](https://www.unicornfactory.co.kr/article/2024092309311434191)
- [현금영수증 의무발행 (크몽 공지)](https://kmong.com/support/expert-center/posts/612)
- [현금영수증 미발급 가산세 (한국경제)](https://www.hankyung.com/article/2025022107957)

### 40장 멀티플레이 게임 서버
- [VALORANT 128틱 서버 (Riot 기술 블로그)](https://technology.riotgames.com/node/112)
- [피커스 어드밴티지 (PC Gamer)](https://pcgamer.com/valorant-peekers-advantage-interview)
- [롤 채팅 서비스 구조 (Riot 기술 블로그)](https://technology.riotgames.com/node/21)
- [Fast-Paced Multiplayer (Gabriel Gambetta)](https://gabrielgambetta.com/client-server-game-architecture.html)
- [클라이언트 예측·서버 보정 (Gabriel Gambetta)](https://gabrielgambetta.com/client-side-prediction-server-reconciliation.html)
- [Source Multiplayer Networking (Valve 개발자 위키)](https://developer.valvesoftware.com/wiki/Source_Multiplayer_Networking)
- [Lag Compensation (Valve 개발자 위키)](https://developer.valvesoftware.com/wiki/Lag_Compensation)
- [포트나이트 배틀로얄 엔진 개선 (Unreal Engine 블로그)](https://www.unrealengine.com/tech-blog/unreal-engine-improvements-for-fortnite-battle-royale)
- [배그 틱 레이트 문제 (Shacknews)](https://shacknews.com/article/105209/please-take-a-look-high-tick-rate-hot-drops)
- [틱 레이트와 비용 (Edgegap)](https://edgegap.com/blog/game-server-tick-rate-explained-gameplay-precision-vs-infrastructure-cost)
- [롤백 넷코드 설명 (Infil)](https://words.infil.net/w02-netcode-p5.html)
- [Agones (GitHub)](https://github.com/googleforgames/agones)
- [Agones에서 GameLift로 (AWS 블로그)](https://aws.amazon.com/blogs/gametech/migrating-from-kubernetes-and-agones-to-amazon-gamelift-servers/)

### 41장 어뷰징·핵 대응
- [크리덴셜 스터핑 방지 치트시트 (OWASP)](https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html)
- [Vanguard 커널 드라이버 설명 (KitGuru)](https://www.kitguru.net/?p=461990)
- [롤 Vanguard 도입 (Esports.net)](https://www.esports.net/news/lol/does-lol-use-vanguard/)
- [게임산업법 위반 처벌 해설 (로톡)](https://www.lawtalk.co.kr/posts/145754)
- [게임 핵 처벌 강화 개정안 (위키트리)](https://www.wikitree.co.kr/articles/270838)
- [게임산업법 위반 통계·처벌 지적 (파이낸셜뉴스)](https://www.fnnews.com/news/202509210428134600)
- [중복계정 혜택 환수 사례 (다음 뉴스)](https://v.daum.net/v/bxTAuqYcQN)
- [다중 계정 차단 (알체라 블로그, 업체 글)](https://www.alchera.ai/resource/blog/ekyc-multiple-account-block-identification)

**⚠️ 확인하지 못한 것**
- **토스페이먼츠 승인 만료 시간(10분)** 은 비공식 라이브러리 문서에서만 봤어요. 웹훅·가상계좌 세부는 공식 문서를 직접 보지 못했어요.
- **대규모유통업법 개정(정산 20일·50% 별도 관리)** 은 2024년 10월 정부 확정안 기준이고, 국회 통과·시행일은 확인하지 못했어요.
- **현금영수증 가산세율**은 보도마다 달랐어요(20%, 10일 이내 자진발급 시 10% 등). 쇼핑몰·PG 매출에 대한 적용은 세무 확인이 필요해요.
- **PG 수수료 1~3%대**는 통합 결제 플랫폼 블로그의 설명이에요.
- **각 게임사 서버 구조**는 대부분 비공개라서 공개 기술 블로그·업계 해설로 정리했어요. 배그 틱 레이트 문제는 2018년 보도 기준이라 지금과 다를 수 있어요.
- **결정론적 록스텝(RTS)** 은 이번 검색에서 근거 자료를 찾지 못해 기존 지식으로 짧게 적었어요.
- **밴 웨이브(몰아서 제재)** 는 업계에서 널리 알려진 방식이지만, 이번 검색에서 공식 근거를 찾지 못했어요.
- **핵 제작·유통 5년/5천만 원, 대리 게임 2년/2천만 원**은 법률 해설·기사 기준이에요. 조문 원문과 시행일은 국가법령정보센터에서 확인하세요.
- **본인인증·AI 탐지 효과**에 관한 자료는 주로 솔루션 업체 글이라 과장됐을 수 있어요.

---

## 42~56장 (창업가의 기본기 · 만들고 키우는 실전)

### 42장 아이디어 검증
- [션 엘리스 40% 테스트 (Learning Loop)](https://learningloop.io/plays/product-market-fit-survey)
- [PMF 설문 (Umbrex)](https://umbrex.com/resources/frameworks/product-management-frameworks/sean-ellis-product-market-fit-survey/)

### 43장 가격
- [반 베스텐도르프 가격 민감도 (Umbrex)](https://umbrex.com/resources/frameworks/marketing-frameworks/van-westendorp-price-sensitivity-meter/)
- [반 베스텐도르프 SaaS 적용 (Monetizely)](https://www.getmonetizely.com/articles/how-to-implement-van-westendorp-price-sensitivity-meter-for-saas-research)

### 44장 돈 관리·법인
- [종합소득세 vs 법인세 2026 (헬프미)](https://www.help-me.kr/blog/article/2026-comprehensive-income-tax-vs-corporate-tax/)
- [법인전환 시점 2026 (택슬리)](https://taxly.kr/post/1777-개인사업자-법인전환-언제-하는-게-좋을까요-2026년-최신-기준)
- [성실신고 대상과 법인 전환 3년 (헬프미)](https://www.help-me.kr/blog/article/sincere-filing-corporation-conversion-3-years/)
- [법인 전환 절세 (비즈넵)](https://help.bznav.com/hc/ko/articles/41035181488281)

### 45장 지원금·투자
- [2026 창업 지원금 (아임웹)](https://imweb.me/blog?idx=191)
- [2026 창업지원사업 일정 (헬프미)](https://www.help-me.kr/blog/article/2026-startup-support-schedule/)
- [2026 예비창업패키지 모집 (대학저널)](https://www.dhnews.co.kr/news/view/1065589716567019)
- [단계별 창업 패키지 (벤처스퀘어)](https://www.venturesquare.net/1021021/)

### 47장 상표·저작권·라이선스
- [생성형 AI 저작권 등록 안내서 (DI매거진)](https://ditoday.com/gai-copyright/)
- [생성형 AI 저작권 안내서 2종 (뉴스서울)](https://www.newsseoul.co.kr/news/view/1065576023564746)
- [상표 출원 비용 (헬프미)](https://www.help-me.kr/blog/article/%EC%83%81%ED%91%9C%EC%B6%9C%EC%9B%90%EB%B9%84%EC%9A%A9/)
- [상표 수수료 계산 (데모데이)](https://demoday.co.kr/tools/trademark-fee)
- [오픈소스 라이선스 준수 (Promise Legal)](https://blog.promise.legal/startup-central/open-source-license-compliance-for-startups/)
- [AGPL 이해 (Revenera)](https://www.revenera.com/software-composition-analysis/glossary/what-is-the-agpl-license)

### 48장 UX
- [5명 사용성 테스트 (Nielsen Norman Group)](https://nngroup.com/articles/why-you-only-need-to-test-with-5-users/)

### 49장 AI로 개발하기
- [Claude Code 모범 사례 (공식 문서)](https://code.claude.com/docs/en/best-practices)
- [Claude Code 모범 사례 (DataCamp)](https://www.datacamp.com/tutorial/claude-code-best-practices)

### 52장 해외 진출
- [비EU OSS 등록 (Stripe 문서)](https://docs.stripe.com/tax/use-stripe-to-register/non-union-oss)
- [EU OSS (Anrok)](https://help-center.anrok.com/hc/en-us/articles/44287096554899-EU-One-Stop-Shop-EU-OSS)

### 53장 외주·팀
- [SW 표준 하도급 계약서 (아이뉴스24)](https://www.inews24.com/view/702975)
- [외주 소스코드 저작권 귀속 분쟁 (Nepla)](https://www.nepla.ai/wiki/%EC%A7%80%EC%8B%9D%EC%9E%AC%EC%82%B0/%EC%A0%80%EC%9E%91%EA%B6%8C/%EC%99%B8%EC%A3%BC-%EA%B0%9C%EB%B0%9C-%EC%86%8C%EC%8A%A4%EC%BD%94%EB%93%9C-%EB%AC%B4%EB%8B%A8-%EC%9E%AC%EC%82%AC%EC%9A%A9-%EC%A0%80%EC%9E%91%EA%B6%8C-%EA%B7%80%EC%86%8D%C2%B7%EC%86%90%ED%95%B4%EB%B0%B0%EC%83%81%EC%9D%80-4%EC%B2%9C%EB%A7%8C-%EC%9B%90-%EB%B0%B0%EC%83%81-%EC%82%AC%EB%A1%80-%EC%B4%9D%EC%A0%95%EB%A6%AC-j3wnko2748y6)

**⚠️ 확인하지 못한 것**
- **『The Mom Test』 질문 원칙**은 이번 검색에서 근거 자료를 찾지 못해 기존 지식으로 요약했어요.
- **2026년 예비·초기창업패키지 금액**은 기사·블로그 기준이고 공고문 원문은 보지 못했어요.
- **법인세율 2026년 인상(10·20·22·25%)** 과 **성실신고 기준 금액**은 세무 업체 해설 기준이에요. 국세청 공지로 확인하세요.
- **간편장부 대상 기준, 세금 신고 월**은 기존 지식으로 적었어요.
- **상표 출원 관납료**는 자료마다 달랐어요(46,000원 / 62,000원). 심사 기간은 찾지 못했어요.
- **AI 결과물 저작권 기준**은 안내서 원문이 아니라 해설 기사로 확인했어요.
- **한국 다크 패턴 규제 강화**, **가격 심리 기법**, **RFM·코호트**, **번아웃 관리**, **이용약관·보험·폐업 절차**는 이번 조사에서 별도로 확인하지 않은 일반 지식이에요. 특히 개인정보 손해배상책임 보험 의무의 대상 기준은 직접 확인하세요.
- **한국 해외 매출 영세율**, **GDPR 적용·EU 대리인 지정**은 이번 검색에서 근거를 찾지 못해 일반론으로만 적었어요.
- **과기정통부 SW 표준계약서**의 세부 조항(하자보수 기간·소스코드 조항)은 확인하지 못했어요.
- **51장 파이썬 예제**는 예시 데이터로 실제 실행해 결과를 확인했어요.

---

## 57장 바이브코딩 수익 사례

### 피터 레벨스 (fly.pieter.com)
- [본인 글: 17일 만에 ARR 100만 달러 (levels.io)](https://levels.io/full-multiplayer-python-websockets-game-ai)
- [바이브코딩 게임이 월 5만 달러 — 당신은 아마 못 번다 (404 Media)](https://404media.co/this-game-created-by-ai-vibe-coding-makes-50-000-a-month-yours-probably-wont)
- [3시간 만에 만들고 17일 만에 ARR 100만 달러, 그 뒤 (DEV)](https://dev.to/promptway/he-built-a-flight-simulator-in-three-hours-and-hit-1m-a-year-in-17-days-then-it-went-to-zero-1b1l)
- [수익을 내는 바이브코딩 앱 4가지 (Indie Hackers)](https://www.indiehackers.com/post/2NUIOp80SUWuPmmfKoS9)
- [3시간 바이브코딩으로 월 1.2억 게임, 피터 레벨스 분석 (조쉬)](https://maily.so/josh/posts/mjz63lnyzwk)

### 마크 루 (TrustMRR)
- [TrustMRR 리뷰 (MakerStack)](https://makerstack.co/reviews/trustmrr-review/)
- [마크 루 프로필 (yespress)](https://yespress.io/marc-lou.md)

### Base44
- [윅스, Base44 인수 (Globes)](https://en.globes.co.il/en/article-wix-acquires-israeli-vibe-coding-co-base44-1001513267)
- [윅스, Base44를 8,000만 달러에 인수 (TipRanks)](https://www.tipranks.com/news/ma-news-wix-com-wix-acquires-base44-for-80m)
- [6개월 만의 인수 (DesignRush)](https://news.designrush.com/wix-buys-ai-startup-base44-for-80m-six-month-sprint-deal)

### Plinq
- [사브리나 마투스가 Plinq를 만든 방법 (Lovable 블로그, 한국어)](https://lovable.dev/ko/blog/how-sabrine-matos-built-plinq)
- [Plinq 투자 유치 (LatamList)](https://latamlist.com/plinq-raises-254k-to-launch-safety-app-for-women-in-brazil/)

### 국내 외주 사례 (불혹코딩)
- [요즘IT 기고 (위시켓)](https://yozm.wishket.com/magazine/detail/3466/)
- [8개월 100건, 2,400만원 사례집 (요즘IT)](https://yozm.wishket.com/magazine/detail/3803)
- [『요즘 바이브 코딩 커서 X 클로드 코드 실전 외주 돈 벌기』 (교보문고)](https://ebook-product.kyobobook.co.kr/dig/epd/ebook/E000013040613)

### 실패·보안 사례
- [EnrichLead, 일주일 만에 종료 (Vibe Graveyard)](https://vibegraveyard.ai/story/enrichlead-vibe-coded-saas-shutdown/)
- [바이브코딩의 보안 문제 (Indie Hackers)](https://www.indiehackers.com/post/vibe-coding-has-a-security-problem-vLxyPTrTlZVwDo76oqvr)
- [CVE-2025-48757 (Intruder)](https://cvemon.intruder.io/cves/CVE-2025-48757)
- [바이브코딩 앱 API 키 노출 (Kodu)](https://blog.kodu.cloud/vibe-coded-apps-leaked-api-keys)

### 참고 (근거가 약해 본문에 넣지 않은 것)
- [바이브코딩 SaaS 1만 달러 MRR 사례 (Medium)](https://medium.com/@samyabratamaji828/these-vibe-coded-saas-products-make-10k-mrr-real-case-studies-8a2b5783892b) — TrendFeed 등. 개인 블로그 글이라 제외했어요.
- [18살 비개발자도 앱으로 수천만원 (조쉬)](https://maily.so/josh/posts/8do7kvwyrgq)

**⚠️ 확인하지 못한 것**
- **모든 매출 숫자**는 본인 SNS 발표나 도구 회사 홍보 글이에요. 감사를 거친 숫자가 아니에요.
- **fly.pieter.com의 현재 수익**은 자료끼리 정반대예요(월 0달러 / 월 13만 8천 달러).
- **"70개 이상 프로젝트 중 4개 성공"**이라는 피터 레벨스의 말은 국내 해설 글에서만 봤어요. 원문은 찾지 못했어요.
- **피터 레벨스의 팔로워 규모**("수십만 명")는 일반 지식으로 적었어요.
- **levels.io, maily.so**는 이 세션의 네트워크 설정 때문에 직접 열어 보지 못했어요. 검색 결과 요약으로만 확인했어요.
- **TrustMRR 출시일**(10월 30일 / 11월)과 **제작 시간**(24시간 / 48시간)이 자료마다 달라요.
- **Base44 직원 수**(6명 / 8명), **Plinq 사용자 수·투자 금액**이 자료마다 달라요.
- **불혹코딩 외주 건수**(70건 이상 / 100건)가 자료마다 달라요. 기고와 책 저자가 같은 사람이라는 것은 필명과 경력으로 추정했어요.
- **EnrichLead 개발자 이름**은 자료마다 표기가 달라서 본문에 넣지 않았어요.
- **"바이브코딩"이라는 말이 2025년 초부터 퍼졌다**는 내용은 일반 지식으로 적었어요.

---

## 58~60장 (설계·모듈화 · 데이터베이스 설계 · API 설계)

### 58장 설계와 모듈화
- [모듈러 모놀리스 안의 기능별 구조 (Milan Jovanović)](https://www.milanjovanovic.tech/blog/where-vertical-slices-fit-inside-the-modular-monolith-architecture)
- [기능별 패키지 구성 (Medium)](https://medium.com/@vitorbritto/the-package-by-feature-approach-c62a197a8a3d)
- [모듈화란 무엇인가 (Substack)](https://kbaranowski.substack.com/p/what-does-modularity-mean)
- [마이클 나이가드 결정 기록 템플릿 (clan)](https://clan.lol/docs/26.05/decisions/template)
- [ADR 용어 설명 (Real Python)](https://realpython.com/ref/software-engineering-glossary/architecture-decision-record/)
- [CLAUDE.md가 너무 길면 안 되는 이유 (tianpan)](https://tianpan.co/blog/2026-02-14-writing-effective-agent-instruction-files)
- [CLAUDE.md 규칙 쓰기 (Better Stack)](https://betterstack.com/community/guides/ai/claude-md-rules/)

### 59장 데이터베이스 설계
- [정규화 1NF~BCNF (DigitalOcean)](https://www.digitalocean.com/community/tutorials/database-normalization)
- [PostgreSQL "Don't Do This" 발표 자료 (FOSDEM 2023)](https://www.postgresql.eu/events/fosdem2023/sessions/session/4099/slides/361/DontDoThis.pdf)
- [PostgreSQL에 돈 저장하기 (TechEarl)](https://techearl.com/store-money-postgresql)
- [수파베이스 RLS 공식 문서](https://supabase.com/docs/guides/database/postgres/row-level-security)
- [수파베이스 RLS 정책 작성 가이드 (공식)](https://supabase.com/docs/guides/getting-started/ai-prompts/database-rls-policies)

### 60장 API 설계
- [RFC 9457 Problem Details for HTTP APIs (IETF)](https://datatracker.ietf.org/doc/html/rfc9457)
- [멱등성 요청 (Stripe 공식 문서)](https://docs.stripe.com/api/idempotent_requests)
- [REST API 모범 사례 (env.dev)](https://env.dev/guides/rest-api-best-practices)

**⚠️ 확인하지 못한 것**
- **세 장의 예제 코드 3개**(결제 감싸기, SQLite 쇼핑몰 표, API 서버)는 문서에 적힌 그대로 실제 실행해 결과를 확인했어요. API 서버는 curl로도 확인했어요.
- **"응집도·결합도", 3계층 구조, 설정은 환경 변수에** 같은 내용은 업계에서 널리 쓰는 일반 지식으로 적었어요. 특정 공식 문서를 근거로 하지 않았어요.
- **ADR 템플릿 형식**은 나이가드의 원문이 아니라 그 형식을 옮긴 자료로 확인했어요.
- **CLAUDE.md 길이 기준**(200~500줄 등)은 블로그 경험담이고 공식 기준이 아니에요. 본문의 "300줄 넘으면 나누기"는 예시로 정한 숫자예요.
- **스트라이프 페이지네이션 파라미터**(`starting_after`, `limit` 1~100)는 검색 결과 요약으로 확인했어요.
- **HTTP 상태 코드 뜻**, **OpenAPI**, **API 버전 관리 관례**, **403 대신 404를 주는 관례**는 일반 지식이에요.
- **정규형 설명**은 입문 튜토리얼 수준으로 쉽게 줄였어요. 엄밀한 정의는 데이터베이스 교재를 보세요.

---

## 61~64장 (광고·홍보·마케팅 심화)

### 61장 유료 광고 심화
- [구글애즈 캠페인 유형별 정리 (AMPM 인사이드)](https://inside.ampm.co.kr/insight/59923)
- [2026년 구글 광고의 종류·비용 (인마케팅)](https://inmarketing.kr/?p=3214)
- [구글 실적 최대화(PMax) 개념 (아이보스)](https://www.i-boss.co.kr/ab-6141-72042)
- [카카오모먼트 예산 (AMPM 인사이드)](https://inside.ampm.co.kr/insight/4096)
- [카카오 비즈니스 광고 공식 안내 (카카오모먼트)](https://kakaobusiness.gitbook.io/main/ad/moment)
- [쿠팡 광고 세팅 가이드 (AMPM 인사이드)](https://inside.ampm.co.kr/insight/59091)
- [쿠팡 광고 운영 전략 (AMPM 인사이드)](https://inside.ampm.co.kr/insight/60422)
- [쿠팡 광고 종류와 설정 (윈들리)](https://www.windly.cc/blog/coupang-ad-types-and-settings)
- [메타 전환 API (AdsUploader)](https://adsuploader.com/blog/meta-conversions-api)
- [iOS 추적 제한과 전환 손실 (TrueROAS)](https://www.trueroas.com/blog/ios-tracking-fix-lost-conversions)
- [메타 광고 소재 테스트 (Segwise)](https://segwise.ai/blog/facebook-ad-creative-testing-framework)
- [소재 피로와 테스트 (Darkroom)](https://www.darkroomagency.com/observatory/creative-fatigue-performance-testing-framework)

### 62장 브랜딩·출시·PR·인플루언서
- [에이프릴 던포드 포지셔닝 템플릿 (Miro, 한국어)](https://miro.com/ko/templates/april-dunfords-positioning-template/)
- [프로덕트 헌트 출시 가이드 2026 (LaunchList)](https://app.getlaunchlist.com/blog/how-to-launch-on-product-hunt-2026)
- [네트워크가 작은 사람을 위한 프로덕트 헌트 가이드 (DEV)](https://dev.to/ahmet_saridag_9232a4f1a24/a-product-hunt-launch-guide-that-doesnt-assume-your-network-is-already-huge-3h8o)
- [스타트업 보도자료 (넥스트유니콘)](https://www.nextunicorn.kr/insight/32e7ef1f73ced445)
- [보도자료 보내기 (브런치)](https://brunch.co.kr/@instinct/18)
- [추천보증 심사지침 안내서 개정본 (뉴스서울)](https://newsseoul.co.kr/news/view/1065583816365047)
- [AI 가상인물 광고 심사지침 개정안 (신&김 뉴스레터)](https://shinkim.com/kor/media/newsletter/pdf/3230)
- [인플루언서 계약과 표시광고 (알법)](https://albup.co.kr/page/column_detail.php?content_id=2190)

### 63장 콘텐츠·검색
- [AI 기능과 내 웹사이트 (구글 검색 센터 공식)](https://developers.google.com/search/docs/appearance/ai-features)
- [2026년 블로그 상위노출 총정리 (브런치)](https://brunch.co.kr/@imd08071/282)
- [지금 검색 화면에서 벌어지는 일 — AI 브리핑 (아이보스)](https://www.i-boss.co.kr/ab-6141-71347)
- [네이버 블로그 최적화 (위픽)](https://letter.wepick.kr/wiki/blog-naver-optimization)

### 64장 자동 메시지
- [친구톡 종료, 카카오 비즈니스 메시지 2026 (AMPM 인사이드)](https://inside.ampm.co.kr/insight/59098)
- [알림톡 vs 브랜드 메시지 (비즈고)](https://blog.bizgo.io/howto/alimtalk-friendtalk-difference/)
- [브랜드 메시지 발송 조건·비용 (비즈고)](https://blog.bizgo.io/?p=4391)

**⚠️ 확인하지 못한 것**
- **61장 손익분기 ROAS 예제 코드**는 문서에 적힌 그대로 실행해 결과를 확인했어요.
- **광고 플랫폼 정보 대부분**(구글 캠페인 변화, 카카오 최소 입찰가, 쿠팡 예산·목표 ROAS)은 **광고 대행사·셀러 블로그** 기준이에요. 카카오 최소 입찰가는 **2023년 자료**라 지금은 다를 수 있어요.
- **소재 테스트 숫자**(훅 비율 25~35%, 빈도 2.5~4회, 클릭률 20~30% 하락)는 업체 블로그 수치이고, 메타 공식 기준을 찾지 못했어요.
- **"메타가 픽셀과 전환 API를 함께 쓰라고 권한다"**는 업체 자료로 확인했고, 메타 개발자 문서 원문은 보지 못했어요.
- **포지셔닝 5단계**는 던포드의 책 원문이 아니라 템플릿·요약 자료를 바탕으로 쉽게 줄였어요.
- **프로덕트 헌트 요령**은 업체·개인 가이드 글 기준이고 프로덕트 헌트 공식 안내가 아니에요. **해커 뉴스·인디 해커스·디스콰이엇** 설명은 일반 지식이에요.
- **보도자료 발송 시간·방법**은 홍보 실무자 블로그 기준이에요. **기사형 광고 표시** 내용은 일반 지식이에요.
- **추천보증 심사지침 2025년 12월 개정 내용**(제목·첫 부분 표시, 애매한 표현 금지)은 기사·법률 해설로 확인했고 공정위 원문은 보지 못했어요. **AI 가상인물 개정안**의 확정 여부도 확인하지 못했어요.
- **네이버 AI 브리핑 적용 비율**(20~40%)은 자료마다 달라 확정할 수 없어요. **네이버 키워드 도구 사용법**은 일반 지식으로 적었어요.
- **E-E-A-T**, **허브 앤 스포크**, **링크 판매 금지**는 이번 검색에서 구글 원문을 확인하지 못한 일반 지식이에요.
- **알림톡·브랜드 메시지 규격**은 딜러사 블로그 기준이에요. **이메일 자동 흐름 6가지와 시점**, **애플 메일 열람률 부정확**, **비교 그룹 방식**은 업계 일반 지식이에요.
- **"구매를 권하는 장바구니 메시지는 광고성으로 보는 게 안전"**은 카카오 템플릿 심사 기준(딜러사 설명)과 30장 법 규칙을 바탕으로 한 보수적 판단이에요.

---

## 65~74장 (빠진 항목 보강)

### 65장 로그인·권한
- [OWASP 비밀번호 저장 치트시트 (공식)](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### 66장 자주 쓰는 기능
- 한국어 검색 예제는 SQLite 3.45의 FTS5(기본·trigram)로 직접 실행해 확인했어요. 별도 외부 출처는 없어요.

### 67장 AI 기능
- [OWASP LLM 10대 위험 2025 해설 (HackerOne)](https://www.hackerone.com/ai/owasp-top-10-llms-2025)
- [OWASP LLM 10대 위험 2025 정리 (F5)](https://www.f5.com/resources/infographic/owasp-llm-top10)
- [OWASP LLM 10대 위험 2025 개요 (DEV)](https://dev.to/foxgem/overview-owasp-top-10-for-llm-applications-2025-a-comprehensive-guide-8pk)

### 68장 속도·오류·접근성·비용
- [코어 웹 바이탈 기준을 정한 방법 (web.dev 공식)](https://web.dev/articles/defining-core-web-vitals-thresholds)
- [코어 웹 바이탈 기준표 (Specification)](https://specification.website/spec/performance/core-web-vitals/)

### 69장 자동화·데이터 수집
- [공개데이터 크롤링, 합법과 불법의 경계 (김경환 변호사, 다음)](https://v.daum.net/v/EyCb0hoKc4)
- [야놀자 vs 여기어때 2심 (다음 뉴스)](https://v.daum.net/v/20220826110606958)
- [크롤링 법적 쟁점 (Nepla)](https://www.nepla.ai/nest/@xxWIvIKZwKx7/insight/크롤링-스크래핑-에-관한-법적-쟁점과-크롤링시-고려-사항-jw5dnz68e6kz)

### 70장 노무
- [2026 최저임금 인상 가이드 (시프티)](https://shiftee.io/ko/blog/article/2026-minimum-wage-increase-guide-for-hr-managers)
- [2026 최저임금 월급 환산표 (비즈폼)](https://www.bizforms.co.kr/365guide/view.asp?number=254)
- [근로계약서 필수 기재사항 (시프티)](https://shiftee.io/ko/blog/article/employment-contract-required-entries-guide)
- [근로계약서 필수 항목 (샤플웍스)](https://www.shoplworks.com/blog/insight/essential-items-employment-contract)
- [2026년 4대보험 요율 총정리 (아시아탑)](https://asiatop.co.kr/insurance-labor/four-insurance-rate-2026-summary/)
- [4대보험 요율과 계산 (위키독스)](https://wikidocs.net/blog/@Insight_Lab/23005/)

### 71장 세금·보험·신고
- [적격증빙 4가지 (더체크)](https://thecheck.co.kr/?p=3514)
- [증빙불비 가산세 (택스가이드)](https://taxguide.im/blog/penalty-for-failure-to-receive-qualifying-proof)
- [노란우산공제 소득공제 한도 2026 (위키독스)](https://wikidocs.net/blog/@Insight_Lab/22095/)
- [노란우산 납입한도 확대, 공제는 600만 원 (매일신문)](https://www.imaeil.com/page/view/2026100307144336255)
- [부가통신사업 신고 (아이뉴스24)](https://www.inews24.com/view/1313798)
- [경품 제세공과금 (세이브택스)](https://www.save-tax.co.kr/blog/%EA%B2%BD%ED%92%88-%EC%84%B8%EA%B8%88-%EB%82%B4%EA%B3%A0-%EB%B0%9B%EC%95%84%EC%95%BC-%ED%95%9C%EB%8B%A4-%EC%9D%98%EC%99%B8%EC%9D%98-%EC%9B%90%EC%B2%9C%EC%A7%95%EC%88%98-%ED%95%AD%EB%AA%A9-5%EA%B0%80)

### 10장 보강 (개인정보 유출 신고)
- [유출 신고 안내 (개인정보보호위원회)](https://pipc.go.kr/np/default/page.do?mCode=D030040000)
- [유출 '의심'만 돼도 72시간 내 고지 (MTN)](https://news.mtn.co.kr/news-detail/2026060210061182263)
- [개인정보 과징금 매출 10% (파이낸셜뉴스)](https://www.fnnews.com/news/202609101158195934)

**⚠️ 확인하지 못한 것**
- **실행 예제 7개**(비밀번호 저장, 파일 검사, 한국어 검색, AI 비용, 최저 월급, 4대보험)는 문서에 적힌 그대로 실행해 결과를 확인했어요. 2026년 최저 월급 2,156,880원은 안내 자료 숫자와 같아요.
- **2026년 4대보험 요율**(국민연금 9.5%, 건강보험 7.19%, 장기요양 13.14%)은 안내 사이트 기준이고 공단 고시 원문은 보지 못했어요. **고용보험 사업주 추가분 0.25%**와 **산재 1%**는 예시로 정한 값이에요.
- **근로계약서 미작성 벌금·과태료 금액**, **5인 미만 적용 여부**, **4대보험 취득 신고 기한**, **퇴사 후 14일 정산**은 블로그·일반 지식 기준이에요. 근로기준법 원문을 확인하지 못했어요.
- **노란우산공제** 소득 구간별 한도와 2026년 **납입 한도**는 자료마다 달라 확정하지 못했어요.
- **간이과세 기준 금액**, **1인 자영업자 고용·산재보험**, **지역가입자 보험료 반영 시점**은 일반 지식이에요.
- **부가통신사업 신고**의 정확한 요건은 시행령 원문을 확인하지 못했어요.
- **경품 부가세 처리**는 자료끼리 설명이 달라 본문에 넣지 않았어요.
- **개인정보법 2026년 9월 개정**은 기사로 확인했고, "1천 명 기준"이 시행령으로 옮겨졌는지 등 세부 조문은 확인하지 못했어요.
- **크롤링 판례**는 기사·변호사 칼럼 기준이고 판결문 원문은 보지 못했어요.
- **소셜 로그인·OAuth 흐름**, **세션·토큰·쿠키 설정**, **패스키**, **회원 탈퇴·장기 미사용 계정**, **업로드·알림·예약 작업·관리자 화면**, **접근성 항목·다크 모드**, **로그·오류 추적**, **클라우드 예산 알림**, **자동화 도구**, **택배·재고·포장·반품 실무**, **RICE·이벤트 공지·추천인 프로그램·콜드메일·B2G**, **공부법·정보 수집**은 업계 일반 지식으로 썼어요.
- **AI 비용 예제의 가격**은 계산 연습용 예시예요. 실제 AI 회사 가격이 아니에요.

---

## 75~79장 (관문·등록·인증·구독 규칙·개발 도구 보강)

### 75장 설치형 프로그램과 코드 서명
- [SmartScreen 평판 (마이크로소프트 공식)](https://learn.microsoft.com/en-us/windows/apps/package-and-deploy/smartscreen-reputation)
- [EV 인증서의 즉시 평판 혜택 종료 (ToDesktop)](https://www.todesktop.com/blog/posts/windows-apps-psa-ev-certs-do-not-grant-immediate-reputation-anymore)
- [MSIX 서명 개요·비용 비교 (마이크로소프트)](https://learn.microsoft.com/en-sg/windows/msix/package/signing-package-overview)
- [Azure Artifact Signing (마이크로소프트)](https://azure.microsoft.com/en-us/products/artifact-signing)
- [Artifact Signing 대상 국가 문답 (Microsoft Q&A)](https://learn.microsoft.com/en-us/answers/questions/2243504/trusted-signing-for-other-countries)
- [OV vs EV 코드 서명 비교 (SSL Insights)](https://sslinsights.com/ov-code-signing-vs-ev-code-signing-certificate/)
- [개인사업자 EV·IV 코드 서명 (SSL.com)](https://ssl.com/certificates/iv-ev-code-signing/buy/)
- [macOS 배포 전 공증 (애플 공식)](https://developer.apple.com/documentation/security/notarizing-macos-software-before-distribution)
- [일렉트론 코드 서명 (공식 문서)](https://www.electronjs.org/docs/latest/tutorial/code-signing)

### 76장 플랫폼 관문
- [구글 플레이 12명 테스터 규칙 (Choicely)](https://www.choicely.com/blog/google-play-12-tester-rule)
- [구글 플레이 비공개 테스트 2026 (ExtendsClass)](https://extendsclass.com/blog/google-plays-closed-testing-requirement-what-developers-need-to-know-in-2026)
- [애플 심사 지침 5.1.1(v) 계정 삭제 (애플 공식)](https://developer.apple.com/help/app-review/guideline-reference/5-1-1-account-deletion)
- [앱 계정 삭제 요건 (Newly)](https://newly.app/how-to/account-deletion-requirement)
- [앱 접근권한 고지 — ISMS-P 기준 해설 (IT위키)](https://itwiki.kr/w/ISMS-P_%EC%9D%B8%EC%A6%9D_%EA%B8%B0%EC%A4%80_3.2.3.%EC%9D%B4%EC%9A%A9%EC%9E%90_%EB%8B%A8%EB%A7%90%EA%B8%B0_%EC%A0%91%EA%B7%BC_%EB%B3%B4%ED%98%B8)
- [크롬 웹스토어 등록비 (Chromium 블로그)](https://blog.chromium.org/2020/03/new-developer-dashboard-and.html)
- [스팀 다이렉트 등록비 (스팀웍스 공식)](https://partner.steamgames.com/doc/gettingstarted/appfee)
- [구글 OAuth 확인되지 않은 앱 (구글 클라우드 도움말)](https://support.google.com/cloud/answer/7454865)
- [카카오싱크·비즈 앱 사전 준비 (카카오 디벨로퍼스)](https://developers.kakao.com/docs/latest/ko/kakaosync/prerequisite)
- [사업자 번호 없이 비즈 앱 (카카오 데브톡)](https://devtalk.kakao.com/t/how-can-i-switch-to-a-biz-app-if-i-do-not-have-any-business-registration-number/71983)
- [Gmail·야후 대량 발송 요건 (Customer.io)](https://customer.io/learn/deliverability/email-sending-requirements-gmail-yahoo)
- [발신번호 사전등록제 (비즈고)](https://blog.bizgo.io/?p=3147)
- [2026 문자사업자 등록요건 강화 (비즈고)](https://blog.bizgo.io/trend/sms-business-registration-requirements/)

### 77장 정부·인증기관
- [KC 인증 가이드 (윈들리)](https://www.windly.cc/blog/kc-certification-guide-with-lookc-service)
- [KC 마크 표시 (윈들리)](https://www.windly.cc/blog/kcmark-guide-and-how-to-use)
- [벤처기업 인증 유형 (택스가이드)](https://taxguide.im/blog/venture-certification-types-overview-guide)
- [기업부설연구소 규제 완화 (다음 칼럼)](https://v.daum.net/v/xegPNIFYFm)
- [소프트웨어사업자 신고 (guard1004)](https://www.guard1004.com/190)
- [ISMS-P 인증 대상 (IT위키)](https://www.itwiki.kr/w/ISMS-P_%EC%9D%B8%EC%A6%9D_%EB%8C%80%EC%83%81)
- [ISMS-P 의무 대상 구체화 시행령 개정안 (디지털데일리)](https://www.ddaily.co.kr/page/view/2026060209483580759)

### 78장 구독·디지털 상품
- [다크패턴 6가지 규제 유형 (아임웹)](https://imweb.me/blog?idx=496)
- [6개 유형 다크패턴 문답서 배포 (뉴스서울)](https://www.newsseoul.co.kr/news/view/1065579616591557)
- [다크패턴 첫 제재 (노컷뉴스)](https://www.nocutnews.co.kr/news/6456984)
- [전자상거래법 청약철회 (korea.legal)](https://korea.legal/wiki/%EC%A0%84%EC%9E%90%EC%83%81%EA%B1%B0%EB%9E%98-%EC%B2%AD%EC%95%BD%EC%B2%A0%ED%9A%8C/)

### 79장 정규식·도커·의존성
- 정규식 예제와 도커 빌드·실행(이미지 생성, 응답 확인, 일반 사용자 실행)은 이 작업 환경에서 직접 실행해 확인했어요. 별도 외부 출처는 없어요.

**⚠️ 확인하지 못한 것**
- **코드 서명 인증서 가격**은 판매처마다 크게 달라 범위로만 적었어요. **Azure Artifact Signing의 개인 대상 국가(미국·캐나다)**는 커뮤니티 답변 기준이고, 한국 법인 가능 여부는 확인하지 못했어요.
- **애플 개발자 프로그램 연회비**는 이번 검색에서 확인하지 못해 금액을 적지 않았어요.
- **백신 오탐 신고 창구**, **VirusTotal 주의점**, **심사 거절 흔한 이유**, **ATT**는 일반 지식이에요.
- **구글 플레이 12명·14일 규칙**은 개발자 블로그 기준이고 구글 도움말 원문은 보지 못했어요. 신원 확인 절차 세부도 확인 못 했어요.
- **카카오 비즈 앱·검수**는 데브톡 답변 기준이에요. **네이버 로그인 검수**는 일반 지식이에요.
- **문자 발송 2026년 변경**(식별코드·전송자격인증 날짜)은 자료마다 달라요.
- **KC 인증 품목 기준·구매대행 과태료**, **벤처기업 혜택**, **연구소 요건**, **SW사업자 신고 수수료·대상**, **청소년 보호책임자 기준**은 확인하지 못했어요.
- **특허 공개 예외 기간·BM 특허 기준·KIPRIS**, **프로그램 저작권 등록 효과**는 일반 지식이에요.
- **숨은 갱신 "30일 전 고지·동의"**와 **과태료 금액**은 블로그·기사 기준이라 법령 원문 확인이 필요해요.
- **미성년자 계약 취소**는 민법 일반 원칙으로 적었고, 게임·앱 결제 적용 기준은 확인하지 못했어요.
- **도커 사용 규칙**, **의존성 관리 방법(Dependabot·npm audit·pip-audit)**, **타이포스쿼팅·AI가 지어낸 패키지 이름**, **ReDoS**는 일반 지식이에요.

---

## 80~81장 (제품 기획·최적화와 안정화)

### 80장 제품 기획
- 이 저장소의 `product/` 기획 문서를 합친 장이에요. 외부 출처는 각 장(42·58~60·62·65·67·81장 등)의 출처를 따라요.

### 81장 최적화와 안정화
- [에러 예산 정책 예시 (구글 SRE 워크북)](https://sre.google/workbook/error-budget-policy/)
- [SLO 용어 (Real Python)](https://realpython.com/ref/software-engineering-glossary/service-level-objective-slo/)
- [에러 예산 (Netdata)](https://www.netdata.cloud/academy/error-budget/)
- [타임아웃·재시도·백오프와 지터 (아마존 빌더스 라이브러리)](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter)
- [카나리 릴리스 (마틴 파울러)](https://www.martinfowler.com/bliki/CanaryRelease.html)
- [하이퍼케어란 (Helply)](https://helply.com/blog/what-is-hypercare)
- [하이퍼케어 기간·끝내는 기준 (SupportBench)](https://www.supportbench.com/?p=27690)

**⚠️ 확인하지 못한 것**
- **실행 예제 4개**(에러 예산 계산, 재시도·차단기, N+1 쿼리 수, 인덱스 전후 측정)는 문서에 적힌 그대로 실행해 확인했어요. 인덱스 측정 시간은 이 작업 환경 기준이고 컴퓨터마다 달라요.
- **에러 예산 75% 기준**, **안정화 기간 끝내는 기준 예시**, **행사 배수 5~10배**는 예시로 정한 값이에요.
- **서킷 브레이커에 대한 마틴 파울러의 원문**은 이번 검색에서 확인하지 못했어요. 차단기 설명은 일반 지식과 아마존 글 요약을 바탕으로 했어요.
- **N+1 문제**, **커누스의 "섣부른 최적화" 인용**, **프로파일러 도구 이름(cProfile, cargo flamegraph)**, **금요일 배포 금지 관례**는 이번 검색에서 원문을 확인하지 못한 일반 지식이에요.

---

## 82장 AI 코드 보안 점검
- [취약점 탐지 코드 언어 모델, 얼마나 왔나 — PrimeVul (arXiv)](https://arxiv.org/abs/2403.18624v2)
- [Claude Code로 보안 리뷰 자동화 (Anthropic)](https://www.anthropic.com/news/automate-security-reviews-with-claude-code)
- [Claude Code 자동 보안 리뷰 (Anthropic 고객센터)](https://support.anthropic.com/en/articles/11932705-automated-security-reviews-in-claude-code)
- [CodeShield 문서 (메타 PurpleLlama/LlamaFirewall)](https://meta-llama.github.io/PurpleLlama/LlamaFirewall/docs/documentation/scanners/code-shield)
- [Foundation-Sec-8B (허깅페이스)](https://huggingface.co/fdtn-ai/Foundation-Sec-8B)
- [Foundation-Sec-8B 소개 (시스코)](https://blogs.cisco.com/security/foundation-sec-cisco-foundation-ai-first-open-source-security-model)
- [Foundation-Sec-8B 라이선스 고지 (허깅페이스 NOTICE)](https://huggingface.co/fdtn-ai/Foundation-Sec-8B-Instruct/blob/aa13cb996e7fc700e7efd6b7367992f14cf349c0/NOTICE.md)
- [오픈소스 AppSec 도구 64개 (AppSec Santa)](https://appsecsanta.com/open-source-tools)
- [오픈소스 비밀 키 스캐너 비교 (AppSec Santa)](https://appsecsanta.com/secret-scanning-tools/best-open-source-secret-scanning-tools)
- [비공개 저장소의 CodeQL (깃허브 문서)](https://docs.github.com/en/code-security/how-tos/scan-code-for-vulnerabilities/troubleshooting/troubleshooting-analysis-errors/cannot-enable-codeql-in-a-private-repository)
- [cargo audit (RustSec)](https://rustsec.org/)
- [오픈소스 침투 테스트 도구 14가지 (TechTarget)](https://www.techtarget.com/cybersecurity/tip/Top-14-open-source-penetration-testing-tools)
- [Nuclei vs OWASP ZAP (Penetrify)](https://www.penetrify.cloud/en/compare/nuclei-vs-owasp-zap/)

**⚠️ 확인하지 못한 것**
- **IDOR 예제**는 문서에 적힌 그대로 실행해 확인했어요. **한 바퀴 앱의 보안 헤더·경로 조작 테스트**는 앱 테스트로 확인했어요.
- **도구 라이선스**는 비교 블로그 기준이에요(Semgrep CE LGPL-2.1, Trivy Apache-2.0, Gitleaks MIT, TruffleHog AGPL-3.0, ZAP Apache-2.0). **OSV-Scanner 라이선스**와 **Bandit·gosec·ESLint 플러그인** 세부는 확인하지 못했어요.
- **CodeQL 비공개 저장소 가격**은 자료마다 달라 금액을 적지 않았어요.
- **CodeShield 정밀도·재현율(96%/79%)**은 2차 자료라 본문에 넣지 않았어요.
- **Qwen2.5-Coder의 3B 라이선스 예외**, **보안 리뷰 성능**은 확인하지 못했어요.
- **Gitleaks·cargo audit·ZAP을 이 작업 환경에서 직접 실행**하는 것은 도구 설치가 허용되지 않아 하지 못했어요. 한 바퀴 앱의 보안 워크플로는 깃허브에서 첫 실행 때 확인돼요.
- **클로드 보안 리뷰 액션의 버전 표기(@main)와 입력 이름**은 미러·문서 색인 기준이라 공식 저장소에서 확인이 필요해요.
- **침투 테스트 도구 라이선스**: ZAP(Apache-2.0)만 확인했고 **Nmap·Metasploit·Nikto·Nuclei**의 라이선스·사용 조건은 각 프로젝트에서 확인이 필요해요. **ZAP 운영 주체**(OWASP → Software Security Project → Checkmarx)도 자료마다 달라요.

---

## 82~84장 (보안 확장: CodeQL·전체 지도·사고 사례)

### 82장 보강 — CodeQL·깃허브 보안 기능
- [CodeQL의 Rust 정식 지원 (깃허브 변경 이력, 2025-10-14)](https://github.blog/changelog/2025-10-14-codeql-scanning-rust-and-c-c-without-builds-is-now-generally-available)
- [CodeQL 2.23.3 Rust 규칙 (깃허브 변경 이력)](https://github.blog/changelog/2025-10-23-codeql-2-23-3-adds-a-new-rust-query-rust-support-and-easier-c-c-scanning)
- [코드 스캐닝 기본 설정 (깃허브 문서)](https://docs.github.com/en/code-security/how-tos/scan-code-for-vulnerabilities/configure-code-scanning/configuring-default-setup-for-code-scanning)
- [Secret Protection·Code Security 출시와 가격 (깃허브 변경 이력)](https://github.blog/changelog/2025-03-04-introducing-github-secret-protection-and-github-code-security/)

### 83장 보안 전체 지도
- [OWASP Top 10 2025 소개 (OWASP)](https://owasp.org/Top10/2025/0x00_2025-Introduction/)
- [OWASP Top 10 2025: 접근 통제 실패 여전히 1위 (The Register)](https://www.theregister.com/2025/11/11/new_owasp_top_ten_broken/)
- [서브도메인 탈취와 댕글링 DNS (Red Sift)](https://redsift.com/blog/dangling-dns-find-and-fix)

### 84장 국내 사례
- [SKT 과징금 1,348억 (전북일보)](https://www.jjan.kr/article/20250828580061)
- [SKT 최종 조사 결과 (디지털데일리)](https://www.ddaily.co.kr/page/view/2025070412563749518)
- [쿠팡 3,370만 계정 유출과 인증키 관리 (CIO)](https://www.cio.com/article/4098352/)
- [쿠팡 유출 결산 (보안뉴스)](https://m.boannews.com/html/detail.html?idx=141221)
- [예스24 랜섬웨어 원인 (보안뉴스)](https://m.boannews.com/html/detail.html?idx=137603)
- [예스24 재공격·백업 복구 (디지털데일리)](https://www.ddaily.co.kr/page/view/2025081110071397714)
- [롯데카드 웹로직 7년 방치 (디지털데일리)](https://www.ddaily.co.kr/page/view/2025101014431200842)
- [롯데카드 해킹 후 성찰 (보안뉴스)](https://m.boannews.com/html/detail.html?idx=142751)
- [KT 불법 펨토셀 조사 결과 (뉴시스)](https://mobile.newsis.com/view/NISX20251106_0003392746)
- [GS리테일 크리덴셜 스터핑 (보안뉴스)](https://m.boannews.com/html/detail.html?idx=135478)
- [GS샵 158만 건 유출 (보안뉴스)](https://m.boannews.com/html/detail.html?idx=136291)

### 84장 해외 사례
- [스노우플레이크 고객사 침해 (CyberInsider)](https://cyberinsider.com/hackers-target-snowflake-customer-instances-for-data-theft-and-extortion/)
- [캐피털원 해킹에서 배울 점 (Krebs on Security)](https://krebsonsecurity.com/2019/08/what-we-can-learn-from-the-capital-one-hack/)
- [캐피털원 사고 (Wiz 사고 데이터베이스)](https://threats.wiz.io/all-incidents/capital-one-incident-march-2019)
- [MOVEit CVE-2023-34362 (CybelAngel)](https://cybelangel.com/blog/moveit-cl0p-breach/)
- [Tea 앱 유출 (404 Media)](https://www.404media.co/women-dating-safety-app-tea-breached-users-ids-posted-to-4chan/)
- [Tea 앱 7만 2천 장 유출 (CyberInsider)](https://cyberinsider.com/tea-app-suffers-data-breach-exposing-72000-users-photos-and-private-messages/)
- [npm 공급망 공격·Shai-Hulud (Pulsedive)](https://blog.pulsedive.com/npm-compromise-the-wrath-of-the-shai-hulud-supply-chain-attack/)
- [polyfill.io 공급망 공격 (The Hacker News)](https://thehackernews.com/2024/06/over-110000-websites-affected-by.html)
- [polyfill.io 38만 호스트 (The Hacker News)](https://thehackernews.com/2024/07/polyfillio-attack-impacts-over-380000.html)
- [우버 MFA 피로 공격 (InfoQ)](https://www.infoq.com/news/2022/09/Uber-breach-mfa-fatigue/)
- [MGM 헬프데스크 사칭 (Computing)](https://www.computing.co.uk/news/4126034/mgm-resorts-hackers-deceived-service-desk-phone)
- [23andMe 크리덴셜 스터핑 (BleepingComputer)](https://bleepingcomputer.com/news/security/genetics-firm-23andme-says-user-data-stolen-in-credential-stuffing-attack)
- [LastPass 엔지니어 집 PC 침해 (Help Net Security)](https://www.helpnetsecurity.com/2023/02/28/lastpass-breach-corporate-vault/)

**⚠️ 확인하지 못한 것**
- **깃허브 보안 기능 가격**은 2025년 4월 출시 가격이에요. 이후 변경 여부는 깃허브 가격 페이지에서 확인하세요.
- **OWASP Top 10 2025**의 A04~A09 세부 순서는 이번 검색에서 원문으로 확인하지 못해 묶어서 적었어요. 최종본 공개 시점도 자료마다 달라요.
- **사례 숫자**(유출 건수·피해자 수·과징금)는 기사·발표마다 다른 경우가 있어 대표 수치만 적었어요. 쿠팡·KT는 **수사·조사가 진행 중**이었고, 예스24의 **몸값 지불**은 보도일 뿐 회사가 확인하지 않았어요.
- **캐피털원 피해 규모(1억 명 이상)**, **노출된 몽고DB·엘라스틱서치 몸값 공격**, **OWASP API·Mobile Top 10 내용**, **STRIDE**, **IMDSv2·SRI·CSP·DMARC 단계 적용**, **3-2-1·불변 백업**, **2025년 깃허브 액션 오염 사건**은 이번 검색에서 원문을 확인하지 못한 일반 지식이에요.
- **Tea 앱의 AI 코드 사용 여부**는 회사가 부인했고 확인되지 않았어요.

---

## 85장 프록시·동적 딜레이·브라우저 자동화

- [구글, 주거용 프록시망 IPIDEA 차단 (Security Affairs)](https://securityaffairs.com/187463/security/google-targets-ipidea-in-crackdown-on-global-residential-proxy-networks)
- [IPIDEA 차단 (SecurityWeek)](https://www.securityweek.com/google-disrupts-ipidea-proxy-network/amp/)
- [주거용 프록시의 문제 (Barracuda)](https://blog.barracuda.com/2026/04/24/home-cheat-home--the-problem-with-residential-proxies)
- [클라우드플레어, AI 크롤러 기본 차단 (MIT Technology Review)](https://www.technologyreview.com/2025/07/01/1119498/cloudflare-will-now-by-default-block-ai-bots-from-crawling-its-clients-websites/amp/)
- [클라우드플레어 pay per crawl (Computerworld)](https://www.computerworld.com/article/4015341/cloudflare-offers-to-make-ai-pay-to-crawl-websites.html)
- [RFC 9309 Robots Exclusion Protocol (IETF)](https://datatracker.ietf.org/doc/html/rfc9309)
- [robots.txt의 미래 (구글 검색 센터 블로그)](https://developers.google.com/search/blog/2025/03/robots-future?hl=en)
- [윤리적 웹 크롤러 모범 사례 (AWS 문서)](https://docs.aws.amazon.com/prescriptive-guidance/latest/web-crawling-system-esg-data/best-practices.html)
- [예의 바른 크롤러 (Slatecave)](https://slatecave.net/blog/being-a-polite-crawler-on-the-web/)

**⚠️ 확인하지 못한 것**
- **실행 예제 2개**(스스로 느려지는 수집기 + 연습 사이트, Playwright로 한 바퀴 앱 E2E)는 이 작업 환경에서 직접 실행해 확인했어요.
- **IPIDEA 사용 조직 550개 이상**은 보안 업체 보도 기준이고, 모든 사용자가 불법이었다는 뜻은 아니에요. 2026년 7월 **NetNut** 조치도 보도로만 확인했어요.
- **클라우드플레어 pay per crawl**은 2025년 시범(비공개 베타) 기준이고, 이후 변경은 확인하지 못했어요.
- **프록시 종류 설명, 합성 모니터링, 봇 막기 방법(행동 신호·캡차·턴스타일)**, **Puppeteer·Selenium**, **차단 우회가 업무방해·부정경쟁으로 이어질 수 있다는 판단**은 69장 판례 해설과 일반 지식을 바탕으로 했어요. 구체적 사안은 변호사와 확인하세요.

---

## 86장 인터넷이 동작하는 원리

- [IPv6 접속 50% 돌파 (The Register)](https://www.theregister.com/2026/04/17/ipv6_50_percent_google/)
- [18년 만에 IPv6 절반 (Internet Society Pulse)](https://pulse.internetsociety.org/blog/18-years-later-ipv6-reaches-majority)
- [구글 IPv6 통계 (구글)](https://www.google.com/ipv6/statistics.html)
- [CGNAT란 (CleanBrowsing)](https://cleanbrowsing.org/learn/what-is-cgnat)
- [CGNAT와 공유 IP (ipfyi)](https://ipfyi.com/guides/ip-basics/carrier-grade-nat-cgnat/)
- [클라우드플레어 2025 결산 (Cloudflare Radar)](https://cfl.re/3NoXVzr)
- [HTTP/3 사용 비율 (W3Techs)](https://w3techs.com/technologies/breakdown/ce-http3/ranking)
- [QUIC 촉발 (APNIC 블로그)](https://blog.apnic.net/2025/07/15/triggering-quic/)

**⚠️ 확인하지 못한 것**
- **실행 예제**(IP 분류, HTTP 글자 주고받기, 리버스 프록시와 X-Forwarded-For 위조 실험, 쿠키, ETag·304)는 문서 코드 그대로 실행해 확인했어요. **TLS 가로채기·CONNECT 403** 장면은 이 작업 환경에서 curl로 실제 관찰한 결과예요.
- **HTTP 버전별 비율**(HTTP/3 약 21%, HTTP/2 약 50%, HTTP/1.x 약 29%)은 클라우드플레어 2025 자료를 인용한 2차 분석 기준이에요. 측정 방식(요청·사이트·트래픽)에 따라 숫자가 달라요. **한국 IPv6 비율**은 확인하지 못했어요.
- **서울-미국 왕복 시간**, **TCP·UDP·TLS·SNI·쿠키·CORS·SSR/SPA 설명**, **제3자 쿠키 제한 동향**, **IP가 개인정보가 될 수 있다는 설명**은 일반 지식이에요.

---

## 87장 사업용 연락처 (도메인 이메일·전화번호)

- [Gmail SMTP와 Cloudflare Email Routing 함께 쓰기 (bmann)](https://bmannconsulting.com/notes/using-gmail-smtp-with-cloudflare-email-routing/)
- [Gmail과 Cloudflare Email Routing (DEV Community)](https://dev.to/pierre/gmail-with-cloudflare-email-routing-4413)
- [Cloudflare Email Routing + Gmail 노트 (juri.dev)](https://juri.dev/notes/email-routing-gmail-cloudflare/)
- [Cloudflare + Brevo + Gmail로 도메인 메일 (agentpedia)](https://agentpedia.codes/blog/free-custom-domain-email-cloudflare-brevo-gmail)
- [Cloudflare Email Service 문제 해결 문서 (Cloudflare)](https://developers.cloudflare.com/email-service/reference/troubleshooting/)
- [LG유플러스 기업 전화 상품 (LG U+)](https://www.lguplus.com/biz/all/telecom/lines/biz-call/B000000130?p=2)
- [070 인터넷전화 요금·인식 정리 (아정당)](https://www.ajd.co.kr/contents/basic-tip/detail/%EC%9D%B8%ED%84%B0%EB%84%B7_%EC%A0%84%ED%99%94_%EB%B2%88%ED%98%B8,_070%EC%9D%80_%EB%8B%A4_%EC%82%AC%EA%B8%B0%EC%A0%84%ED%99%94%EB%9D%BC%EA%B3%A0_%EC%95%84%EB%8B%99%EB%8B%88%EB%8B%A4!-40891)
- [국가법령정보센터 — 전자상거래법 제10조(신원 및 거래조건에 대한 정보의 제공)](https://www.law.go.kr/법령/전자상거래등에서의소비자보호에관한법률)

**⚠️ 확인하지 못한 것**
- **검사기 예제**(SPF 기록 개수·조회 10개 한도·`+all`, DMARC `p`·`rua`, 헤더 결과 읽기)는 문서 코드 그대로 실행해 확인했어요. 실제 DNS를 조회하지 않고 붙여 넣은 글자만 보며, `include:` 안쪽의 조회는 세지 않아요(그래서 "최소").
- **Gmail "다른 주소에서 보내기"의 DMARC 정렬 실패**는 여러 해설 글의 공통 설명이에요. Gmail 쪽 동작이 바뀌었을 수 있으니 4절 방법(원본 보기)으로 직접 확인하세요. Cloudflare의 **보내기 서비스(Email Service)의 요금·제공 범위**는 확인하지 못했어요.
- **전화 요금**: 대표번호 월 11,000원(LG U+), KT 안심번호 월 1,100원, KT 듀얼번호 Lite 3,300원·Plus 8,800원, LG U+ 듀얼넘버 플러스 8,800원, SKT 넘버플러스II 3,850원 등은 검색으로 본 **공개 안내·기사 기준**이고 수시로 바뀌어요. **070 월 기본료는 자료끼리 숫자가 서로 달라** 장 본문에 금액을 적지 않았어요. 두 번째 번호로 걸 때 누르는 특수번호(*281·*77 등)는 2022년 기사 기준이에요. SKT "마이투넘버"(2026년 8월 출시 보도)의 요금·조건은 확인하지 못했어요.
- **전자상거래법 표시 의무**의 세부 항목(시행령 제11조의4, 시행규칙 제7조)과 2025년 과태료 사례는 검색 요약 기준이에요. 통신판매업 신고 면제 대상 등은 업종마다 달라요. **통화 녹음 고지**는 법적 의무 여부를 단정하지 않고 "안전한 운영 습관"으로 적었어요.
- **security.txt 형식**(Contact·Expires 필수)은 일반 지식(RFC 9116)이에요.

---

## 코딩 공부 노트

### 2장 언어 지도
- [TIOBE 2026년 10월 (TechRepublic)](https://www.techrepublic.com/article/news-tiobe-october-2026-java-closes-cpp-gap/)
- [TIOBE 2026년 10월 (Blog du Modérateur)](https://www.blogdumoderateur.com/20-langages-informatiques-populaires-octobre-2026/)
- [Stack Overflow 2025 설문 (공식)](https://survey.stackoverflow.co/2025/technology/)
- [Stack Overflow 2025 사용률 정리 (Enstacked)](https://enstacked.com/stack-overflow-developer-survey-insights/)
- [Stack Overflow 2025 사용률 정리 (SecondTalent)](https://www.secondtalent.com/resources/top-programming-usage-statistics/)

**⚠️ 확인하지 못한 것**
- 언어별 사용 비율(자바스크립트 약 69% 등)은 설문 공식 페이지가 아니라 정리 기사에서 가져왔어요.
- **C#·코틀린·스위프트 예제 코드**는 조사 환경에 실행 도구가 없어서 돌려 보지 못했어요. 나머지 10개 언어 예제와 문서 속 파이썬·C·웹 예제는 실제로 실행해서 확인했어요.
