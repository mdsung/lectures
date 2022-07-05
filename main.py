import asyncio
from pathlib import Path

from src.config import load_config
from src.downloader import download_raw_data
from src.preprocess import (
    create_feature_tensor,
    create_label_tensor,
    dummify_columns,
    fill_null_values,
    merge_train_test_data,
    normalize_numeric_columns,
    read_csv_files,
)


def main():
    config = load_config()
    download_raw_data(config, Path("data"))

    train_df, test_df = read_csv_files(
        Path(f"data/{config['train_file']}"),
        Path(f"data/{config['test_file']}"),
    )
    data = (
        merge_train_test_data(train_df, test_df)
        .pipe(normalize_numeric_columns)
        .pipe(fill_null_values)
        .pipe(dummify_columns)
    )

    n_train = train_df.shape[0]

    train_X, test_X = create_feature_tensor(data, n_train)
    train_y = create_label_tensor(train_df)


if __name__ == "__main__":
    main()
