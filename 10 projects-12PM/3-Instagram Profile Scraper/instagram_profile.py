import requests

def scrape_instagram_profile(username):
    url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "x-ig-app-id": "936619743392459"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_data = response.json().get('data', {}).get('user', {})
        profile_info = {
            "username": user_data.get("username"),
            "full_name": user_data.get("full_name"),
            "biography": user_data.get("biography"),
            "followers": user_data.get("edge_followed_by", {}).get("count"),
            "following": user_data.get("edge_follow", {}).get("count"),
            "posts": user_data.get("edge_owner_to_timeline_media", {}).get("count"),
            "profile_pic_url": user_data.get("profile_pic_url_hd"),
            "is_verified": user_data.get("is_verified"),
            "is_private": user_data.get("is_private")
        }
        return profile_info
    else:
        print(f"Failed to retrieve data for {username}. Status code: {response.status_code}")
        return None

# Example usage
if __name__ == "__main__":
    username = "kmanojmca"  # Replace with the target username
    profile_data = scrape_instagram_profile(username)
    if profile_data:
        for key, value in profile_data.items():
            print(f"{key.capitalize()}: {value}")
