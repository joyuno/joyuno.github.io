---
layout: post
title: "LLM 앱 운영의 현실: LangSmith vs Langfuse로 디버깅·비용·품질을 한 번에 잡는 법"
date: 2026-01-26
categories: [AI, MLOps]
tags: [ai, mlops, trend, 2026-01]
author: Daewook Kwon
reading_time: 14
source: https://daewooki.github.io/posts/llm-langsmith-vs-langfuse-2026-1-2/
---

LLM 애플리케이션 운영은 단순 로깅을 넘어 **관측 가능성(Observability)**이 필수입니다. 개발자들은 "어떤 프롬프트가, 어떤 컨텍스트로, 어떤 모델을, 얼마나 사용했는지, 어디서 실패했는지"를 요청 단위로 추적해야 합니다.

2025~2026년의 주요 변화는 두 제품 모두 **OpenTelemetry(OTel) 기반 엔드-투-엔드 분산 트레이싱**을 강화하고 있다는 점입니다.

## 핵심 개념

### 1) Trace / Span / Observation

- **Trace**: 사용자 요청 전체 실행 단위 (LLM, tool, retrieval 포함)
- **Span(OTel)**: 분산 트레이싱 기본 단위로 부모-자식 관계 형성
- **Observation(Langfuse)**: OTel span을 자체 모델로 매핑

가장 중요한 능력은 **컨텍스트 전파**로, 모듈이 분기되고 비동기 처리가 섞여도 각 요청이 어느 사용자에 속하는지 자동으로 연결되어야 합니다.

### 2) 디버깅의 본질

일반적인 LLM 앱 장애:
- 프롬프트/시스템 메시지 변경으로 성능 붕괴
- retrieval 품질 저하
- tool I/O 스키마 불일치
- latency 병목

트레이스는 LLM 호출뿐 아니라 tool, retrieval, 비즈니스 로직 span까지 같은 트리에 포함해야 합니다.

### 3) 비용 추적의 난점

2026년 기준 비용은 LLM 토큰만이 아닙니다:
- **LLM**: input/output token, cache read, reasoning token, multimodal token
- **Tool**: 외부 API 과금, 벡터DB 쿼리 비용, 크롤링 비용

LangSmith는 "full-stack cost tracking"을 강조하며 trace tree, stats, dashboards에서 토큰·비용 분석을 제공합니다.

## 실전 코드

OTel 기반 계측으로 백엔드 선택 유연성을 유지하는 접근법:

```python
# OTLP Exporter 설정
# Langfuse: OTLP endpoint 지원
# LangSmith: OTel 기반 tracing 지원

# 주요 구성:
# 1) TracerProvider + BatchSpanProcessor
# 2) 비즈니스 로직(tool, LLM 호출)을 span으로 계측
# 3) attribute에 token/cost 정보 포함
# 4) 최상위 request span으로 전체 trace 통합
```

## 실전 팁

**1) 환경별 Sampling 전략**
- dev/staging: 100% trace
- prod: 에러/지연/고비용은 100%, 나머지는 샘플링

**2) 비용 추적은 자동 + 수동 혼합**
- LLM 비용: 토큰 usage 기반 자동 집계
- tool/retrieval: 수동 비용 제출 또는 span attribute

**3) 컨텍스트 전파 문제 우선 확인**
- 비동기, 백그라운드 큐, 멀티프로세스에서 trace 단절 주의

**4) 보관 및 과금 모델 정책 수립**
- LangSmith: 14일 vs 400일 보관 기간에 따라 가격 상이
- trace 수 제한으로 예산 관리

**5) GenAI semantic conventions 표준화**
- 속성 네이밍 표준 사전 정의 (예: `llm.model`, `tokens.input`, `cost.usd`)

## 마무리

2026년 기준으로 LangSmith와 Langfuse의 공통 방향은 "OTel을 중심으로 LLM Observability를 분산 시스템 관측의 영역으로 확대"하는 것입니다.

- **LangSmith**: 평가, 대시보드, 비용 집계를 제품 내 강하게 통합
- **Langfuse**: OTLP 수신 + OTEL-native SDK로 호환성과 오픈 생태계 강조

**다음 학습 추천**:
- OTel에서 context propagation (async, background job) 마스터하기
- 비용을 LLM 토큰 외 tool/retrieval까지 합산하는 데이터 모델 설계
- 프로덕션 sampling/PII 마스킹/retention 정책 수립

---
*원본 출처: [Daewook's Dev Log](https://daewooki.github.io/posts/llm-langsmith-vs-langfuse-2026-1-2/)*
