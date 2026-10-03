from collections import Counter

def parse_logs(log_lines):
    status_counts = Counter()
    for line in log_lines:
        parts = line.strip().split()
        if len(parts) >= 3:
            status = parts[-1]
            status_counts[status] += 1
    return dict(status_counts)

if __name__ == "__main__":
    sample_logs = [
        "GET /index.html 200",
        "POST /login 200",
        "GET /dashboard 404",
        "GET /api/data 500",
        "GET /about 200"
    ]
    results = parse_logs(sample_logs)
    print("Parsed Log Counts:", results)
