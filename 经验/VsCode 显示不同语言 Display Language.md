# VsCode显示不同语言的3种办法

## 第一种，配置"Configure Display Language"
按 Ctrl+Shift+P 到Command Palette，之后输入"Configure Display Language",可以选择不同语言。

## 第二种，修改argv.json里"locale"内容
`.vscode`目录下`argv.json`文件里面修改`"locale"`的内容 
*windows一般在当前用户的.vscdoe下*

Windows例子：
  - 修改`C:\Users\test\.vscode\argv.json的"locale"`
  - 修改为简体中文
    `"locale": "zh-cn"`
  - 修改为英语
    `"locale": "en"`
###第三种，加启动参数--locale
给vscode的启动文件code.exe加参数 --locale来指明语言。

*会忽略argv.json和"Configure Display Language"的设置*

如：
- `Code.exe --locale=en`
- `"D:\Microsoft VS Code\Code.exe"  --locale=en`
- `"D:\Microsoft VS Code\Code.exe" --locale=zh-cn`

*windows可以用快捷方式加参数。*

## 参考
 
	en	English(US)
	zh-cn	Simplified Chinese
	zh-tw	Traditional Chinese
	fr	French
	de	German
	it	Italian
	es	Spanish
	ja	Japanese
	ko	Korean
	ru	Russian
	bg	Bulgarian
	hu	Hungarian
	pt-br	Portuguese(Brazil)
	tr	Turkish
	pl	Polish
	cs	Czech