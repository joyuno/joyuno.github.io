---
layout: post
title: "2026-03-16 개발 작업 리포트"
date: 2026-03-16 09:46:14 +0900
categories: [dev-report]
tags: [daily-report, development]
---

# 🤖 Claude CLI 작업 리포트

- **feat**(otel_project): 401 에러로 인한 알림 폴링 중단 처리
  → NotificationContext.tsx에 토큰 만료 시 폴링 중지 로직 추가

- **fix**(otel_project): axios 인터셉터 토큰 갱신 실패 처리 개선
  → client.ts에 refreshToken 실패 시 로그아웃 및 리다이렉트 구현

- **refactor**(obsidian): GitHub 블로그 자동 배포 스크립트 경로 정규화
  → upload_blog.py 등에서 절대경로를 상대경로로 일괄 수정

- **chore**(obsidian): 빈 작업일지 자동 생성 방지
  → update_daily_note.py에 유효 작업 내용 검증 로직 추가

- **fix**(obsidian): 스터디 및 블로그 콘텐츠 미업로드 문제 해결
  → study_generator.py와 scraper.py 실행 흐름 점검 및 수정

---

💡 오늘의 AI 활용 팁: "에러가 발생했어요"보다 "이 에러 로그와 관련 코드(파일명, 라인)를 보내드릴게요. 원인 분석과 수정 코드를 함께 제안해 주세요"처럼 구체적인 컨텍스트를 제공하면 더 정확한 해결책을 얻을 수 있습니다.

## 📁 작업한 프로젝트

- **otel_project**
- **드롭쉬핑자동화**

## 📊 사용 통계

| 항목 | 값 |
|------|-----|
| 세션 수 | 2 |
| 프로젝트 수 | 2 |
| 명령어 수 | 7 |
| 총 메시지 | 45 |
| 도구 호출 | 65 |
| 수정된 파일 | 7 |