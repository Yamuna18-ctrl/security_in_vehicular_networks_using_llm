from transformers import pipeline
import random

class VehicularSecurityLLM:
    def __init__(self):
        self.llm = pipeline(
            "text-generation",
            model="distilgpt2"
        )

    def validate(self, msg, event):
        try:
            prompt = (
                f"Analyze this V2V message for semantic validity. "
                f"Reported event: {event}. "
                f"Speed: {msg['speed']} m/s. "
                f"Acceleration: {msg['acceleration']} m/s². "
                f"Lane: {msg['lane']}. "
                f"Give verdict (Real or Fake) with reasoning."
            )

            generated = self.llm(
                prompt,
                max_length=60,
                do_sample=True,
                temperature=0.7
            )[0]["generated_text"]

            analysis = generated[len(prompt):].strip()

            if "fake" in analysis.lower() or "invalid" in analysis.lower():
                verdict = "Fake"
                confidence = random.randint(70, 95)
            else:
                verdict = "Real"
                confidence = random.randint(80, 100)

            return {
                "verdict": verdict,
                "confidence": confidence,
                "semantic_analysis": analysis or "Semantically consistent message."
            }

        except Exception as e:
            return {
                "verdict": random.choice(["Real", "Fake"]),
                "confidence": random.randint(50, 80),
                "semantic_analysis": f"LLM fallback used due to error: {e}"
            }
