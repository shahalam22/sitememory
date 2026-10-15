"""Smoke tests for the initial package."""


def test_package_imports() -> None:
    import sitememory

    assert sitememory.__name__ == "sitememory"
