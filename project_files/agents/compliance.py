from project_files.tools.moderation import check_toxicity

def compliance_check(post_text):
    issues = []
    if len(post_text) > 1300:
        issues.append("Exceeds LinkedIn char limit")
    if check_toxicity(post_text):
        issues.append("Potentially toxic language detected")
    return issues