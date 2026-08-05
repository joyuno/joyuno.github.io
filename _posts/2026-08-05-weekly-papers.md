---
layout: post
title: "이번 주에 살펴볼 만한 AI/ML 논문 모음 (2026-08-05)"
date: 2026-08-05
categories: [AI, Weekly Papers]
tags: [AI, 논문, weekly, arxiv]
weekly_topic_id: 30531
weekly_source: "GeekNews · ninebow"
---

> 큐레이션 출처: [GeekNews · ninebow — [2026/06/08 ~ 14] ì´ë² ì£¼ì ì´í´ë³¼ ë§í AI/ML ë¼ë¬¸ ëª¨ì](https://news.hada.io/topic?id=30531). 본문은 arXiv abstract 만 기반으로 한 본인 시각의 재정리.

## 이번 주 트렌드

이번 주 큐레이션은 에이전트 자기조직화, 최적화 데이터 효율성, 과학·검증 확장이라는 세 축으로 정리된다.

**에이전트 자기조직화** — 다중에이전트 경제 상호작용으로 중앙 제어 없이 집단지성을 만드는 연구부터, 에이전트가 자신의 장치(harness)를 스스로 개선하는 Self-Harness, 장기 실험을 병렬로 수행하는 AutoScientists까지, 시스템 스스로 구조를 진화시키는 흐름이 두드러진다.

**최적화의 자동화와 데이터 효율성** — AutoForge는 에이전트 강화학습용 환경 합성을 자동화하고, APEX는 프롬프트 탐색 과정에서 데이터를 동적으로 선별해 연산 낭비를 줄인다. 또 언어모델 기반 하이퍼파라미터 최적화가 고전 알고리즘을 넘지 못한다는 연구는 자동 탐색의 한계와 개선 방향을 함께 보여준다.

**과학·검증 영역으로의 확장과 한계** — FP8 텐서 연산을 과학 컴퓨팅의 기반으로 제시하는 시도, 고차원 시계열에서 동역학 위상공간을 배우는 정보병목 모델, AI 리뷰어의 실제 역량 검증, 검색 에이전트가 외부 증거보다 내재 지식에 의존하는 문제 등은 과학 발전에 AI를 적용할 때의 기회와 경계를 동시에 드러낸다.

이처럼 이번 주 연구들은 에이전트의 자율성과 효율성을 높이는 동시에, 적용 범위를 과학적 발견과 신뢰 평가로 넓히는 중간 단계를 보여준다.

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

시뮬레이션 환경에서 강화학습(RL)을 수행하는 것은 언어 기반 에이전트를 비용 효율적으로 확장 가능한 방식으로 향상시키는 방법이지만, 기존 연구는 반자동 환경 합성에 머물거나 과제 난이도가 충분하지 않아 폭과 깊이 모두 제한적이었다. 또한 환경에 통합된 시뮬레이션 사용자의 불안정성과 서로 다른 시뮬레이션 환경 간 이질성은 에이전트 강화학습에 추가적인 장애물로 작용해 왔다. 본 논문은 이러한 문제를 해결하기 위해 자동화되고 확장 가능한 환경 합성 파이프라인과 환경 수준 강화학습 알고리즘을 제안한다. 첫 번째 구성 요소는 높은 난이도이면서도 검증이 쉬운 과제를 포함한 시뮬레이션 환경을 자동으로 대량 생성하는 통합 파이프라인으로, 기존의 수동 개입을 줄이고 다양한 환경을 효율적으로 확보하게 한다. 두 번째 구성 요소는 환경 수준에서 어드밴티지 추정(advantage estimation)을 수행하면서 사용자 불안정성을 효과적으로 완화하는 강화학습 알고리즘으로, 이를 통해 훈련 효율성과 안정성을 동시에 개선한다. 기술적으로 핵심은 불안정한 시뮬레이션 사용자를 개별 보상의 잡음으로 처리하지 않고 환경 전체의 특성으로 모델링하는 점과, 에피소드나 스텝 단위가 아닌 환경 단위로 어드밴티지를 추정하여 이질적인 환경 간 비교를 가능하게 한 데 있다. 이로써 에이전트는 특정 환경에 과적합되기보다 환경 분포 전반에서 일반화된 정책을 학습할 수 있다. 논문은 tau-bench, tau2-Bench, VitaBench와 같은 에이전트 벤치마크에서 제안 방법을 종합적으로 평가하여 유효성을 입증했으며, 추가 분석을 통해 분포 외 일반화(out-of-domain generalization) 성능이 두드러짐을 강조한다. 본 연구는 시뮬레이션 환경의 자동 합성과 환경 수준 학습이라는 두 축에서 에이전트 강화학습의 확장성과 견고성을 동시에 끌어올렸다는 의의를 지닌다.

> **Abstract.** Conducting reinforcement learning (RL) in simulated environments offers a cost-effective and highly scalable way to enhance language-based agents. However, previous work has been limited to semi-automated environment synthesis or tasks lacking sufficient difficulty, offering little breadth or depth. In addition, the instability of simulated users integrated into these environments, along with the heterogeneity across simulated environments, poses further challenges for agentic RL. In this work, we propose: (1) a unified pipeline for automated and scalable synthesis of simulated environments as…

🔗 [arXiv](https://arxiv.org/abs/2512.22857v1) · [PDF](https://arxiv.org/pdf/2512.22857v1)

---


## 3. APEX: Automated Prompt Engineering eXpert with Dynamic Data Selection

*Fei Wang, Si Si, Cho-Jui Hsieh 외 · `cs.CL` · 2026-06-09*

대규모 언어모델(LLM)은 프롬프트 구성에 매우 민감하므로 자동 프롬프트 최적화가 중요하다. 기존 진화 알고리즘 기반 기법들은 개발 데이터셋을 정적 벤치마크로 삼아 유의미하지 않은 데이터에 계산 예산을 낭비하는 데이터 효율성 병목을 겪는다. 본 논문은 프롬프트 탐색과 데이터 사용을 함께 최적화하는 APEX(Automatic Prompt Engineering eXpert) 프레임워크를 제안한다. APEX는 최적화 과정에서 얻은 이력(optimization lineage)을 바탕으로 데이터셋을 쉬움(Easy), 어려움(Hard), 혼합(Mixed) 계층으로 동적 분류하고, LLM의 성능이 혼재된 Mixed 계층에 우선순위를 둔다. 이 계층에서 유용한 변이(mutation)를 생성하는 addressable frontier와 후보 품질을 구분하는 rank-sensitive frontier라는 두 가지 고레버리지 부분집합을 식별한다. 즉 단순히 어렵거나 쉬운 데이터가 아니라 모델이 비일관적인 성능을 보이는 데이터를 집중적으로 활용함으로써 적은 평가 호출로도 효과적인 프롬프트 개선을 도모한다. APEX는 IFBench, SimpleQA Verified, FACTS Grounding 세 벤치마크에서 5,000회 평가 호출이라는 고정 예산 하에 평가되었으며, Gemini 2.5 Flash에서 초기 프롬프트 대비 평균 11.2%, Gemma 3 27B에서 6.8% 성능 향상을 달성했다. 이는 프롬프트 최적화에서 데이터 선택이 핵심 효율 요인임을 보여주며, 데이터 중심 접근이 진화 알고리즘의 계산 부담을 줄이는 데 효과적임을 시사한다.

> **Abstract.** Large Language Models are highly sensitive to prompt formulation, necessitating automatic prompt optimization to unlock their full potential. While evolutionary algorithms have emerged as the dominant paradigm, they suffer from a critical bottleneck: data efficiency. Current methods treat the development dataset as a static benchmark, wasting significant compute budget on uninformative data. In this work, we introduce APEX (Automatic Prompt Engineering eXpert), a novel framework that optimizes the data usage alongside the prompt search. APEX dynamically stratifies the dataset into Easy, Hard, …

🔗 [arXiv](https://arxiv.org/abs/2606.11459v1) · [PDF](https://arxiv.org/pdf/2606.11459v1)

---


## 4. Self-Harness: Harnesses That Improve Themselves

*Hangfan Zhang, Shao Zhang, Kangcong Li 외 · `cs.CL` · 2026-06-08*

LLM 기반 에이전트의 성능은 기반 모델과 환경 사이를 중개하는 하네스(harness) 설계에 함께 좌우된다. 그런데 모델마다 행동 특성이 달라 효과적인 하네스는 본질적으로 모델별로 다르게 설계되어야 하지만, 현재는 인간 전문가가 수작업으로 설계하는 경우가 많아 모델이 다양해지고 빠르게 진화하는 환경에서 확장성이 떨어진다는 문제가 있다. 이에 본 논문은 Self-Harness라는 새로운 패러다임을 제안한다. 이는 에이전트가 인간 엔지니어나 더 강한 외부 에이전트에 의존하지 않고 자신의 작동 하네스를 스스로 개선하는 방식이다. 구체적으로 Self-Harness는 약점 발견(Weakness Mining), 하네스 제안(Harness Proposal), 제안 검증(Proposal Validation)의 세 단계로 구성된 반복 루프로 동작한다. 먼저 실행 추적(trace)에서 모델 특유의 실패 패턴을 식별하고, 그 실패와 연결된 다양하면서도 최소한의 하네스 수정안을 생성한 뒤, 회귀 테스트(regression testing)를 통과한 후보만 채택한다. 기술적 핵심은 일반적인 지시문을 추가하는 데 그치지 않고, 모델별 약점을 구체적이고 실행 가능한 하네스 변경으로 변환한다는 점이다. 저자들은 Terminal-Bench-2.0에서 최소 초기 하네스와 서로 다른 계열의 모델인 MiniMax M2.5, Qwen3.5-35B-A3B, GLM-5를 사용해 실험했고, held-out 통과율이 각각 40.5%에서 61.9%, 23.8%에서 38.1%, 42.9%에서 57.1%로 향상되었다. 이러한 결과는 하네스에 의해 수동적으로 형성되던 에이전트가 스스로 하네스 개선에 참여할 수 있음을 보여주며, LLM 기반 에이전트의 자기 개선 연구에 중요한 시사점을 남긴다.

> **Abstract.** The performance of LLM-based agents is jointly shaped by their base models and the harnesses that mediate their interaction with the environment. Because different models exhibit distinct behaviors, effective harness design is inherently model-specific. Yet agent harnesses are still largely engineered by human experts, a paradigm that scales poorly as modern LLMs become increasingly diverse and rapidly evolving. In this paper, we introduce Self-Harness, a new paradigm in which an LLM-based agent improves its own operating harness, without relying on human engineers or stronger external agents.…

🔗 [arXiv](https://arxiv.org/abs/2606.09498v1) · [PDF](https://arxiv.org/pdf/2606.09498v1)

---


## 5. Can LLMs Beat Classical Hyperparameter Optimization Algorithms? A Study on autoresearch

*Fabio Ferreira, Lucca Wobbe, Arjun Krishnakumar 외 · `cs.LG` · 2026-03-25*

본 논문은 autoresearch 저장소를 테스트베드로 삼아, 고정된 계산 예산 아래에서 작은 언어 모델의 하이퍼파라미터를 튜닝할 때 고전적 HPO 알고리즘과 LLM 기반 방법을 비교한다. autoresearch는 LLM 에이전트가 학습 코드를 직접 수정하여 하이퍼파라미터를 최적화하게 해주는 도구이며, 실험에서 검색 공간을 고정했을 때 CMA-ES와 TPE 같은 고전 방법이 LLM 기반 에이전트보다 일관되게 우수했다. 여기서 핵심은 검색 다양성보다 out-of-memory 실패를 피하는 것이 더 중요하다는 점이다. LLM이 소스 코드를 직접 편집하도록 허용하면 고전 방법과의 격차가 좁혀지지만, 작성 시점 기준 최신 모델인 Claude Opus 4.6과 Gemini 3.1 Pro Preview를 사용해도 완전히 따라잡지는 못했다. 저자들은 LLM이 시행 간 최적화 상태를 추적하는 데 어려움을 겪는 반면, 고전 방법은 LLM이 가진 도메인 지식이 없다고 분석한다. 두 접근의 장점을 결합하기 위해 Centaur를 제안한다. Centaur는 CMA-ES의 해석 가능한 내부 상태, 즉 평균 벡터, 스텝 크기, 공분산 행렬을 LLM과 공유하는 하이브리드다. 실험에서 Centaur가 가장 좋은 성능을 냈으며, 0.8B 규모의 LLM만으로도 모든 고전 방법과 순수 LLM 방법을 능가했다. 반면 제약 없는 코드 편집에서는 더 큰 모델이 필요했다. 저자는 검색 다양성, 0.8B에서 최신 모델까지의 스케일링, Centaur에서 LLM이 제안하는 시행 비율에 대한 분석도 제공한다. 종합하면 LLM은 고전 최적화기를 대체하기보다 보완할 때 가장 효과적이라는 시사점을 준다.

> **Abstract.** The autoresearch repository enables an LLM agent to optimize hyperparameters by editing training code directly. We use it as a testbed to compare classical HPO algorithms against LLM-based methods on tuning the hyperparameters of a small language model under a fixed compute budget. When defining a fixed search space over autoresearch, classical methods such as CMA-ES and TPE consistently outperform LLM-based agents, where avoiding out-of-memory failures matters more than search diversity. Allowing the LLM to directly edit source code narrows the gap to the classical methods but does not close …

🔗 [arXiv](https://arxiv.org/abs/2603.24647v5) · [PDF](https://arxiv.org/pdf/2603.24647v5) · [Code](https://github.com/ferreirafabio/autoresearch-automl)

---


## 6. FP8 is All You Need (Part 1): Debunking Hardware FP64 as the HPC Holy Grail (June 13th version)

*Satoshi Matsuoka · `cs.AR` · 2026-05-28*

전통적 HPC에서는 네이티브 FP64가 과학계산의 불가침 기반으로 간주된다. 그러나 NVIDIA B300 세대 이후 AI 최적화 GPU에서 FP64 처리량은 약 1.3 TFLOPS로 붕괴한 반면 FP8 텐서 처리량은 수 PFLOPS로 성장했다. 본 논문은 이 상황을 견딜 수 있다는 차원을 넘어, FP8 텐서코어 행렬곱이 배정밀도 과학계산의 유일한 계산 프리미티브가 되어야 한다고 주장한다. 핵심 아이디어는 중국인 나머지 정리(CRT) 기반 Ozaki Scheme II를 사용해 조밀/희소 선형대수, 스펙트럼 변환, 스텐실 등 모든 표준 커널과 이를 조합한 애플리케이션을 FP8 행렬 연산 시퀀스로 환원하는 것이다. 재구성에 필요한 비FP8 연산은 제한된 고정폭 정수 누적뿐이며, 이로써 FP64는 하드웨어 요구사항이 아니라 FP8 위에서 합성으로 얻어지는 파생적 정밀도 보증으로 격하된다. 저자는 주장을 FP8 op, Ozaki II, Berkeley dwarfs, 복합 솔버, 전체 애플리케이션의 다섯 계층으로 조직하고, dwarf 분류가 과학계산 전반을 포괄하므로 표본이 아닌 모든 dwarf에 대한 환원을 제시한다. 반증 가능성을 위해 Roofline을 확장한 TME(Tensor-Memory Equilibrium) 모델과 에뮬레이션 파라미터 alpha, beta, gamma를 도입하고, 레지스터 수준 융합을 메모리 한계 요인으로 식별한다. B300과 Rubin에서 회복된 FP64 성능을 H100 기준선과 대비해 투영하고, 동반 FFT 분석과 보상된 감소(compensated reductions)로 커널 커버리지를 완성한다. 모델은 부정적 결과를 내놓을 수 있었지만 모든 dwarf와 그 조합에서 통과했다. 이는 2부작 프로그램 중 분석적 절반이며, 후속 구현이 실제 실리

> **Abstract.** Conventional HPC holds that native hardware FP64 is the irreducible foundation of scientific computing. On AI-optimized GPUs of the NVIDIA B300 generation and beyond, native FP64 throughput has collapsed to ~1.3 TFLOPS even as FP8 tensor throughput has grown to multiple PFLOPS. We argue something stronger than that this is survivable: the FP8 tensor-core matrix-multiply is the sole computational primitive on which double-precision scientific computing needs to be built. Every canonical kernel -- dense and sparse linear algebra, spectral transforms, stencils -- and every application composing t…

🔗 [arXiv](https://arxiv.org/abs/2606.06510v3) · [PDF](https://arxiv.org/pdf/2606.06510v3)

---


## 7. On the limits and opportunities of AI reviewers: Reviewing the reviews of Nature-family papers with 45 expert scientists

*Seungone Kim, Dongkeun Yoon, Kiril Gashteovski 외 · `cs.CL` · 2026-05-20*

과학 논문 심사에서 AI 리뷰어가 실제로 배치되기 시작했지만, 이들을 단순한 확률적 시스템으로 보는 회의적 시각과 충분한 근거 없이 낙관하는 시각이 공존하며 그 역량과 신뢰성에 대한 검증이 시급한 상황이다. 기존 평가 연구들은 AI 리뷰어의 판정이 인간과 일치하는지(점수 일치도, 수락 예측 등)에만 초점을 맞춰 실제 능력과 한계를 제대로 규명하지 못했다는 문제의식을 가진다. 이에 본 논문은 물리·생물·의학 분야 45명의 전문 과학자가 469시간에 걸쳐 Nature 계열 논문 82편에 대한 인간 리뷰와 AI 생성 리뷰에서 나온 2,960개의 개별 비평(criticism)을 정확성(correctness), 중요성(significance), 증거 충분성(sufficiency of evidence) 기준으로 평가한 대규모 전문가 주석 연구를 수행한다. 특히 단순 판정 일치 비교를 넘어 비평 단위로 분해해 평가했다는 점에서 차별화되며, GPT-5.2 기반 리뷰 에이전트는 종합 점수 60.0% 대 48.2%로 각 논문의 최고 평점 인간 리뷰어를 능가했고 세 AI 리뷰어 모두 모든 차원에서 최저 평점 인간보다 높은 성적을 기록했다. 또한 AI 리뷰어의 정확한 비평은 인간 비평보다 중요성과 증거 충분성에서 더 높은 평가를 받았으며, 인간이 제기하지 않는 26%의 고유 이슈를 발견하는 데 성공했다. 그러나 AI 리뷰어 간 비평 중복도는 21%로 인간 대비(3%) 훨씬 높아 다양성이 부족하고, 세부 분야 지식 부족, 여러 파일에 걸친 장기 컨텍스트 관리 어려움, 사소한 문제에 대한 과도하게 비판적 태도 등 인간과 공유하지 않는 16가지 반복적 취약점도 확인되었다. 종합적으로 저자들은 현재 AI 리뷰어가 인간 리뷰어를 대체하는 존재가 아니라 보완하는 도구임을 강조하며, 그 한계를 인식한 상태에서 활용될 필요가 있음을 시사한다.

> **Abstract.** With the advancement of AI capabilities, AI reviewers are beginning to be deployed in scientific peer review, yet their capability and credibility remain in question: many scientists simply view them as probabilistic systems without the expertise to evaluate research, while other researchers are more optimistic about their readiness without concrete evidence. Understanding what AI reviewers do well, where they fall short, and what challenges remain is essential. However, existing evaluations of AI reviewers have focused on whether their verdicts match human verdicts (e.g., score alignment, acc…

🔗 [arXiv](https://arxiv.org/abs/2605.20668v1) · [PDF](https://arxiv.org/pdf/2605.20668v1)

---


## 8. LiveBrowseComp: Are Search Agents Searching, or Just Verifying What They Already Know?

*HuiMing Fan, Xiao Wang, Zheng Chu 외 · `cs.AI` · 2026-05-27*

최근 LLM 기반 검색 에이전트(search agent)가 실제로 새로운 정보를 찾는지, 아니면 이미 알고 있는 내용을 웹 검색으로 확인하는지에 대한 의문이 제기된다. 본 논문은 BrowseComp 벤치마크에 세 가지 진단 방법을 적용해 이 문제를 분석한다. 그 결과 도구를 쓸 수 있어도 에이전트가 검색 전 모델에 이미 내재된 지식, 즉 내재적 지식 의존(Intrinsic Knowledge Dependence, IKD)에 크게 기대는 현상이 드러난다. 구체적으로 에이전트는 BrowseComp 질문의 최대 44.5%를 도구 없이도 답할 수 있었고, 생성하는 검색 질의의 절반 이상이 검색에서 얻은 단서가 아니라 내부적으로 만든 가설에서 나왔으며, 답을 뒷받침하는 증거를 제거하면 폐쇄형(closed-book) 기준선보다 오히려 성능이 떨어졌다. 이는 정적 검색 벤치마크가 증거 기반 발견보다 기억 기반 검증을 보상할 수 있음을 시사하며, 에이전트가 아는 것과 찾을 수 있는 것을 구별해야 함을 보여준다. 이에 저자들은 내재적 지식 범위를 넘어서는 심층 검색 벤치마크(deep-search benchmark)인 라이브 브라우즈컴프(LiveBrowseComp)를 제안한다. 이 벤치마크는 구축 시점보다 90일 이내에 발표된 사실에 답이 의존하는 335개의 인간 작성 질문으로 구성되며, 전 세계적으로 유명한 사건은 제외하고 여섯 개의 갱신되는 소스에서 수집되었다. 실험 결과 모든 평가 대상 에이전트의 폐쇄형 정확도는 2% 미만이었고, 검색을 더한 점수는 BrowseComp 대비 25~40포인트 하락했으며, 기존 모델 순위는 더 이상 성능을 신뢰 있게 예측하지 못했다. LiveBrowseComp는 공개되어 있어 향후 검색 에이전트의 진정한 탐색 능력을 측정하는 기준으로 활용될 수 있을 것이다.

> **Abstract.** Are LLM-based search agents genuinely searching, or using the web to verify what they already know? We study this question on BrowseComp with three diagnostics. Our analysis reveals Intrinsic Knowledge Dependence (IKD): even with tool access, agents often rely on intrinsic knowledge -- information encoded in the model before retrieval -- rather than on external evidence. Agents answer up to 44.5% of BrowseComp questions without tools, generate more than half of their search queries from internally produced hypotheses rather than retrieved leads, and perform worse than closed-book baselines whe…

🔗 [arXiv](https://arxiv.org/abs/2605.28721v1) · [PDF](https://arxiv.org/pdf/2605.28721v1)

---


## 9. Information bottleneck for learning the phase space of dynamics from high-dimensional experimental data

*K. Michael Martini, Eslam Abdelaleem, Paarth Gulati 외 · `physics.data-an` · 2026-04-27*

_(한국어 해설 생성 실패. 원문 abstract:)_

Identifying the dynamical state variables of a system from high-dimensional observations is a central problem across physical sciences. The challenge is that the state variables are not directly observable and must be inferred from raw high-dimensional data without supervision. Here we introduce DySIB (Dynamical Symmetric Information Bottleneck) as a method to learn low-dimensional representations of time-series data by maximizing predictive mutual information between past and future observation windows while penalizing representation complexity. This objective operates entirely in latent space and avoids reconstruction of the observations. We apply DySIB to an experimental video dataset of a physical pendulum, where the underlying state space is known. The method, with hyperparameters of the learning architecture set self-consistently by the data, recovers a two-dimensional representation that matches the dimensionality, topology, and geometry of the pendulum phase space, with the learned coordinates aligning smoothly with the canonical angle and angular velocity. These results demonstrate, on a well-characterized experimental system, that predictive information in latent space ca

> **Abstract.** Identifying the dynamical state variables of a system from high-dimensional observations is a central problem across physical sciences. The challenge is that the state variables are not directly observable and must be inferred from raw high-dimensional data without supervision. Here we introduce DySIB (Dynamical Symmetric Information Bottleneck) as a method to learn low-dimensional representations of time-series data by maximizing predictive mutual information between past and future observation windows while penalizing representation complexity. This objective operates entirely in latent spac…

🔗 [arXiv](https://arxiv.org/abs/2604.24662v2) · [PDF](https://arxiv.org/pdf/2604.24662v2)

---


## 10. AutoScientists: Self-Organizing Agent Teams for Long-Running Scientific Experimentation

*Shanghua Gao, Ada Fang, Marinka Zitnik · `cs.AI` · 2026-05-27*

과학적 연구는 가설 수립, 실험 설계, 실행, 수정의 반복적 순환으로 진행된다. AI 에이전트가 이 과정을 자동화할 수 있지만, 기존 방법은 단일 연구 궤적을 따르거나 고정된 목표를 가진 중앙 계획자에 의존하는 경우가 많아 병렬 탐색을 지속하지 못하고 실험 증거가 바뀔 때 적응하지 못하며 장기 실험에서 실패한 방향에 대한 지식을 보존하지 못한다. 이 문제를 해결하기 위해 본 논문은 AutoScientists를 제안한다. AutoScientists는 분산형 AI 에이전트 팀으로, 에이전트들이 공유 실험 상태(shared experimental state)를 해석하고 유망한 가설 주변에서 스스로 팀을 조직하며, 실험 계산을 사용하기 전에 제안을 비판적으로 검토하고 성공과 실패를 공유해 중복 탐색을 줄인다. 기술적으로는 중앙 계획자 없이 에이전트들이 동적으로 재편성되는 자기 조직화(self-organization)와, 비용이 큰 실험 실행 전 단계에서 제안을 검증하는 비평(critique) 메커니즘이 핵심이다. 또한 실패한 방향까지 공유 상태에 보존함으로써 장기 실험에서 지식을 축적한다. 실험 결과, BioML-Bench의 24개 작업에서 평균 리더보드 백분위 74.4%를 달성해 가장 강한 기존 AI 에이전트보다 +8.33%p 높았다. GPT 훈련 최적화에서는 Autoresearch보다 목표

> **Abstract.** Scientific research proceeds through iterative cycles of hypothesis generation, experiment design, execution, and revision. AI agents can automate parts of this process, but existing approaches typically follow a single research trajectory or coordinate through a central planner with fixed objectives. As a result, they struggle to sustain parallel exploration, adapt as experimental evidence changes, or preserve knowledge of failed directions over long-running experiments. We introduce AutoScientists, a decentralized team of AI agents for long-running computational scientific experimentation. A…

🔗 [arXiv](https://arxiv.org/abs/2605.28655v1) · [PDF](https://arxiv.org/pdf/2605.28655v1)

---



### 출처

이번 주 논문 10편의 선정은 [GeekNews 의 주간 AI/ML 논문 모음](https://news.hada.io/topic?id=30531) (큐레이터: ninebow) 의 큐레이션을 따랐고, 본문 해설은 각 논문 arXiv abstract 만을 근거로 본인 시각에서 재정리한 것입니다. 원문 큐레이터의 깊이 있는 코멘트는 원본 GeekNews 글을 참고해 주세요.