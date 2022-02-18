# gitlab-deploy-preview-bot

This bot is used to comment on all PRs a simple link to the deployment preview.

## Environment Variables

```yaml
GITLAB_TOKEN: "The token to use to authenticate to GitLab."
GITLAB_URL: "The URL to the GitLab instance."
GITLAB_PROJECT: Comma separated list of projects to listen to.
GITLAB_DEPLOY_URL_TEMPLATE: "The URL template to use for the deployment preview."
```

### Template variables

- `{project}`: The project name.
- `{branch}`: The branch name.
