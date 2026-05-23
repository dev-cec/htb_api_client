# HTB API Client

A Python client library for accessing the [HackTheBox (HTB)](https://www.hackthebox.com) API. This library provides a clean Python interface to HTB's REST API, grouped around two main entities: **Universities** and **Users**.

## Requirements

- Python >= 3.14
- `requests` >= 2.34.2
- `python-dotenv` >= 1.2.2

## Installation

```bash
pip install python-dotenv requests
```

## Quick Start

```python
import os
from dotenv import load_dotenv
from htb_api_client import HTBAPIClient

load_dotenv()

client = HTBAPIClient(api_key=os.getenv("HTB_API_KEY"))

# Fetch universities
universities = client.get_universities(per_page=10, page=1)

# Fetch a user profile
user = client.get_user_basic_profile(user_id=1812190)
```

## Authentication

This client uses **Bearer token** authentication. Set your API key in a `.env` file:

```
HTB_API_KEY=your_api_key_here
```

A sample template is available in `.env.example`.

---

# API Endpoints

## University Endpoints

### `GET /v5/universities` — `get_universities(per_page=15, page=1)`

Retrieve a paginated list of universities on HackTheBox.

| Parameter     | Type   | Required | Default | Description                                |
|---------------|--------|----------|---------|--------------------------------------------|
| `per_page`    | `int`  | No       | `15`    | Number of universities returned per page   |
| `page`        | `int`  | No       | `1`     | Page number to retrieve                    |

**Returns:** A `dict` containing the list of universities under the `data` key, plus pagination metadata.

```python
response = client.get_universities(per_page=10, page=1)
```

---

### `GET /v4/university/my` — `get_my_university()`

Retrieve the university associated with the currently authenticated user.

**Parameters:** None.

**Returns:** A `dict` with the current user's university data.

```python
response = client.get_my_university()
```

---

### `GET /v4/university/profile/{university_id}` — `get_university_profile(university_id)`

Retrieve the full profile of a specific university by its ID.

| Parameter        | Type   | Required | Default | Description          |
|------------------|--------|----------|---------|----------------------|
| `university_id`  | `int`  | Yes      | —       | The university ID    |

**Returns:** A `dict` with the university's profile data.

```python
response = client.get_university_profile(university_id=1306)
```

---

### `GET /v5/universities/{university_id}/stats` — `get_university_stats(university_id)`

Retrieve statistics for a specific university.

| Parameter        | Type   | Required | Default | Description          |
|------------------|--------|----------|---------|----------------------|
| `university_id`  | `int`  | Yes      | —       | The university ID    |

**Returns:** A `dict` with the university's statistics.

```python
response = client.get_university_stats(university_id=1306)
```

---

### `GET /v4/university/members/{university_id}` — `get_university_members(university_id)`

Retrieve the list of members belonging to a specific university.

| Parameter        | Type   | Required | Default | Description          |
|------------------|--------|----------|---------|----------------------|
| `university_id`  | `int`  | Yes      | —       | The university ID    |

**Returns:** A `list[dict]` of member objects, or an empty list if none are found.

```python
response = client.get_university_members(university_id=1306)
```

---

### `GET /v4/university/invitations/{university_id}` — `get_university_invitations(university_id)`

Retrieve pending invitations for a specific university.

| Parameter        | Type   | Required | Default | Description          |
|------------------|--------|----------|---------|----------------------|
| `university_id`  | `int`  | Yes      | —       | The university ID    |

**Returns:** A `dict` containing invitations data.

```python
response = client.get_university_invitations(university_id=1306)
```

---

## User Endpoints

### `GET /v4/user/profile/basic/{user_id}` — `get_user_basic_profile(user_id)`

Retrieve the basic profile of a specific user.

| Parameter     | Type   | Required | Default | Description              |
|---------------|--------|----------|---------|--------------------------|
| `user_id`     | `int`  | Yes      | —       | The user's unique ID     |

**Returns:** A `dict` with the user's basic profile information.

```python
response = client.get_user_basic_profile(user_id=1812190)
```

---

### `GET /experience/v1/account/{account_uuid}` — `get_user_experience(account_uuid)`

Retrieve experience data for a user identified by their account UUID.

| Parameter        | Type    | Required | Default | Description                        |
|------------------|---------|----------|---------|------------------------------------|
| `account_uuid`   | `str`   | Yes      | —       | The user's account UUID            |

**Returns:** A `dict` with the user's experience data.

```python
response = client.get_user_experience(account_uuid="9bc206ad-e5ef-4a4d-a0dc-7b32b5db5e9e")
```

---

### `GET /v4/badges` — `get_badges()`

Retrieve all available badges on HackTheBox.

**Parameters:** None.

**Returns:** A `dict` containing badge categories and their associated badges.

```python
response = client.get_badges()
```

---

### `GET /v4/season/user/{user_id}/ranks` — `get_user_season_ranks(user_id)`

Retrieve the season rankings for a specific user.

| Parameter     | Type   | Required | Default | Description              |
|---------------|--------|----------|---------|--------------------------|
| `user_id`     | `int`  | Yes      | —       | The user's unique ID     |

**Returns:** A `dict` with the user's season rank data.

```python
response = client.get_user_season_ranks(user_id=1812190)
```

---

### `GET /v4/user/profile/progress/{progress_type}/{user_id}` — `get_user_progress(user_id, progress_type)`

Retrieve a user's progress within a specific HTB content type.

| Parameter        | Type   | Required | Default | Description                                                 |
|------------------|--------|----------|---------|-------------------------------------------------------------|
| `user_id`        | `int`  | Yes      | —       | The user's unique ID                                        |
| `progress_type`  | `str`  | Yes      | —       | One of: `machines`, `challenges`, `sherlocks`, `prolab`, `fortress` |

**Returns:** A `dict` with the user's progress for the specified content type.

```python
response = client.get_user_progress(user_id=1812190, progress_type="machines")
response = client.get_user_progress(user_id=1812190, progress_type="sherlocks")
```

---

### `GET /v4/users/{user_id}/profile/progress/chart` — `get_user_progress_chart(user_id, duration, content_type)`

Retrieve chart data for visualizing a user's progress over time.

| Parameter        | Type   | Required | Default          | Description                                                          |
|------------------|--------|----------|------------------|----------------------------------------------------------------------|
| `user_id`        | `int`  | Yes      | —                | The user's unique ID                                                 |
| `duration`       | `str`  | No       | `"1M"`           | Time window for the chart (e.g. `1M` for 1 month, `1Y` for 1 year)  |
| `content_type`   | `str`  | No       | `"machines"`     | Content type to chart (e.g. `machines`, `challenges`)                |

**Returns:** A `dict` containing chart data points.

```python
response = client.get_user_progress_chart(
    user_id=1812190,
    duration="1M",
    content_type="machines",
)
```

---

### `GET /v5/user/profile/activity/{user_id}` — `get_user_activity(user_id, per_page=5)`

Retrieve a user's recent activity feed on HackTheBox.

| Parameter     | Type   | Required | Default | Description                                 |
|---------------|--------|----------|---------|---------------------------------------------|
| `user_id`     | `int`  | Yes      | —       | The user's unique ID                        |
| `per_page`    | `int`  | No       | `5`     | Number of activity items per page           |

**Returns:** A `dict` containing the user's recent activity items.

```python
response = client.get_user_activity(user_id=1812190, per_page=10)
```

---

### `GET /v4/user/profile/badges/{user_id}` — `get_user_badges(user_id, rare=None)`

Retrieve the badges earned by a specific user.

| Parameter     | Type        | Required | Default | Description                                                 |
|---------------|-------------|----------|---------|-------------------------------------------------------------|
| `user_id`     | `int`       | Yes      | —       | The user's unique ID                                        |
| `rare`        | `int \| None` | No      | `None`  | Filter results by rarity level (optional)                   |

**Returns:** A `dict` with the user's badge data.

```python
response = client.get_user_badges(user_id=1812190)
response = client.get_user_badges(user_id=1812190, rare=8)
```

---

### `GET /v5/user/profile/content/{user_id}/counts` — `get_user_content_counts(user_id)`

Retrieve a breakdown of content type counts for a specific user (machines, challenges, sherlocks, writeups).

| Parameter     | Type   | Required | Default | Description              |
|---------------|--------|----------|---------|--------------------------|
| `user_id`     | `int`  | Yes      | —       | The user's unique ID     |

**Returns:** A `dict` containing counts per content category.

```python
response = client.get_user_content_counts(user_id=1812190)
```

---

## Running the Example

A complete usage demonstration is available in `pprint_example.py`:

```bash
# Set your API key first
echo "HTB_API_KEY=your_key" > .env

# Run the example
python pprint_example.py
```

This script calls every method in `HTBAPIClient` and pretty-prints the JSON responses to the console.
