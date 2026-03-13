from .node import Gemini3ResolutionSnapper

NODE_CLASS_MAPPINGS = {
    "Gemini3ResolutionSnapper": Gemini3ResolutionSnapper
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Gemini3ResolutionSnapper": "💎 Gemini3 Resolution Snapper"
}

print("✅ Gemini3 Snapper Loaded.")
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
