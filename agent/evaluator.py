def evaluate(result):
    if not result:
        return "మీకు ప్రస్తుతం అర్హత ఉన్న పథకాలు కనిపించలేదు."
    return f"మీకు అర్హత ఉన్న పథకాలు: {', '.join(result)}"
