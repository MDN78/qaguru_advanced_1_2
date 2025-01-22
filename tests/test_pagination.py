import pytest
import requests


def test_page_and_size_in_users(app_url):
    response = requests.get(f"{app_url}/api/users/")
    data = response.json()
    assert data["total"] == 12
    assert data["page"] == 1
    assert data["size"] == 50


@pytest.mark.parametrize("page, size", [(1, 12), (2, 6), (4, 3)])
def test_page_size(app_url, page, size):
    response = requests.get(f"{app_url}/api/users/", params={"page": page, "size": size})
    data = response.json()
    assert page == data['page']
    assert size == data['size']
    assert len(data["items"]) == size
