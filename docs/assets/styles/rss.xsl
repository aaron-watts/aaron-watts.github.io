<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="3.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" version="1.0" encoding="utf-8" indent="yes"/>
    <xsl:template match="/">
        <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
                <title>
                    <xsl:value-of select="/rss/channel/title"/> RSS Feed
                </title>
                <!--<link href="/images/apple-touch-icon.png" rel="apple-touch-icon" sizes="180x180"/>
                <link href="/images/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
                <link href="/images/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
                <link href="/site.webmanifest" rel="manifest"/>-->
                <link href="/assets/styles/style.css" rel="stylesheet"/>
            </head>
            <body>
                <header>
                    <nav class="breadcrumbs">
                        <span class="host"><a href="/home">aaronwatts@dev</a></span>:<span class="path">/<a href="/rss">rss</a>/feed $</span>
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
                        <hr/>
                        <div class="article">
                            <h2>
                                <xsl:value-of select="title"/>
                            </h2>
                            <date>
                                <xsl:value-of select="substring(pubDate,1,16)"/>
                           </date>
                            <div>
                                <a>
                                    <xsl:attribute name="href">
                                        <xsl:value-of select="link"/>
                                    </xsl:attribute>
                                    Go to article
                                </a>
                            </div>
                           <p class="description">
                                <xsl:value-of select="description"/>
                            </p>
                            <date></date>
                        </div>
                    </xsl:for-each>
                </main>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
