# FfBmM

## 名称FfBmM

FfBmM firefox bookmarks move移动工具。

## 起因

有一个firefox的书签备份文件，json格式，类似“bookmarks-2022-01-21.json”，里有1500多条书签。
有些书签记录的是同一个网站的不同内容，且分布在不同的书签文件夹里。

### 例子，书签结构例子

计算机->c#->c#正则表达式说明书
项目->xxxx项目->要用的技术->c#正则表达式的应用
博客->新浪技术博客->xxxx的博客->c#的正则表达式测试例子

## 需求

把记录同一个网站不同内容的所有书签，移动到一个书签文件夹里，这个文件夹已经建好。

### 移动方式有两种

1. 移动后，保持原来的文件夹结构。
2. 移动后，都在一个文件夹里。

### 共同都需要的

- 把原文件夹结构，作为 标签 更新到书签里。

### 移动后效果例子

新文件夹
`"C#技术"`

1. 移动后时，保持原来的文件夹结构。

    ```书签
    c#技术->计算机->c#->c#正则表达式说明书
    c#技术->项目->xxxx项目->要用的技术->c#正则表达式的应用
    c#技术->博客->新浪技术博客->xxxx的博客->c#的正则表达式测试例子
    ```

2. 移动后，都在一个文件夹里。

    ```书签
    c#技术->c#正则表达式说明书
    c#技术->c#正则表达式的应用
    c#技术->c#的正则表达式测试例子
    ```

3. 共同都需要的
    "c#的正则表达式测试例子",这个书签增加4个 标签

    ```书签
    "c#技术" "博客" "新浪技术博客" "xxxx的博客"
    ```

## 背景

来源一个知识管理平台构想，其中元数据管理里，需要完成浏览器书签类型的元数据抽取和更新。
针对firefox导出的书签，进行元数据抽取和更新。
其中一个工具，移动firefox书签。

## 资料

### Metadata

Metadata 即描述资料的资料，可用来协助对网络电子资源的辨识、描述、指示其位置的任何资

### MS微软的meta

```html

<meta property="og:title" content="正则表达式语言 - 快速参考" /><meta property="og:type" content="website" />
<meta property="og:url" content="https://docs.microsoft.com/zh-cn/dotnet/standard/base-types/regular-expression-language-quick-reference" />
<meta property="og:description" content="此快速参考介绍了如何使用正则表达式模式匹配输入文本。 模式具有一个或多个字符文本、运算符或构造。" />
<meta property="og:image" content="https://docs.microsoft.com/dotnet/media/dot-net-cross-platform.png" />
<meta property="og:image:alt" content="正则表达式语言 - 快速参考 | Microsoft Docs" />
<meta name="twitter:card" content="summary" />
<meta name="twitter:site" content="@docsmsft" />
<meta name="color-scheme" content="light dark">
<meta name="apiPlatform" content="dotnet" />
<meta name="author" content="adegeo" />
<meta name="bilingual_type" content="hover over" />
<meta name="breadcrumb_path" content="/dotnet/breadcrumb/toc.json" />
<meta name="depot_name" content="VS.core-docs" />
<meta name="description" content="此快速参考介绍了如何使用正则表达式模式匹配输入文本。 模式具有一个或多个字符文本、运算符或构造。" />
<meta name="document_id" content="16d4698e-4220-c422-a554-8a481803d240" />
<meta name="document_version_independent_id" content="f0e3b82a-8d81-ad9e-97fc-efb92f7d0d38" />
<meta name="gitcommit" content="https://github.com/dotnet/docs.zh-cn/blob/df24caa7c06680f7f6e6bd5a4a8332e615e9b3ea/docs/standard/base-types/regular-expression-language-quick-reference.md" />
<meta name="locale" content="zh-cn" />
<meta name="ms.assetid" content="930653a6-95d2-4697-9d5a-52d11bb6fd4c" />
<meta name="ms.author" content="adegeo" />
<meta name="ms.contentlocale" content="zh-CN" />
<meta name="ms.date" content="03/30/2017" />
<meta name="ms.devlang" content="dotnet" />
<meta name="ms.lasthandoff" content="11/18/2020" />
<meta name="ms.locfileid" content="94818799" />
<meta name="ms.openlocfilehash" content="1b261211997837e8664ea60e9210a7f0517f7a9f" />
<meta name="ms.prod" content="dotnet-fundamentals" />
<meta name="ms.sourcegitcommit" content="965a5af7918acb0a3fd3baf342e15d511ef75188" />
<meta name="ms.topic" content="how-to" />
<meta name="ms.translationtype" content="HT" />
<meta name="original_content_git_url" content="https://github.com/dotnet/docs.zh-cn/blob/live/docs/standard/base-types/regular-expression-language-quick-reference.md" />
<meta name="page_type" content="conceptual" />
<meta name="pdf_url_template" content="https://docs.microsoft.com/pdfstore/zh-cn/VS.core-docs/{branchName}{pdfName}" />
<meta name="recommendations" content="true" />
<meta name="schema" content="Conceptual" />
<meta name="search.mshattr.devlang" content="csharp" />
<meta name="show_latex" content="true" />
<meta name="site_name" content="Docs" />
<meta name="toc_rel" content="../../fundamentals/toc.json" />
<meta name="uhfHeaderId" content="MSDocsHeader-DotNet" />
<meta name="updated_at" content="2021-09-15 11:11 AM" />
<meta name="word_count" content="3526" />
```

