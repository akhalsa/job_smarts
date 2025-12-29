---
name: beautifulsoup
description: A Python library for parsing HTML and XML documents. Use it to extract data from HTML strings using CSS selectors and navigation methods.
---

# Beautiful Soup 4 Quickstart (No Installation Section)

Beautiful Soup is a Python library for extracting data from HTML and XML. It turns markup into a structured parse tree so you can navigate, search, and modify it using Pythonic syntax. It works with Python’s built-in parser or third-party parsers like `lxml` and `html5lib`.

---

## First Example

```python
from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">
Once upon a time there were three little sisters:
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
</p>
</body></html>
'''

soup = BeautifulSoup(html, "html.parser")
```

`soup` now holds a parsed document you can work with.

---

## Pretty Print the Parsed Document

```python
print(soup.prettify())
```

---

## Basic Navigation

Access tags directly:

```python
soup.title
soup.title.string
soup.title.parent.name
soup.p
soup.a
```

Access attributes like a dictionary:

```python
soup.p["class"]
soup.a["href"]
```

---

## Finding Elements

### Find first match
```python
soup.find("a")
```

### Find all matches
```python
soup.find_all("a")
```

### Search by attribute
```python
soup.find(id="link3")
```

### Extract all links
```python
for link in soup.find_all("a"):
    print(link.get("href"))
```

### Get all visible text
```python
print(soup.get_text())
```

---

## CSS Selectors (Very Powerful)

Beautiful Soup supports CSS selectors via `select()`:

```python
soup.select("a.sister")
soup.select("#link1")
soup.select("p > a")
```

Get only the first:

```python
soup.select_one(".sister")
```

---

## Working with Text

Search by exact text or regex:

```python
import re
soup.find(string=re.compile("Dormouse"))
```

Extracting text only:

```python
soup.get_text(strip=True)
```

Iterate text cleanly:

```python
for text in soup.stripped_strings:
    print(text)
```

---

## Modifying the Tree

Change tag name or attributes:

```python
tag = soup.p
tag.name = "div"
tag["class"] = "newclass"
```

Replace contents:

```python
tag.string = "New text"
```

Append content:

```python
tag.append(" More text")
```

Create new tags:

```python
new = soup.new_tag("a", href="http://example.com")
new.string = "Example"
tag.append(new)
```

Remove elements:

```python
tag.decompose()   # delete entirely
tag.extract()     # remove but keep reference
```

---

## Parsers: Which One?

Pass parser choice as the 2nd argument:

| Parser | Syntax | Pros | Cons |
|-------|--------|------|------|
| Built-in | `"html.parser"` | Included, decent | Slower, less tolerant |
| lxml HTML | `"lxml"` | Fastest, strong | External dependency |
| lxml XML | `"xml"` | Best XML | Needs lxml |
| html5lib | `"html5lib"` | Most accurate | Slow |

Example:

```python
BeautifulSoup(html, "lxml")
```

---

## Common Tasks

### Get all URLs
```python
urls = [a["href"] for a in soup.find_all("a", href=True)]
```

### Get all paragraphs
```python
[p.get_text() for p in soup.find_all("p")]
```

### Handle multi-value attributes like class
```python
soup.find_all("p", class_="story")
```

---

## Pretty Output vs Raw Output

Pretty formatted:

```python
print(soup.prettify())
```

Raw HTML:

```python
str(soup)
```

Bytes:

```python
soup.encode("utf-8")
```

---

## Parsing Only What You Need

Use **SoupStrainer** for speed:

```python
from bs4 import BeautifulSoup, SoupStrainer
only_a = SoupStrainer("a")

soup = BeautifulSoup(html, "html.parser", parse_only=only_a)
```

---

## Encoding / Messy HTML Help

Force encoding:

```python
BeautifulSoup(html, from_encoding="utf-8")
```

Fix mixed encodings:

```python
from bs4 import UnicodeDammit
UnicodeDammit.detwingle(data)
```

---

## Debugging

If parsing fails or output looks wrong:

1️⃣ Try another parser  
2️⃣ Validate HTML  
3️⃣ Use:

```python
from bs4.diagnose import diagnose
diagnose(html)
```

---

## Summary

Beautiful Soup is ideal for **screen scraping, quick extraction, messy HTML, and flexible tree navigation**. Pair with `requests` or browser automation as needed.
