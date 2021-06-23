# --------------------------------------------- #
# Plugin Name           : DiscordAirdropBot     #
# Author Name           : fabston               #
# File Name             : main.py               #
# --------------------------------------------- #

from io import BytesIO
from time import gmtime, strftime

import discord
import eth_utils
import pymysql
from discord.ext import commands

import config

bot = commands.Bot(command_prefix=config.bot_command_prefix)


def get_connection():
    connection = pymysql.connect(
        host=config.mysql_host,
        user=config.mysql_user,
        password=config.mysql_pw,
        db=config.mysql_db,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True,
    )
    return connection


def create_tables():
    connection = get_connection()
    with connection.cursor() as cursor:
        table_name = "users"
        try:
            cursor.execute(
                "	CREATE TABLE `"
                + table_name
                + "` ( `user_id` varchar(18) DEFAULT NULL,  `address` varchar(42) DEFAULT NULL )"
            )
            print("------------------------------")
            print("Database tables created.")
            return create_tables
        except:
            pass


def get_airdrop_users():
    connection = get_connection()
    with connection.cursor() as cursor:
        sql = "SELECT user_id FROM users"
        cursor.execute(sql)
        tmp = []
        for user in cursor.fetchall():
            tmp.append(user["user_id"])
        return tmp


def get_airdrop_wallets():
    connection = get_connection()
    with connection.cursor() as cursor:
        sql = "SELECT address FROM users"
        cursor.execute(sql)
        tmp = []
        for user in cursor.fetchall():
            tmp.append(user["address"])
        return tmp


@bot.event
async def on_ready():
    print("------------------------------")
    print("Plugin: Discord Airdrop Bot")
    print("Author: fabston")
    print("------------------------------")
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------------------------------")


@bot.group()
async def airdrop(ctx):
    if not ctx.guild:
        connection = get_connection()
        with connection.cursor() as cursor:
            if not config.airdrop_live:
                await ctx.send(config.texts["airdrop_start"])
            elif str(ctx.message.author.id) in airdrop_users:
                sql = "SELECT address FROM users WHERE user_id = %s"
                cursor.execute(sql, str(ctx.message.author.id))
                wallet_address = cursor.fetchone()["address"]
                await ctx.send(
                    f"You successfully joined the airdrop. 🥳\n\nYour wallet address is:\n\n`{wallet_address}`"
                )
            elif len(airdrop_users) >= config.airdrop_cap:
                await ctx.send(config.texts["airdrop_max_cap"])
            elif str(ctx.subcommand_passed) in airdrop_wallets:
                await ctx.send(config.texts["airdrop_walletused"])
            elif eth_utils.is_address(ctx.subcommand_passed):
                sql = "INSERT INTO users(address, user_id) VALUES (%s, %s)"
                cursor.execute(sql, (ctx.subcommand_passed, ctx.message.author.id))
                airdrop_wallets.append(ctx.subcommand_passed)
                airdrop_users.append(ctx.message.author.id)
                await ctx.send(config.texts["airdrop_confirmation"])
                try:
                    channel = bot.get_channel(config.log_channel)
                    await channel.send(
                        "🎈 **Airdrop_Entry ({0}):**\n"
                        " • User: <@{1}> (`{1}`)\n"
                        " • Address: `{2}`\n"
                        " • Time: `{3} UTC`".format(
                            len(airdrop_users),
                            ctx.message.author.id,
                            ctx.subcommand_passed,
                            strftime("%Y-%m-%d %H:%M:%S", gmtime()),
                        )
                    )
                except:
                    pass
            elif ctx.subcommand_passed is None:
                await ctx.send(
                    "To join the airdrop use the following command:\n\n`!airdrop <YOUR WALLET ADDRESS>`"
                )
            else:
                await ctx.send(
                    f"❌ **Invalid address!**\n\nPlease try again by re-running the command.\n\n`!airdrop <YOUR WALLET ADDRESS>`"
                )
    else:
        await ctx.send(f"<@{ctx.message.author.id}>, this command works only DM's!")


@bot.command()
async def airdroplist(ctx):
    if not ctx.guild and str(ctx.message.author.id) in config.admins:
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "SELECT address FROM users"
            cursor.execute(sql)
            airdrop = "AIRDROP ({}):\n\n".format(len(airdrop_users))
            for user in cursor.fetchall():
                if user["address"] is not None:
                    address = user["address"]
                    airdrop += "{}\n".format(address)

            with BytesIO(str.encode(airdrop)) as output:
                await ctx.send(file=discord.File(fp=output, filename="AIRDROP.txt"))
    else:
        pass


create_db_tables = create_tables()
airdrop_users = get_airdrop_users()
airdrop_wallets = get_airdrop_wallets()

create_db_tables

bot.run(config.bot_token)
