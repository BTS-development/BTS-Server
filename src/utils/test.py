import os

_BASE = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(_BASE)
ROOT_DIR = os.path.dirname(BASE_DIR)

CONFIG_SECRET_DIR = os.path.join(ROOT_DIR, ".config_secret")

CONFIG_SECRET_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, "settings_common.json")
CONFIG_SECRET_DEV_FILE = os.path.join(CONFIG_SECRET_DIR, "settings_dev.json")
CONFIG_SECRET_DEPLOY_FILE = os.path.join(CONFIG_SECRET_DIR, "settings_deploy.json")

config_secret_common = json.loads(open(CONFIG_SECRET_COMMON_FILE).read())
