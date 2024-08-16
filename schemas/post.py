from datetime import datetime


def postEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": item.get("title"),
        "short_description": item.get("short_description"),
        "description": item.get("description"),
        "tags": item.get("tags"),
        "create_date": item.get("create_date").strftime("%Y-%m-%d %H:%M:%S") if item.get("create_date") else None,
        "update_date": item.get("update_date").strftime("%Y-%m-%d %H:%M:%S") if item.get("update_date") else None
    }


def postsEntity(entity) -> list:
    return [postEntity(item) for item in entity]
