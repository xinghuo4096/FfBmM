# git连接服务器，以gitee为例子

## 先取得项目的ssh地址

- 如：`https://gitee.com/项目名称xxx/FFBMM.git`

## 查看本机git可链接的远程服务器

- `git remote -v`

## 生成ssh的key

- `ssh-keygen -t ed25519 -C "项目名称xxx`
- 生成的文件一般在用户.ssh目录下
如：Windows系统生成文件在当前用户`.ssh`目录下。
- *特别建议：密码最好为空*

## 测试能否能链接gitee

- `ssh -T git@gitee.com`
- 会生成`known_hosts`文件

## git增加remote
