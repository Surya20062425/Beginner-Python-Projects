"""
URL Shortener
Difficulty: Hard
Concepts: Hashing, File I/O, CLI + Optional Flask
"""

import json
import os
import hashlib
import secrets
import string
from urllib.parse import urlparse

try:
    from flask import Flask, request, redirect, render_template_string
    FLASK_AVAILABLE = True
except ImportError:
    FLASK_AVAILABLE = False

DATA_FILE = "url_mappings.json"


class URLShortener:
    """Manages URL shortening and retrieval."""

    def __init__(self):
        self.mappings = {}
        self.clicks = {}
        self.load()

    def load(self):
        """Load mappings from JSON file."""
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r") as f:
                    data = json.load(f)
                    self.mappings = data.get("mappings", {})
                    self.clicks = data.get("clicks", {})
            except (json.JSONDecodeError, IOError):
                pass

    def save(self):
        """Save mappings to JSON file."""
        with open(DATA_FILE, "w") as f:
            json.dump({
                "mappings": self.mappings,
                "clicks": self.clicks
            }, f, indent=2)

    def _generate_code(self, url, length=6):
        """Generate a short code using hash + random fallback."""
        # Try hash-based first
        hash_obj = hashlib.md5(url.encode())
        code = hash_obj.hexdigest()[:length]
        
        # Collision check
        if code in self.mappings and self.mappings[code] != url:
            # Fall back to random string
            chars = string.ascii_letters + string.digits
            while True:
                code = ''.join(secrets.choice(chars) for _ in range(length))
                if code not in self.mappings:
                    break
        return code

    def shorten(self, url, custom_alias=None):
        """Shorten a URL. Returns short code or None on error."""
        if not self._validate_url(url):
            return None, "Invalid URL format"

        # Check if already shortened
        for code, mapped_url in self.mappings.items():
            if mapped_url == url:
                return code, "Already exists"

        if custom_alias:
            if custom_alias in self.mappings:
                return None, "Custom alias already taken"
            if not custom_alias.isalnum() or len(custom_alias) < 3:
                return None, "Alias must be 3+ alphanumeric characters"
            code = custom_alias
        else:
            code = self._generate_code(url)

        self.mappings[code] = url
        self.clicks[code] = 0
        self.save()
        return code, "Success"

    def lookup(self, code):
        """Get original URL and increment click count."""
        if code in self.mappings:
            self.clicks[code] = self.clicks.get(code, 0) + 1
            self.save()
            return self.mappings[code]
        return None

    def get_stats(self):
        """Return all URLs with click statistics."""
        return {
            code: {
                "url": url,
                "clicks": self.clicks.get(code, 0),
                "short_url": f"http://localhost:5000/{code}"
            }
            for code, url in self.mappings.items()
        }

    @staticmethod
    def _validate_url(url):
        """Basic URL validation."""
        parsed = urlparse(url)
        return bool(parsed.scheme in ('http', 'https') and parsed.netloc)


def run_cli():
    """Run the CLI version."""
    shortener = URLShortener()

    print("=" * 50)
    print("🔗 URL SHORTENER")
    print("=" * 50)

    while True:
        print("\n📂 Menu:")
        print("  1. ➕ Shorten URL")
        print("  2. 🔍 Lookup URL")
        print("  3. 📊 View all URLs & stats")
        print("  4. 🚪 Exit")

        choice = input("\nChoose (1-4): ").strip()

        if choice == "1":
            url = input("\nEnter URL to shorten: ").strip()
            custom = input("Custom alias (optional, press Enter to skip): ").strip() or None

            code, msg = shortener.shorten(url, custom)
            if code:
                short_url = f"http://localhost:5000/{code}" if FLASK_AVAILABLE else f"short:{code}"
                print(f"\n✅ {msg}")
                print(f"   Short URL: {short_url}")
                print(f"   Code: {code}")
            else:
                print(f"\n❌ {msg}")

        elif choice == "2":
            code = input("\nEnter short code: ").strip()
            original = shortener.lookup(code)
            if original:
                print(f"\n✅ Original URL: {original}")
                print(f"   Clicks: {shortener.clicks.get(code, 0)}")
            else:
                print("\n❌ Code not found.")

        elif choice == "3":
            stats = shortener.get_stats()
            if not stats:
                print("\n📭 No URLs stored yet.")
                continue

            print(f"\n{'─' * 70}")
            print(f"  {'Code':<12}{'Clicks':<8}{'URL'}")
            print(f"{'─' * 70}")
            for code, data in stats.items():
                url = data["url"][:45] + "..." if len(data["url"]) > 45 else data["url"]
                print(f"  {code:<12}{data['clicks']:<8}{url}")
            print(f"{'─' * 70}")
            print(f"  Total: {len(stats)} URL(s)")

        elif choice == "4":
            print("\n👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice.")


