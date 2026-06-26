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


def patch_config(text: str) -> str:
    pattern = re.escape(TARGET_PREFIX) + r".*?(?=\s+custom_proxy_group=🚀 手动切换`select`)"
    patched, count = re.subn(pattern, FIXED_GROUP, text, count=1)

    if count != 1:
        raise RuntimeError("未找到 ACL4SSR 的“节点选择”代理组，可能上游格式变了。")

    return patched if patched.endswith("\n") else patched + "\n"


def main() -> None:
    with urlopen(UPSTREAM_URL, timeout=30) as response:
        source = response.read().decode("utf-8")

    OUTPUT.write_text(patch_config(source), encoding="utf-8")
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()
