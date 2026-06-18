# 壁挂式龙头几何安装计算 Skill

语言: [English](README.md) | [中文](README.zh-CN.md)

用于计算壁挂式龙头出水口、台盆盆沿、排水目标点和水流角度之间的直线几何关系。

![壁挂式龙头与台盆几何关系](assets/wall_mounted_faucet_geometry_v2.svg)

安装到 Codex agents:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/<owner>/wall-mounted-faucet-layout-skill.git ~/.codex/skills/wall-mounted-faucet-layout
```

在 agent 提示中使用:

```text
Use $wall-mounted-faucet-layout to calculate the faucet layout with K=5 cm, W=40 cm, H2=14 cm, L=20.5 cm, and theta=10 degrees.
```

文件:

- `SKILL.md` - 公式、工作流程、校验规则和示例
- `agents/openai.yaml` - 供支持该元数据的 agent 使用的可选 UI 信息
- `scripts/faucet_geometry.py` - 确定性的计算脚本
- `assets/wall_mounted_faucet_geometry_v2.svg` - 适合 GitHub 渲染的可缩放示意图
- `assets/wall_mounted_faucet_geometry_v2.png` - 同一示意图的栅格备用版本

核心关系:

```text
tan(theta) = (K + WS - L) / (H1 + H2)
```

渲染文档时建议使用 SVG，因为缩放后标签仍然清晰，便于阅读各个参数。

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
