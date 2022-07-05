import asyncio
from pathlib import Path

from src.config import load_config
from src.downloader import download_raw_data


async def main():
    config = load_config()
    await download_raw_data(config, Path("data"))


if __name__ == "__main__":
    asyncio.run(main())
