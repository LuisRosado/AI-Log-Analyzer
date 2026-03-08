import requests
import json
import re

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"


def analyze_with_ai(context):

    prompt = f"""
    You are a senior DevOps and Site Reliability Engineer (SRE) analyzing system logs.

    Based on the following log statistics and patterns, determine what is happening in the system.

    Return ONLY valid JSON in the following format and nothing else:

    {{
    "summary": "Short explanation of the situation in 1-2 sentences",
    "root_cause": "Most likely technical cause of the issue",
    "severity": "LOW | MEDIUM | HIGH",
    "recommendations": [
        "actionable recommendation 1",
        "actionable recommendation 2",
        "actionable recommendation 3"
    ]
    }}

    Guidelines:
    - HIGH severity: repeated errors, service failures, crashes, timeouts affecting functionality
    - MEDIUM severity: warnings, intermittent errors, degraded performance
    - LOW severity: informational or minor issues
    - Recommendations must be practical DevOps actions (monitoring, scaling, configuration, retries, etc.)
    - Do not include explanations outside the JSON.

    Log statistics:
    {context}
    """

    try:

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "phi3:mini",
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        data = response.json()

        text = data.get("response", "").strip()

        # limpiar markdown si el modelo lo agrega
        text = text.replace("```json", "").replace("```", "").strip()

        # encontrar JSON dentro del texto
        match = re.search(r"\{.*\}", text, re.DOTALL)

        if match:
            json_text = match.group()
            ai_result = json.loads(json_text)

            return {
                "summary": ai_result.get("summary", ""),
                "root_cause": ai_result.get("root_cause", ""),
                "severity": ai_result.get("severity", "UNKNOWN"),
                "recommendations": ai_result.get("recommendations", [])
            }

        else:
            raise ValueError("No JSON found in AI response")

    except Exception as e:

        print("AI ERROR:", e)

        return {
            "summary": "AI analysis failed",
            "root_cause": "",
            "severity": "UNKNOWN",
            "recommendations": []
        }