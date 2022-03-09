from gidgetlab.aiohttp import GitLabBot
from os import getenv

bot = GitLabBot(getenv("GL_USER"))
deploy_template = getenv("DEPLOY_URL_TEMPLATE")

# Register a callack for a webhook event on merge requests
@bot.router.register("Merge Request Hook", action="open")
async def merge_opened_event(event, gl, *args, **kwargs):
  url = f"/projects/{event.project_id}/merge_requests/{event.object_attributes['iid']}/discussions"

  branch = event.object_attributes['source_branch']
  branch = branch.replace("/", "")
  # Truncate the branch name to 12 characters
  if len(branch) > 12:
    branch = branch[:12]
  # Convert to lowercase
  branch = branch.lower()

  deploy_url = deploy_template.format(branch=branch, project=event.object_attributes['source']['name'])
  # Replace " " with "-", because " " is not allowed in a URL
  deploy_url = deploy_url.replace(" ", "-")
  
  message=f"Thanks💖✨for your👆💁 issue🚀🦄!\n\nDeploy📦 URL🌐 when it's ready🤑⏰: [🙈Click Me!🤫]({deploy_url})"
  await gl.post(url, data={"body": message})

bot.run()