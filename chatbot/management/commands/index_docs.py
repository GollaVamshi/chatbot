from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
import re
from chatbot.models import Documentation

CDP_URLS = {
    "Segment": "https://segment.com/docs/connections/sources/",
    "mParticle": "https://docs.mparticle.com/",
    "Lytics": "https://docs.lytics.com/",
    "Zeotap": "https://docs.zeotap.com/"  # Verify this URL
}

class Command(BaseCommand):
    help = "Indexes CDP documentation"

    def handle(self, *args, **kwargs):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://www.google.com/"
        }
        
        for cdp, url in CDP_URLS.items():
            self.stdout.write(f"Indexing {cdp}...")
            try:
                response = requests.get(url, headers=headers, timeout=10)
                response.raise_for_status()
                
                self.stdout.write(f"URL resolved to: {response.url}")  # Log final URL after redirects
                soup = BeautifulSoup(response.content, "html.parser")
                body = soup.find('body')
                content = body.get_text(separator=" ") if body else soup.get_text(separator=" ")
                content = re.sub(r"\s+", " ", content).strip()

                self.stdout.write(f"Extracted content preview: {content[:200]}...")  # Log first 200 chars
                if not content:
                    self.stdout.write(self.style.WARNING(f"No content found for {cdp}. Page might be dynamic or empty."))
                    continue

                Documentation.objects.update_or_create(
                    cdp=cdp,
                    url=url,
                    defaults={"content": content[:5000]}
                )
                self.stdout.write(self.style.SUCCESS(f"Indexed {cdp} successfully."))
            except requests.exceptions.HTTPError as e:
                self.stdout.write(self.style.ERROR(f"HTTP Error for {cdp}: {e}"))
            except requests.exceptions.RequestException as e:
                self.stdout.write(self.style.ERROR(f"Failed to index {cdp}: {e}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Unexpected error for {cdp}: {e}"))
        
        self.stdout.write(self.style.SUCCESS("Indexing complete."))