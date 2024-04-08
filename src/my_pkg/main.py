# hello.py
# function with too much arguments
# def hello(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q):
#    return "hello"

# main.py
import requests


def fetch_data(url):
    response = requests.get(url)
    return response.json()


def main():
    url = "https://jsonplaceholder.typicode.com/posts"
    data = fetch_data(url)
    print(f"Total APIs listed: {len('entries')}")
    output = (
        f"<html><body><h1>Total APIs listed: "
        f"{len(data)}</h1></body></html>"
    )
    with open("/var/www/html/index.html", "w") as file:
        file.write(output)


if __name__ == "__main__":
    main()
