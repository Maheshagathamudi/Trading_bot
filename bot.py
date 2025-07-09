from binance.client import Client
from binance.enums import *
import logging

class BasicBot:
    def __init__(self):
        self.api_key = "your_testnet_api_key"
        self.api_secret = "your_testnet_api_secret"

        self.client = Client(self.api_key, self.api_secret)

        # ✅ Set Binance Futures Testnet base URL
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'

        logging.basicConfig(level=logging.INFO)
        logging.info("Initialized Binance Futures Testnet client.")

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side == "BUY" else SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            return order
        except Exception as e:
            logging.error(f"Market order error: {e}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side == "BUY" else SIDE_SELL,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=str(price)
            )
            return order
        except Exception as e:
            logging.error(f"Limit order error: {e}")
            return None

    def place_stop_limit_order(self, symbol, side, quantity, stop_price, limit_price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side == "BUY" else SIDE_SELL,
                type=ORDER_TYPE_STOP_MARKET,
                stopPrice=str(stop_price),
                price=str(limit_price),
                quantity=quantity,
                timeInForce=TIME_IN_FORCE_GTC
            )
            return order
        except Exception as e:
            logging.error(f"Stop-limit order error: {e}")
            return None
