---
layout: post
title: "2026-01-23 개발 작업 리포트"
date: 2026-01-23 00:00:00 +0900
tags: [daily-report, development]
---

# 🤖 Claude CLI 작업 리포트

오늘 수행한 주요 작업들을 상세히 요약하겠습니다:

## Programmers 프로젝트 관련 작업
- 문제 생성 스크립트 개선 → gemini_parallel_generator.py 수정
  - 주석 생성 문제 해결: 프롬프트에 주석 생성 금지 조건 재확인 
  - 테스트 케이스 출력 방식 개선: print(3024) 같은 하드코딩 방식에서 다른 테스트 방법 모색
  - Judge0을 활용한 테스트 케이스 입출력 검증 코드 작성
  - 프로그래머스 문제 550문제 중 525문제 생성 성공 여부 검증 (@programmers/validate_solutions.py)

## Codefill 프로젝트 관련 작업
- 문제 풀이 DB 연동 → feedback_service.py 등 다수 파일 수정
  - 문제 풀이 수 증가 메커니즘 구현
- 프론트엔드 아키텍처 최적화 → UnifiedPractice.tsx, page.tsx 등 수정
  - S3 vs EC2 호스팅 전략 재검토
  - 동적/정적 엔드포인트 설계 고찰
  - 프록시 서버 설정 고려
  - SSR(서버 사이드 렌더링) 접근 방식 검토
  - NextJS 프레임워크 서버 활용 전략
- 분석 도구 연동 → ga4.ts, clarity.ts 수정
  - GA4 및 Clarity 분석 도구 연동 문제 진단
- 타입스크립트 컴파일 검증 → 다양한 TypeScript 컴파일 명령 실행

## 주요 기술적 고려사항
- 백엔드와 프론트엔드 간 API 통신 최적화
- 서비스 호스팅 전략 (S3, EC2, 프록시 서버)
- 코드 생성 및 검증 자동화
- 분석 도구 통합

## 개선된 파일들
- Python: feedback_service.py, openrouter.py, agent.py, solving.py 등
- TypeScript: UnifiedPractice.tsx, agent.ts, PracticeChatPanel.tsx
- 설정 파일: .env.local, .env.production 등
- SQL: 20260124_increment_problem_solve.sql

이 요약은 오늘 수행한 다양한 기술적 작업과 개선 사항을 포괄적으로 보여줍니다.

## 📁 작업한 프로젝트

- **codefill_solutions**
  - 경로: `/Users/admin/Downloads/codefill_solutions`
- **codefill**
  - 경로: `/Users/admin/Downloads/codefill`

## 📊 사용 통계

| 항목 | 값 |
|------|-----|
| 세션 수 | 3 |
| 프로젝트 수 | 2 |
| 명령어 수 | 110 |
| 총 메시지 | 627 |
| 도구 호출 | 856 |
| 수정된 파일 | 46 |

## 📝 상세 작업 내역

<details>
<summary>펼쳐서 보기</summary>

#### programmers

**수정된 파일:**
- `gemini_parallel_generator.py`

**주요 작업:**
- `Bash`: ls -la /Users/admin/Downloads/codefill_solutions/baekjoon/*.
- `Bash`: python3 -c "import json; d=json.load(open('/Users/admin/Down
- `Edit`: /Users/admin/Downloads/codefill_solutions/programmers/gemini
- `Bash`: cd /Users/admin/Downloads/codefill_solutions/programmers && 
- `Bash`: python3 -c "
import json
with open('/Users/admin/Downloads/c
- `Bash`: python3 << 'PYEOF'
import json
with open('problems.json') as
- `Bash`: rm -f parallel_progress.json gemini_generated_solutions.json

**주요 이슈 및 작업:**
- 🗣️ @programmers/ 문제도 @programmers/gemini_parallel_generator.py 사용해서 풀고 싶은데 solution
- 🗣️ 명령어 텍스트로 다시 줘 
- 🗣️ 분명히 프롬프트에 주석은 코드에 생성하지 말라했는데 왜 코드 확인해보니까 주석이 생겼지?
- 🗣️ 그리고 모두 바로  테스트 케이스 입출력 judge0으로 테스트  가능하도록 코드 작성한거맞지?
- 🗣️ 별도의 테스트 스크립트가뭐야?
- 🗣️ 응 1번으로 해줘 다시 551문제 해보게 생성한 데이터는 리셋하고 
- 🗣️ print(3024) 이런식이면 테스트 케이스가 여러개 있으면 코드가 틀리게되잖아 다른 좋은 방법없어? 
- 🗣️ 방법 2로 변경
- 🗣️ 프로그래머스 코테문제 그럼이제 550문제중 525문제는 성공적으로 생성되었다는데 정답 검증 해줘 @programmers/validate_solu

**Claude 요약:**
> Python API script limit bug and graceful shutdown

#### codefill (`deploy`)

**수정된 파일:**
- `feedback_service.py`
- `UnifiedPractice.tsx`
- `.env.local`
- `MessageBubble.tsx`
- `openrouter.py`
- `agent.py`
- `practice.ts`
- `clarity.ts`
- `.env.example`
- `puzzle_validator.py`

**주요 작업:**

**주요 이슈 및 작업:**
- 🗣️ 아 그리고 문제를 정답까지 맞췃는데 푼 사람 수가 오르지가 않잖아 이거 db 연동해줘야지 
- 🗣️ 근데 프론트를 이전에 s3 만들려 하다가 왜 ec2로 하게됐지 /{id}/{} 뭐 이런 엔드포인트가 있어서 그렇다고 했던거같은데 
- 🗣️ 이걸 정적으로 처음부터 설계 하지 않은이유도 알려줄수있어?
- 🗣️ 이런것들을 다 백엔드에서 처리해도 됐지 않냐는 질문을 받았어서 물어봤어
- 🗣️ api call인데 왜 동적으로 구성해야 하자? 어차피 request 에 담아서 보내는 건데?
- 🗣️ 프록시 서버를 설정해야 된다는 말인가? 
- 🗣️ cloudfront는 과한것 같은데 국내 서비스로 한정할 거야 그럼 프록시 가 더 효율적이잖아 
- 🗣️ 404 페이지는 그냥 리다이렉션 처리하면되잖아 
- 🗣️ SSR 이 서버 사이드 렌더링을 말하는건가?
- 🗣️ nextjs를 하나의 서버로 판단하는 건가? 그냥 프레임워크 아닌가? 
- 🗣️ 내장 서버를 굳이 안쓰면 s3를 쓰는게 더 올바른것 같은데 이미 서버가 구현이 되어 있어 
- 🗣️   // getServerSideProps 사용 시                                          
  export 
- 🗣️   // getServerSideProps 사용 시                                          
  export 
- 🗣️ 근데 ga4랑 clarity 연동된거맞아? 기록이안되는데?
- 🗣️ This session is being continued from a previous conversation that ran out of con

</details>