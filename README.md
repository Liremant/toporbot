# ToporBot 🔥

A Telegram userbot that transforms any message into aggressive tabloid-style headlines using Google's Gemini AI. Perfect for adding dramatic flair to mundane conversations!

## Features

- 🎯 **Reply-based processing**: Reply to any message with `/topor` or `\topor`
- ⚡ **Aggressive headlines**: Converts boring text into sensational tabloid-style headlines
- 🤖 **AI-powered**: Uses Google Gemini 1.5 Flash for content generation
- 📱 **Userbot**: Runs on your own Telegram account
- 🔥 **Customizable prompts**: Easy to modify the generation style

## Example

**Input message:**
```
The website is experiencing some lag issues
```

**ToporBot output:**
```
⚡️SERVERS ARE FUCKED⚡️SYSADMINS SCREWED UP⚡️WEBSITE IS TOTALLY BROKEN⚡️
```

## Prerequisites

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) package manager
- Telegram account
- Google AI API key

## Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd toporbot
   ```

2. **Install dependencies using uv:**
   ```bash
   uv sync
   ```

3. **Get your Telegram API credentials:**
   - Visit [my.telegram.org](https://my.telegram.org)
   - Create a new application
   - Note down your `API_ID` and `API_HASH`

4. **Get your Google AI API key:**
   - Visit [Google AI Studio](https://ai.google.dev)
   - Create a new API key
   - Note down your `GEMINI_API_KEY`

5. **Create a `.env` file:**
   ```env
   API_ID=your_telegram_api_id
   API_HASH=your_telegram_api_hash
   GEMINI_API_KEY=your_gemini_api_key
   ```

## Usage

1. **Start the bot:**
   ```bash
   uv run python main.py
   ```

2. **In Telegram:**
   - Reply to any message with `/topor` or `\topor`
   - The bot will generate aggressive tabloid-style headlines
   - Use `/start` to see available commands

## Commands

- `/topor` or `\topor` - Reply to a message to generate tabloid headlines
- `/start` - Show help and available commands

## Project Structure

```
toporbot/
├── main.py           # Main bot code
├── pyproject.toml    # Project dependencies
├── uv.lock          # Dependency lock file
├── .env             # Environment variables (create this)
├── .gitignore       # Git ignore rules
└── README.md        # This file
```

## Configuration

The bot uses environment variables for configuration:

| Variable | Description | Required |
|----------|-------------|----------|
| `API_ID` | Telegram API ID from my.telegram.org | Yes |
| `API_HASH` | Telegram API Hash from my.telegram.org | Yes |
| `GEMINI_API_KEY` | Google AI API key from ai.google.dev | Yes |

## Customization

You can modify the `TOPOR_PROMPT` variable in `main.py` to change the generation style, add different languages, or adjust the aggressiveness level.

## Dependencies

- `pyrogram` - Telegram client library
- `google-generativeai` - Google Gemini AI client
- `python-dotenv` - Environment variable management

## Legal Notice

⚠️ **Important**: This is a userbot that runs on your personal Telegram account. Be aware of Telegram's Terms of Service regarding automated actions. Use responsibly and at your own risk.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is provided as-is for educational purposes. Please respect Telegram's Terms of Service and use responsibly.

## Troubleshooting

**Bot doesn't respond:**
- Check if all environment variables are set correctly
- Ensure your Telegram session is active
- Verify API keys are valid

**Authentication errors:**
- Delete the `.session` files and restart the bot
- Double-check your API_ID and API_HASH

**Gemini API errors:**
- Verify your GEMINI_API_KEY is correct
- Check if you have available quota on Google AI

## Support

If you encounter issues, please check:
1. All environment variables are correctly set
2. You have internet connection
3. Your API keys are valid and have sufficient quota

---

Made with 🔥 and aggressive headlines
