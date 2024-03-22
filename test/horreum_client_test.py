import httpx
import pytest
from kiota_abstractions.authentication import BaseBearerTokenAuthenticationProvider
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.headers_collection import HeadersCollection
from kiota_abstractions.method import Method
from kiota_abstractions.request_information import RequestInformation

from horreum.horreum_client import new_horreum_client, HorreumClient
from horreum.raw_client.api.test.test_request_builder import TestRequestBuilder
from horreum.raw_client.models.protected_type_access import ProtectedType_access
from horreum.raw_client.models.test import Test

username = "user"
password = "secret"


@pytest.fixture()
async def anonymous_client() -> HorreumClient:
    print("Setting up anonymous client")
    client = await new_horreum_client(base_url="http://localhost:8080")
    return client


def test_check_client_version(anonymous_client: HorreumClient):
    version = HorreumClient.version()
    # TODO: we could load the toml and check the versions match
    assert version != ""
