# 壁挂式龙头几何安装计算 Skill

语言: [English](README.md) | [中文](README.zh-CN.md)

用于计算壁挂式龙头出水口、台盆盆沿、排水目标点和水流角度之间的直线几何关系。

![壁挂式龙头与台盆几何关系](assets/wall_mounted_faucet_geometry_v2_zh.svg)

## 安装

这个仓库是一个文件系统形式的 skill package。安装目录应命名为 `wall-mounted-faucet-layout`，因为这是 `SKILL.md` 中声明的 skill 名称。

### Codex / OpenAI 风格 skills

安装为用户级 skill:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/starsy/wall-mounted-faucet-layout-skill.git ~/.codex/skills/wall-mounted-faucet-layout
```

### Claude / Claude Code

如果你的 Claude 运行环境支持本地 skill 目录:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/starsy/wall-mounted-faucet-layout-skill.git ~/.claude/skills/wall-mounted-faucet-layout
```

如果你的 Claude 运行环境通过压缩包导入 Skills，请先 clone 该仓库，把 `wall-mounted-faucet-layout` 文件夹压缩成 ZIP，然后在 Skills UI 中导入该 ZIP。

### OpenClaw

安装为 OpenClaw 全局 skill:

```bash
mkdir -p ~/.openclaw/skills
git clone https://github.com/starsy/wall-mounted-faucet-layout-skill.git ~/.openclaw/skills/wall-mounted-faucet-layout
```

如果你的 OpenClaw 配置使用工作区级 skills 目录，也可以把同名文件夹 clone 到该工作区的 skills 目录中。

### Cursor 和其他基于规则/上下文的 agents

如果 agent 不会自动发现 `SKILL.md` package，可以把该仓库 clone 到项目中的固定位置，然后让 agent 的规则或上下文系统引用 `SKILL.md`。

```bash
mkdir -p vendor/skills
git clone https://github.com/starsy/wall-mounted-faucet-layout-skill.git vendor/skills/wall-mounted-faucet-layout
```

对于 Cursor，可以添加类似 `.cursor/rules/wall-mounted-faucet-layout.mdc` 的项目规则:

```md
---
description: Use wall-mounted faucet geometry calculations
alwaysApply: false
---

When asked about wall-mounted faucet installation geometry, read and follow
`vendor/skills/wall-mounted-faucet-layout/SKILL.md`. Prefer the deterministic
calculator at `vendor/skills/wall-mounted-faucet-layout/scripts/faucet_geometry.py`.
```

在 agent 提示中使用:

```text
Use $wall-mounted-faucet-layout to calculate the faucet layout with K=5 cm, W=40 cm, H2=14 cm, L=20.5 cm, and theta=10 degrees.
```

文件:

- `SKILL.md` - 公式、工作流程、校验规则和示例
- `agents/openai.yaml` - 供支持该元数据的 agent 使用的可选 UI 信息
- `scripts/faucet_geometry.py` - 确定性的计算脚本
- `assets/wall_mounted_faucet_geometry_v2_zh.svg` - 中文 README 使用的可缩放示意图
- `assets/wall_mounted_faucet_geometry_v2_zh.png` - 中文示意图的栅格备用版本
- `assets/wall_mounted_faucet_geometry_v2.svg` - 英文版可缩放示意图
- `assets/wall_mounted_faucet_geometry_v2.png` - 英文版栅格备用版本

核心关系:

```text
tan(theta) = (K + WS - L) / (H1 + H2)
```

渲染文档时建议优先使用 SVG，因为缩放后标签仍然清晰；PNG 仅作为不支持 SVG 的环境中的备用图。

示例:

```bash
python scripts/faucet_geometry.py \
  --solve WS \
  --K 5 \
  --H1 15 \
  --H2 14 \
  --L 20.5 \
  --theta 10 \
  --W 40 \
  --unit cm
```

期望结果:

```text
WS = 20.613482 cm
horizontal_offset = 5.113482 cm
vertical_drop = 29.000000 cm
reverse_theta = 10.000000 degrees
drain_center_offset = 0.613482 cm
```

该计算器提供的是几何估算。封墙前请使用现场样板或实际放水测试确认最终安装位置。
