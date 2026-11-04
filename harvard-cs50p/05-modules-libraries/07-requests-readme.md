# Python APIs

## 1. What is an API?

API stands for **Application Programming Interface**.

An API allows two different software applications or systems to communicate with each other.

For example:
- A Python application can communicate with a third-party service.
- The service receives a request and sends back a response.
- Our Python program can use the information returned by the API.

**Example:** A Python application can communicate with Apple's iTunes API to search for songs and retrieve information about them.

### JSON library- to encode or decode json
- https://docs.python.org/3/library/json.html 

## 2. Making API Calls Using Python

Python has a popular third-party package called `requests` that allows us to make HTTP requests to APIs.

The `requests` package is not included with Python, so we need to install it using `pip`.

### Documentation

- **Requests package:** [PyPI - Requests](https://pypi.org/project/requests/)
- **Requests documentation:** [Requests Documentation](https://requests.readthedocs.io/)

### Installation

Run the following command in your terminal:

```bash
python3 -m pip install requests
```

This installs the `requests` package so we can use it in our Python programs.

## 3. Example: iTunes Search API

We can use Apple's iTunes Search API to search for songs and retrieve information about them.

### API URL

Search for Weezer songs on iTunes - (https://itunes.apple.com/search?entity=song&limit=1&term=weezer)

The URL contains three parameters:

| Parameter | Purpose |
|---|---|
| `entity=song` | Searches for songs |
| `limit=1` | Returns one result |
| `term=weezer` | Searches for Weezer |

### Understanding the API Request

When we open the API URL in a browser:

1. The browser sends a request to Apple's API.
2. Apple's API processes the search request.
3. The API returns a response containing song information.
4. The response is provided in JSON format.

JSON stands for **JavaScript Object Notation**. It is a common format used to exchange data between applications.

## 4. Key Takeaways

- API stands for Application Programming Interface.
- APIs allow different applications and services to communicate.
- We can write Python code to send requests to third-party APIs.
- `requests` is a popular Python package for making HTTP requests.
- Install `requests` using `pip`.
- APIs commonly return data in JSON format.

**Remember:** An API acts as a bridge between our Python application and an external service.