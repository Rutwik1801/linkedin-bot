import os
import requests

def post_to_linkedin(content):
    access_token = os.getenv("LINKEDIN_ACCESS_TOKEN")
    urn = "urn:li:person:YOUR_PERSON_URN"  # Replace with your LinkedIn URN

    payload = {
        "author": urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": content
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }

    response = requests.post("https://api.linkedin.com/v2/ugcPosts", json=payload, headers=headers)
    print(response.status_code, response.text)
