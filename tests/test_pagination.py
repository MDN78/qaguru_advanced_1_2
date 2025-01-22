import pytest
import requests


def test_total_page_and_size_in_users(app_url):
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


def test_users_in_pages(app_url):
    first_page = {"page": 2, "size": 4}
    second_page = {"page": 3, "size": 4}
    response_1 = requests.get(f"{app_url}/api/users/", params=first_page)
    response_2 = requests.get(f"{app_url}/api/users/", params=second_page)
    data_1 = response_1.json()
    data_2 = response_2.json()
    assert data_1['items'][1] != data_2['items'][1]
