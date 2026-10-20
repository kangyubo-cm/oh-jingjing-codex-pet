# 吃白饭的大肥鱼——哦鲸鲸的codex桌宠

顶着铁盆，捧着白饭，陪你写代码。哦鲸鲸～ 🐋🍚

![顶盆大肥鱼的动作预览](previews/all-states.gif)

**[下载 v1.0.0 桌宠安装包](https://github.com/kangyubo-cm/oh-jingjing-codex-pet/releases/download/v1.0.0/deepseek-basin-whale-v1.0.0.zip)** · [全部版本](https://github.com/kangyubo-cm/oh-jingjing-codex-pet/releases) · [素材来源与授权范围](NOTICE.md)

## 她会什么

- 头顶倒扣银色铁盆，手捧一盆白饭，拿着小勺。
- 蓝发、蓝眼睛、女仆装，保留半身小挂件的样子。
- 9 组基础动作：眨眼、左右移动、挥手、跳跃、委屈、等你、思考、检查成果。
- 16 个注视方向，包含抬头、低头和左右看。
- 透明 WebP 图集，适用于支持自定义 v2 Pets 的 Codex / ChatGPT 客户端。

| 待机眨眼 | 挥手招呼 | 捧盆等你 |
| --- | --- | --- |
| ![待机](previews/idle.gif) | ![挥手](previews/waving.gif) | ![等待](previews/waiting.gif) |

| 认真思考 | 轻轻跳起 | 委屈了 |
| --- | --- | --- |
| ![思考](previews/running.gif) | ![跳跃](previews/jumping.gif) | ![委屈](previews/failed.gif) |

本项目提供原生动画资源。原 DSH 插件的点击喂饭、摸头和换装菜单需要宿主功能支持，不会随着这个素材包一同安装。

## Windows 安装

1. 下载上面的 `deepseek-basin-whale-v1.0.0.zip`，解压得到 `deepseek-basin-whale` 文件夹。
2. 打开 `%USERPROFILE%\.codex\pets`。如果设置了 `CODEX_HOME`，则使用该目录下的 `pets`。
3. 将整个 `deepseek-basin-whale` 文件夹放进去，目录应当是：

   ```text
   .codex/pets/
   └── deepseek-basin-whale/
       ├── pet.json
       └── spritesheet.webp
   ```

4. 刷新客户端的 Pets 列表，选择 **顶盆大肥鱼**。没有出现时，完全退出客户端后重新打开。

不需要安装 Python，也不需要运行仓库里的脚本。已有同名版本时，先备份旧文件夹再替换。其他宠物可以保留。

macOS 的对应目录通常是 `~/.codex/pets/`；是否支持自定义 Pets 取决于客户端版本与功能开放情况。

## 更多预览

- [全部动作 GIF](previews/all-states.gif) / [MP4](previews/all-states.mp4)
- [透明背景待机动画](previews/idle.webp)
- [待机 → 跳跃 → 待机](previews/idle-jump-idle.gif)
- [十六方向循环](previews/look-loop.gif)
- [完整动作图集](previews/contact-sheet.png)

## 素材与重建

```text
pets/deepseek-basin-whale/  可以直接安装的桌宠
artwork/frames/            73 张透明 PNG 帧，可单独编辑
artwork/canonical-base.png 高分辨率造型基准
artwork/prompts/           角色和动作制作说明
previews/                 GIF、WebP、MP4 与动作总览
tools/build_atlas.py       从逐帧素材重建 v2 图集
validation/               发布素材的验证结果与方向检查说明
downloads/                安装包与校验值
```

需要重新组装图集时，在 Python 3.10+ 环境运行：

```sh
python -m pip install -r requirements.txt
python tools/build_atlas.py --output build
```

输出为 `build/pet.json`、`build/spritesheet.png` 和 `build/spritesheet.webp`。脚本只组装已有帧，不调用模型、不联网，也不修改已安装的宠物。

图集规格：1536 × 2288，8 列 × 11 行，单格 192 × 208。前九行动作帧数为 `6, 8, 8, 4, 5, 8, 6, 6, 6`；最后两行是 16 个注视方向，其余 15 个格子保持透明。

## 已做的检查

发布图集已通过结构、透明边缘及原生 Pets 上传校验，73 个必需格完整，未使用格透明。跳跃有实际离地并回到同一落点，方向检查由三份独立盲审交叉确认。

四个接近垂直的斜向姿态，水平分量比较轻微；两处跨行方向衔接出现像素差异统计提示，经视觉检查接受。原始指标和说明保存在 [验证报告](validation/summary.json) 与 [方向检查记录](validation/direction-semantics.json)，没有把这些提示删掉。

## 来源与许可

角色造型参考自 **[nailiang002-wq/deepseek-girl-harness](https://github.com/nailiang002-wq/deepseek-girl-harness)** 提供的吃饭姿势、铁盆帽与预览图。感谢原项目作者。

本项目用 ImageGen 根据上述参考重新制作原生 v2 动画，提供逐帧素材和重建工具。本项目是社区二创，与 DeepSeek、OpenAI 或 Codex 官方无隶属关系。

本仓库原创代码、配置及说明文档采用 [MIT License](LICENSE)。角色图像与第三方角色权利的范围见 [NOTICE.md](NOTICE.md)；MIT 许可证不代表取得了原角色或参考图的第三方权利。