### intel的meta

```html

<meta name="X-Server" content=INTE-T1/>
<meta http-equiv="X-UA-Compatible" content="IE=Edge"/>
<meta http-equiv="x-dns-prefetch-control" content="on"/>
<!--[if lte IE 9]>
<meta http-equiv="X-UA-Compatible" content="IE=9"/>
<![endif]-->
<meta name="apple-itunes-app" content="app-id=587995732"/>
<meta name="twitter:app:id:googleplay" content="com.intel.ark"/>
<meta name="twitter:card" content="summary"/>
<meta name="twitter:app:id:ipad" content="id587995732"/>
<meta name="description" content="英特尔® 产品规格、特性和兼容性快速参考指南和代码名称解码器。比较产品，包括处理器、台式机主板、服务器产品和网络产品。"/>
<meta name="language" content="zh"/>
<meta name="twitter:app:name:googleplay" content="Intel® ARK (Product Specs)"/>
<meta name="twitter:app:id:iphone" content="id587995732"/>
<meta name="twitter:creator" content="@IntelSupport"/>
<meta name="twitter:site" content="@IntelSupport"/>
<meta name="twitter:app:name:ipad" content="Intel® ARK (Product Specs)"/>
<meta name="google-play-app" content="app-id=com.intel.ark"/>
<meta name="twitter:app:name:iphone" content="Intel® ARK (Product Specs)"/>
<meta property="og:image" content="http://ark.intel.com/inc/images/fusionmobile/intel-logo-blue.png"/>
<meta property="og:type" content="article"/>
<meta property="og:sitename" content="Intel® ARK (Product Specs)"/>
<meta property="og:title" content="英特尔产品规格"/>
<meta property="og:url" content="https://www.intel.cn/content/www/cn/zh/ark.html"/>
<meta property="og:description" content="英特尔® 产品规格、特性和兼容性快速参考指南和代码名称解码器。比较产品，包括处理器、台式机主板、服务器产品和网络产品。"/>

<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">

```

### 人民网pepole

```html
<meta name="renderer" content="webkit" />
<meta http-equiv="X-UA-Compatible" content="IE=Edge" />
<meta name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0" />
<meta name="keywords" content="" />
<meta name="description" content="发展政府性融资担保，是促进实体经济发展的重要逆周期调节工具。在近日举行的全国财政工作视频会议上，财政部提出2022年将继续实行小微企业融资担保降费奖补。政府性融资担保体系如何自上而下撬动更多担保资金去" />
<meta name="copyright" content="人民网版权所有" />
<meta name="filetype" content="0">
<meta name="publishedtype" content="1">
<meta name="pagetype" content="1">
<meta name="catalogs" content="1004">
<meta name="contentid" content="32337124">
<meta name="publishdate" content="2022-01-22">
<meta name="author" content="1464">
<meta name="editor" content="">
<meta name="source" content="来源：人民日报">
<meta name="sourcetype" content="">
```

### google

```html
<meta name="viewport" content="width=device-width,initial-scale=1,minimum-scale=1.0" />
<meta name="google" content="notranslate" />
<meta name="format-detection" content="telephone=no" />
<meta name="google-site-verification" content="sp-RFHUl69ePlsCUjwgzU3Y0H0P5dxzzaszJOtwaDNQ" />
<meta name="mobile-web-app-capable" content="yes" />
<meta name="apple-mobile-web-app-capable" content="yes" />
<meta name="application-name" content="Google Translate" />
<meta name="apple-mobile-web-app-title" content="Google Translate" />
<meta name="theme-color" content="#4285F4" />
<meta name="msapplication-tap-highlight" content="no" />
```

### baidu百度

```html
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
<meta content="always" name="referrer" />
<meta name="theme-color" content="#ffffff" />
<meta name="description" content="全球领先的中文搜索引擎、致力于让网民更便捷地获取信息，找到所求。百度超过千亿的中文网页数据库，可以瞬间找到相关的搜索结果。" />
```
