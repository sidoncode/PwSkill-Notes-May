from bs4 import BeautifulSoup
# pip install beautifulsoup4

html_doc = """
<html>
    <head>
        <title>
        My Page
        </title>
    </head>
<body>
<h1>Welcome to My Page</h1>
<p class="content">This is a paragraph.</p>
<a href="http://example.com">Example Link</a>
</body></html>
"""

soup1 = BeautifulSoup(html_doc,'html.parser')

#extact title
print(soup1.title)