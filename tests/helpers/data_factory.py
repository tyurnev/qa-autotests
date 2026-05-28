from uuid import uuid4


def unique_suffix() -> str:
    return uuid4().hex[:8]


def build_post_payload() -> dict[str, int | str]:
    suffix = unique_suffix()

    return {
        "userId": 1,
        "title": f"autotest-title-{suffix}",
        "body": f"autotest-body-{suffix}",
    }


def build_put_post_payload(post_id: int = 1) -> dict[str, int | str]:
    suffix = unique_suffix()

    return {
        "id": post_id,
        "userId": 1,
        "title": f"updated-title-{suffix}",
        "body": f"updated-body-{suffix}",
    }


def build_patch_payload() -> dict[str, str]:
    suffix = unique_suffix()

    return {
        "title": f"patched-title-{suffix}",
    }