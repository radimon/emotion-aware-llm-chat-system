from __future__ import annotations
from dataclasses import dataclass

@dataclass
class EmotionState:
    label: str         # e.g., sad/angry/neutral
    intensity: float   # 0.0 ~ 1.0
    confidence: float  # 0.0 ~ 1.0


class EmotionAnalyzer:
    """
    MVP emotion analyzer (rule-based).
    Later you can sway this with an ML model without changing other modules.
    """
    def analyze(self, text: str) -> EmotionState:
        t = text.lower()

        if any(k in t for k in ["難過", "想哭", "sad", "depressed", "hurt"]):
            return EmotionState(label="sad", intensity=0.8, confidence=0.7)
        
        if any(k in t for k in ["生氣", "angry", "氣死", "mad"]):
            return EmotionState(label="angry", intensity=0.7, confidence=0.7)
        
        if any(k in t for k in ["焦慮", "緊張", "anxious", "panic"]):
            return EmotionState(label="anxious", intensity=0.6, confidence=0.6)
        
        return EmotionState(label="Neutral", intensity=0.2, confidence=0.6)