---
layout: post
title: "2026-03-12 개발 작업 리포트"
date: 2026-03-12 14:53:13 +0900
categories: [dev-report]
tags: [daily-report, development]
---

# 🤖 Claude CLI 작업 리포트

- **feat**(ml-anomaly-detection): 이상 탐지 이론 문서 작성
  → ml-anomaly-detection-theory.md에 CV 필터 및 Z-score 적용 방식 정리

- **refactor**(MLFilterResult.tsx): 이상점수 분포 차트 세로 막대형으로 변경
  → 가로 막대형에서 세로 막대형 차트로 개선

- **fix**(MLTest.tsx): L2+L3 이상 탐지 타임라인에서 critical 레벨만 시각화
  → warning 및 info 필터링 로직 추가

- **chore**(otel_project): 프론트엔드 빌드 및 도커 서비스 재배포
  → apm-frontend, ml-engine 컨테이너 업데이트

- **feat**(옵시디언정리): dev 블로그 리포트 생성 파이프라인 개선
  → deepseek 모델 연동 및 카테고리 구조 변경

- **refactor**(옵시디언정리): 블로그 네비게이션 및 레이아웃 수정
  → AI Tech 링크 추가 및 카테고리 페이지 트리 구조 설계

- **fix**(자동매매): 대시보드 보유종목 표시 로직 개선
  → 종목코드 대신 종목명 매핑하여 표시

---

💡 오늘의 AI 활용 팁: "왜 안되는지 설명해줘"보다 "현재 Z-score 공식은 X인데, 서비스별 분포를 적용하려면 Y 부분을 어떻게 수정해야 하나요?"처럼 구체적인 현재 상태와 원하는 방향을 명시하면 더 정확한 해결책을 제시받을 수 있습니다.

## 📁 작업한 프로젝트

- **otel_project**
- **드롭쉬핑자동화**
- **.claude-daily-report**
- **토지이음_등기부등본**
- **자동매매**
- **유튜브(좌우파)**

## 📊 사용 통계

| 항목 | 값 |
|------|-----|
| 세션 수 | 11 |
| 프로젝트 수 | 6 |
| 명령어 수 | 64 |
| 총 메시지 | 303 |
| 도구 호출 | 468 |
| 수정된 파일 | 26 |