def run_flask_app():
    """Run the Flask web interface."""
    if not FLASK_AVAILABLE:
        print("Flask not installed. Run: pip install flask")
        return

    app = Flask(__name__)
    shortener = URLShortener()

    HTML_TEMPLATE = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>URL Shortener</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; }
            h1 { color: #333; }
            input[type="url"], input[type="text"] { width: 100%; padding: 10px; margin: 10px 0; font-size: 16px; }
            button { padding: 10px 20px; background: #007bff; color: white; border: none; cursor: pointer; }
            button:hover { background: #0056b3; }
            .result { margin-top: 20px; padding: 15px; background: #e8f5e9; border-radius: 5px; }
            .error { background: #ffebee; }
            table { width: 100%; margin-top: 20px; border-collapse: collapse; }
            th, td { padding: 10px; text-align: left; border-bottom: 1px solid #ddd; }
        </style>
    </head>
    <body>
        <h1>🔗 URL Shortener</h1>
        <form method="POST">
            <input type="url" name="url" placeholder="Enter URL to shorten" required>
            <input type="text" name="alias" placeholder="Custom alias (optional)">
            <button type="submit">Shorten</button>
        </form>
        {% if result %}
        <div class="result {% if error %}error{% endif %}">
            <strong>{{ result }}</strong>
            {% if short_url %}<br><a href="{{ short_url }}">{{ short_url }}</a>{% endif %}
        </div>
        {% endif %}
        
        <h2>📊 All URLs</h2>
        <table>
            <tr><th>Code</th><th>Clicks</th><th>URL</th></tr>
            {% for code, data in stats.items() %}
            <tr>
                <td><a href="/{{ code }}">{{ code }}</a></td>
                <td>{{ data.clicks }}</td>
                <td>{{ data.url[:50] }}{% if data.url|length > 50 %}...{% endif %}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """

    @app.route("/", methods=["GET", "POST"])
    def index():
        result = None
        short_url = None
        error = False

        if request.method == "POST":
            url = request.form.get("url", "").strip()
            alias = request.form.get("alias", "").strip() or None

            code, msg = shortener.shorten(url, alias)
            if code:
                short_url = f"{request.host_url}{code}"
                result = f"Shortened! Code: {code}"
            else:
                result = msg
                error = True

        return render_template_string(
            HTML_TEMPLATE,
            result=result,
            short_url=short_url,
            error=error,
            stats=shortener.get_stats()
        )

    @app.route("/<code>")
    def redirect_url(code):
        original = shortener.lookup(code)
        if original:
            return redirect(original)
        return "URL not found", 404

    print("\n🌐 Starting Flask server...")
    print("   Open: http://127.0.0.1:5000")
    app.run(debug=True, port=5000)


def main():
    """Main entry point."""
    print("=" * 50)
    print("🔗 URL SHORTENER")
    print("=" * 50)

    if FLASK_AVAILABLE:
        print("\nChoose mode:")
        print("  1. 💻 CLI mode")
        print("  2. 🌐 Web mode (Flask)")
        mode = input("\nSelect (1-2): ").strip()
    else:
        print("\nFlask not installed. Running CLI mode.")
        print("Install with: pip install flask")
        mode = "1"

    if mode == "2":
        run_flask_app()
    else:
        run_cli()


if __name__ == "__main__":
    main()
