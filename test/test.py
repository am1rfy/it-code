import requests


def get_request_github(username: str):
    res = requests.get(f"https://github.com/{username}")
    return res


def get_user_url(response):
    return response.url


def check_username(response) -> bool:
    if response.status_code != 200:
        return True
    else:
        return False


def main():
    print("1 - Check username is availability\n2 - Exit\n")
    choose = int(input())

    match choose:
        case 1:
            username = input()
            if check_username(get_request_github(username)):
                print("This username is free\n")
            else:
                print(
                    f"This username is taken: {get_user_url(get_request_github(username))}\n")
            main()
        case 2:
            pass
        case 3:
            print("invalid code\n")
            main()


if __name__ == "__main__":
    main()
