from importlib.metadata import version


def get_client_version():
    return version("horreum")
