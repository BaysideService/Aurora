from __future__ import annotations

import os
from typing import Any, Dict, List

from aurora_apis.http_client import http_get, http_post


class RedditClient:
    """
    Minimal Reddit client for ticker mention scraping using OAuth2.

    This uses the application-only client_credentials flow and requires:

    - REDDIT_CLIENT_ID
    - REDDIT_CLIENT_SECRET
    - REDDIT_USER_AGENT
    """

    TOKEN_URL = "https://www.reddit.com/api/v1/access_token"
    BASE_URL = "https://oauth.reddit.com"

    def __init__(
        self,
        client_id: str | None = None,
        client_secret: str | None = None,
        user_agent: str | None = None,
    ) -> None:
        self.client_id = client_id or os.getenv("REDDIT_CLIENT_ID")
        self.client_secret = client_secret or os.getenv("REDDIT_CLIENT_SECRET")
        self.user_agent = user_agent or os.getenv("REDDIT_USER_AGENT")
        self._access_token: str | None = None

    def _get_token(self) -> str:
        if self._access_token:
            return self._access_token

        if not (self.client_id and self.client_secret and self.user_agent):
            raise RuntimeError("Reddit credentials are not fully configured")

        data = {"grant_type": "client_credentials"}
        headers = {"User-Agent": self.user_agent}
        payload = http_post(
            self.TOKEN_URL,
            data=data,
            headers=headers,
            auth_basic=(self.client_id, self.client_secret),
        )
        token = payload["access_token"]
        self._access_token = token
        return token

    def search_subreddit(self, subreddit: str, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        token = self._get_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "User-Agent": self.user_agent or "aurora-reddit-client",
        }
        params = {"q": query, "limit": limit, "sort": "new", "restrict_sr": True}
        url = f"{self.BASE_URL}/r/{subreddit}/search"
        data = http_get(url, headers=headers, params=params)
        children = data.get("data", {}).get("children", [])
        return [c.get("data", {}) for c in children]
