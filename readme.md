# gitlab-deploy-preview-bot

This bot is used to comment on all PRs a simple link to the deployment preview.

## Environment Variables

```yaml
GL_ACCESS_TOKEN: "<your access token>"
GL_URL: "https://gitlab.com"
GL_SECRET: "<webhook secret>"
GL_USER: "<your username>"
DEPLOY_URL_TEMPLATE: "The URL template to use for the deployment preview."
```

### Template variables

- `{project}`: The project name.
- `{branch}`: The branch name.
