python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

## Hig Level Design

<img width="1135" height="546" alt="Screenshot 2026-01-12 at 1 17 58 AM" src="https://github.com/user-attachments/assets/b922255a-e996-4ff9-9bbe-8b08db43745d" />


### ai-platform-serv
* basically a cold-started serverless VM

So when someone hits site:

```
Cloudflare → Backend
           → backend is asleep   
           → cloud provider boots it
           → ~40–60 seconds
           → request finally reaches LLM
```

That’s why users see “no response” or timeouts sometimes.

### Cloudflare Worker

Security perimeter
* Blocks bots and scrapers
* Shields your origin IP
* Hides your backend from the internet
* Can reject abusive requests before they reach your VM
* Can rate-limit per IP, country, ASN

Edge execution layer
Handles CORS
* Handles OPTIONS preflight

AI firewall
* Your robots.txt and “no AI training” rules live here.
* Even if someone scrapes your site, they never reach your AI API.

### Future Scope for Scale
Single backend -> Auto-scaling pool
Cold starts	-> Always-warm replicas
1 region ->	Multi-region
Manual limits	-> Rate limits + quotas
In-memory conversation	-> Redis / Postgres
