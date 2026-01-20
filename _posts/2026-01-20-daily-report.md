---
layout: post
title: "2026-01-20 개발 작업 리포트"
date: 2026-01-20 23:58:02 +0900
tags: [daily-report, development]
---

# 🤖 Claude CLI 작업 리포트

- 4개 프로젝트에서 작업 수행
- 16개 파일 수정/생성
- 25개의 작업 요청 처리

## 📁 작업한 프로젝트

- **옵시디언 정리**
  - 경로: `/Users/admin/Downloads/옵시디언 정리`
- **자동매매**
  - 경로: `/Users/admin/Downloads/자동매매`
- **포트폴리오**
  - 경로: `/Users/admin/Downloads/포트폴리오`
- **codefill**
  - 경로: `/Users/admin/Downloads/codefill`

## 📊 사용 통계

| 항목 | 값 |
|------|-----|
| 세션 수 | 4 |
| 프로젝트 수 | 4 |
| 명령어 수 | 25 |
| 총 메시지 | 181 |
| 도구 호출 | 220 |
| 수정된 파일 | 16 |

## 📝 상세 작업 내역

<details>
<summary>펼쳐서 보기</summary>

#### .claude-daily-report

**주요 작업:**
- `Bash`: file=$(find ~/.claude/projects -maxdepth 2 -name "*.jsonl" -

#### quantflow/backend

**주요 작업:**
- `Bash`: sleep 8 && curl -s http://localhost:9000/health 2>/dev/null 
- `Bash`: pip3 install sqlalchemy aiosqlite playwright httpx cryptogra
- `Bash`: lsof -ti:9000 | xargs kill -9 2>/dev/null; sleep 1; cd /User
- `Bash`: sleep 10 && curl -s http://localhost:9000/health 2>/dev/null

**Claude 요약:**
> QuantFlow Trading System: Signals, Strategy, Health

#### website

**수정된 파일:**
- `Talet_프로젝트_경험기술서.txt`
- `style.css`
- `프로젝트별_기술스택_요약.txt`
- `ADBIAS_프로젝트_경험기술서.txt`
- `IMSAM_프로젝트_경험기술서.txt`

**주요 작업:**
- `Bash`: cp "/Users/admin/Downloads/포트폴리오/내사진.jpeg" "/Users/admin/Dow
- `Edit`: /Users/admin/Downloads/포트폴리오/website/css/style.css
- `Bash`: cd /Users/admin/Downloads/포트폴리오/website && git status
- `Bash`: cd /Users/admin/Downloads/포트폴리오/website && git add . && git 
- `Task`: fast-interview 폴더 전방위 분석
- `Write`: /Users/admin/Downloads/포트폴리오/IMSAM_프로젝트_경험기술서.txt
- `Task`: Talet, ADBIAS 프로젝트 탐색
- `Write`: /Users/admin/Downloads/포트폴리오/ADBIAS_프로젝트_경험기술서.txt
- `Write`: /Users/admin/Downloads/포트폴리오/Talet_프로젝트_경험기술서.txt
- `Write`: /Users/admin/Downloads/포트폴리오/프로젝트별_기술스택_요약.txt

**주요 이슈 및 작업:**
- 🗣️ https://techblog.musinsa.com/ 해당 사이트는 무신사 테크 블로그의 내용인데 들어가서 여러정보들 파악해서 요약해볼수있겠어?
- 🗣️ 일단 github 포트폴리오 에 있는 프로필 사진을  위 이미지로 바꿔줘 
- 🗣️ [Image: source: /Users/admin/Downloads/포트폴리오/내사진.jpeg]
- 🗣️ 존의 수동적인 데이터 수집 방식은 최소 1-2시간이 소요에서 수집->가공->리포트 작성 전단계를 자동화하여 15분 소요로 80%이상 시간 단축 
- 🗣️ https://joyuno.github.io/yunos-portfolio/ 변경 안된가겉아 아니면 저 각진 흰색 테두리 프레임을 없애주던가 
- 🗣️ [Request interrupted by user]
- 🗣️ https://joyuno.github.io/yunos-portfolio/ 변경 안된가겉아 아니면 저 각진 흰색 테두리 프레임을 없애주던가 
- 🗣️ This session is being continued from a previous conversation that ran out of con
- 🗣️ 1. CodeFill: Langgraph 활용 AI 코딩 튜터 플랫폼 개발 프로젝트 (3인)
동기: 코딩테스트를 준비하는 취준생 입장에서 단순히
- 🗣️ 좋은데 /Users/admin/Downloads/포트폴리오/fast-interview 폴더를 최대한 전방위적으로 분석해서 ai 엔지니어 적인 부
- 🗣️ 디테일한건 좋은데 인사팀이 볼걸 생각해서 전문용어는 최소한으로 줄여줄수 있어? 그리고 나도 바이브로 해서 그렇게 정확하게 내용을 파악하고 있지않
- 🗣️ txt 파일로 저장해줘
- 🗣️ 그럼 이제 위와 같은 양식으로 Talet과 ADBIAS 프로젝트에 대해서도  작성해줘 
- 🗣️ 4가지 프로젝트에서 주로 어떤 기술을 사용했는지 각각 간략하게 정리해줘
- 🗣️ 내가 각프로젝트에서 맡은 역할을 고려하여 주요기술 구체적으로 다시 작성해줘 그리고 표로 만들지 말고 
1. 2. 3. 4. 이렇게 적어  

#### codefill (`yuno`)

**수정된 파일:**
- `page.tsx`
- `capture_flow.py`
- `UnifiedPractice.tsx`
- `solving_assist_tool.py`
- `stats_cache.py`
- `capture_full_flow.py`
- `hint_service.py`
- `PracticeChatPanel.tsx`
- `agent.py`
- `users.py`

**주요 작업:**
- `Bash`: which playwright 2>/dev/null || which puppeteer 2>/dev/null 

**주요 이슈 및 작업:**
- 🗣️ 현재 linear mcp 사용해서 자동 기록하는 시스템 때문인지 모르겠는데 이전 기록이 다 날라간거같은데 복구 방법없을까? 
- 🗣️ This session is being continued from a previous conversation that ran out of con
- 🗣️ 아직도 빈칸에 대한 힌트가 문제 유형생성과 동시에 생성되고 있지 않거나 백엔드에서 가지고있던 힌트 내용을 프론트로 이동과정에서 레이턴시가 발생하
- 🗣️ 그리고 빈칸 문제에서 힌트 클릭시 정답은 직접 생각해보세요! 라는 문구가 있는데 이제 빈칸힌트는 정답과 설명을 제공하는 걸로 바뀌었으니 해당 문
- 🗣️ 오케이 이건 해결했다고 치고 아래는 문제 풀이 하다가 힌트를 사용후 왜 해당 코드 위치에 해당 답변이 들어가는지 아직도 이해가 안가거나 문제 풀
- 🗣️ This session is being continued from a previous conversation that ran out of con

</details>