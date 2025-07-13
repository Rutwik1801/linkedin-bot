import requests
import os
import json
from generate_post import generate_linkedin_post

# Your post text
post_text = generate_linkedin_post()

headers = {
    "Authorization": f"Bearer ${os.getenv("LINKEDIN_ACCESS_TOKEN")}",
    "Content-Type": "application/json",
    "X-Restli-Protocol-Version": "2.0.0"
}

post_data = {
    "author": os.getenv("URN"),
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": post_text
            },
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
}

response = requests.post(
    "https://api.linkedin.com/v2/ugcPosts",
    headers=headers,
    data=json.dumps(post_data)
)

if response.status_code == 201:
    print("✅ Post created successfully!")
else:
    print("❌ Failed to create post.")
    print(f"Status code: {response.status_code}")
    print(response.text)
