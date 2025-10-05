import yaml

with open("cms/config/config.yaml", "r") as f:
    settings = yaml.safe_load(f)

BASE_URL = settings['base_url']
ROOT = settings['root']
SUB_DIRECTORIES = settings['sub_directories'].split()
SITEMAP = settings['sitemap']
FEEDS = settings['feeds']
NAMESPACES = settings['namespaces']
