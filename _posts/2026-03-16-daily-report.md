---
layout: post
title: "2026-03-16 개발 작업 리포트"
date: 2026-03-16 09:44:33 +0900
categories: [dev-report]
tags: [daily-report, development]
---

# 🤖 Claude CLI 작업 리포트

- **feat**(otel_project): 401 에러 발생 시 토큰 갱신 로직 추가
  → axios 인터셉터에서 refreshToken 호출 후 원 요청 재시도

- **refactor**(otel_project): 알림 폴링 로직 개선
  → NotificationProvider의 불필요한 중복 요청 방지 및 에러 처리 강화

- **chore**(otel_project): 프론트엔드 빌드 및 도커 컴포즈 재배포
  → 포트 3000 자동 배포 확인 및 빌드 프로세스 실행

- **fix**(obsidian): 일일 리포트 중복 생성 방지
  → update_daily_note.py에 작업 내용 존재 여부 검사 추가

- **feat**(obsidian): 블로그 자동 배포 스크립트 경로 수정
  → upload_blog.py의 파일 접근 루트를 obsidian 기준으로 통일

- **refactor**(obsidian): 스터디 내용 자동 생성 로직 개선
  → study_generator.py의 GitHub Actions 연동 및 실행 흐름 최적화

---

💡 오늘의 AI 활용 팁: "무한 반복 에러" 디버깅 시 "현재 코드 조각과 콘솔 에러 로그 전체를 함께 제공해줘"라고 요청하면 AI가 상태 관리와 API 호출 흐름을 더 정확히 분석해줍니다.

## 📁 작업한 프로젝트

- **otel_project**
- **드롭쉬핑자동화**

## 📊 사용 통계

| 항목 | 값 |
|------|-----|
| 세션 수 | 2 |
| 프로젝트 수 | 2 |
| 명령어 수 | 7 |
| 총 메시지 | 40 |
| 도구 호출 | 59 |
| 수정된 파일 | 7 |