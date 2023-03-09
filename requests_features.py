import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


user_agent = UserAgent()

headers = {
    "user-agent": user_agent.random
}

params = {
    "query": "some_query",
    "query2": "another_param",
}

cookies = {
    "cookie": "some_cookie"
}

url = "https://wtools.io/ru/check-my-user-agent"


def get_user_agent_data():
    response = requests.get(
        url,
        headers=headers,
        params=params,
        cookies=cookies
    )
    print(response.url)
    # soup = BeautifulSoup(response.text, "lxml")
    # user_agent_data = soup.find(id="resultInputpre").text
    # print(user_agent_data)


if __name__ == "__main__":
    get_user_agent_data()
