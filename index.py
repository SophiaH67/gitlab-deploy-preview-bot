from gidgetlab.aiohttp import GitLabBot
from os import getenv

bot = GitLabBot(getenv("GL_USER"))

# Register a callack for a webhook event
@bot.router.register("Issue Hook", action="open")
async def issue_opened_event(event, gl, *args, **kwargs):
  url = f"/projects/{event.project_id}/issues/{event.object_attributes['iid']}/notes"
  print(f"Posting to {url}")
  message = f"Thanks for the report @{event.data['user']['username']}! I will look into it ASAP! (I'm a bot)."
  await gl.post(url, data={"body": message})

bot.run()