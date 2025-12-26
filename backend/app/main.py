from __future__ import annotations
from fastapi import FastAPI
from pydantic import BaseModel

from backend.core.session import get_session
from backend.services.emotion import EmotionAnalyzer
from backend.services.policy import PolicyEngine

app = FastAPI(title="Emotion-Aware Chat System (MVP)")

emotion_analyzer = EmotionAnalyzer()
policy_engine = PolicyEngine()

class ChatRequest(BaseModel):
    user_id: str
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    sess = get_session(req.user_id)
    sess.history.append(req.message)

    emo = emotion_analyzer.analyze(req.message)
    pol = policy_engine.decide(emo)

    # Templete responder (MVP): controllable & safe
    if pol.style == "supportive":
        reply = "我聽到你現在很不好受，我在這裡陪你。你願意多說一點發生了什麼嗎？"
    elif pol.style == "deescalate":
        reply = "我感覺你很不舒服。我先理解一下：是什麼讓你最生氣或最委屈？"
    elif pol.style == "clarify":
        reply = "我可能理解的不完整。你希望我先請聽、一起分析，還是給你建議？"
    else:
        reply = "收到。我可以更了解一下你的情況嗎？"

    return {
        "reply": reply,
        "emotion": {"label": emo.label, "intensity": emo.intensity, "confidence": emo.confidence},
        "policy": {"style": pol.style, "max_words": pol.max_words},
        "history_len": len(sess.history),
    }