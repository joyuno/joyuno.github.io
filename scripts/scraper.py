#!/usr/bin/env python3
"""
Daewook's Dev Log 블로그 스크래퍼
매일 전날의 글을 가져와서 마크다운 파일로 저장합니다.
"""

import os
import re
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json

BASE_URL = "https://daewooki.github.io"
POSTS_DIR = "_posts"

def get_yesterday_date():
    """어제 날짜 반환"""
    yesterday = datetime.now() - timedelta(days=1)
    return yesterday.strftime("%Y-%m-%d")

def get_archive_posts():
    """아카이브 페이지에서 글 목록 가져오기"""
    url = f"{BASE_URL}/archives/"
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    posts = []

    # 모든 링크에서 포스트 찾기
    for link in soup.find_all('a', href=True):
        href = link.get('href', '')
        if '/posts/' in href and href != '/posts/':
            full_url = urljoin(BASE_URL, href)
            title = link.get_text(strip=True)
            if title:
                posts.append({
                    'url': full_url,
                    'title': title,
                    'href': href
                })

    return posts

def extract_date_from_page(soup):
    """페이지에서 날짜 추출"""
    # meta 태그에서 날짜 찾기
    meta_date = soup.find('meta', {'property': 'article:published_time'})
    if meta_date:
        date_str = meta_date.get('content', '')[:10]
        return date_str

    # time 태그에서 날짜 찾기
    time_tag = soup.find('time')
    if time_tag:
        datetime_attr = time_tag.get('datetime', '')
        if datetime_attr:
            return datetime_attr[:10]

    # 텍스트에서 날짜 패턴 찾기
    text = soup.get_text()
    date_patterns = [
        r'(\d{4})[/-](\d{1,2})[/-](\d{1,2})',
        r'(\d{4})년\s*(\d{1,2})월\s*(\d{1,2})일'
    ]

    for pattern in date_patterns:
        match = re.search(pattern, text)
        if match:
            year, month, day = match.groups()
            return f"{year}-{int(month):02d}-{int(day):02d}"

    return None

def extract_post_content(url):
    """포스트 내용 추출"""
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    # 제목 추출
    title = ""
    h1 = soup.find('h1')
    if h1:
        title = h1.get_text(strip=True)

    # 날짜 추출
    date = extract_date_from_page(soup)

    # 카테고리 추출
    categories = []
    category_links = soup.find_all('a', href=lambda x: x and '/categories/' in x)
    for cat in category_links:
        cat_text = cat.get_text(strip=True)
        if cat_text and cat_text not in categories:
            categories.append(cat_text)

    # 태그 추출
    tags = []
    tag_links = soup.find_all('a', href=lambda x: x and '/tags/' in x)
    for tag in tag_links:
        tag_text = tag.get_text(strip=True).lstrip('#')
        if tag_text and tag_text not in tags:
            tags.append(tag_text)

    # 본문 추출
    content = ""
    article = soup.find('article') or soup.find('div', class_='post-content') or soup.find('main')

    if article:
        # 불필요한 요소 제거
        for elem in article.find_all(['nav', 'footer', 'aside', 'script', 'style']):
            elem.decompose()

        # HTML을 마크다운으로 변환
        content = html_to_markdown(article)

    # 읽는 시간 추출
    reading_time = None
    time_text = soup.find(string=re.compile(r'\d+\s*분'))
    if time_text:
        match = re.search(r'(\d+)\s*분', time_text)
        if match:
            reading_time = int(match.group(1))

    return {
        'title': title,
        'date': date,
        'categories': categories,
        'tags': tags,
        'content': content,
        'reading_time': reading_time,
        'source': url
    }

