# 💎 ComfyUI Gemini3 Resolution Snapper

🤖 **AI-Generated \& Personal Use Statement / AI 生成与自用声明**

> \*\*\[EN]\*\* The code for this plugin was generated with the assistance of AI. This repository is primarily published so the author can conveniently `git clone` and sync the node across different personal devices.
> 
> \*\*\[中文]\*\* 本插件代码由 AI 辅助生成。将其放到公开仓库，主要是为了方便作者本人在不同的设备之间直接 `git clone` 同步使用。

\---

## 📖 Introduction (简介)

### \[English]

The core purpose of this custom node is to automatically match input images to safe, standard resolutions based on their aspect ratios.

**Why use this?**

* **Prevent VRAM OOM:** It prevents the frustrating Out-Of-Memory (OOM) errors where certain aspect ratios generate perfectly fine, but slightly different ratios suddenly blow up your VRAM.
* **Optimized for "Nano Banana Pro":** The author frequently uses the `nano banana pro` model. Therefore, the resolution presets and scaling tiers in this node correspond exactly to "banana" ratios.
* **Perfect for Upscaling:** It allows for convenient exact-multiple scaling. For example, you can easily select a higher tier to safely scale a `768` base resolution up to `1536` without weird decimal artifacts.

### \[中文]

这个自定义节点的核心作用，是供作者自己方便地匹配不同比例图片的安全分辨率。

**为什么需要它？**

* **防止爆显存：** 在跑图时，我们常遇到某些比例可以正常生成，但特定比例的像素总数稍一变化就会导致爆显存。这个节点将比例严格吸附到安全预设上，彻底解决这个问题。
* **为 "Nano Banana Pro" 打造：** 因为作者平时使用 `nano banana pro` 较多，所以节点里的几个档次和分辨率预设，都是严格对应 banana 的标准比例设置的。
* **完美的成倍放大：** 这种设计非常方便进行成倍的高清放大操作，比如一键切换档位，将 `768` 的基准分辨率精准成倍放大为 `1536`。

\---

## 🎛️ Usage (节点说明)

**Node Name / 节点名称**: `💎 Gemini3 Resolution Snapper` (Located in `utils/math` / 位于 `utils/math` 类别下)

### Inputs (输入参数)

* `image`: Your reference image to detect the aspect ratio. / 你的参考输入图片，用于侦测原始比例。
* `level`:

  * `1K (Base)`: Standard base generation (e.g., 1024x1024 or 768x1408). / 基准分辨率。
  * `2K (High)`: 2x multiplier for safe upscaling. / 2倍放大档位（如 768 -> 1536）。
  * `4K (Ultra)`: 4x multiplier. / 4倍放大档位。

### Outputs (输出参数)

* `width`: Exact calculated width / 计算得出的精准宽度。
* `height`: Exact calculated height / 计算得出的精准高度。
* `long\_side`: Length of the longer edge / 长边像素值。
* `short\_side`: Length of the shorter edge / 短边像素值。
* `matched\_preset`: The matched aspect ratio name / 匹配到的比例名称 (例如 "16:9 Cinematic")。

\---

## 📦 Installation (安装方法)

Navigate to your ComfyUI `custom\_nodes` directory and clone this repo:
（进入你的 ComfyUI `custom\_nodes` 目录，然后克隆此仓库：）

```bash
cd ComfyUI/custom\_nodes/
git clone https://github.com/ih455/ComfyUI-Gemini3-Resolution-Snapper

