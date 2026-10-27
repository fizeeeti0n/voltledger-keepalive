
import os
import urllib.request
from datetime import datetime, timezone

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "https://voltledger-api.onrender.com/api/health"
)

def main():
    timestamp = datetime.now(timezone.utc).isoformat()

    try:
        request = urllib.request.Request(
            BACKEND_URL,
            headers={"User-Agent": "VoltLedger-KeepAlive/1.0"}
        )

        with urllib.request.urlopen(request, timeout=90) as response:
            print(f"[{timestamp}] Backend status: {response.status}")
            response.read()

            if response.status != 200:
                raise RuntimeError(
                    f"Unexpected HTTP status: {response.status}"
                )

    except Exception as error:
        print(f"[{timestamp}] Ping failed: {error}")
        raise

if __name__ == "__main__":
    main()
