import re
import random
from datetime import datetime

class CryptoBuddy:
    def __init__(self):
        self.name = "CryptoBuddy"
        self.crypto_db = {
            "Bitcoin": {
                "symbol": "BTC",
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3,
                "risk_level": "medium",
                "current_price": 67500,
                "description": "The original cryptocurrency and digital gold standard"
            },
            "Ethereum": {
                "symbol": "ETH", 
                "price_trend": "stable",
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6,
                "risk_level": "medium",
                "current_price": 3800,
                "description": "Smart contract platform powering DeFi and NFTs"
            },
            "Cardano": {
                "symbol": "ADA",
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8,
                "risk_level": "medium-high",
                "current_price": 0.45,
                "description": "Research-driven blockchain focused on sustainability"
            },
            "Solana": {
                "symbol": "SOL",
                "price_trend": "volatile",
                "market_cap": "high",
                "energy_use": "low",
                "sustainability_score": 7,
                "risk_level": "high",
                "current_price": 140,
                "description": "Fast blockchain for DeFi and Web3 applications"
            },
            "Polygon": {
                "symbol": "MATIC",
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "very_low",
                "sustainability_score": 9,
                "risk_level": "medium-high",
                "current_price": 0.72,
                "description": "Ethereum scaling solution with carbon-negative goals"
            }
        }
        
        self.greetings = [
            "Hey there, crypto explorer! 🚀 I'm CryptoBuddy, your AI-powered financial sidekick!",
            "Welcome to the crypto universe! 🌟 Ready to find your next green investment?",
            "Greetings, future crypto millionaire! 💰 Let's navigate these digital waters together!"
        ]
        
        self.goodbye_phrases = [
            "Happy investing! Remember: DYOR (Do Your Own Research)! 🚀",
            "May your portfolio be green and your gains be real! 💚📈",
            "Crypto adventure awaits! Stay safe out there! 🛡️✨"
        ]

    def greet(self):
        """Welcome message with personality"""
        greeting = random.choice(self.greetings)
        menu = """
🤖 What can I help you with today?

💡 Try asking me:
• "What's the most sustainable crypto?"
• "Which coin is trending up?"
• "Show me low-risk investments"
• "Compare Bitcoin and Ethereum"
• "What should I buy for long-term growth?"
• "Help" for more options
• "Quit" to exit

⚠️ DISCLAIMER: Crypto investments are risky - always do your own research!
        """
        return f"{greeting}\n{menu}"

    def analyze_query(self, query):
        """AI decision-making logic based on user intent"""
        query = query.lower().strip()
        
        # Goodbye detection
        if any(word in query for word in ['bye', 'quit', 'exit', 'goodbye']):
            return random.choice(self.goodbye_phrases)
        
        # Help menu
        if 'help' in query:
            return self.show_help()
        
        # Sustainability focus
        if any(word in query for word in ['sustainable', 'eco', 'green', 'environment', 'energy']):
            return self.recommend_sustainable()
        
        # Profitability focus
        if any(word in query for word in ['profit', 'rising', 'trending', 'growing', 'gains']):
            return self.recommend_profitable()
        
        # Risk-based recommendations
        if any(word in query for word in ['safe', 'low risk', 'stable', 'secure']):
            return self.recommend_low_risk()
        
        if any(word in query for word in ['high risk', 'volatile', 'risky']):
            return self.recommend_high_risk()
        
        # Long-term vs short-term
        if any(word in query for word in ['long term', 'long-term', 'future', 'hold']):
            return self.recommend_long_term()
        
        # Comparison requests
        if 'compare' in query or 'vs' in query:
            return self.handle_comparison(query)
        
        # Specific coin queries
        for coin in self.crypto_db:
            if coin.lower() in query or self.crypto_db[coin]['symbol'].lower() in query:
                return self.analyze_specific_coin(coin)
        
        # Market overview
        if any(word in query for word in ['overview', 'summary', 'all', 'list']):
            return self.market_overview()
        
        # Default response with suggestions
        return self.default_response()

    def recommend_sustainable(self):
        """Find most eco-friendly crypto"""
        sustainable_coins = [(coin, data['sustainability_score']) 
                           for coin, data in self.crypto_db.items()]
        sustainable_coins.sort(key=lambda x: x[1], reverse=True)
        
        top_coin = sustainable_coins[0][0]
        data = self.crypto_db[top_coin]
        
        response = f"""🌱 **SUSTAINABILITY CHAMPION**: {top_coin} ({data['symbol']})

🏆 **Why it's eco-friendly**:
• Sustainability Score: {data['sustainability_score']}/10
• Energy Use: {data['energy_use'].title()}
• {data['description']}

💰 **Investment Profile**:
• Current Price: ${data['current_price']:,}
• Trend: {data['price_trend'].title()}
• Risk Level: {data['risk_level'].title()}

🌟 **CryptoBuddy's Take**: Perfect for environmentally conscious investors who want to support green blockchain technology!"""

        return response

    def recommend_profitable(self):
        """Find trending/rising cryptocurrencies"""
        rising_coins = [(coin, data) for coin, data in self.crypto_db.items() 
                       if data['price_trend'] in ['rising', 'volatile']]
        
        if not rising_coins:
            return "🤔 Currently no coins are showing strong upward trends. Market might be consolidating!"
        
        # Prioritize by market cap and sustainability
        rising_coins.sort(key=lambda x: (
            1 if x[1]['market_cap'] == 'high' else 0,
            x[1]['sustainability_score']
        ), reverse=True)
        
        recommendations = []
        for coin, data in rising_coins[:3]:  # Top 3 recommendations
            recommendations.append(f"• **{coin}** ({data['symbol']}): {data['price_trend'].title()} trend, ${data['current_price']:,}")
        
        response = f"""📈 **TRENDING UP**: Hot cryptocurrencies right now!

{chr(10).join(recommendations)}

🎯 **Pro Tip**: {rising_coins[0][0]} combines strong growth potential with decent fundamentals. But remember - rising trends can reverse quickly in crypto!

⚠️ **Risk Warning**: Trending coins can be volatile. Consider your risk tolerance!"""

        return response

    def recommend_low_risk(self):
        """Recommend stable, established cryptocurrencies"""
        stable_coins = [(coin, data) for coin, data in self.crypto_db.items() 
                       if data['market_cap'] == 'high' and data['risk_level'] in ['low', 'medium']]
        
        if not stable_coins:
            stable_coins = [(coin, data) for coin, data in self.crypto_db.items() 
                           if data['market_cap'] == 'high']
        
        response = "🛡️ **STABLE PICKS**: Lower-risk crypto options\n\n"
        
        for coin, data in stable_coins[:2]:
            response += f"""**{coin}** ({data['symbol']}):
• Market Cap: {data['market_cap'].title()}
• Risk Level: {data['risk_level'].title()}
• Price: ${data['current_price']:,}
• Status: {data['price_trend'].title()}

"""
        
        response += "💡 **CryptoBuddy's Advice**: Even 'stable' crypto is riskier than traditional investments. Start small and diversify!"
        
        return response

    def recommend_high_risk(self):
        """Recommend higher-risk, higher-reward options"""
        risky_coins = [(coin, data) for coin, data in self.crypto_db.items() 
                      if 'high' in data['risk_level']]
        
        if not risky_coins:
            return "🎲 Currently no high-risk options in my database. That might be a good thing! 😅"
        
        response = "🎲 **HIGH RISK, HIGH REWARD**: For the bold investors!\n\n"
        
        for coin, data in risky_coins:
            response += f"""**{coin}** ({data['symbol']}):
• Risk Level: {data['risk_level'].title()}
• Price: ${data['current_price']:,}
• Trend: {data['price_trend'].title()}
• Potential: {data['description']}

"""
        
        response += "⚠️ **WARNING**: Only invest what you can afford to lose completely!"
        
        return response

    def recommend_long_term(self):
        """Long-term investment recommendations"""
        # Prioritize sustainability and market cap for long-term
        long_term_scores = []
        for coin, data in self.crypto_db.items():
            score = data['sustainability_score']
            if data['market_cap'] == 'high':
                score += 3
            elif data['market_cap'] == 'medium':
                score += 1
            long_term_scores.append((coin, score, data))
        
        long_term_scores.sort(key=lambda x: x[1], reverse=True)
        
        top_pick = long_term_scores[0]
        
        response = f"""🏗️ **LONG-TERM HODL RECOMMENDATION**:

🥇 **Top Pick**: {top_pick[0]} ({top_pick[2]['symbol']})
• Sustainability Score: {top_pick[2]['sustainability_score']}/10
• Market Position: {top_pick[2]['market_cap'].title()}
• Technology: {top_pick[2]['description']}
• Current Price: ${top_pick[2]['current_price']:,}

🎯 **Why for long-term**:
• Strong fundamentals
• Sustainable technology
• Established market presence

📅 **Strategy**: Consider dollar-cost averaging over 6-12 months rather than lump sum investing!"""

        return response

    def handle_comparison(self, query):
        """Handle comparison requests"""
        mentioned_coins = []
        for coin in self.crypto_db:
            if coin.lower() in query or self.crypto_db[coin]['symbol'].lower() in query:
                mentioned_coins.append(coin)
        
        if len(mentioned_coins) < 2:
            return "🤔 I need at least two cryptocurrencies to compare. Try: 'Compare Bitcoin and Ethereum'"
        
        coin1, coin2 = mentioned_coins[0], mentioned_coins[1]
        data1, data2 = self.crypto_db[coin1], self.crypto_db[coin2]
        
        response = f"""⚖️ **CRYPTO COMPARISON**: {coin1} vs {coin2}

**{coin1} ({data1['symbol']})**:
• Price: ${data1['current_price']:,}
• Trend: {data1['price_trend'].title()}
• Sustainability: {data1['sustainability_score']}/10
• Risk: {data1['risk_level'].title()}

**{coin2} ({data2['symbol']})**:
• Price: ${data2['current_price']:,}
• Trend: {data2['price_trend'].title()}
• Sustainability: {data2['sustainability_score']}/10  
• Risk: {data2['risk_level'].title()}

🏆 **Winner depends on your goals**:
• For sustainability: {coin1 if data1['sustainability_score'] > data2['sustainability_score'] else coin2}
• For stability: {coin1 if data1['market_cap'] == 'high' else coin2}"""

        return response

    def analyze_specific_coin(self, coin):
        """Detailed analysis of a specific cryptocurrency"""
        data = self.crypto_db[coin]
        
        # Generate recommendation based on multiple factors
        pros = []
        cons = []
        
        if data['sustainability_score'] >= 7:
            pros.append("Eco-friendly and sustainable")
        elif data['sustainability_score'] <= 4:
            cons.append("High energy consumption")
        
        if data['market_cap'] == 'high':
            pros.append("Established market leader")
        elif data['market_cap'] == 'low':
            cons.append("Smaller market presence")
        
        if data['price_trend'] == 'rising':
            pros.append("Currently trending upward")
        elif data['price_trend'] == 'volatile':
            cons.append("High price volatility")
        
        recommendation = "STRONG BUY 🟢" if len(pros) > len(cons) else "MODERATE BUY 🟡" if len(pros) == len(cons) else "PROCEED WITH CAUTION 🟠"
        
        response = f"""📊 **DETAILED ANALYSIS**: {coin} ({data['symbol']})

💰 **Current Price**: ${data['current_price']:,}
📈 **Trend**: {data['price_trend'].title()}
🏢 **Market Cap**: {data['market_cap'].title()}
🌱 **Sustainability**: {data['sustainability_score']}/10
⚠️ **Risk Level**: {data['risk_level'].title()}

📝 **About**: {data['description']}

✅ **Pros**: {', '.join(pros) if pros else 'Stable fundamentals'}
❌ **Considerations**: {', '.join(cons) if cons else 'Standard crypto risks apply'}

🎯 **CryptoBuddy's Verdict**: {recommendation}"""

        return response

    def market_overview(self):
        """Overview of all tracked cryptocurrencies"""
        response = "📊 **CRYPTO MARKET OVERVIEW**\n\n"
        
        for coin, data in self.crypto_db.items():
            trend_emoji = "📈" if data['price_trend'] == 'rising' else "📊" if data['price_trend'] == 'stable' else "⚡"
            eco_emoji = "🌱" if data['sustainability_score'] >= 7 else "⚠️" if data['sustainability_score'] <= 4 else "🟡"
            
            response += f"""{trend_emoji} **{coin}** ({data['symbol']}): ${data['current_price']:,}
   Status: {data['price_trend'].title()} | Eco: {eco_emoji} {data['sustainability_score']}/10

"""
        
        response += "💡 **Quick Stats**: Tracking 5 major cryptocurrencies with sustainability focus!"
        return response

    def show_help(self):
        """Show available commands and features"""
        return """🤖 **CRYPTOBUDDY HELP MENU**

🔍 **What I can analyze**:
• Sustainability and eco-friendliness
• Price trends and profitability
• Risk levels and stability
• Long-term vs short-term potential
• Detailed coin comparisons

💬 **Try these commands**:
• "Most sustainable crypto"
• "Which coin is rising?"
• "Low risk investments"
• "Compare Bitcoin vs Ethereum"
• "Tell me about Cardano"
• "Market overview"
• "Long-term recommendations"

🎯 **My AI Decision Process**:
I analyze multiple factors including sustainability scores, market trends, risk levels, and market cap to provide personalized recommendations based on your investment goals!

⚠️ **Remember**: I'm here to help with research, but always do your own due diligence before investing!"""

    def default_response(self):
        """Default response when query isn't understood"""
        suggestions = [
            "Which crypto is most sustainable?",
            "Show me trending cryptocurrencies",
            "What's good for long-term investment?",
            "Compare Bitcoin and Ethereum"
        ]
        
        return f"""🤔 I didn't quite catch that! Let me help you explore crypto investments.

💡 **Try asking me**:
• "{random.choice(suggestions)}"
• Type "help" for all available options
• Or just tell me what kind of investment you're looking for!

🎯 **What are you interested in**: Sustainability? Profits? Low risk? Long-term growth?"""

def main():
    """Main chatbot interaction loop"""
    bot = CryptoBuddy()
    print("="*60)
    print(bot.greet())
    print("="*60)
    
    conversation_count = 0
    
    while True:
        try:
            user_input = input(f"\n💬 You: ").strip()
            
            if not user_input:
                print("🤖 CryptoBuddy: I'm here when you're ready to talk crypto! Try asking me something.")
                continue
            
            response = bot.analyze_query(user_input)
            print(f"\n🤖 CryptoBuddy: {response}")
            
            conversation_count += 1
            
            # Occasional engagement prompts
            if conversation_count % 3 == 0:
                print(f"\n💡 Tip: Try asking about sustainability or comparing different coins!")
            
            # Check for goodbye
            if any(word in user_input.lower() for word in ['bye', 'quit', 'exit', 'goodbye']):
                break
                
        except KeyboardInterrupt:
            print(f"\n\n🤖 CryptoBuddy: {random.choice(bot.goodbye_phrases)}")
            break
        except Exception as e:
            print(f"🤖 CryptoBuddy: Oops! Something went wrong. Let's try again! 🔄")

# Run the chatbot
if __name__ == "__main__":
    main()
