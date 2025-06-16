def score_weather(temp, precipitation, wind, event_type, description):
    score = 0
    if event_type == "cricket":
        if 15 <= temp <= 30: score += 30
        if precipitation < 20: score += 25
        if wind < 20: score += 20
        if "clear" in description or "cloud" in description: score += 25
    elif event_type == "wedding":
        if 18 <= temp <= 28: score += 30
        if precipitation < 10: score += 30
        if wind < 15: score += 25
        if "clear" in description: score += 15

    if score >= 80:
        return "Good"
    elif score >= 50:
        return "Okay"
    else:
        return "Poor"
