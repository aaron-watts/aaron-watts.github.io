import yaml

with open("cms/config/config.yaml", "r") as f:
    settings = yaml.safe_load(f)

BASE_URL = settings['base_url']
ROOT = settings['root']
HOME = settings['home']
SUB_DIRECTORIES = settings['sub_directories'].split()
SELECTORS = settings['selectors']
SITEMAP = settings['sitemap']
RSS = settings['rss']
FEEDS = settings['feeds']
NAMESPACES = settings['namespaces']
