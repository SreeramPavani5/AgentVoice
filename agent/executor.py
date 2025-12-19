from tools.schme_Api import fetch_schemes
from tools.eligibility import check_eligibility

def execute(action, memory):
    if action == "CHECK_ELIGIBILITY":
        schemes = fetch_schemes()
        return check_eligibility(memory.data, schemes)
