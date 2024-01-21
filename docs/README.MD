## Dad Jokes!

If you don't have a dad, but you want to hear funny dad jokes told by your favorite AI Voice Generator, now you can!

## Get Started
Fork and Clone Dadjokes from Github and create a new .env file with the keys:

```
OPENAI_API_KEY = "YOUR_API_KEY"
ELEVENLABS_API_KEY = "YOUR_ELEVENLABS_KEY"
```
replaceing the line in quotes with your actual api key. NOTE: Ensure that your .env file is in the .gitignore file to avoid sharing your API key with others. By Default in this project, it is, but the golden rule is Trust but Verify.


## Important Steps:
For this project, you will need to navigate to the Dadjokes directory and in your terminal/command line run "docker-compose build", and then "docker-compose up". After this, you will also need to have FFmpeg installed. On Mac, you can use "brew install ffmpeg" in the command line, or if you're on Windows go to the official site @ https://ffmpeg.org/
