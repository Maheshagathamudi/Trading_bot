from bot import BasicBot

def main():
    bot = BasicBot()
    print("=== Binance Futures Trading Bot ===")

    try:
        symbol = input("Enter trading symbol (e.g., BTCUSDT): ").strip().upper()
        side = input("Enter side (BUY/SELL): ").strip().upper()
        order_type = input("Order type (MARKET/LIMIT/STOP-LIMIT): ").strip().upper()
        quantity = float(input("Enter quantity: "))

        if order_type == "LIMIT":
            price = float(input("Enter limit price: "))
            response = bot.place_limit_order(symbol, side, quantity, price)
        elif order_type == "STOP-LIMIT":
            stop_price = float(input("Enter stop price: "))
            limit_price = float(input("Enter limit price: "))
            response = bot.place_stop_limit_order(symbol, side, quantity, stop_price, limit_price)
        else:
            response = bot.place_market_order(symbol, side, quantity)

        print("\n=== Order Response ===")
        print(response)

    except Exception as e:
        import traceback
        print(f"Error: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    main()
