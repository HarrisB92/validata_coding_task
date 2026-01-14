from __future__ import annotations

import json
import logging
import os
from typing import Any, Dict

import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def _print_response(label: str, response: requests.Response) -> None:
    try:
        payload: Dict[str, Any] | list[Any] | str = response.json()
    except ValueError:
        payload = response.text
    logger.info("%s -> %s: %s", label, response.status_code, json.dumps(payload, default=str))


def main() -> None:
    base_url = os.getenv("API_BASE_URL", "http://127.0.0.1:5000/api")

    create_resp = requests.post(
        f"{base_url}/banks",
        json={"name": "Validata Bank", "location": "Seattle"},
        timeout=10,
    )
    _print_response("CREATE", create_resp)
    if create_resp.status_code != 201:
        return

    bank_id = create_resp.json()["id"]

    list_resp = requests.get(f"{base_url}/banks", timeout=10)
    _print_response("LIST", list_resp)

    get_resp = requests.get(f"{base_url}/banks/{bank_id}", timeout=10)
    _print_response("GET", get_resp)

    update_resp = requests.put(
        f"{base_url}/banks/{bank_id}",
        json={"name": "Validata Bank Updated", "location": "Portland"},
        timeout=10,
    )
    _print_response("UPDATE", update_resp)

    delete_resp = requests.delete(f"{base_url}/banks/{bank_id}", timeout=10)
    _print_response("DELETE", delete_resp)


if __name__ == "__main__":
    main()
