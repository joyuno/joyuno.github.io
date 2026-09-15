#!/usr/bin/env python3
"""protect_liquid 자가 검증 — python3 scripts/test_protect_liquid.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scraper import protect_liquid

FM = "---\nlayout: post\ntitle: t\n---\n"

# Liquid 문법이 없으면 그대로 둔다
plain = FM + "\n본문만 있습니다.\n"
assert protect_liquid(plain) == plain

# 코드 블록의 {{ }} 는 raw 로 감싼다
out = protect_liquid(FM + '\n```\n{{ "category": "{cat_id}" }}\n```\n')
assert out.startswith(FM + "{% raw %}"), out
assert out.rstrip().endswith("{% endraw %}"), out

# 원본에 있던 raw/endraw 는 제거 — 중첩되면 첫 endraw 에서 래핑이 끊긴다
out = protect_liquid(FM + "\n{% raw %}{{ x }}{% endraw %}\n{% if y %}\n")
assert out.count("{% raw %}") == 1 and out.count("{% endraw %}") == 1, out

# front matter 가 없으면 건드리지 않는다
assert protect_liquid("{{ x }}") == "{{ x }}"

print("ok")
