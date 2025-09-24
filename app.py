from fastapi import FastAPI, Request, HTTPException, Depends, status
from disc
from discord_webhook import DiscordWebhook, DiscordEmbed

app = FastAPI()

# Root route
@app.get("/")
def root():
    return {"message": "Welcome to the root route!"}

@app.post("/api/sellauth", status_code=status.HTTP_200_OK)
async def sellauth(request: Request):
    embed = DiscordEmbed(title="Test", description=f"Headers: {request.headers}\nBody: {request.body()}")
    send_webhook_message("https://discord.com/api/webhooks/1418947147046588526/Lxs1FBxpDCiDrSyrszabrxtWTmeawWz9IVQuUdfIvuHN-KU2rAK9z9x4pLj2T-4Tsyqg", "", embed)

def send_webhook_message(webhook_url, content, embed):
    webhook = DiscordWebhook(url=webhook_url, content=content)
    webhook.add_embed(embed)
    response = webhook.execute()
    if response.status_code in [200, 201, 202, 203, 204, 205, 206, 207]:
        pass
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
