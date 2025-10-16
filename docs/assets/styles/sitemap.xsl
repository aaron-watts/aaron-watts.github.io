<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
xmlns:sm="http://www.sitemaps.org/schemas/sitemap/0.9">
    <xsl:output method="html" version="1.0" encoding="utf-8" indent="yes"/>
    <xsl:template match="/">
        <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
                <link href="/assets/styles/style.css" rel="stylesheet"/>
            </head>
            <body>
                <header>
                    <nav class="breadcrumbs">
                        <span class="host">aaronwatts@dev</span>:<span class="path">~ $ sitemap.xml</span>
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
