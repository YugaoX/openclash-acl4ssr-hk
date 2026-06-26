# OpenClash ACL4SSR 香港固定配置

这个小项目会自动跟踪 ACL4SSR 的 `ACL4SSR_Online_Full_Netflix.ini`，并把 `节点选择` 代理组改成默认香港：

```ini
custom_proxy_group=🚀 节点选择`select`[]🇭🇰 香港节点`[]🚀 手动切换`[]🇨🇳 台湾节点`[]🇸🇬 狮城节点`[]🇯🇵 日本节点`[]🇺🇲 美国节点`[]🇰🇷 韩国节点`[]DIRECT
```

## 使用方法

使用这个 raw 地址作为 subconverter 的 `config=` 参数：

https://raw.githubusercontent.com/YugaoX/openclash-acl4ssr-hk/main/ACL4SSR_Online_Full_Netflix_HK.ini

把它 URL 编码后，替换你订阅链接里的原始 `config=` 地址。

如果需要自动同步上游 ACL4SSR 配置，可以再添加 `.github/workflows/update.yml`。

## 本地更新

也可以在本地或 NAS 上运行：

```bash
python3 scripts/update_config.py
```

然后把生成的 `ACL4SSR_Online_Full_Netflix_HK.ini` 通过 HTTP 服务托管出来。
