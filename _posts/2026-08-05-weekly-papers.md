---
layout: post
title: "[2026/06/08 ~ 14] 이번 주에 살펴볼 만한 AI/ML 논문 모음"
date: 2026-08-05
categories: [AI, Weekly Papers]
tags: [AI, 논문, weekly, arxiv]
weekly_topic_id: 30531
weekly_source: "GeekNews · ninebow"
---

> 큐레이션 출처: [GeekNews · ninebow — [2026/06/08 ~ 14] 이번 주에 살펴볼 만한 AI/ML 논문 모음](https://news.hada.io/topic?id=30531). 본문은 arXiv abstract 만 기반으로 한 본인 시각의 재정리.

## 이번 주 트렌드

_(트렌드 도입 생성 실패)_

---


## 1. Economy of Minds: Emerging Multi-Agent Intelligence with Economic Interactions

*Zhenting Qi, Huangyuan Su, Ao Qu 외 · `cs.CL` · 2026-06-01*

_(한국어 해설 생성 실패. 원문 abstract:)_

How can a population of agents self-orchestrate and self-adapt into stronger collective intelligence without centralized control? Inspired by Friedrich Hayek's economic theory of decentralized coordination in markets, we study this question through an agent economy in which agents compete via auctions for the right to act, exchange payments, and accumulate wealth from environmental rewards. These simple economic signals induce decentralized credit assignment, driving planning without global orchestration or explicit communication protocols. The population evolves through economic selection: effective agents accumulate wealth and are mutated via exploitation, while ineffective ones go bankrupt and are replaced via exploration. We show that, initialized with weak agents, the economy produces emergent multi-step reasoning strategies and outperforms stronger monolithic baselines across five agentic tasks, including mathematical reasoning, financial research, scientific research, accelerator design, and distributed-system optimization. We further provide theoretical insights into how economic dynamics shape agent behaviors, linking local incentives to long-term global performance. Our r

> **Abstract.** How can a population of agents self-orchestrate and self-adapt into stronger collective intelligence without centralized control? Inspired by Friedrich Hayek's economic theory of decentralized coordination in markets, we study this question through an agent economy in which agents compete via auctions for the right to act, exchange payments, and accumulate wealth from environmental rewards. These simple economic signals induce decentralized credit assignment, driving planning without global orchestration or explicit communication protocols. The population evolves through economic selection: ef…

🔗 [arXiv](https://arxiv.org/abs/2606.02859v1) · [PDF](https://arxiv.org/pdf/2606.02859v1)

---


## 2. AutoForge: Automated Environment Synthesis for Agentic Reinforcement Learning

*Shihao Cai, Runnan Fang, Jialong Wu 외 · `cs.CL` · 2025-12-28*

강화학습(RL)을 시뮬레이션 환경에서 수행하는 것은 언어 기반 에이전트를 비용 효율적으로 확장 가능한 방식으로 개선하는 수단이지만, 기존 연구는 환경 합성의 반자동성이나 과제 난이도 부족으로 폭과 깊이 모두 제한적이었다. 또한 시뮬레이션 사용자의 불안정성과 환경 간 이질성은 에이전트 RL을 더욱 어렵게 만든다. 이러한 문제를 해결하기 위해 본 논문은 자동화되고 확장 가능한 환경 합성 파이프라인과 환경 수준 RL 알고리즘을 제안한다. 우선 고난도이면서도 검증이 쉬운 과제를 갖춘 시뮬레이션 환경을 자동으로 합성하는 통합 파이프라인을 구성한다. 다음으로 환경 수준에서 이점 추정(advantage estimation)을 수행하는 RL 알고리즘을 도입하여 시뮬레이션 사용자 불안정성을 완화하고 훈련 효율과 안정성을 높인다. 기술적으로 핵심은 검증 가능성(verifiability)과 난이도를 동시에 만족하는 작업 생성과, 에이전트 개별 단계가 아닌 환경 단위로 이점을 추정해 학습 신호를 안정화하는 데 있다. tau-bench, tau2-Bench, VitaBench 등 에이전트 벤치마크 평가에서 제안 방법의 효과가 확인되었으며, 추가 분석을 통해 도메인 외 일반화(out-of-domain generalization) 성능도 입증되었다.

> **Abstract.** Conducting reinforcement learning (RL) in simulated environments offers a cost-effective and highly scalable way to enhance language-based agents. However, previous work has been limited to semi-automated environment synthesis or tasks lacking sufficient difficulty, offering little breadth or depth. In addition, the instability of simulated users integrated into these environments, along with the heterogeneity across simulated environments, poses further challenges for agentic RL. In this work, we propose: (1) a unified pipeline for automated and scalable synthesis of simulated environments as…

🔗 [arXiv](https://arxiv.org/abs/2512.22857v1) · [PDF](https://arxiv.org/pdf/2512.22857v1)

---


## 3. APEX: Automated Prompt Engineering eXpert with Dynamic Data Selection

*Fei Wang, Si Si, Cho-Jui Hsieh 외 · `cs.CL` · 2026-06-09*

대규모 언어모델(LLM)은 동일한 작업이라도 프롬프트 표현 방식에 따라 성능이 크게 달라지며, 따라서 수동 프롬프트 설계의 한계를 넘는 자동 최적화 기법이 필수적이다. 기존의 진화 알고리즘(evolutionary algorithm) 기반 자동 프롬프트 최적화는 지배적인 패러다임이지만 개발 데이터셋을 정적 벤치마크처럼 고정한 채 사용한다는 점에서 치명적인 데이터 효율성 병목을 갖는다. 즉, 많은 평가 호출이 모델을 개선하는 데 별 도움이 되지 않는 무정보(uninformative) 데이터에 낭비된다. 이 문제를 해결하기 위해 본 논문은 APEX(Automated Prompt Engineering eXpert)를 제안한다. APEX는 프롬프트 탐색과 데이터 사용을 동시에 최적화하는 프레임워크로, 최적화가 진행된 계보(optimization lineage)를 추적해 데이터셋을 Easy, Hard, Mixed의 세 계층으로 동적으로 층화한다. 이 중 LLM의 성능이 데이터에 따라 엇갈리는 Mixed 계층에 우선순위를 두며, 그 안에서 유익한 변이(mutation)를 생성하는 데 적합한 addressable frontier와 후보 프롬프트의 품질을 더 잘 구분해 주는 rank-sensitive frontier라는 두 가지 고효율 하위집합을 찾아낸다. 이렇게 선별된 데이터를 중심으로 프롬프트 변이와 평가를 수행함으로써 동일한 예산에서 더 나은 프롬프트를 탐색한다. APEX는 IFBench, SimpleQA Verified, FACTS Grounding 세 벤치마크에서 고정 예산 5,000회의 평가 호출만으로 평가되었으며, 초기 프롬프트 대비 Gemini 2.5 Flash에서 평균 11.2%, Gemma 3 27B에서 평균 6.8%의 성능 향상을 달성했다. 이는 프롬프트 최적화의 효율성을 높이는 데 있어 탐색 알고리즘 자체보다 데이터 선택 방식이 핵심 열쇠임을 시사한다.

> **Abstract.** Large Language Models are highly sensitive to prompt formulation, necessitating automatic prompt optimization to unlock their full potential. While evolutionary algorithms have emerged as the dominant paradigm, they suffer from a critical bottleneck: data efficiency. Current methods treat the development dataset as a static benchmark, wasting significant compute budget on uninformative data. In this work, we introduce APEX (Automatic Prompt Engineering eXpert), a novel framework that optimizes the data usage alongside the prompt search. APEX dynamically stratifies the dataset into Easy, Hard, …

🔗 [arXiv](https://arxiv.org/abs/2606.11459v1) · [PDF](https://arxiv.org/pdf/2606.11459v1)

---


## 4. Self-Harness: Harnesses That Improve Themselves

*Hangfan Zhang, Shao Zhang, Kangcong Li 외 · `cs.CL` · 2026-06-08*

LLM 기반 에이전트의 성능은 기반 모델과 환경 사이를 중개하는 하네스(harness)에 의해 함께 결정되는데, 모델마다 행동 특성이 달라 효과적인 하네스 설계는 본질적으로 모델별로 달라야 한다. 그러나 현재 하네스는 대부분 인간 전문가가 수작업으로 설계하기 때문에, LLM이 다양해지고 빠르게 진화할수록 확장에 한계가 있다. 본 논문은 Self-Harness라는 새로운 패러다임을 제안한다. 에이전트가 인간 엔지니어나 더 강한 외부 에이전트의 도움 없이 자기 자신의 하네스를 스스로 개선하게 만든다는 것이 핵심이다. 이를 위해 Self-Harness는 반복 루프를 사용한다. 먼저 실행 궤적(execution trace)에서 모델 특유의 실패 패턴을 찾는 Weakness Mining, 그 실패와 연결된 다양하면서도 최소한의 하네스 수정안을 생성하는 Harness Proposal, 회귀 테스트(regression testing)를 통과한 후보만 채택하는 Proposal Validation의 세 단계로 구성된다. 실험은 Terminal-Bench-2.0에서 최소 초기 하네스와 MiniMax M2.5, Qwen3.5-35B-A3B, GLM-5 등 서로 다른 계열의 세 기반 모델로 수행했다. 그 결과 모든 모델에서 성능이 일관되게 향상되었으며, hold-out 통과율은 각각 40.5%에서 61.9%, 23.8%에서 38.1%, 42.9%에서 57.1%로 상승했다. 정성 분석에 따르면 Self-Harness는 단순히 일반적인 지시문을 추가하는 데 그치지 않고, 모델 고유의 약점을 구체적이고 실행 가능한 하네스 변경으로 변환한다. 이는 에이전트가 하네스에 수동적으로 영향받을 뿐 아니라, 하네스를 재형성하는 데 스스로 참여할 수 있는 가능성을 보여준다.

> **Abstract.** The performance of LLM-based agents is jointly shaped by their base models and the harnesses that mediate their interaction with the environment. Because different models exhibit distinct behaviors, effective harness design is inherently model-specific. Yet agent harnesses are still largely engineered by human experts, a paradigm that scales poorly as modern LLMs become increasingly diverse and rapidly evolving. In this paper, we introduce Self-Harness, a new paradigm in which an LLM-based agent improves its own operating harness, without relying on human engineers or stronger external agents.…

🔗 [arXiv](https://arxiv.org/abs/2606.09498v1) · [PDF](https://arxiv.org/pdf/2606.09498v1)

---


## 5. Can LLMs Beat Classical Hyperparameter Optimization Algorithms? A Study on autoresearch

*Fabio Ferreira, Lucca Wobbe, Arjun Krishnakumar 외 · `cs.LG` · 2026-03-25*

_(한국어 해설 생성 실패. 원문 abstract:)_

The autoresearch repository enables an LLM agent to optimize hyperparameters by editing training code directly. We use it as a testbed to compare classical HPO algorithms against LLM-based methods on tuning the hyperparameters of a small language model under a fixed compute budget. When defining a fixed search space over autoresearch, classical methods such as CMA-ES and TPE consistently outperform LLM-based agents, where avoiding out-of-memory failures matters more than search diversity. Allowing the LLM to directly edit source code narrows the gap to the classical methods but does not close it, even with frontier models available at the time of writing such as Claude Opus 4.6 and Gemini 3.1 Pro Preview. We observe that LLMs struggle to track optimization state across trials. In contrast, classical methods lack the domain knowledge of LLMs. To combine the strengths of both, we introduce Centaur, a hybrid that shares CMA-ES's interpretable internal state, including mean vector, step-size, and covariance matrix, with an LLM. Centaur achieves the best result in our experiments, and a 0.8B LLM already suffices to outperform all classical and pure LLM methods. Unconstrained code editin

> **Abstract.** The autoresearch repository enables an LLM agent to optimize hyperparameters by editing training code directly. We use it as a testbed to compare classical HPO algorithms against LLM-based methods on tuning the hyperparameters of a small language model under a fixed compute budget. When defining a fixed search space over autoresearch, classical methods such as CMA-ES and TPE consistently outperform LLM-based agents, where avoiding out-of-memory failures matters more than search diversity. Allowing the LLM to directly edit source code narrows the gap to the classical methods but does not close …

🔗 [arXiv](https://arxiv.org/abs/2603.24647v5) · [PDF](https://arxiv.org/pdf/2603.24647v5) · [Code](https://github.com/ferreirafabio/autoresearch-automl)

---


## 6. FP8 is All You Need (Part 1): Debunking Hardware FP64 as the HPC Holy Grail (June 13th version)

*Satoshi Matsuoka · `cs.AR` · 2026-05-28*

기존 HPC 커뮤니티는 네이티브 FP64 하드웨어가 과학 계산의 불가침한 기반이라고 간주해 왔다. 그러나 NVIDIA B300 세대 이후 AI 최적화 GPU에서는 네이티브 FP64 처리량이 약 1.3 TFLOPS로 붕괴된 반면, FP8 텐서 처리량은 수 PFLOPS 수준으로 성장했다. 저자는 이러한 상황이 단순히 견딜 만한 것이 아니라, FP8 텐서코어 행렬 곱셈이 배정밀도 과학 계산을 구축해야 할 유일한 계산 프리미티브(computational primitive)라고 더 강하게 주장한다. 핵심 아이디어는 중국인의 나머지 정리(CRT)에 기반한 Ozaki Scheme II를 통해 밀집·희소 선형대수, 스펙트럼 변환, 스텐실(stencil) 같은 모든 표준 커널이 FP8 행렬 연산들의 열로 환원된다는 것이다. 재구성 단계에서 필요한 유일한 비-FP8 연산은 범위가 제한된 고정 너비(fixed-width) 정수 누적뿐이며, 따라서 FP64는 하드웨어 요구사항이 아닌 FP8 프리미티브의 합성으로 얻어지는 파생적 정밀도 보증으로 격하된다. 이 논문은 주장을 FP8 연산, Ozaki II, Berkeley 드워프(dwarfs) 커널, 복합 솔버, 전체 애플리케이션으로 이어지는 5계층 구조로 조직하고, 드워프 분류가 과학 계산 전체를 이미 포괄한다는 점을 이용해 표본이 아닌 모든 드워프에 대한 환원을 제시한다. 또한 이 주장을 시험할 도구로 Roofline 모델을 확장한 TME(Tensor-Memory Equilibrium) 모델을 구축하고, 에뮬레이션 파라미터(alpha, beta, gamma)를 도입했으며, 레지스터 수준 융합(register-level fusion)이 에뮬레이션을 메모리 바운드로 유지하게 하는 메커니즘임

> **Abstract.** Conventional HPC holds that native hardware FP64 is the irreducible foundation of scientific computing. On AI-optimized GPUs of the NVIDIA B300 generation and beyond, native FP64 throughput has collapsed to ~1.3 TFLOPS even as FP8 tensor throughput has grown to multiple PFLOPS. We argue something stronger than that this is survivable: the FP8 tensor-core matrix-multiply is the sole computational primitive on which double-precision scientific computing needs to be built. Every canonical kernel -- dense and sparse linear algebra, spectral transforms, stencils -- and every application composing t…

🔗 [arXiv](https://arxiv.org/abs/2606.06510v3) · [PDF](https://arxiv.org/pdf/2606.06510v3)

---


## 7. On the limits and opportunities of AI reviewers: Reviewing the reviews of Nature-family papers with 45 expert scientists

*Seungone Kim, Dongkeun Yoon, Kiril Gashteovski 외 · `cs.CL` · 2026-05-20*

_(한국어 해설 생성 실패. 원문 abstract:)_

With the advancement of AI capabilities, AI reviewers are beginning to be deployed in scientific peer review, yet their capability and credibility remain in question: many scientists simply view them as probabilistic systems without the expertise to evaluate research, while other researchers are more optimistic about their readiness without concrete evidence. Understanding what AI reviewers do well, where they fall short, and what challenges remain is essential. However, existing evaluations of AI reviewers have focused on whether their verdicts match human verdicts (e.g., score alignment, acceptance prediction), which is insufficient to characterize their capabilities and limits. In this paper, we close this gap through a large-scale expert annotation study, in which 45 domain scientists in Physical, Biological, and Health Sciences spent 469 hours rating 2,960 individual criticisms (each targeting one specific aspect of a paper) from human-written and AI-generated reviews of 82 Nature-family papers on correctness, significance, and sufficiency of evidence. On a composite of all three dimensions, a reviewing agent powered by GPT-5.2 scores above each paper's top-rated human reviewe

> **Abstract.** With the advancement of AI capabilities, AI reviewers are beginning to be deployed in scientific peer review, yet their capability and credibility remain in question: many scientists simply view them as probabilistic systems without the expertise to evaluate research, while other researchers are more optimistic about their readiness without concrete evidence. Understanding what AI reviewers do well, where they fall short, and what challenges remain is essential. However, existing evaluations of AI reviewers have focused on whether their verdicts match human verdicts (e.g., score alignment, acc…

🔗 [arXiv](https://arxiv.org/abs/2605.20668v1) · [PDF](https://arxiv.org/pdf/2605.20668v1)

---


## 8. LiveBrowseComp: Are Search Agents Searching, or Just Verifying What They Already Know?

*HuiMing Fan, Xiao Wang, Zheng Chu 외 · `cs.AI` · 2026-05-27*

LLM 기반 검색 에이전트가 실제로 외부 정보를 찾는지, 아니면 모델이 이미 알고 있는 지식을 검증하는 데 그치는지에 대한 의문이 제기된다. 저자들은 BrowseComp 데이터셋에 세 가지 진단 기법을 적용해 분석했으며, 그 결과 도구 접근 권한이 있어도 에이전트가 검색 이전에 모델에 부호화된 내재 지식(intrinsic knowledge)에 의존하는 경향, 즉 내재 지식 의존성(IKD)을 확인했다. 구체적으로 에이전트는 도구 없이도 BrowseComp 질문의 최대 44.5%를 답할 수 있었고, 검색 쿼리의 절반 이상이 검색에서 얻은 단서가 아니라 내부적으로 생성한 가설에서 비롯되었다. 또한 답을 뒷받침하는 증거를 제거했을 때 오히려 폐쇄형 기준선보다 낮은 성능을 보였다. 이는 정적 검색 벤치마크가 증거 기반 발견보다는 기억 기반 검증을 보상할 수 있음을 시사한다. 이러한 한계를 극복하기 위해 저자들은 LiveBrowseComp라는 딥서치 벤치마크를 제안한다. LiveBrowseComp는 벤치마크 구축 90일 이내에 발표된 사실에 의존하는 335개의 인간 작성 질문으로 구성되며, 여섯 개의 업데이트 소스에서 추출하고 전 세계적으로 유명한 사건은 제외했다. 실험 결과 모든 평가 대상 에이전트의 폐쇄형 정확도는 2% 미만이었고, 검색 증강 점수는 BrowseComp 대비 25~40점 하락했으며, 기존 모델 순위가 성능을 더 이상 예측하지 못했다. 즉 LiveBrowseComp는 에이전트의 실제 탐색 능력을 평가하는 데 더 적합한 기준을 제공한다.

> **Abstract.** Are LLM-based search agents genuinely searching, or using the web to verify what they already know? We study this question on BrowseComp with three diagnostics. Our analysis reveals Intrinsic Knowledge Dependence (IKD): even with tool access, agents often rely on intrinsic knowledge -- information encoded in the model before retrieval -- rather than on external evidence. Agents answer up to 44.5% of BrowseComp questions without tools, generate more than half of their search queries from internally produced hypotheses rather than retrieved leads, and perform worse than closed-book baselines whe…

🔗 [arXiv](https://arxiv.org/abs/2605.28721v1) · [PDF](https://arxiv.org/pdf/2605.28721v1)

---


## 9. Information bottleneck for learning the phase space of dynamics from high-dimensional experimental data

*K. Michael Martini, Eslam Abdelaleem, Paarth Gulati 외 · `physics.data-an` · 2026-04-27*

고차원 관측 데이터로부터 시스템의 동역학적 상태 변수를 찾는 것은 물리 과학 전반의 핵심 문제다. 상태 변수는 직접 관측되지 않으며, 라벨 없는 원시 고차원 데이터에서 비지도 방식으로 추론해야 한다는 점이 어려움이다. 본 논문은 이러한 문제를 해결하기 위해 DySIB(Dynamical Symmetric Information Bottleneck)를 제안한다. DySIB는 시계열 데이터의 과거와 미래 관측 창 사이의 예측적 상호정보(predictive mutual information)를 최대화하면서 표현 복잡도에 페널티를 주는 방식으로 저차원 표현을 학습한다. 이 목적 함수는 전적으로 잠재 공간(latent space)에서 작동하며 관측값의 재구성(reconstruction)을 요구하지 않는다. 기술적으로 가장 두드러진 결정은 정보 병목(information bottleneck)의 대칭적 활용과, 학습 아키텍처의 하이퍼파라미터를 데이터가 스스로 결정하도록 설정했다는 점이다. 저자들은 상태 공간이 알려진 실험용 진자(physical pendulum) 비디오 데이터에 DySIB를 적용했다. 그 결과 방법은 진자 위상 공간(phase space)의 차원, 위상, 기하와 일치하는 2차원 표현을 복구했으며, 학습된 좌표는 표준 각도와 각속도에 매끄럽게 정렬되었다. 이는 잘 특성화된 실험 시스템에서 잠재 공간의 예측적 정보만으로 고차원 데이터로부터 해석 가능한 동역학적 좌표를 복원할 수 있음을 보여준다.

> **Abstract.** Identifying the dynamical state variables of a system from high-dimensional observations is a central problem across physical sciences. The challenge is that the state variables are not directly observable and must be inferred from raw high-dimensional data without supervision. Here we introduce DySIB (Dynamical Symmetric Information Bottleneck) as a method to learn low-dimensional representations of time-series data by maximizing predictive mutual information between past and future observation windows while penalizing representation complexity. This objective operates entirely in latent spac…

🔗 [arXiv](https://arxiv.org/abs/2604.24662v2) · [PDF](https://arxiv.org/pdf/2604.24662v2)

---


## 10. AutoScientists: Self-Organizing Agent Teams for Long-Running Scientific Experimentation

*Shanghua Gao, Ada Fang, Marinka Zitnik · `cs.AI` · 2026-05-27*

과학 연구는 가설 생성, 실험 설계, 수행, 수정의 반복적 순환을 통해 진행되는데, 기존 AI 에이전트는 단일 연구 궤적만 따라가거나 고정된 목표를 가진 중앙 계획자에 의존하는 경우가 많아 병렬 탐색을 지속하고 실험 증거 변화에 적응하며 장기 실험에서 실패한 방향의 지식을 보존하기 어렵다는 한계가 있다. 본 논문은 이 문제를 해결하기 위해 AutoScientists를 제안한다. AutoScientists는 분산형(decentralized) AI 에이전트 팀으로, 에이전트들이 공유된 실험 상태(shared experimental state)를 해석하고 유망한 가설 주변에서 스스로 팀을 구성(self-organize)하며, 실험 계산 비용을 쓰기 전에 제안을 비판적으로 검토한다. 또한 성공과 실패 정보를 공유해 중복 탐색을 줄이는 방식으로 장기 계산 과학 실험을 수행한다. 기술적 핵심은 고정된 중앙 계획자 없이 에이전트들이 실험 상태를 기준으로 동적으로 팀을 재구성하고, 제안 단계에서 비판(critique) 과정을 도입해 낭비되는 실험 비용을 사전에 줄인 점이다. 성공과 실패의 공유는 실패한 방향을 조직적으로 기억하게 하여 같은 경로를 반복 탐색하지 않도록 돕는다. 실험 결과, 동일한 예산 조건에서 BioML-Bench의 24개 작업에 대해 평균 리더보드 백분위 74.4%를 달성해 기존 최강 AI 에이전트보다 +8.33% 개선했다. GPT 훈련 최적화에서는 목표 검증 bits-per-byte에 Autoresearch보다 1.9배 빠르게 도달했고, 단일 에이전트는 개선을 하나도 찾지 못하는 상황에서도 7개의 수용된 개선을 발견했다. ProteinGym 적합성 예측에서는 ACE2-Spike 결합에 대해 기존 최고 모델 대비 Spearman 상관계수 +12.5% 향상된 방법을 발견했으며, 수정 없이 217개 전체 분석에 적용했을 때도 기존 최고 대비 +6.5% 개선을 보였다. 본 논문은 장기 과학 실험에서 자율적 팀 조직과 지식 공유가 탐색 효율과 발견 성능을 동시에 높일 수 있음을 보여준다.

> **Abstract.** Scientific research proceeds through iterative cycles of hypothesis generation, experiment design, execution, and revision. AI agents can automate parts of this process, but existing approaches typically follow a single research trajectory or coordinate through a central planner with fixed objectives. As a result, they struggle to sustain parallel exploration, adapt as experimental evidence changes, or preserve knowledge of failed directions over long-running experiments. We introduce AutoScientists, a decentralized team of AI agents for long-running computational scientific experimentation. A…

🔗 [arXiv](https://arxiv.org/abs/2605.28655v1) · [PDF](https://arxiv.org/pdf/2605.28655v1)

---



### 출처

이번 주 논문 10편의 선정은 [GeekNews 의 주간 AI/ML 논문 모음](https://news.hada.io/topic?id=30531) (큐레이터: ninebow) 의 큐레이션을 따랐고, 본문 해설은 각 논문 arXiv abstract 만을 근거로 본인 시각에서 재정리한 것입니다. 원문 큐레이터의 깊이 있는 코멘트는 원본 GeekNews 글을 참고해 주세요.