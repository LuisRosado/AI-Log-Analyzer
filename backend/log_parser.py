import re
from collections import Counter


def parse_logs(log_text):

    lines = log_text.splitlines()

    errors = re.findall(r"ERROR.*", log_text)
    warnings = re.findall(r"WARNING.*", log_text)

    http_500 = re.findall(r"500", log_text)
    connection_refused = re.findall(r"connection refused", log_text, re.IGNORECASE)
    timeouts = re.findall(r"timeout", log_text, re.IGNORECASE)

    # palabras frecuentes
    words = re.findall(r"\b[a-zA-Z]+\b", log_text.lower())
    common_words = Counter(words).most_common(5)

    total_lines = len(lines)

    return {
        "total_lines": total_lines,
        "error_count": len(errors),
        "warning_count": len(warnings),
        "timeout_count": len(timeouts),
        "http_500_count": len(http_500),
        "connection_refused_count": len(connection_refused),
        "errors": errors[:5],
        "common_words": common_words
    }