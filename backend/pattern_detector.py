import re
from collections import Counter


def normalize_log_line(line):

    # reemplazar números
    line = re.sub(r'\d+', '*', line)

    # reemplazar IPs
    line = re.sub(r'\b\d+\.\d+\.\d+\.\d+\b', '*', line)

    return line


def detect_patterns(log_text):

    lines = [
        line.strip()
        for line in log_text.splitlines()
        if line.strip() and len(line.strip()) > 3
    ]

    normalized = [normalize_log_line(line) for line in lines]

    pattern_counts = Counter(normalized)

    # top 5 patrones
    top_patterns = pattern_counts.most_common(5)

    patterns = []

    for pattern, count in top_patterns:
        patterns.append({
            "pattern": pattern,
            "occurrences": count
        })

    return patterns