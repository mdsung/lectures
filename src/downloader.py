from pathlib import Path

import requests
import yaml


def download(data_url: str, filename: str, target_path: Path) -> str:
    r = requests.get(data_url + filename, stream=True, verify=True)
    with open(Path(target_path, filename), "wb") as f:
        f.write(r.content)
    return filename


if __name__ == "__main__":
    with open("config.yaml", "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    download(config["url"], config["train_file"], Path("data"))
    download(config["url"], config["test_file"], Path("data"))
