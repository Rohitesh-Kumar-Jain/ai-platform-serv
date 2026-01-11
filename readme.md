python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

## Hig Level Design
<img width="1146" height="611" alt="Screenshot 2026-01-11 at 11 06 27 PM" src="https://github.com/user-attachments/assets/67913470-d5e8-40c3-8856-92210a41cc57" />

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
