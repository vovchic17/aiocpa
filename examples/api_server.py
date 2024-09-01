from cryptopay import MAINNET, TESTNET, CryptoPay

main_client = CryptoPay(
    token="API_TOKEN",
    api_server=MAINNET,  # MAINNET is default
)

test_client = CryptoPay(
    token="API_TOKEN",
    api_server=TESTNET,
)
