<?xml version="1.0" encoding="utf"?>
<xsl:stylesheet version="3.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" version="1.0" encoding="utf-8" indent="yes"/>
    <xsl:template match="/">
        <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
                <link href="/assets/styles/style.css" rel="stylesheet"/>
            </head>
            <body>
                <header>
                    <nav class="breadcrumbs">
                        <span class="host">aaronwatts@dev</span>:<span class="path">~ $ feed.xml</span>
                    </nav>
                    <h1>
                        <xsl:value-of select="/rss/channel/title"/>
                    </h1>
                    <p>
                        If you found your way here, then it's likely you know what you're
                        doing. But in case you're new to RSS feeds, or you stumbled here
                        by mistake, you just need to copy this page's url, and paste it
                        into your favourite feed reader to get new articles sent to you
                        as soon as they get published!
                    </p>
                </header>
                <main>
                    <xsl:for-each select="/rss/channel/item">
                        <div class="article">
                            <h2>
                                <xsl:value-of select="title"/>
                            </h2>
                            <a>
                                <xsl:attribute name="href">
                                    <xsl:value-of select="link"/>
                                </xsl:attribute>
                                Go to article
                            </a>
                            <br/>
                            <date>
                               <xsl:value-of select="pubDate"/>
                            </date>
                            <p class="description">
                                <xsl:value-of select="description"/>
                            </p>
                        </div>
                    </xsl:for-each>
                </main>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
