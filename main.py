import os
import requests


def get_extension(image_url: str) -> str | None:
    extensions: list[str] = ['.png', '.jpeg', '.jpg', '.gif', ',svg']
    for ext in extensions:
        if ext in image_url:
            return ext
        
