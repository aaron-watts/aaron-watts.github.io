<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
xmlns:sm="http://www.sitemaps.org/schemas/sitemap/0.9">
    <xsl:output method="html" version="1.0" encoding="utf-8" indent="yes"/>
    <xsl:template match="/">
        <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
                <meta charset="utf-8"/>
                <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
                <title>
                    AWD - Sitemap
                </title>
                <link href="/images/apple-touch-icon.png" rel="apple-touch-icon" sizes="180x180"/>
                <link href="/images/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
                <link href="/images/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
                <link href="/site.webmanifest" rel="manifest"/>
                <link href="https://aaronwatts.dev/feed.xml" rel="alternate" title="AaronWattsDev RSS Feed - All" type="application/rss+xml"/>
                <link href="https://aaronwatts.dev/guides/feed.xml" rel="alternate" title="AaronWattsDev RSS Feed - Guides" type="application/rss+xml"/>
                <link href="https://aaronwatts.dev/tech/feed.xml" rel="alternate" title="AaronWattsDev RSS Feed - Tech" type="application/rss+xml"/>
                <link href="/assets/styles/style.css" rel="stylesheet"/>
            </head>
            <body>
                <header>
                    <nav class="breadcrumbs">
                        <span class="host"><a href="/home">aaronwatts@dev</a></span>:<span class="path">~ $ sitemap.xml</span>
                    </nav>
                    <h1>Sitemap</h1>
                </header>
                <main>
                    <ul>
                        <xsl:for-each select="sm:urlset/sm:url">
                            <li>
                                <xsl:variable name="link" select="substring(sm:loc,23)"/>
                                <a href="{$link}">
                                    <xsl:value-of select="$link"/>
                                </a>
                            </li>
                        </xsl:for-each>
                    </ul>
                </main>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
