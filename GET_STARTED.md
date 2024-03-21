<div align="center">

# Get Started Guide

</div>

In this document you can find all information to get started using the Horreum python library from scratch.

Right now the library is not published anywhere, therefore the only way to install it is from source.

---
## Prerequisites

* Python environment, e.g., `pyenv` or `miniconda` with all development dependencies installed:
```bash
pip install -r dev-requirements.txt
```

## Installation

Once all dependencies are installed simply build the `whl` by running:

```bash
poetry build
```

Now you can install the local build of `horreum` python client:

```bash
pip install dist/horreum-*.dev0-py3-none-any.whl --force-reinstall
```

## Usage

```bash
>>> import asyncio

# Import the constructor function
>>> from horreum.horreum_client import new_horreum_client

# Initialize the client
>>> client = await new_horreum_client(base_url="http://localhost:8080", username="..", password="..")

# Call the api using the underlying raw client, in this case retrieve the Horreum server version
>>> await client.raw_client.api.config.version.get()
VersionInfo(additional_data={}, privacy_statement=None, start_timestamp=1710864862253, version='0.13.0')
```

The previous api call is equivalent to the following `cURL`:
```bash
curl --silent -X 'GET' 'http://localhost:8080/api/config/version' -H 'accept: application/json' | jq '.'
```
