---
layout: post
title: "2026-01-19 개발 작업 리포트"
date: 2026-01-19 00:00:00 +0900
tags: [daily-report, development]
---

# 🤖 Claude CLI 작업 리포트

오늘 수행한 주요 작업들을 상세하게 요약해드리겠습니다.

## .claude-daily-report 프로젝트
- 데일리 리포트 자동화 스크립트 실행 → main.py를 통해 2026-01-17 날짜의 데일리 리포트 생성 및 로그 수집
- 여러 설정 및 스크립트 파일 수정 → collect_logs.py, config.json, summarize.py 등 파일들의 세부 로직 업데이트
- 파일 수정 범위 확대 → _config.yml, main.py, index.html, default.html, post.html, upload_blog.py 등 다수 파일 편집

## 자동매매 프로젝트
- AI 분석 페이지 기능 개선 → AIAnalysis.tsx에서 Gemini API 관련 오류 수정
- 주가 분석 기능 확장 → technical.py와 market.py 수정을 통해 주가 차트 및 거래량 선 추가 작업
- Gemini API 키 설정 문제 해결 → .env 파일의 API 키 설정 재확인 및 수정

## 백준 문제 자동 솔루션 프로젝트
- 코드 자동 리라이팅 및 검증 스크립트 고도화 → rewrite_solutions.py와 gemini_parallel_generator.py 수정
- Gemini Flash 모델 사용한 솔루션 생성 → 13개 실패, 6개 리라이팅, 1개 이미 양호한 상태로 처리
- 검증 프로세스 개선 → Judge0 API 활용 방안 모색 및 입력 방식 최적화
- API 키 제한 대응 → 작업 중단 및 키 교체 전략 수립

## Codefill 프로젝트
- 사용자 문제 풀이 경험 개선 → 문제 포기 및 세션 종료 시 경고 팝업 추가 (ExitWarningDialog.tsx)
- ELO 점수 시스템 조정 → 오답 제출 5회 초과 시 점수 변동 방지 로직 구현
- 피드백 서비스 개선 → attempts 테이블의 점수 및 피드백 관련 컬럼 데이터 처리 최적화
- 다양한 에이전트 및 서비스 파일 수정 → agent.py, users.py, practice.py 등 여러 파일에 걸친 광범위한 수정

각 프로젝트에서 기능 개선, 버그 수정, 성능 최적화 등 다양한 작업을 수행했습니다. 특히 AI 모델 활용, API 통합, 사용자 경험 개선에 중점을 둔 작업들이 돋보입니다.

## 📁 작업한 프로젝트

- **옵시디언 정리**
  - 경로: `/Users/admin/Downloads/옵시디언 정리`
- **자동매매**
  - 경로: `/Users/admin/Downloads/자동매매`
- **codefill_solutions**
  - 경로: `/Users/admin/Downloads/codefill_solutions`
- **.claude-daily-report**
  - 경로: `/Users/admin/.claude-daily-report`
- **codefill**
  - 경로: `/Users/admin/Downloads/codefill`

## 📊 사용 통계

| 항목 | 값 |
|------|-----|
| 세션 수 | 14 |
| 프로젝트 수 | 5 |
| 명령어 수 | 66 |
| 총 메시지 | 502 |
| 도구 호출 | 674 |
| 수정된 파일 | 50 |

## 📝 상세 작업 내역

<details>
<summary>펼쳐서 보기</summary>

#### .claude-daily-report

**수정된 파일:**
- `_config.yml`
- `main.py`
- `index.html`
- `summarize.py`
- `default.html`
- `post.html`
- `collect_logs.py`
- `index.html`
- `upload_blog.py`
- `config.json`

**주요 작업:**
- `Bash`: cd ~/.claude-daily-report && python3 main.py 2026-01-17 --dr
- `Edit`: /Users/admin/.claude-daily-report/scripts/collect_logs.py
- `Edit`: /Users/admin/.claude-daily-report/scripts/summarize.py
- `Bash`: cd ~/.claude-daily-report && python3 main.py 2026-01-17 2>&1
- `Bash`: cd ~/.claude-daily-report && python3 << 'EOF'
from scripts.c

**주요 이슈 및 작업:**
- 🗣️ 실행 코드 알려줘 
- 🗣️ 근데 내가 입력했던 명령어 말고도 내가 입력했던 명령어에 대한 너의 대답에 대한 요약 즉 우리가 주고받았던 전반적인 대화내용을 나:문제제시, 클
- 🗣️ 그리고 요약 내용을 조금만 더 자세하게 할수 없을까 조금만 더 어떻게 해결했는지 의 관한 내용 위주로 
- 🗣️ 오늘 날짜로도 테스트해봐
- 🗣️ 1. 옵시디언 파일 저장소의 위치는 /Users/admin/Documents/Obsidian Vault 거기에 저장해야하고
2. 주요 이슈 및 
- 🗣️ This session is being continued from a previous conversation that ran out of con
- 🗣️ 오늘꺼 다시 한번더 실행

#### 자동매매

**수정된 파일:**
- `technical.py`
- `gemini_service.py`
- `market.py`
- `AIAnalysis.tsx`

**주요 작업:**
- `Edit`: /Users/admin/Downloads/자동매매/quantflow/frontend/src/pages/AIA
- `Bash`: cd /Users/admin/Downloads/자동매매/quantflow/backend && source v

