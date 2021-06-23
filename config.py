# --------------------------------------------- #
# Plugin Name           : DiscordAirdropBot     #
# Author Name           : fabston               #
# File Name             : config.py             #
# --------------------------------------------- #

# Enable / disable the airdrop
airdrop_live = True

# Discord
bot_token = "<YOUR BOT TOKEN>"  # More: https://www.writebots.com/discord-bot-token/
bot_command_prefix = "!"  # Bot prefix: Example: !airdrop, ?airdrop, $airdrop etc.
log_channel = 0  # Channel ID. Example: 654874484842692660
admins = [""]  # Discord User ID's. Admins are able to execute command "!airdroplist"
airdrop_cap = 100  # Max airdrop submissions that are being accepted

# MySQL Database
mysql_host = "localhost"
mysql_db = "DiscordAirdropBot"
mysql_user = "AirdropUser"
mysql_pw = "<YOUR PASSWORD>"

texts = {
    "airdrop_start": "The airdrop didn't start yet. Please come back later.",
    "airdrop_max_cap": "ℹ️ The airdrop reached its max cap.",
    "airdrop_walletused": "⚠️ That address has already been used. Use a different one.",
    "airdrop_confirmation": "✅ Your address has been added to airdrop list.",
}
