from project_files.agents.planner import create_brief
from project_files.agents.researcher import gather_evidence
from project_files.agents.writer import draft_posts
from project_files.agents.editor import refine_post
from project_files.agents.compliance import compliance_check
from project_files.tools.voice_profile import load_voice_profile

def generate_linkedin_posts(topic):
    voice_profile = load_voice_profile()
    brief = create_brief(topic)
    evidence = gather_evidence(topic)
    drafts = draft_posts(topic, evidence, voice_profile)

    
    final_variants = []
    for variant in drafts.split("Variant"):
        if not variant.strip():
            continue
        issues = compliance_check(variant)
        if issues:
            variant += f"\n\n⚠ Issues: {issues}"
        refined = refine_post(variant)
        final_variants.append(refined)
    
    return {
        "brief": brief,
        "evidence": evidence,
        "variants": final_variants
    }