**주요 이슈 및 작업:**
- 🗣️ 디바운싱 (debounce) - 입력할 때마다 API 호출 방지
퍼지 검색 (fuzzy search) - 오타 허용 검색 적용해줘 
- 🗣️ 검색기능은 잘 들어갔는데 분석 버튼만 누르면 아직도 기술 분석 페이지에서 아래와 같은 오류가 나와 그리고 technical 탭 누르면 아무것도 
- 🗣️ [Request interrupted by user]
- 🗣️ 검색기능은 잘 들어갔는데 분석 버튼만 누르면 아직도 기술         
  분석 페이지에서 아래와 같은 오류가 나와 그리고 technical 
- 🗣️ Gemini API가 설정되지 않았습니다. GEMINI_API_KEY를 확인하세요. ai anaylsis 버튼 클릭하니까 키없다는데 나 .env
- 🗣️ 래서 분석 agent gemini 모델                    
  gemini-3-pro-preview 로 쓰고 technical 
- 🗣️ 그리고 ai 분석 리포트 결과에 뉴스 내용은 가져오는데 실패 했다는데 삼성관련 뉴스를 못긁어 오는게 말이돼? 그리고 yahoo꺼랑 종목 토론방에

#### baekjoon

**수정된 파일:**
- `gemini_parallel_generator.py`
- `gemini_parallel_generator.py`
- `rewrite_solutions.py`

**주요 작업:**
- `Edit`: /Users/admin/Downloads/codefill_solutions/baekjoon/gemini_pa
- `Edit`: /Users/admin/Downloads/codefill_solutions/programmers/gemini
- `Bash`: cd /Users/admin/Downloads/codefill_solutions/programmers && 
- `Bash`: python3 << 'EOF'
import json

# Check GitHub solutions style
- `Bash`: cd /Users/admin/Downloads/codefill_solutions/baekjoon && pyt
- `Write`: /Users/admin/Downloads/codefill_solutions/baekjoon/rewrite_s
- `Edit`: /Users/admin/Downloads/codefill_solutions/baekjoon/rewrite_s
- `Bash`: cd /Users/admin/Downloads/codefill_solutions/baekjoon && ech

**주요 이슈 및 작업:**
- 🗣️ 3 flash 로 하는건 어떄 3 flash 의 무료티어 1 토큰 제한 알려줘 
- 🗣️ gemini 3 flash 모델 호출 이름 알려줘
- 🗣️ 그리고 한번 실패한건 넘기지말고 될때 까지 해줘 이건 이미 정답이 확인된 코드니까 그렇게 해도 문제 없어 
- 🗣️ Total processed: 10
Time: 2.2 minutes
  already_good: 1
  failed: 13
  rewritten
- 🗣️ admin@yuno-MacBook-Pro baekjoon % python3 rewrite_solutions.py --api-key "AIzaSy
- 🗣️ 2026-01-19 13:21:56,972 - WARNING - Validation failed for baekjoon_10024, attemp
- 🗣️ 아니 검증 할때는 judge0 api 사용해서 하면 안될까 그럼 이거 사용하면 sys 안써도 input() 으로 받을수 있어? 
- 🗣️ a로 sys는 허용하는걸로할게 
- 🗣️ 현재까지의 /Users/admin/Downloads/codefill_solutions/baekjoon/validated_problems_educ
- 🗣️ /Users/admin/Downloads/codefill_solutions/baekjoon/validated_problems_educationa
- 🗣️ 키 리밋이 끝나서 다른 키로 변경해서 마저 작업해야하는데 현재 작업 중인거 저장하고 중단안되나?
- 🗣️ ^C2026-01-19 16:32:22,655 - INFO - Shutting down gracefully... 뜨고 계속 멈추질않는데?
- 🗣️ admin@yuno-MacBook-Pro baekjoon % kill %1
2026-01-19 16:33:38,096 - INFO - Shutt
- 🗣️ ㅁ남은 문제와 실패한 문제만 다시 하려고하는데 

**Claude 요약:**
> Baekjoon/Programmers Solutions Generation & Validation

#### codefill (`yuno`)

**수정된 파일:**
- `agent.py`
- `next.config.js`
- `fix_question_formatting.py`
- `puzzle_problem_agent.py`
- `analysis_agent.py`
- `agent.ts`
- `page.tsx`
- `intent_tools.py`
- `nodes.py`
- `practice.py`

**주요 작업:**
- `Bash`: python3 -c "
import json
with open('/Users/admin/Downloads/c
- `Write`: /Users/admin/Downloads/codefill/scripts/fix_question_formatt

**주요 이슈 및 작업:**
- 🗣️ 둘 다 해줘 그리고 오답 제출이 5회 초과 상태로(attempts 테이블의 attempt_number 컬럼값참고 더좋은 방안 ok)  정답을  
- 🗣️ 그리고 attempts 테이블에 score값(피드백 점수 평균)과 feedback_grade,feedback_data,total_hints_re
- 🗣️ This session is being continued from a previous conversation that ran out of con
- 🗣️ [Request interrupted by user]
- 🗣️ 그리고 chat페이지에서 나가거나 문제 포기하거나 뒤로가기 하면  나가면 사용자의 실력 측정에 불이익을 받을수 있다고 하는 경고문과 함께 나가기

</details>