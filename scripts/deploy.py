from brownie import FundMe, MockV3Aggregator, network, config

# may need to create blank '__init__.py' file in same folder to pull function below
# ...supposedly depends on the Python version
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENV


def deploy_fund_me():
    account = get_account()

    # if on persistent network use associated pricefeed address
    # else, deploy mock
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENV:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    # can use the 'publish_source' to publish to Etherscan and verify contract
    fund_me = FundMe.deploy(
        # passing variable to constructor w/ brownie
        price_feed_address,
        {"from": account},
        # T/F based on what the network settings are in config file
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
