#!/usr/bin/env python3
"""
기술 스택 스터디 가이드 자동 생성기 (GitHub Actions용)
DeepSeek (OpenRouter) API를 사용하여 매일 키워드 하나씩 실무 스터디 HTML 생성

Usage:
  python scripts/study_generator.py
"""

import json
import os
import re
import subprocess
import time
import urllib.request
import urllib.error
from datetime import date
from pathlib import Path

BLOG_DIR = Path(__file__).parent.parent
KEYWORDS_FILE = BLOG_DIR / "_data" / "keywords.json"
STUDY_GUIDES_DIR = BLOG_DIR / "study-guides"
DATA_FILE = BLOG_DIR / "_data" / "study_guides.yml"

CATEGORY_MAP = {
    "data-engineering": "데이터 엔지니어 · 데이터 사이언티스트",
    "ai-ml": "AI 개발 엔지니어 · MLOps 엔지니어",
    "infra": "데브옵스 · 인프라 엔지니어",
    "security": "AI 정보보안 엔지니어 · 보안 전문가",
}


def slugify(text: str) -> str:
    slug = text.lower()
    slug = re.sub(r'[^a-z0-9\s\-]', ' ', slug)
    slug = re.sub(r'\s+', '-', slug.strip())
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')


def get_next_keyword():
    with open(KEYWORDS_FILE, encoding='utf-8') as f:
        data = json.load(f)
    for kw in data['keywords']:
        if kw['status'] == 'pending':
            return kw, data
    return None, None


def update_keyword_done(kw_id: int, data: dict, today: str):
    for kw in data['keywords']:
        if kw['id'] == kw_id:
            kw['status'] = 'done'
            kw['published_date'] = today
            break
    with open(KEYWORDS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def append_study_data(slug: str, keyword: str, category: str, tags: list, today: str):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    tag_str = ', '.join(f'"{t}"' for t in tags)
    entry = (
        f'- keyword: "{keyword}"\n'
        f'  slug: "{slug}"\n'
        f'  category: "{category}"\n'
        f'  tags: [{tag_str}]\n'
        f'  date: "{today}"\n'
        f'  url: "/study-guides/{slug}-study-guide.html"\n'
    )
    with open(DATA_FILE, 'a', encoding='utf-8') as f:
        f.write(entry)


def generate_html(keyword: str, category: str, tags: list, api_key: str) -> str:
    audience = CATEGORY_MAP.get(category, "데이터 엔지니어 · AI 엔지니어")
    tags_str = ", ".join(tags)

    prompt = f"""{keyword}에 대한 실무 스터디 가이드 HTML 파일을 생성해주세요.

**대상 독자**: {audience}

**요구사항**:
1. 완전한 단독 HTML 파일 (외부 CSS/JS 없음, <!DOCTYPE html>부터 시작)
2. 다크 테마 CSS 변수:
   --bg: #0d1117  --surface: #161b22  --surface2: #1c2333
   --border: #30363d  --text: #e6edf3  --text-muted: #8b949e
   --accent: #58a6ff  --accent2: #3fb950  --accent3: #d2a8ff  --accent4: #f0883e  --danger: #f85149
3. 문서 구조 (이 순서대로):
   - Hero 섹션 (제목, 부제목 "데이터 엔지니어 · AI 엔지니어를 위한 핵심 요약", 메타 뱃지)
   - 목차 (TOC, 번호 있는 링크)
   - 1. {keyword}란? (정의, 3대 핵심 능력 카드 그리드)
   - 2. 왜 써야 하는가? (기존 대안과 비교표)
   - 3. 핵심 개념 (ASCII 아키텍처 다이어그램 포함)
   - 4. 퀵스타트 (설치 → 설정 → 첫 예제, 단계별 코드블록)
   - 5. 핵심 설정 레퍼런스 (표 형태)
   - 6. 실무 팁 & 트러블슈팅 (자주 겪는 문제 + 해결책)
   - 7. 참고 자료 (공식 문서 링크)
   - Footer
4. CSS 클래스: .hero, .toc, .section, .concept-grid, .concept-card, .callout, .callout.warn, .diagram, table
5. Python 코드 예제 우선, CLI 명령어 포함
6. ASCII 다이어그램으로 아키텍처 시각화 (monospace font, .diagram 클래스)
7. 분량: 브라우저 15~20 스크롤 분량
8. 관련 태그: {tags_str}
9. 2026.03 작성 날짜 표시

오직 완전한 HTML만 출력하세요. 마크다운 코드펜스(```) 없이 <!DOCTYPE html>로 시작하는 순수 HTML."""

    payload = json.dumps({
        "model": "deepseek/deepseek-v3.2",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 10000,
        "temperature": 0.3,
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    last_err = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=300) as resp:
                body = json.loads(resp.read().decode("utf-8"))
            break
        except Exception as e:
            last_err = e
            print(f"  ⚠️  API 호출 실패 (시도 {attempt+1}/3): {e}")
            if attempt < 2:
                time.sleep(15)
    else:
        raise last_err

    text = body["choices"][0]["message"]["content"].strip()

    if text.startswith("```html"):
        text = text[7:]
    elif text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]

    return text.strip()


def git_commit_push(keyword: str, today: str):
    os.chdir(BLOG_DIR)
    subprocess.run(['git', 'add',
        f'study-guides/', f'_data/study_guides.yml', f'_data/keywords.json'
    ], check=True)
    subprocess.run([
        'git', 'commit', '-m',
        f'study: add {keyword} study guide ({today})'
    ], check=True)
    subprocess.run(['git', 'push', 'origin', 'main'], check=True)


def run():
    today = date.today().strftime('%Y-%m-%d')
    print(f"📚 {today} 스터디 가이드 생성 중...")

    api_key = os.environ.get('OPENROUTER_API_KEY', '')
    if not api_key:
        # 로컬 실행 시 config.json에서 읽기
        config_file = Path.home() / ".claude-daily-report" / "config.json"
        if config_file.exists():
            with open(config_file) as f:
                api_key = json.load(f).get('openrouter_api_key', '')
    if not api_key:
        print("❌ OPENROUTER_API_KEY 환경변수 또는 config.json이 필요합니다.")
        return

    kw_data, full_data = get_next_keyword()
    if not kw_data:
        print("✅ 모든 키워드 완료!")
        return

    keyword = kw_data['keyword']
    slug = slugify(keyword)
    category = kw_data['category']
    tags = kw_data['tags']

    print(f"  🎯 키워드: {keyword} (category={category})")
    print("  🤖 DeepSeek으로 HTML 생성 중... (최대 5분 소요)")

    html = generate_html(keyword, category, tags, api_key)

    if not html or not html.startswith('<!'):
        print(f"  ⚠️  생성된 HTML이 비정상입니다:\n{html[:200]}")

    STUDY_GUIDES_DIR.mkdir(parents=True, exist_ok=True)
    guide_file = STUDY_GUIDES_DIR / f"{slug}-study-guide.html"
    with open(guide_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  ✓ 파일 저장: {guide_file.name} ({len(html):,} bytes)")

    append_study_data(slug, keyword, category, tags, today)
    print("  ✓ _data/study_guides.yml 업데이트")

    update_keyword_done(kw_data['id'], full_data, today)
    print("  ✓ _data/keywords.json 업데이트")

    print("  🌐 GitHub 업로드 중...")
    git_commit_push(keyword, today)

    print(f"\n✅ 완료!")
    print(f"   URL: https://joyuno.github.io/study-guides/{slug}-study-guide.html")


if __name__ == '__main__':
    run()
