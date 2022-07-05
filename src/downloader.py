import asyncio
import time
from pathlib import Path

import requests

from src.config import load_config


async def download_file(data_url: str, filename: str, target_path: Path):
    r = requests.get(data_url + filename, stream=True, verify=True)
    with open(Path(target_path, filename), "wb") as f:
        f.write(r.content)


async def download_raw_data(config: dict[str, str], target_path: Path) -> None:
    asyncio.gather(
        download_file(config["url"], config["train_file"], target_path),
        download_file(config["url"], config["test_file"], target_path),
    )


if __name__ == "__main__":
    start = time.perf_counter()
    config = load_config()
    asyncio.run(download_raw_data(config, Path("data")))
    print(f"Downloaded in {time.perf_counter() - start} seconds")