def html_to_markdown(element):
    """HTML을 마크다운으로 변환"""
    lines = []

    for child in element.children:
        if hasattr(child, 'name'):
            if child.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                level = int(child.name[1])
                text = child.get_text(strip=True)
                lines.append(f"\n{'#' * level} {text}\n")

            elif child.name == 'p':
                text = child.get_text(strip=True)
                if text:
                    lines.append(f"\n{text}\n")

            elif child.name == 'ul':
                for li in child.find_all('li', recursive=False):
                    text = li.get_text(strip=True)
                    lines.append(f"- {text}")
                lines.append("")

            elif child.name == 'ol':
                for i, li in enumerate(child.find_all('li', recursive=False), 1):
                    text = li.get_text(strip=True)
                    lines.append(f"{i}. {text}")
                lines.append("")

            elif child.name == 'pre':
                code = child.find('code')
                if code:
                    lang_class = code.get('class', [])
                    lang = ""
                    for cls in lang_class:
                        if cls.startswith('language-'):
                            lang = cls.replace('language-', '')
                            break
                    code_text = code.get_text()
                    lines.append(f"\n```{lang}\n{code_text}\n```\n")

            elif child.name == 'blockquote':
                text = child.get_text(strip=True)
                lines.append(f"\n> {text}\n")

            elif child.name == 'code':
                text = child.get_text(strip=True)
                lines.append(f"`{text}`")

            elif child.name in ['strong', 'b']:
                text = child.get_text(strip=True)
                lines.append(f"**{text}**")

            elif child.name in ['em', 'i']:
                text = child.get_text(strip=True)
                lines.append(f"*{text}*")

            elif child.name == 'a':
                text = child.get_text(strip=True)
                href = child.get('href', '')
                if href and text:
                    lines.append(f"[{text}]({href})")

            elif child.name == 'img':
                src = child.get('src', '')
                alt = child.get('alt', 'image')
                if src:
                    if not src.startswith('http'):
                        src = urljoin(BASE_URL, src)
                    lines.append(f"\n![{alt}]({src})\n")

            elif child.name == 'div':
                # 재귀적으로 처리
                nested = html_to_markdown(child)
                if nested.strip():
                    lines.append(nested)

            elif child.name == 'table':
                # 테이블 처리
                rows = child.find_all('tr')
                if rows:
                    lines.append("")
                    for i, row in enumerate(rows):
                        cells = row.find_all(['th', 'td'])
                        row_text = " | ".join(cell.get_text(strip=True) for cell in cells)
                        lines.append(f"| {row_text} |")
                        if i == 0:
                            lines.append("|" + " --- |" * len(cells))
                    lines.append("")

    return "\n".join(lines)

def create_markdown_file(post_data):
    """마크다운 파일 생성"""
    date = post_data['date']
    title = post_data['title']

    # 파일명 생성 (날짜-제목-슬러그)
    slug = re.sub(r'[^\w가-힣\s-]', '', title)
    slug = re.sub(r'\s+', '-', slug)[:50]
    filename = f"{date}-scraped-{slug}.md"
    filepath = os.path.join(POSTS_DIR, filename)

    # 이미 존재하면 건너뛰기
    if os.path.exists(filepath):
        print(f"이미 존재함: {filename}")
        return False

    # Front matter 생성
    frontmatter = f"""---
layout: post
title: "{title}"
date: {date}
categories: [{', '.join(post_data['categories'])}]
tags: [{', '.join(post_data['tags'])}]
author: Daewook Kwon
"""

    if post_data.get('reading_time'):
        frontmatter += f"reading_time: {post_data['reading_time']}\n"

    frontmatter += f"source: {post_data['source']}\n---\n\n"

    content = frontmatter + post_data['content']
    content += f"\n\n---\n*원본 출처: [{post_data['source']}]({post_data['source']})*\n"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"생성됨: {filename}")
    return True

def main():
    """메인 함수"""
    yesterday = get_yesterday_date()
    print(f"스크래핑 시작: {yesterday} 날짜의 글 검색")

    # 글 목록 가져오기
    posts = get_archive_posts()
    print(f"총 {len(posts)}개의 글 발견")

    scraped_count = 0

    for post in posts:
        try:
            post_data = extract_post_content(post['url'])

            if post_data['date'] == yesterday:
                print(f"전날 글 발견: {post_data['title']}")

                if create_markdown_file(post_data):
                    scraped_count += 1

        except Exception as e:
            print(f"오류 발생 ({post['url']}): {e}")
            continue

    print(f"\n완료: {scraped_count}개의 새 글 추가됨")

if __name__ == "__main__":
    main()
