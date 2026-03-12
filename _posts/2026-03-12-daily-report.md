---
layout: post
title: "2026-03-12 개발 작업 리포트"
date: 2026-03-12 13:53:46 +0900
categories: [dev-report]
tags: [daily-report, development]
---

# 🤖 Claude CLI 작업 리포트

feat(ml-anomaly-detection): 이상 탐지 이론 문서 작성 → ml-anomaly-detection-theory.md에 CV 필터 및 Z-score 적용 방식 정리
refactor(MLFilterResult.tsx): 이상점수 분포 차트 세로 막대형으로 변경 → 가로 막대형에서 세로 막대형 차트로 시각화 개선
chore(MLFilterResult.tsx): 그래프 레이아웃 및 빈 공간 조정 → 4*3, 8*3 크기로 한 라인에 배치 및 빈 공간 제거
feat(summarize.py): 요약 모델 OpenRouter/DeepSeek으로 교체 → config.json API 키 및 모델 엔드포인트 업데이트
refactor(default.html): 블로그 네비게이션 및 카테고리 구조 개선 → AI Tech 링크 추가 및 카테고리 페이지 트리 구조 설계
chore(index.html): 블로그 프로필 및 테마 설정 변경 → AI Engineer 타이틀, 라이트 모드 기본값, 프로필 이미지 경로 수정
fix(scraper.py): 외부 블로그 콘텐츠 스크래핑 로직 수정 → 지정된 URL 구조 파싱 및 업데이트된 내용만 추가하도록 개선
chore(upload_blog.py): 보안을 위한 작업 경로 필터링 추가 → otel_project 내부 폴더 경로 노출 방지

---

💡 오늘의 AI 활용 팁: 문제 해결 요청 시 "현재 코드/설정은 A인데, B 문제가 발생한다. 원인 분석과 수정된 코드를 C 형식으로 제시해줘"처럼 현재 상태, 문제, 원하는 출력 형식을 명시하면 더 정확한 해결책을 얻을 수 있습니다.

## 📁 작업한 프로젝트

- **otel_project**
- **드롭쉬핑자동화**
- **.claude-daily-report**
- **자동매매**

## 📊 사용 통계

| 항목 | 값 |
|------|-----|
| 세션 수 | 6 |
| 프로젝트 수 | 4 |
| 명령어 수 | 32 |
| 총 메시지 | 186 |
| 도구 호출 | 299 |
| 수정된 파일 | 18 |