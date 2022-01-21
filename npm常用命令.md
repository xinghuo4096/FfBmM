
# 常用命令

* 查看镜像源使用状态：  
`npm get registry`  
结果：  
`https://registry.npmjs.org/`

# 使用 nrm 切换镜像源

npm install -g nrm
nrm ls
看一下  

```cmd结果
  npm ---------- https://registry.npmjs.org/
  yarn --------- https://registry.yarnpkg.com/
  tencent ------ https://mirrors.cloud.tencent.com/npm/
  cnpm --------- https://r.cnpmjs.org/
  taobao ------- https://registry.npmmirror.com/
  npmMirror ---- https://skimdb.npmjs.com/registry/
```

换腾讯源

```cmd
nrm use tencent
npm get registry
https://mirrors.cloud.tencent.com/npm/
```
