import requests


def fetch_json_placeholder_data(url_postfix):
    base_url = "https://jsonplaceholder.typicode.com/"
    full_url = base_url + url_postfix

    try:
        response = requests.get(full_url)
        return response.json()
    except requests.RequestException as error:
        print("Error fetching data:", error)
        return []


if __name__ == "__main__":
    posts = fetch_json_placeholder_data("posts/10")
    print("Posts:", posts)
    users = fetch_json_placeholder_data("users/2")
    print("Users:", users)
