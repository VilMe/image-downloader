import os
import requests


def get_extension(image_url: str) -> str | None:
    extensions: list[str] = ['.png', '.jpeg', '.jpg', '.gif', ',svg']
    for ext in extensions:
        if ext in image_url:
            return ext
        

def download_image(image_url: str, name: str, folder: str = None):
    if ext := get_extension(image_url):
        if folder:
            image_name: str = f'{folder}/{name}{ext}'
        else:
            image_name; str = f'{name}{ext}'
    else:
        raise Exception('Image extension could not ve located')


    