import pytest
from typing import Generator
from importlib.resources import files, as_file


@pytest.fixture(scope="session", autouse=True)
def data_file_path() -> Generator[str, None, None]:
    data_resource = files("geotz.data").joinpath("geonames_all_countries_sorted.tsv")
    with as_file(data_resource) as data_resource_path:
        yield str(data_resource_path)
