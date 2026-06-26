#!/usr/bin/env python3
from pathlib import Path
import re
from urllib.request import urlopen


UPSTREAM_URL = (
    "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/"
    "Clash/config/ACL4SSR_Online_Full_Netflix.ini"
)

OUTPUT = Path(__file__).resolve().parents[1] / "ACL4SSR_Online_Full_Netflix_HK.ini"

TARGET_PREFIX = "custom_proxy_group=🚀 节点选择`select`"
FIXED_GROUP = (
    "custom_proxy_group=🚀 节点选择`select`"
    "[]🇭🇰 香港节点"
    "`[]🚀 手动切换"
    "`[]🇨🇳 台湾节点"
    "`[]🇸🇬 狮城节点"
    "`[]🇯🇵 日本节点"
    "`[]🇺🇲 美国节点"
    "`[]🇰🇷 韩国节点"
    "`[]DIRECT"
)

AI_PREFIX = "custom_proxy_group=💬 Ai平台`select`"
FIXED_AI_GROUP = "custom_proxy_group=💬 Ai平台`select`[]🚀 手动切换"


def patch_config(text: str) -> str:
    patches = [
        (
            TARGET_PREFIX,
            FIXED_GROUP,
            r"(?=\s+custom_proxy_group=🚀 手动切换`select`)",
            "节点选择",
        ),
        (
            AI_PREFIX,
            FIXED_AI_GROUP,
            r"(?=\s+custom_proxy_group=📹 油管视频`select`)",
            "Ai平台",
        ),
    ]

    patched = text
    for prefix, replacement, suffix, name in patches:
        pattern = re.escape(prefix) + r".*?" + suffix
        patched, count = re.subn(pattern, replacement, patched, count=1)
        if count != 1:
            raise RuntimeError(f"未找到 ACL4SSR 的“{name}”代理组，可能上游格式变了。")

    return patched if patched.endswith("\n") else patched + "\n"


def main() -> None:
    with urlopen(UPSTREAM_URL, timeout=30) as response:
        source = response.read().decode("utf-8")

    OUTPUT.write_text(patch_config(source), encoding="utf-8")
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()
