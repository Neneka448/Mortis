import os

global_config = {
    "ARK_API_KEY": os.environ.get("ARK_API_KEY"),
    "AK": os.environ.get("VOLC_ACCESSKEY"),
    "SK": os.environ.get("VOLC_SECRETKEY")
}
