from __future__ import annotations
from dataclasses import dataclass
from backend.services.emotion import EmotionState

@dataclass
class Policy:
    style: str     # supportive / deescalate / clarify / neutral
    max_words: int # simplt controllable knob


class PolicyEngine:
    def decide(self, emo: EmotionState) -> Policy:
        # If we are uncertain, ask clearifying question rather than guessing.
        if emo.confidence < 0.45:
            return Policy(style="clarify", max_words=40)
        
        if emo.label == "sad" and emo.intensity >= 0.7:
            return Policy(style="supportive", max_words=50)
        
        if emo.label == "angry" and emo.intensity >= 0.6:
            return Policy(style="deescalate", max_words=45)
        
        if emo.label == "anxious" and emo.intensity >= 0.5:
            return Policy(style="supportive", max_words=50)
        
        return Policy(style="neutral", max_words=60)