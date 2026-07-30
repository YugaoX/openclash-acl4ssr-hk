#!/usr/bin/env python3
from pathlib import Path
import importlib.util


BASE_DIR = Path(__file__).resolve().parents[1]
MAIN_SCRIPT = BASE_DIR / "scripts" / "update_config.py"
OUTPUT = BASE_DIR / "ACL4SSR_Online_Full_Netflix_HK_RemoteLAN.ini"
LAN_AI_RULE = "ruleset=💬 Ai平台,[]IP-CIDR,192.168.100.0/24,no-resolve"


def load_main_module():
    spec = importlib.util.spec_from_file_location("update_config", MAIN_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def add_remote_lan_rule(text: str) -> str:
    if LAN_AI_RULE in text:
        return text

    marker = ";设置规则标志位\n"
    if marker not in text:
        raise RuntimeError("未找到 ACL4SSR 的规则标志位，可能上游格式变了。")

    return text.replace(marker, marker + LAN_AI_RULE + "\n", 1)


def main() -> None:
    main_config = load_main_module()
    with main_config.urlopen(main_config.UPSTREAM_URL, timeout=30) as response:
        source = response.read().decode("utf-8")

    OUTPUT.write_text(add_remote_lan_rule(main_config.patch_config(source)), encoding="utf-8")
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()
