# Web Pages

> Web pages are written in HTML [\[1\]](#footnotes), a **markup language**.

<small>(HTML is an extension of SGML (Standard Generalized Markup Language) an ISO standard for defining markup languages.)</small>

HTML consists of a set of **tags** which describe the content they enclose. The first tag in a pair is the **opening tag** whilst the other is the **closing tag**.

*For example:* `<blockquote>This is a quote!</blockquote>`

Some tags are less obvious like `<b>`, `<i>` and `<p>` (bold, italics and paragraph). This *reduces* the human **readability of the language**.

**NB:** Some tags are deprecated (no longer in use) like `<u>` for underlining.

HTML pages are often styled (look+formatting) using **CSS (cascading style sheets)** and most browsers support **JavaScript - an interpreted programming language**.

*Example:*

```
<html>
    <head>
        <title>An Example Page</title>
    </head>
    <body>
        <h1>A heading</h1>
        <p>A paragraph of text w/ <b> a bold section </b>
        </p>
     </body>
</html>
```
is rendered as...

![Rendered HTML](https://www.filepicker.io/api/file/LdP7H06TTbOSwllMbPnZ) 

###### More tags:
+ `<a>` - Anchor tag, used for links
+ `<input type="x">` - Input *X* can be text, checkbox etc
+ `<img>` - Image
+ `<em>` - Emphasis

HTML is **standardized** by W3 [\[2\]](#footnotes). Standardization has both *advantages and disadvantages*.

###### Advantages:

+ Pages *should* look the same in all browsers.
+ Easy to develop for many devices.
+ Consistent experience for the user.
+ Ensures features keep 'up to date'.

###### Disadvantages:

+ Some browser manufacturers may choose not to support some tags or add their own.
+ Changes to the standard can be slow.


To avoid having to write HTML by hand tools such as Adobe Dreamweaver & Microsoft Publisher can be used which output HTML in the background whilst the user uses WYSIWYG [\[4\]](#footnotes) tools to style the document.
---

HTML is transferred to the browser over HTTP [\[3\]](#footnotes) a text based protocol.

*An HTTP Session:*
** Browser request **
```
GET / HTTP/1.1
Host: www.google.co.uk
```
** Google response **
```
HTTP/1.1 200 OK
Date: Sat, 25 May 2013 15:05:06 GMT
Content-Type: text/html; charset=UTF-8
... 
<!-- HTML of page here -->
```

---
<a id="footnotes"></a>
[1] HTML is an acronym for Hypertext markup language
[2] The World Wide Web Consortium - [HTML Specification](http://www.w3.org/html/wg/drafts/html/master/)
[3] HTTP is an acronym for Hypertext transfer protocol
[4] WYSIWYG - **W**hat **Y**ou **S**ee **I**s **W**hat **Y**ou **G**et. A term used to refer to publishing tools where the user can see the style of the final document before it is published. e.g. Word *etc*.
