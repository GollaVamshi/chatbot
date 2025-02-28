from django.shortcuts import render
from django.http import JsonResponse
from .models import Documentation
import re

CDP_URLS = {
    "Segment": "https://segment.com/docs/",
    "mParticle": "https://docs.mparticle.com/",
    "Lytics": "https://docs.lytics.com/",
    "Zeotap": "https://docs.zeotap.com/home/en-us/"
}

def search_docs(query):
    query_words = set(query.lower().split())
    results = []
    
    for doc in Documentation.objects.all():
        content_words = set(doc.content.lower().split())
        common_words = query_words & content_words
        if common_words:
            relevance = len(common_words)
            snippet = doc.content[:150] + "..." if len(doc.content) > 150 else doc.content
            results.append((relevance, doc.cdp, doc.url, snippet))
    
    results.sort(reverse=True)
    return results[:2]

def compare_cdps(query):
    query_lower = query.lower()
    if "compare" not in query_lower:
        return None
    
    cdps_mentioned = [cdp for cdp in CDP_URLS.keys() if cdp.lower() in query_lower]
    if len(cdps_mentioned) < 2:
        return None
    
    comparison = [f"Comparing {', '.join(cdps_mentioned)}..."]
    for cdp in cdps_mentioned:
        doc = Documentation.objects.filter(cdp=cdp).first()
        if doc:
            snippet = doc.content[:100] + "..." if len(doc.content) > 100 else doc.content
            comparison.append(f"- {cdp}: {snippet}")
    return "\n".join(comparison)

def index(request):
    return render(request, "chatbot/index.html")

def chat(request):
    if request.method == "POST":
        query = request.POST.get("query", "").strip()
        
        # Check if query is CDP-related
        if not any(cdp.lower() in query.lower() for cdp in CDP_URLS.keys()):
            return JsonResponse({"response": "I can only help with Segment, mParticle, Lytics, or Zeotap questions."})
        
        # Handle comparison
        comparison = compare_cdps(query)
        if comparison:
            return JsonResponse({"response": comparison})
        
        # Search documentation
        results = search_docs(query)
        if results:
            response = "\n\n".join(f"From {cdp} ({url}):\n{snippet}" for _, cdp, url, snippet in results)
        else:
            response = "Sorry, I couldn’t find an answer. Try rephrasing your question."
        
        return JsonResponse({"response": response})
    return JsonResponse({"error": "Invalid request"}, status=400)