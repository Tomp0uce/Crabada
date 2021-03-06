Scripts & bots to interact with [Crabada](play.crabada.com)'s smart contracts.

# Features

- Automatically send crabs mining.
- Automatically claim rewards.
- Choose between several reinforcement strategies.
- Run the bot without human supervision.
- Send multiple teams mining (experimental)

# Looting

Building a looting bot is more difficult than a mining one, because there is more competition and you need to be faster than the other bots.

I am currently working towards this end, and so far the results have been satisfying.

Contact me if you are interested in the looting bot, but please be aware that it will not be free to use 🙂

# Quick start

1. Make sure you have Python 3.9 or later installed.
1. Install dependencies: `pip install -r requirements.txt`.
1. Copy _.env.example_ in _.env_ and customize the latter.
1. Make sure you `cd` in the root folder of the project (the same where this readme is)
1. Run any of the scripts in the _bin_ folder.

For example, run `python -m bin.mining.sendTeamsMining <your address>` to send teams mining and `python -m bin.mining.closeMines <your address>` to claim rewards on finished mines.

## Requirements

The bot requires Python 3.9; I have personally tested it on:

- **Mac Os 11 (Big Sur)** > Install python3 and pip3 with [Homebrew](https://brew.sh/) > `brew install python3`
- **Debian GNU/Linux 11 (bullseye)** > Install python3 and pip with apt-get > `apt-get install python3 pip git`

Users told me that they managed to run the bot on Ubuntu, too.

# Run without human supervision

In order to run the bot without human supervision, you'll need to set a cron job.

I would recommend to set the cron job on a remote server (for example on Vultr or AWS).
If you can't be bothered, you can also do it on your computer: just make sure you keep the computer turned on all the time.

### Mac instructions

Follow these instructions to send all available teams mining & to collect rewards for you:

1. Open crontab > `env EDITOR=nano crontab -e`
2. Insert the following lines:
    ```
    0,30 * * * * cd $HOME/crabada.py && /usr/local/bin/python -m bin.mining.sendTeamsMining <your address>
    15,45 * * * * cd $HOME/crabada.py && /usr/local/bin/python -m bin.mining.closeMines <your address>
    ```
3. Customize the lines with the path to the script and your wallet address.
4. The cron job will run twice every 30 minutes. Feel free to change the frequency; if in doubt use [Crontab Guru](https://crontab.guru/).
5. If you want to reinforce defense too, just add another line to the crontab that runs bin.mining.reinforceDefense.

Note: When editing python path (/usr/local/bin/python), use `which python3` or `which python` in Terminal to determine where your python3 is installed.

### Linux instructions

The above instructions for the Mac should work fine on Linux with minimal modifications.

### Windows instructions

I do not have a Windows machine to run tests; __if you know how to reliably set a cron job on Windows, feel free to add the instructions here :-)__

# Support for multiple teams

The bot can send multiple teams mining with one command, here's how:

1. Register the teams in the .env file:
    ```bash
    USER_1_TEAM_1="1111"
    USER_1_TEAM_2="2222"
    USER_1_TEAM_3="3333"
    ```
2. Run `python -m bin.mining.sendTeamsMining <your address>` to send all available teams mining.
3. Claim rewards on finished mines with `python -m bin.mining.closeMines <your address>`.

Please note that __multi-team support has not been thoroughly tested yet__: [create an issue](https://github.com/coccoinomane/dex-sniper.hardhat/issues/new) if you encounter any problem :-)

# Crabada.com Endpoints

The Crabada API has REST endpoints with base uri https://idle-api.crabada.com/public/idle/.

For a list of endpoints, see the [Postman collection](https://go.postman.co/workspace/Crypto~19d2a5ae-faa1-4999-af6e-e1c4c8428a7e/collection/18622998-191ed6a2-1026-4ae2-8fbd-a9f5b233bc9c).

# Contract

The idle game contract can be found at the following link:

- [Crabada: Game](https://snowtrace.io/address/0x82a85407bd612f52577909f4a58bfc6873f14da8) > [Decompiled](https://snowtrace.io/bytecode-decompiler?a=0x82a85407bd612f52577909f4a58bfc6873f14da8)

### Mining transactions

- [Start mining expedition tx](https://snowtrace.io/tx/0x46594658e0f65181d65bd6c229837d9fff962a0480e13d21f542733c0c1dbbb6)
- [First reinforcement tx](https://snowtrace.io/tx/0x1d8e002f497b925fba9f76b8909fa87d59a45d99e7e8ca9a1e0f6119b23da4b7)
- [Second reinforcemente tx](https://snowtrace.io/tx/0xe1cd5862278930acb1bf861ecba18fbb63e5696cb5779c3bcc590f8a397ad3b3)
- [Claim tx](https://snowtrace.io/tx/0x55a75966158e03c22058ac24dbe855ee7aa2437d719c61b54cf14c4a906d9631)
- [Claim tx](https://snowtrace.io/tx/0x65d7d2783f7817f3302cee3b5f1ca0dd3bb7ace19b172770df00800a51403124) (different sequence)

### Looting transactions

- [Attack tx](https://snowtrace.io/tx/0x21a7f94f6e02103b55d9b9fa53243ae1ac0eab8531f5588cfc4a0e6ace126902)
- [Settle tx](https://snowtrace.io/tx/0xb6853b50dd85e59062964a060e796ffcd13e3d72711e0789127f2f3d81f523d1)
- [startGame](https://snowtrace.io/tx/0x429bf6ad1fadf7666bb32e004572b2cd7e95f88fc6aeac2fd6052d338f663fc7) attacked [after 2 blocks](https://snowtrace.io/tx/0xa416719950157ebb7e2fc7078cd1ae3a98232c9229fc4f27ef678b38a3618205); look [how many tried to attack](https://snowtrace.io/txs?block=10345304) it without success!
- [startGame](https://snowtrace.io/tx/0x1ea87957255498b626423f578b8ca01e950deca53c7ada96b94c55012aa0c307) attacked [after 1 block](https://snowtrace.io/tx/0x47766dce7c005f796d6f6272a4a3365ac473eb8d7f8a39d2ec195ddc9f2e56e8).
- [startGame](https://snowtrace.io/tx/0xb1cac8f04de6f432858ddabb687f23c221cc5ed34b80639b54f54807afb3a793) attacked [after 2 blocks](https://snowtrace.io/tx/0x9363a133c736b06233688425978e8d7fd8b09f02a6b92129c3ee72f07e08ebbf).

# Events

### startGame

- Method > 0xe5ed1d59
- Example transaction > [0x41705baf18b1ebc8ec204926a8524d3530aada11bd3c249ca4a330ed047f005e](https://snowtrace.io/tx/0x41705baf18b1ebc8ec204926a8524d3530aada11bd3c249ca4a330ed047f005e) (click on "Logs")
- Topics:
 0. 0x0eef6f7452b7d2ee11184579c086fb47626e796a83df2b2e16254df60ab761eb
 1. Mine number, e.g. 605198
 2. Team number, e.g. 4476
 3. Game duration in seconds, e.g. 14400 is 4 hours
 4. CRA reward for miner win, in Wei, e.g. 4125000000000000000 is 4.125 CRA (with prime)
 5. TUS reward for miner win, in Wei, e.g. 334125000000000000000 is 334.125 TUS (with prime)

# To do

* Use a virtual environment to manage dependencies
* Adapt bot for anti-bot measures of the 7th of March
* Looting: No need to fetch team information from endpoint!
* Looting: Implement faction advantage
* Multi-user support: send teams from multiple wallets

# Might do

* Use cron library to schedule scripts
* Gas control: Stop if wallet has less than X ETH + set daily gas limit
* Better gas estimation ([eth_baseFee and eth_maxPriorityFeePerGas](https://docs.avax.network/learn/platform-overview/transaction-fees/))
* Use web3 default variable WEB3_PROVIDER_URI instead of WEB3_NODE_URI
* Use @property to define classattributes > https://realpython.com/python-property/

# Done

* Better validation of config values from .env
* Add cron example to README
* Add Twilio to reqs
* Fix lower-case folders bug (pull request #1)
* Extend Web3Watcher with async loop
* Define a Web3Watcher class to watch for logs
* Web3Client: Allow to specify contract and ABI ovverriding props
* In Python all class attributes are static > should declare them in the constructor? Even better: declare them only in docstring
* Implement a team's task parameter; more in general: how to run cron job for mining vs for looting?
* Find a way to differentiate/manage mines & loots
* Write reinforcement script
* Write startGame script
* Write closeGame script
* Reasonable defaults for gasLimit and maxPriorityFeePerGas for Avalanche
* Make it work for different chains than AVAX (gas limit, poa middleware...)
* Use EIP-1559 gas
* Embed gas estimation in client (without need to use parameters)
