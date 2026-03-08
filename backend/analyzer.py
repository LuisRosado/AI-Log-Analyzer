from log_parser import parse_logs
from pattern_detector import detect_patterns
from ai_analysis import analyze_with_ai


def analyze_logs(log_text):

    parsed = parse_logs(log_text)

    patterns = detect_patterns(log_text)

    total_lines = parsed.get("total_lines", 0)
    error_count = parsed.get("error_count", 0)

    error_rate = 0
    if total_lines > 0:
        error_rate = error_count / total_lines

    # construir contexto reducido para el modelo
    pattern_summary = "\n".join(
        [f"{p['pattern']} ({p['occurrences']})" for p in patterns]
    )

    context = f"""
Error rate: {error_rate}
Timeout count: {parsed.get("timeout_count", 0)}

Patterns:
{pattern_summary}
"""

    ai_result = analyze_with_ai(context)

    return {
        "summary": ai_result.get("summary", ""),
        "root_cause": ai_result.get("root_cause", ""),
        "severity": ai_result.get("severity", "UNKNOWN"),
        "recommendations": ai_result.get("recommendations", []),

        "total_lines": total_lines,
        "error_count": error_count,
        "warning_count": parsed.get("warning_count", 0),
        "timeout_count": parsed.get("timeout_count", 0),
        "http_500_count": parsed.get("http_500_count", 0),

        "error_rate": error_rate,

        "patterns": patterns,
        "common_words": parsed.get("common_words", []),
        "sample_errors": parsed.get("errors", [])
    }