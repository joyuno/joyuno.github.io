---
layout: post
title: "2026-01-21 개발 작업 리포트"
date: 2026-01-21 23:55:00 +0900
tags: [daily-report, development]
---

# 🤖 Claude CLI 작업 리포트

- 5개 프로젝트에서 작업 수행
- 41개 파일 수정/생성
- 59개의 작업 요청 처리

## 📁 작업한 프로젝트

- **옵시디언 정리**
  - 경로: `/Users/admin/Downloads/옵시디언 정리`
- **자동매매**
  - 경로: `/Users/admin/Downloads/자동매매`
- **codefill_solutions**
  - 경로: `/Users/admin/Downloads/codefill_solutions`
- **포트폴리오**
  - 경로: `/Users/admin/Downloads/포트폴리오`
- **codefill**
  - 경로: `/Users/admin/Downloads/codefill`

## 📊 사용 통계

| 항목 | 값 |
|------|-----|
| 세션 수 | 52 |
| 프로젝트 수 | 5 |
| 명령어 수 | 59 |
| 총 메시지 | 655 |
| 도구 호출 | 521 |
| 수정된 파일 | 41 |

## 📝 상세 작업 내역

<details>
<summary>펼쳐서 보기</summary>

#### quantflow/backend

**주요 작업:**
- `Bash`: pip3 install python-jose passlib bcrypt ta scikit-learn tran
- `Bash`: lsof -ti:9000 | xargs kill -9 2>/dev/null; sleep 1; cd /User
- `Bash`: sleep 12 && curl -s http://localhost:9000/health 2>/dev/null
- `Bash`: pip3 install psutil pykis
- `Bash`: sleep 10 && curl -s http://localhost:9000/health 2>/dev/null
- `Bash`: tail -50 /tmp/backend.log
- `Bash`: which python3.10 || /Users/admin/.pyenv/versions/3.10.18/bin

**주요 이슈 및 작업:**
- 🗣️ ㅎㅏ던 작업 잠깐 중단됐었는데 다시 해줄래?

**Claude 요약:**
> Stock News Crawling Fixed, Scheduler Replaced

#### baekjoon

**주요 작업:**
- `Bash`: python3 << 'EOF'
import json

with open('rewrite_progress.js
- `Bash`: cd /Users/admin/Downloads/codefill_solutions/baekjoon && pyt

**주요 이슈 및 작업:**
- 🗣️ 이제 몇개남았는지 확인해줘
- 🗣️ 이제 마무리 됐는지 확인해줄래

**Claude 요약:**
> Baekjoon Solution Rewrite to Educational Code

#### codefill (`yuno`)

**수정된 파일:**
- `Dockerfile`
- `requirements.txt`
- `index.ts`
- `.dockerignore`
- `next.config.js`
- `page.tsx`
- `PracticeChatPanel.tsx`
- `problems.py`
- `page.tsx`
- `AWS_TERMINOLOGY.md`

**주요 작업:**
- `Write`: /Users/admin/Downloads/codefill/AWS_DEPLOYMENT_TASKS.md
- `Write`: /Users/admin/Downloads/codefill/AWS_TERMINOLOGY.md
- `Write`: /Users/admin/Downloads/codefill/AWS_TERMINOLOGY_NOTION.md
- `Edit`: /Users/admin/Downloads/codefill/AWS_DEPLOYMENT_TASKS.md

**주요 이슈 및 작업:**
- 🗣️ 백엔드 테이블명 수정해줘 
- 🗣️ [Request interrupted by user for tool use]
- 🗣️ 문제 목록 페이지에서 어떤 API를 사용하는지 확인해서 레거시는 다삭제해
- 🗣️ This session is being continued from a previous conversation that ran out of con
- 🗣️ 현재여기서 프록시로 넘어갈때 포트  백엔드가 8000 프론트 3000 맞지?
- 🗣️ .env 에 있는 내용 다 https://api.codefill.co.kr/auth/github/callback 안쓰고 localhost:800
- 🗣️ http://localhost:3000/_next/static/css/app/layout.css?v=1768993320976 net::ERR_A

#### codefill (`yuno`)

**수정된 파일:**
- `solving.py`
- `solving_intent.py`
- `discovery_graph.py`
- `parse_input.py`
- `langsmith_config.py`
- `langsmith_tracker.py`
- `intent_tools.py`
- `orchestrator_v2.py`
- `confirm_value.py`
- `langsmith.py`

**주요 작업:**
- `Edit`: /Users/admin/Downloads/codefill/backend/app/tools/solving_as

**주요 이슈 및 작업:**
- 🗣️ This session is being continued from a previous conversation that ran out of con
- 🗣️ 이전에 했던 작업 마무리해줄래? 중간에 끊겼어서
- 🗣️ 그리고 미사용 빈칸 질문에 대해서는 힌트 버튼 먼저 눌러보세요 유도가 아니라 힌트에대한 간접적인 정보를 말해주는 채팅 힌트 챗봇있잖아(약한 힌트
- 🗣️ 수동로깅보다 LangSmith를 활용하고 싶은데 
- 🗣️ 응 만들어줘   - 각 노드별 입출력                                                            
- 🗣️ 그래서 그 추적되는게 어디에 저장되는거고 그냥 서버열고 들어가면 자동으로 찍히는거야 이제?
- 🗣️ 상세 메타데이터 (입출력 요약, 커스텀 태그) 사람눈으로 보기 좋게 데코레이터를 추가해서 상세분석 가능하게 해줘 
- 🗣️ This session is being continued from a previous conversation that ran out of con
- 🗣️ # 1. <VPC_ID>, <AMI_ID>, <INSTANCE_ID> 등은 실제 값으로 교체
# 2. <YOUR_IP>는 본인 IP로 교체 (h

**Claude 요약:**
> Hint-based chat filtering & LangSmith evaluation setup

</details>