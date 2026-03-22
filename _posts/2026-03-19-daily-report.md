---
layout: post
title: "2026-03-19 개발 작업 리포트"
date: 2026-03-19 00:00:00 +0900
categories: [dev-report]
tags: [daily-report, development]
---

# 🤖 Claude CLI 작업 리포트

- **feat**(otel): OIDC SSO 인증 오류 해결
  → Azure AD 리디렉트 URI 불일치 수정 및 .env 설정 보완

- **fix**(otel): 컬렉터 메트릭 수집 실패 원인 분석
  → docker-compose.yml 내 엔드포인트 호스트/IP 오타 수정

- **refactor**(otel): 알림 시스템 개선
  → ToastNotification.tsx 및 NotificationPanel.tsx 분리 및 신뢰도 표시 로직 보강

- **chore**(otel): 불필요한 APM 관련 도커 서비스 정리
  → docker-compose.yml에서 사용하지 않는 서비스 제거

- **feat**(report): GitHub Actions 자동화 스케줄 추가
  → daily_report.yml에 한국시간 오전 7시 크론 작업 설정

- **fix**(trade): 매매 이력 조회 오류 해결
  → TradeHistory.tsx의 null 데이터 처리 및 pipeline.py SQL 쿼리 컬럼명 수정

- **feat**(shopify): MutBe 앱 개발 환경 구성
  → next.config.ts 리버스 프록시 설정 및 .env 클라이언트 인증 정보 추가

---

💡 오늘의 AI 활용 팁: 오류 발생 시 "에러 메시지 전문"과 "관련 설정 파일/코드 조각"을 함께 제공하면, AI가 맥락을 빠르게 파악하고 정확한 원인 분석과 수정안을 제시할 수 있습니다.

## 📁 작업한 프로젝트

- **otel_project**
- **포트폴리오**
- **드롭쉬핑자동화**
- **토지이음_등기부등본**
- **자동매매**

## 📊 사용 통계

| 항목 | 값 |
|------|-----|
| 세션 수 | 4 |
| 프로젝트 수 | 5 |
| 명령어 수 | 96 |
| 총 메시지 | 278 |
| 도구 호출 | 277 |
| 수정된 파일 | 32 |