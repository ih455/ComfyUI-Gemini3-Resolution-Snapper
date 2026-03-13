import torch
import math

class Gemini3ResolutionSnapper:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),  # 用于侦测原始比例
                "level": (["1K (Base)", "2K (High)", "4K (Ultra)"],), # 对应表格的三列
            }
        }

    RETURN_TYPES = ("INT", "INT", "INT", "INT", "STRING")
    RETURN_NAMES = ("width", "height", "long_side", "short_side", "matched_preset")
    FUNCTION = "snap_resolution"
    CATEGORY = "utils/math"

    def snap_resolution(self, image, level):
        # 0. 防御代码
        if image is None:
            print("🔴 No image input.")
            return (1024, 1024, 1024, 1024, "Error")

        # 1. 定义标准库 (基于 Gemini 3 Image Pro 表格)
        # 格式: ratio_value: (width_1k, height_1k, name)
        # 注意：这里只需存 1K 的基准，2K/4K 通过乘法获得
        PRESETS = [
            (1.00,  1024, 1024, "1:1 Square"),
            (1.33,  1280, 960,  "4:3 Landscape"),
            (0.75,  960,  1280, "3:4 Portrait"),
            (1.50,  1216, 832,  "3:2 Classic"),     # 实际上 1.46
            (0.66,  832,  1216, "2:3 Classic P"),
            (1.77,  1408, 768,  "16:9 Cinematic"),  # 实际上 1.83
            (0.56,  768,  1408, "9:16 Vertical"),
            (2.40,  1536, 640,  "21:9 Ultra-Wide"), # 表格是1536x640(2.4), 这里的21:9是通俗叫法
            (0.80,  896,  1152, "4:5 Portrait"),
            (1.25,  1152, 896,  "5:4 Landscape"),
        ]

        # 2. 获取输入图像的比例
        _, h, w, _ = image.shape
        input_ar = w / h

        # 3. 寻找最接近的预设 (Nearest Neighbor Search)
        # 比较 abs(input_ar - preset_ar)
        best_match = min(PRESETS, key=lambda x: abs(x[0] - input_ar))
        
        target_w_1k = best_match[1]
        target_h_1k = best_match[2]
        preset_name = best_match[3]

        # 4. 根据等级缩放 (1K / 2K / 4K)
        multiplier = 1
        if level == "2K (High)":
            multiplier = 2
        elif level == "4K (Ultra)":
            multiplier = 4
        
        final_w = target_w_1k * multiplier
        final_h = target_h_1k * multiplier

        # 5. 计算长短边
        final_long = max(final_w, final_h)
        final_short = min(final_w, final_h)

        # 控制台日志
        print(f"\n[Gemini3 Snapper]")
        print(f"Input AR: {input_ar:.3f} -> Snapped to: {preset_name}")
        print(f"Level: {level} -> Output: {final_w}x{final_h}")

        return (final_w, final_h, final_long, final_short, preset_name)
