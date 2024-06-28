#!/usr/bin/env python3
"""
Main file advance
"""

import requests

BASE_URL = "http://yourserver.com"  # Replace with your actual server URL


def register_user(email: str, password: str) -> None:
    url = f"{BASE_URL}/register"
    payload = {'email': email, 'password': password}
    response = requests.post(url, json=payload)
    assert response.status_code == 200, (
        f"Unexpected status code: {response.status_code}"
    )
    assert response.json() == {"email": email, "message": "user created"}, (
        f"Unexpected response: {response.json()}"
    )


def log_in_wrong_password(email: str, password: str) -> None:
    url = f"{BASE_URL}/login"
    payload = {'email': email, 'password': password}
    response = requests.post(url, json=payload)
    assert response.status_code == 401, (
        f"Unexpected status code: {response.status_code}"
    )
    assert response.json() == {"error": "wrong password"}, (
        f"Unexpected response: {response.json()}"
    )


def log_in(email: str, password: str) -> str:
    url = f"{BASE_URL}/login"
    payload = {'email': email, 'password': password}
    response = requests.post(url, json=payload)
    assert response.status_code == 200, (
        f"Unexpected status code: {response.status_code}"
    )
    session_id = response.cookies.get("session_id")
    assert session_id is not None, "Session ID not found in response cookies"
    return session_id


def profile_unlogged() -> None:
    url = f"{BASE_URL}/profile"
    response = requests.get(url)
    assert response.status_code == 403, (
        f"Unexpected status code: {response.status_code}"
    )
    assert response.json() == {"error": "forbidden"}, (
        f"Unexpected response: {response.json()}"
    )


def profile_logged(session_id: str) -> None:
    url = f"{BASE_URL}/profile"
    cookies = {'session_id': session_id}
    response = requests.get(url, cookies=cookies)
    assert response.status_code == 200, (
        f"Unexpected status code: {response.status_code}"
    )
    assert "email" in response.json(), (
        f"Unexpected response: {response.json()}"
    )


def log_out(session_id: str) -> None:
    url = f"{BASE_URL}/logout"
    cookies = {'session_id': session_id}
    response = requests.post(url, cookies=cookies)
    assert response.status_code == 200, (
        f"Unexpected status code: {response.status_code}"
    )
    assert response.json() == {"message": "logout successful"}, (
        f"Unexpected response: {response.json()}"
    )


def reset_password_token(email: str) -> str:
    url = f"{BASE_URL}/reset_password"
    payload = {'email': email}
    response = requests.post(url, json=payload)
    assert response.status_code == 200, (
        f"Unexpected status code: {response.status_code}"
    )
    reset_token = response.json().get("reset_token")
    assert reset_token is not None, "Reset token not found in response"
    return reset_token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    url = f"{BASE_URL}/update_password"
    payload = {
        'email': email,
        'reset_token': reset_token,
        'new_password': new_password
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200, (
        f"Unexpected status code: {response.status_code}"
    )
    assert response.json() == {"email": email, "message": "password updated"}, (
        f"Unexpected response: {response.json()}"
    )



EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
