# 🤖 LinkedIn Post Bot

This is an automated LinkedIn posting bot that uses the [ChatGPT API](https://platform.openai.com/docs) to generate daily posts and the [LinkedIn API](https://learn.microsoft.com/en-us/linkedin/) to publish them to your personal LinkedIn profile. It runs every morning at **9 AM** using **GitHub Actions**.

---

## 🚀 Features

- 🧠 **AI-Generated Content**: Uses ChatGPT to generate unique and relevant daily LinkedIn posts.
- 🔗 **Automatic Posting**: Publishes directly to your LinkedIn profile using the LinkedIn REST API.
- ⏰ **Scheduled Automation**: Leveraged via GitHub Actions to run daily at 9 AM.
- 📄 **Customizable Prompts**: Easily modify prompt logic to control the tone, topic, or format of posts.

---

## 🛠️ Tech Stack

- **OpenAI API** - for content generation
- **LinkedIn API** - for posting to your profile
- **GitHub Actions** - for daily automation
- **Python** 

---

## 🔐 Environment Variables

To run the bot, set the following secrets in your GitHub repository:

| Variable Name         | Description                                      |
|-----------------------|--------------------------------------------------|
| `OPENAI_API_KEY`      | Your OpenAI API key                              |
| `LINKEDIN_ACCESS_TOKEN` | OAuth token with `w_member_social` scope       |
| `LINKEDIN_PROFILE_URN` | Your LinkedIn URN or ID (e.g. `urn:li:person:xyz`) |

---

## 🗓️ GitHub Workflow

The workflow is triggered daily at 9:00 AM UTC

      - name: Run the bot
        run: node index.js
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          LINKEDIN_ACCESS_TOKEN: ${{ secrets.LINKEDIN_ACCESS_TOKEN }}
          LINKEDIN_PROFILE_ID: ${{ secrets.LINKEDIN_PROFILE_ID }}
