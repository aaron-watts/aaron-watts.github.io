from config.settings import FEEDS, NAMESPACES
from utils import xtree
from utils.files import path_to_url

def build_item(parent):
    item = xtree.child_element(parent, "item")
    return item

def build_rss(doc_tree):
    """
    Return RSS XML as tree object
    """
    ATOM_LINK_HREF = FEEDS['all']['link']
    TITLE = FEEDS['all']['title']
    LINK = FEEDS['all']['link']
    DESC = FEEDS['all']['description']

    rss = xtree.root_element(NAMESPACES['rss'], "rss")
    rss = xtree.set_attribute(rss, "version", "2.0")
    channel = xtree.child_element(rss, "channel")

    atom_link = xtree.child_element(channel, "atom:link")
    xtree.set_attribute(atom_link, "href", ATOM_LINK_HREF)
    xtree.set_attribute(atom_link, "rel", "self")
    xtree.set_attribute(atom_link, "type", "applications/rss+xml")

    xtree.child_element(channel, "title", TITLE)
    xtree.child_element(channel, "link", LINK)
    xtree.child_element(channel, "description", DESC)
    xtree.child_element(channel, "category", "Technology")
    # Populate Channel
    
    # Populate Items

    # 3 Feeds: All, Guides, Tech
    # {Titles and descriptions}
    #   <channel>
    #       <atom:link href="feed url" rel="self" type="applications/rss+xml"/>
    #       <title>{Title}</title>
    #       <description>{Description}</description>
    #       <category>Technology</category>
    #   </channel>
    # Articles exist in doc tree
    # For each article: extract data from soup:
    #   <item>
    #       <title>h1 text<title>
    #       <link>pathname to url</link>
    #       <pubDate>format date from time element</pubDate>
    #       <description>p#intro text</description>
    #       <guid>pathname to url</guid>
    #       <content:encoded>format main</content:encoded>
    #       <enclosure url="img['src']" length="0" type="image/jepg"/>
    #       <media:thumbnail url="img['src']" width="1920" height="1080"/>
    #       <media:content type="image/jpeg" url="img['src']"/>
    #   </item>
    return rss
