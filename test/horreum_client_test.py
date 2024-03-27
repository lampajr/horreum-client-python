import pytest

from horreum.horreum_client import new_horreum_client, HorreumClient


@pytest.fixture()
async def anonymous_client() -> HorreumClient:
    print("Setting up anonymous client")
    client = await new_horreum_client(base_url="http://localhost:8080")
    return client


@pytest.mark.asyncio
async def test_check_client_version(anonymous_client: HorreumClient):
    version = HorreumClient.version()
    # TODO: we could load the toml and check the versions match
    assert version != ""
