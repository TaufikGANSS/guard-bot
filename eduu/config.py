import os.path

from typing import List, Optional


API_ID: int = 29717887
API_HASH: str = "dbceb604465fabeb200f43b2fd32770d"
TOKEN: str = "5575104615:AAEFK4-4P45PXDoWR5U4ONHNvpOZUYV3fd4"

log_chat: int = -1001873724459
sudoers: List[int] = [5615965845, 5615965845]
super_sudoers: List[int] = [5615965845, 5615965845]

prefix: List[str] = ["/", "!", ".", "$", "-"]

disabled_plugins: List[str] = []

WORKERS = 24

DATABASE_PATH = os.path.join("eduu", "database", "eduu.db")

TENOR_API_KEY: Optional[str] = "X9HD35B7ZGP6"

sudoers.extend(super_sudoers)

# notes

# 1. api_id & api_hash get from my.telegram.org
# 2. token fill with your bot_token get from @BotFather
# 3. log_chat fill with the chat id of a group that you should create for the bot logger
# 4. [optional] var disabled_plugins let you to disable an plugin to be loaded. Example:
# You don't want the youtube plugin to be loaded, then fill disabled_plugins var with youtube (or any name of the plugins file)
