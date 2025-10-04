import yaml

with open("cms/config/config.yaml", "r") as f:
    settings = yaml.safe_load(f)
