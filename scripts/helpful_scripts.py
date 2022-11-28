from brownie import network, config, accounts, MockV3Aggregator

FORKED_LOCAL_ENV = ["mainnet-fork", "mainnet-fork-dev"]
# created ganache-local to be run on ganache app (not the cli)
# ...created in terminal by: 'ganache networks add Ethereum ganache-local host={URL in ganache} chainid={id in ganache}'
# ...this way can see deployment populate in 'deployments' folder
LOCAL_BLOCKCHAIN_ENV = ["development", "ganache-local"]
DECIMALS = 8
STARTING_PRICE = 1200e8

# if deploying on a dev chain can use account[0], otherwise pull from config
# get error for account[0] if not dev chain because no default account[0]
def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENV
        or network.show_active() in FORKED_LOCAL_ENV
    ):  # 'network' keyword in brownie
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    # MockV3Aggregator constructor takes inputs of (decimals, initial_answer)
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print("Mocks deployed")
