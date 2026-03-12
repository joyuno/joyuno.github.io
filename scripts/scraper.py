#!/usr/bin/env python3
"""
daewooki.github.io 포스트 임포터
GitHub API를 사용하여 원본 마크다운을 직접 가져옵니다.

Usage:
  python scripts/scraper.py          # 어제 날짜 포스트만 (daily 모드)
  python scripts/scraper.py --all    # 전체 포스트 일괄 임포트
"""

import argparse
import os
import re
import sys
import time

import requests
from datetime import datetime, timedelta

GITHUB_API_URL = "https://api.github.com/repos/daewooki/daewooki.github.io/contents/_posts"
SOURCE_BLOG_URL = "https://daewooki.github.io"
POSTS_DIR = "_posts"


def get_yesterday_date():
    yesterday = datetime.now() - timedelta(days=1)
    return yesterday.strftime("%Y-%m-%d")


def build_headers():
    headers = {"Accept": "application/vnd.github.v3+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"token {token}"
    return headers


def fetch_post_list(headers):
    """GitHub API로 _posts 파일 목록 반환"""
    response = requests.get(GITHUB_API_URL, headers=headers, timeout=30)
    response.raise_for_status()
    return response.json()


def fetch_raw_content(download_url, headers):
    response = requests.get(download_url, headers=headers, timeout=30)
    response.raise_for_status()
    return response.text


def get_source_url(filename):
    """파일명에서 원본 URL 생성 (2026-01-26-some-post.md -> /posts/some-post/)"""
    name = os.path.splitext(filename)[0]
    slug = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', name)
    return f"{SOURCE_BLOG_URL}/posts/{slug}/"


def process_frontmatter(content, source_url):
    """
    front matter 후처리:
      - layout: post 보장
      - ai-tech 카테고리 제거
      - source: <url> 추가
    """
    if not content.startswith("---"):
        return f"---\nlayout: post\nsource: {source_url}\n---\n\n{content}"

    end_idx = content.find("---", 3)
    if end_idx == -1:
        return content

    fm_raw = content[3:end_idx]
    body = content[end_idx + 3:]

    lines = fm_raw.split("\n")
    new_lines = []
    has_layout = False
    has_source = False

    i = 0
    while i < len(lines):
        line = lines[i]

        # layout
        if re.match(r'^layout\s*:', line):
            has_layout = True
            new_lines.append("layout: post")
            i += 1
            continue

        # source
        if re.match(r'^source\s*:', line):
            has_source = True
            new_lines.append(f"source: {source_url}")
            i += 1
            continue

        # categories 인라인 배열: categories: [ai-tech, foo]
        inline_m = re.match(r'^(categories\s*:\s*)\[([^\]]*)\]', line)
        if inline_m:
            cats = [c.strip() for c in inline_m.group(2).split(",") if c.strip()]
            cats = [c for c in cats if c.lower() != "ai-tech"]
            new_lines.append(f"categories: [{', '.join(cats)}]")
            i += 1
            continue

        # categories 단일 값: categories: ai-tech
        single_m = re.match(r'^categories\s*:\s*(\S+)\s*$', line)
        if single_m:
            val = single_m.group(1).lower()
            if val == "ai-tech":
                new_lines.append("categories: []")
            else:
                new_lines.append(line)
            i += 1
            continue

        # categories 블록 배열:
        # categories:
        #   - ai-tech
        #   - foo
        if re.match(r'^categories\s*:\s*$', line):
            new_lines.append(line)
            i += 1
            while i < len(lines) and re.match(r'^\s+-\s+', lines[i]):
                cat_name = re.sub(r'^\s+-\s+', '', lines[i]).strip()
                if cat_name.lower() != "ai-tech":
                    new_lines.append(lines[i])
                i += 1
            continue

        new_lines.append(line)
        i += 1

    if not has_layout:
        new_lines.insert(0, "layout: post")
    if not has_source:
        new_lines.append(f"source: {source_url}")

    return f"---\n{''.join(l + chr(10) for l in new_lines)}---{body}"


def save_post(filename, content):
    os.makedirs(POSTS_DIR, exist_ok=True)
    filepath = os.path.join(POSTS_DIR, filename)

    if os.path.exists(filepath):
        print(f"  이미 존재: {filename}")
        return False

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"  생성: {filename}")
    return True


def import_post(file_info, headers):
    filename = file_info["name"]
    download_url = file_info["download_url"]
    try:
        raw = fetch_raw_content(download_url, headers)
        source_url = get_source_url(filename)
        processed = process_frontmatter(raw, source_url)
        return save_post(filename, processed)
    except Exception as e:
        print(f"  오류 ({filename}): {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="daewooki.github.io 포스트 임포터")
    parser.add_argument("--all", action="store_true", help="전체 포스트 일괄 임포트")
    args = parser.parse_args()

    headers = build_headers()
    has_token = bool(os.environ.get("GITHUB_TOKEN"))

    print("GitHub API에서 포스트 목록 가져오는 중...")
    try:
        files = fetch_post_list(headers)
    except requests.RequestException as e:
        print(f"GitHub API 오류: {e}")
        sys.exit(1)

    md_files = [f for f in files if isinstance(f, dict) and f.get("name", "").endswith(".md")]
    print(f"총 {len(md_files)}개 포스트 발견")

    if not args.all:
        yesterday = get_yesterday_date()
        md_files = [f for f in md_files if f["name"].startswith(yesterday)]
        print(f"어제({yesterday}) 날짜 포스트: {len(md_files)}개")
    else:
        print("--all 모드: 전체 포스트 임포트")

    count = 0
    for idx, file_info in enumerate(md_files, 1):
        result = import_post(file_info, headers)
        if result:
            count += 1
        # 토큰 없을 때 GitHub API rate limit 방지
        if not has_token and idx % 10 == 0:
            time.sleep(1)

    print(f"\n완료: {count}개의 새 포스트 추가됨")


if __name__ == "__main__":
    main()
