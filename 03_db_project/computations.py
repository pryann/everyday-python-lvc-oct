def generate_stat(values):
    stat = {"min": None, "max": None, "average": None, "count": 0, "sum": 0}

    if len(values) > 0:
        stat["count"] = len(values)
        stat["sum"] = sum(values)
        stat["min"] = min(values)
        stat["max"] = max(values)
        stat["average"] = stat["sum"] / stat["count"]

    return stat
