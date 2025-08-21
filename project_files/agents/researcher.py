from project_files.tools.search_tool import search_web_ddg
from project_files.tools.scrape_tool import scrape_url

def gather_evidence(topic):
    results = search_web_ddg(topic)
    # evidence = []
    # for r in results:
    #     text = scrape_url(r["url"])
    #     if text:
    #         evidence.append({"url": r["url"], "snippet": text[:500]})
    return results