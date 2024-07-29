import gzip
from pathlib import Path
import pytest
from typing import Generator
from importlib.resources import files, as_file


@pytest.fixture(scope="session", autouse=True)
def data_file_path() -> Generator[str, None, None]:
    with as_file(files("geotz.data")) as data_dir:
        gzip_resource = data_dir.joinpath("geonames_all_countries_sorted.tsv.gz")
        data_resource = data_dir.joinpath("geonames_all_countries_sorted.tsv")

        if not data_resource.exists():
            _unzip(gzip_resource, data_resource)

        yield str(data_resource)


def _unzip(gzpath: Path, destpath: Path) -> None:
    with gzip.open(gzpath, "rb") as input, open(destpath, "wb") as output:
        output.writelines(input)
