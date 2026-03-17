---
layout: post

title: "LangChain으로 RAG 시스템 구축하기 📚"
date: 2025-12-10 10:00:00 +0900
categories: [AI, LangChain]
tags: [langchain, rag, llm, ai, vector-db]

source: https://daewooki.github.io/posts/langchain-rag-tutorial/
---

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-7990TVG7C7"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-7990TVG7C7');
</script>
## RAG란?

**RAG (Retrieval-Augmented Generation)**는 LLM의 한계를 극복하는 핵심 기술입니다.

LLM의 문제점:
- ❌ 학습 데이터 이후 정보 모름
- ❌ 회사 내부 문서 모름
- ❌ 할루시네이션 (거짓 정보 생성)

RAG의 해결책:
- ✅ 외부 문서에서 관련 정보 검색
- ✅ 검색된 정보를 컨텍스트로 제공
- ✅ 근거 기반 응답 생성

---

## 🏗️ 아키텍처

```
[문서] → [청킹] → [임베딩] → [Vector DB]
                                    ↓
[질문] → [임베딩] → [유사도 검색] → [관련 문서]
                                    ↓
                    [LLM + 컨텍스트] → [응답]
```

---

## 💻 구현 코드

### 1. 필요한 패키지 설치

```bash
pip install langchain langchain-openai chromadb pypdf
```

### 2. 문서 로드 및 청킹

```python
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# PDF 문서 로드
loader = PyPDFLoader("company_docs.pdf")
documents = loader.load()

# 청킹 (문서를 작은 단위로 분할)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", ".", " "]
)
chunks = text_splitter.split_documents(documents)

print(f"총 {len(chunks)}개의 청크 생성")
```

### 3. 벡터 DB 구축

```python
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# 임베딩 모델
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Chroma DB에 저장
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

# 검색기 생성
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}  # 상위 3개 문서 검색
)
```

### 4. RAG 체인 구성

```python
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

# LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 프롬프트 템플릿
template = """다음 컨텍스트를 기반으로 질문에 답변해주세요.
컨텍스트에 없는 내용은 "해당 정보를 찾을 수 없습니다"라고 답변하세요.

컨텍스트:
{context}

질문: {question}

답변:"""

prompt = ChatPromptTemplate.from_template(template)

# RAG 체인
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# 실행
response = rag_chain.invoke("회사의 연차 정책이 어떻게 되나요?")
print(response)
```

---

## 🔧 고급 기능

### 1. Hybrid Search (키워드 + 의미 검색)

```python
from langchain.retrievers import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever

# BM25 (키워드 기반)
bm25_retriever = BM25Retriever.from_documents(chunks)
bm25_retriever.k = 3

# 앙상블 (하이브리드)
ensemble_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, retriever],
    weights=[0.4, 0.6]
)
```

### 2. Reranker로 정확도 향상

```python
from langchain.retrievers import ContextualCompressionRetriever
from langchain_cohere import CohereRerank

reranker = CohereRerank(model="rerank-multilingual-v3.0")
compression_retriever = ContextualCompressionRetriever(
    base_compressor=reranker,
    base_retriever=retriever
)
```

### 3. 대화 기록 유지

```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory
)
```

---

## 💡 실전 팁

1. **청크 사이즈는 실험적으로** - 500~1500 사이에서 테스트
2. **오버랩은 필수** - 문맥이 끊기지 않도록
3. **메타데이터 활용** - 출처, 페이지 번호 등
4. **평가 지표 설정** - Faithfulness, Relevance 측정

---

## 🎯 마무리

RAG는 기업용 AI 챗봇의 핵심 기술입니다.

이 기본 구조를 이해하면:
- 사내 문서 Q&A 봇
- 고객 지원 챗봇
- 법률/의료 문서 분석

등 다양한 응용이 가능합니다!

다음 글에서는 **프로덕션 RAG 시스템 최적화**를 다뤄보겠습니다.

