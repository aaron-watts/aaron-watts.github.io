<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="3.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" version="1.0" encoding="utf-8" indent="yes"/>
    <xsl:template match="/">
        <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
                <meta charset="utf-8"/>
                <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
                <title>
                    <xsl:value-of select="/rss/channel/title"/> RSS Feed
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
                    <aside>
                        Want more help getting set up with RSS? <a href="#help">Click here</a>
                    </aside>
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
                    <hr/>
                </main>
                <div id ="help">
                    <h3><em>HELP!</em> Getting Set Up with RSS</h3>
                    <p>
                        Gone are the days when RSS Feed Readers were bundled in to web
                        browsers as standard. The story tends to lean toward tech debt,
                        security, and social media being for more monetisable, depending
                        on who you ask. RSS is still widely used today, and I would bet
                        there are scores of bloggers using CMS systems to make content
                        who are unaware they even have an RSS feed.
                    </p>
                    <p>
                        If you want in on the fun, then you just need to get yourself
                        an RSS feed reader and start subscribing to your favourite
                        bloggers, youtube creators, subreddits, podcasts and more -
                        all without targeted advertising or accounts! Feed readers come
                        in a number of forms, the most superior being web extensions
                        for your browser (if it features autodiscover then it's
                        supercharged!), followed by certain email clients,
                        and even dedicated software for your computer or phone.
                    </p>
                    <p>
                        Here's a few of my favourite methods:
                    </p>
                    <ul>
                        <li><a href="https://addons.mozilla.org/en-GB/firefox/addon/feedbroreader/" target="_blank">Feedbro add-on for Firefox</a></li>
                        <li><a href="https://apps.nextcloud.com/apps/news" target="_blank">News app for Nextcloud</a></li>
                        <li><a href="https://www.thunderbird.net/en-GB/" target="_blank">Thunderbird email client</a></li>
                    </ul>
                </div>
                <footer>
                    <div>
                        Made by Hand. Powered by
                    </div>
                    <a href="https://pages.github.com/" target="_blank">
                        <img alt="https://pages.github.com/" src="/images/githubpages.svg"/>
                    </a>
                </footer>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
