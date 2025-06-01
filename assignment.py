print("Hey there! I'm CryptoBuddy 🤖💰 – your AI-powered sidekick for smart, sustainable crypto picks!")
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}
def crypto_advice_bot():
    print("Hey there! I'm CryptoBuddy 🤖💰 – your AI-powered sidekick for smart, sustainable crypto picks!")
    
    while True:
        user_query = input("\nAsk me about crypto (type 'exit' to leave): ").lower()

        if 'exit' in user_query:
            print("Goodbye! Remember: Crypto is risky—always do your own research! 📉📈")
            break

        elif 'sustainable' in user_query:
            recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
            print(f"🌱 Invest in {recommend}! It’s eco-friendly and has long-term potential!")

        elif 'trending' in user_query or 'rising' in user_query:
            trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
            print(f"📈 These coins are trending up: {', '.join(trending)}")

        elif 'long-term' in user_query or 'growth' in user_query:
            long_term = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising" and crypto_db[coin]["sustainability_score"] > 0.7]
            if long_term:
                print(f"🚀 For long-term growth, consider: {', '.join(long_term)}")
            else:
                print("🤔 No coins fit that criteria right now.")

        elif 'market cap' in user_query:
            high_cap = [coin for coin in crypto_db if crypto_db[coin]["market_cap"] == "high"]
            print(f"💰 Coins with high market cap: {', '.join(high_cap)}")

        else:
            print("🤷‍♂️ I didn’t understand that. Try asking about trends, sustainability, or long-term growth.")
