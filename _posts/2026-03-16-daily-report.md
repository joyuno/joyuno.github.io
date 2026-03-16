---
layout: post
title: "2026-03-16 개발 작업 리포트"
date: 2026-03-16 09:45:16 +0900
categories: [dev-report]
tags: [daily-report, development]
---

# 🤖 Claude CLI 작업 리포트

- **feat**(otel_project): 401 에러 해결을 위한 인증 헤더 추가
  → NotificationContext.tsx에 axios 인터셉터 구현

- **refactor**(otel_project): 불필요한 폴링 제거 및 에러 핸들링 개선
  → NotificationContext.tsx에서 무한 재시도 로직 수정

- **chore**(otel_project): 프론트엔드 빌드 및 도커 컴포즈 재배포
  → docker compose up --build 실행

- **fix**(obsidian): 잘못 생성된 일일 리포트 파일 제거 로직 추가
  → update_daily_note.py에 작업 내용 검증

- **feat**(obsidian): GitHub 블로그 자동 배포를 위한 파일 경로 통일
  → upload_blog.py 등에서 상대 경로를 절대 경로로 수정

- **refactor**(obsidian): 스터디 및 블로그 업로드 실패 디버깅
  → main.py와 scraper.py의 실행 흐름 개선

---

💡 오늘의 AI 활용 팁: 에러 디버깅 요청 시 "이 에러 로그의 [구체적인 라인]과 [관련 파일/컨텍스트]를 보면, [추측 원인]일 것 같은데 맞는지 확인하고 수정 코드를 제안해줘"처럼 문제를 구체화하면 더 정확한 해결책을 얻을 수 있습니다.

## 📁 작업한 프로젝트

- **otel_project**
- **드롭쉬핑자동화**

## 📊 사용 통계

| 항목 | 값 |
|------|-----|
| 세션 수 | 2 |
| 프로젝트 수 | 2 |
| 명령어 수 | 7 |
| 총 메시지 | 42 |
| 도구 호출 | 61 |
| 수정된 파일 | 7 |