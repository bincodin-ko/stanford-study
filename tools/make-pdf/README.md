# PDF 다시 만들기

문서를 고친 뒤 PDF를 새로 만들 때 쓰는 스크립트예요.

준비물: pandoc, Node.js + Playwright(크로미움), 한글 글꼴 Pretendard(TTF)

```bash
# 1) 모든 마크다운을 한 HTML로 합치기 (장 사이 링크를 PDF 안 이동 링크로 바꿈)
python3 tools/make-pdf/build.py . /tmp/book.html

# 2) 긴 한글 앵커 이름을 짧은 ID로 바꾸기
python3 tools/make-pdf/shorten_ids.py /tmp/book.html /tmp/book2.html

# 3) 크로미움으로 PDF 인쇄 (쪽 번호·책갈피 포함)
node tools/make-pdf/print.js /tmp/book2.html "pdf/인터넷-사업-공부-교재.pdf"
```

슬라이드 PDF는 LibreOffice로 변환해요: `soffice --headless --convert-to pdf slides/*.pptx`
