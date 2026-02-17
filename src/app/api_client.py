from dataclasses import dataclass
from typing import Any
import requests

@dataclass
class ApiClient:
    base_url: str
    timeout_seconds: int = 10

    def get(self, path: str) -> requests.Response:
        url = f"{self.base_url}{path}"
        return requests.get(url, timeout=self.timeout_seconds)

    def get_json(self, path: str) -> tuple[int, dict[str, Any] | list[Any]]:
        resp = self.get(path)
        content_type = resp.headers.get("Content-Type", "")
        if "application/json" not in content_type:
            raise AssertionError(f"Expected JSON response, got Content-Type={content_type}")

        return resp.status_code, resp.json()

    def post_json(self, path: str, payload: dict[str, Any]) -> tuple[int, dict[str, Any] | list[Any]]:
        url = f"{self.base_url}{path}"
        resp = requests.post(url, json=payload, timeout=self.timeout_seconds)

        content_type = resp.headers.get("Content-Type", "")
        if "application/json" not in content_type:
            raise AssertionError(f"Expected JSON response, got Content-Type={content_type}")

        return resp.status_code, resp.json()

    def _json_or_fail(self, resp: requests.Response) -> dict[str, Any] | list[Any]:
        content_type = resp.headers.get("Content-Type", "")
        if "application/json" not in content_type:
            raise AssertionError(f"Expected JSON response, got Content-Type={content_type}")
        return resp.json()

    def put_json(self, path: str, payload: dict[str, Any]) -> tuple[int, dict[str, Any] | list[Any]]:
        url = f"{self.base_url}{path}"
        resp = requests.put(url, json=payload, timeout=self.timeout_seconds)
        return resp.status_code, self._json_or_fail(resp)

    def patch_json(self, path: str, payload: dict[str, Any]) -> tuple[int, dict[str, Any] | list[Any]]:
        url = f"{self.base_url}{path}"
        resp = requests.patch(url, json=payload, timeout=self.timeout_seconds)
        return resp.status_code, self._json_or_fail(resp)

    def delete(self, path: str) -> int:
        url = f"{self.base_url}{path}"
        resp = requests.delete(url, timeout=self.timeout_seconds)
        return resp.status_code