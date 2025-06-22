from pycoingecko import CoinGeckoAPI

def get_crypto_price(coin_id='bitcoin', currency='usd'):
    cg = CoinGeckoAPI()
    data = cg.get_price(ids=coin_id, vs_currencies=currency)
    if coin_id in data:
        price = data[coin_id][currency]
        print(f"💰 {coin_id.capitalize()} price in {currency.upper()}: {price}")
    else:
        print("❌ Coin not found or API error.")

# Example usage
get_crypto_price('bitcoin', 'usd')
get_crypto_price('ethereum', 'inr')