# BackupRepos
list/clone/update user repos

说明
---

列出指定用户的所有公共仓库(public repos)

克隆远程仓库到本地，或更新本地已存在仓库。

请求次数限制
---

未认证请求每小时最高60次，认证后限制为每小时5000次请求。

具体参见[Rate limiting](https://developer.github.com/v3/#rate-limiting)

可以配置`personal access token`提高请求次数。