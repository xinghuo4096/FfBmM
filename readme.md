# FFBMM

## 名称

ffbmm firefoxbookmarksmove移动工具。

## 起因

有一个firefox的书签的导出文件，json格式，类似“bookmarks-2022-01-21.json”，里有1500多条书签。
书签中有的时同一个网站不同内容，且分布在不同的若干层书签文件夹里。
类似:
计算机->c#->c#正则表达式说明书
项目->xxxx项目->要用的技术->c#正则表达式的应用
博客->新浪技术博客->xxxx的博客->c#的正则表达式测试例子
mozlz4 edit

## 需求

把同一个网站不同内容的所有书签，移动到一个书签文件夹里，这个文件夹已经建好。
移动方式有两种
1、移动时保持原来的
firefox的bookmark导出后，

## 背景

在做一个知识管理平台下，
其中元数据管理里
需要完成浏览器书签类型的元数据抽取和更新。
针对firefox导出的书签，进行元数据抽取和更新。
其中一个工具，移动firefox书签。

Metadata即描述资料
的资料，可用来协助对网络电子资源的辨识、描述、指示其位置的任何资

## 资料

## 资料一微软的meta

```html
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
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
