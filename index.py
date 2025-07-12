from bot.generate_post import generate_linkedin_post
from bot.post_to_linkedin import post_to_linkedin

if __name__ == "__main__":
    content = generate_linkedin_post()
    post_to_linkedin(content)
