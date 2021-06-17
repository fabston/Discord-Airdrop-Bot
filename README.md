<p align="center"><a href="https://github.com/fabston/Discord-Airdrop-Bot" target="_blank"><img src="https://github.com/fabston/Discord-Airdrop-Bot/blob/main/assets/logo.png?raw=true"></a></p>

<p align="center">
    <a href="https://www.python.org/downloads/release/python-380/"><img src="https://img.shields.io/badge/python-3.8-blue.svg?style=plastic" alt="Python version"></a>
    <a href="https://github.com/fabston/Discord-Airdrop-Bot/blob/master/LICENSE"><img src="https://img.shields.io/github/license/fabston/Discord-Airdrop-Bot?style=plastic" alt="GitHub license"></a>
    <a href="https://github.com/fabston/Discord-Airdrop-Bot/issues"><img src="https://img.shields.io/github/issues/fabston/Discord-Airdrop-Bot?style=plastic" alt="GitHub issues"></a>
    <a href="https://github.com/fabston/Discord-Airdrop-Bot/pulls"><img src="https://img.shields.io/github/issues-pr/fabston/Discord-Airdrop-Bot?style=plastic" alt="GitHub pull requests"></a>
    <br /><a href="https://github.com/fabston/Discord-Airdrop-Bot/stargazers"><img src="https://img.shields.io/github/stars/fabston/Discord-Airdrop-Bot?style=social" alt="GitHub stars"></a>
    <a href="https://github.com/fabston/Discord-Airdrop-Bot/network/members"><img src="https://img.shields.io/github/forks/fabston/Discord-Airdrop-Bot?style=social" alt="GitHub forks"></a>
    <a href="https://github.com/fabston/Discord-Airdrop-Bot/watchers"><img src="https://img.shields.io/github/watchers/fabston/Discord-Airdrop-Bot?style=social" alt="GitHub watchers"></a>
</p>

<p align="center">
  <a href="#about">About</a>
  •
  <a href="#features">Features</a>
  •
  <a href="#installation">Installation</a>
  •
  <a href="#images">Images</a>
  •
  <a href="#how-can-i-help">Help</a>
</p>

## About
The **Discord Airdrop Bot** 💰 helps you to manage your airdrops on ERC-20, BEP-20 etc. tokens.

### Telegram Airdrop Bot
I have also published a similar bot for Telegram. You can find it [here](https://github.com/fabston/Telegram-Airdrop-Bot).


## Features
- Check if a correct ERC-20 address has been provided
- Set a max cap
- Each wallet address can only be submitted once
- Receive detailed notifications for new submissions
- Enable / disable the airdrop
- Admins can export the airdrop list by command (`!airdroplist`)

> 💡 Got a feature idea? Open an [issue](https://github.com/fabston/Discord-Airdrop-Bot/issues/new?assignees=&labels=enhancement&template=feature-request---.md) and I might implement it.


## Installation
> ⚠️ Best to run the bot on a VPS. I can recommend [Hetzner](https://fabston.dev/hetzner).
1. Log into MySQL (`sudo mysql`) and create a dedicated database and user with the following commands:
   1. `CREATE DATABASE DiscordAirdropBot;`
   1. `CREATE USER 'AirdropUser'@'localhost' IDENTIFIED BY '<YOUR PASSWORD>';`
   1. `GRANT ALL PRIVILEGES ON DiscordAirdropBot . * TO 'AirdropUser'@'localhost';`
   1. `exit;`
1. Clone this repository `git clone https://github.com/fabston/Discord-Airdrop-Bot.git`
1. Create your virtual environment `python3 -m venv Discord-Airdrop-Bot`
1. Activate it `source Discord-Airdrop-Bot/bin/activate && cd Discord-Airdrop-Bot`
1. Install all requirements `pip install -r requirements.txt`
1. Edit and update [`config.py`](https://github.com/fabston/Discord-Airdrop-Bot/blob/master/config.py)
1. Run the bot `python main.py`


## Images
Coming soon...

## How can I help?
All kinds of contributions are welcome 🙌! The most basic way to show your support is to `⭐️ star` the project, or raise [`🐞 issues`](https://github.com/fabston/Discord-Airdrop-Bot/issues/new/choose). You can also support this project by becoming a [sponsor on GitHub](https://github.com/sponsors/fabston) to ensure this journey continues indefinitely! 🚀

***

<p align="center">
    <a href="https://www.buymeacoffee.com/fabston"><img alt="Buy Me A Coffee" title="☕️" src="https://github.com/fabston/Discord-Airdrop-Bot/blob/main/assets/bmac.png?raw=true" width=200px></a>
</p>