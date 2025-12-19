from tools.eligibility import check_eligibility

def plan(user_text, memory):
    if "లక్ష" in user_text:
        memory.update("income", 150000)
    
    missing = memory.missing()
    if missing:
        return "మీ ఆదాయం చెప్పండి."

    return check_eligibility(memory.data["income"])
