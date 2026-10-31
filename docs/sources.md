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
