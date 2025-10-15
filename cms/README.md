# CMS module

## Content Management System for aaronwatts.dev

### Usage

```python3 cms/run.py```

#### 1. Runs Tests

Check HTML documents for common errors or things that will cause issues with file generation. Exits if errors are found.

#### 2. Compiles and Sorts Documents

Will scrape all HTML article files for relevant data and sort by date and category

#### 3. Builds Sitemap

Generates `sitemap.xml` with links sorted alphabetically and by directory

#### 4. Builds RSS Feeds

Generates `feed.xml`, `guides/feed.xml` and `tech/feed.xml`. Limits number of feed entries based on settings in `cms/config.yaml`

#### 5. Adds XSL to XML files

Inserts XSL template instruction to XML files

#### 6. Generates Home and Index Pages

Regenerates `home.html`, `guides/index/html` and `tech/index.html` to include newly created articles


