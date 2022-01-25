# vscode python使用中问题

## 导入路径问题

### 问题

如果代码在src下，默认sys.path路径没有src，增加办法

### 解决

1. .vscode目录下settings.json
"python.envFile": "${workspaceFolder}/.env"
2. 文件.env
里面 PYTHONPATH=./src
