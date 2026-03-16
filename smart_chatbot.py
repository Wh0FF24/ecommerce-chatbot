#!/usr/bin/env python3
"""
AI Chatbot with OpenAI Integration - Production Ready
For E-commerce Projects
"""
import os
import json

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

class SmartEcommerceChatbot:
    def __init__(self, openai_api_key=None):
        self.client = OpenAI(api_key=openai_api_key) if openai_api_key and OPENAI_AVAILABLE else None
        self.products = self._load_products()
        self.conversation_history = []
        
    def _load_products(self):
        return [
            {"id": 1, "name": "Wireless Headphones", "price": 79.99, "category": "electronics", "desc": "Premium noise-cancelling"},
            {"id": 2, "name": "Smart Watch Pro", "price": 299.99, "category": "electronics", "desc": "Health tracking + notifications"},
            {"id": 3, "name": "Running Shoes", "price": 89.99, "category": "sports", "desc": "Lightweight, breathable"},
            {"id": 4, "name": "Laptop Stand", "price": 49.99, "category": "accessories", "desc": "Ergonomic adjustable"},
            {"id": 5, "name": "USB-C Hub", "price": 39.99, "category": "accessories", "desc": "7-in-1 connectivity"},
        ]
    
    def chat(self, user_message, use_ai=True):
        """Main chat method"""
        self.conversation_history.append({"role": "user", "content": user_message})
        
        if use_ai and self.client:
            return self._ai_response(user_message)
        else:
            return self._rule_based_response(user_message)
    
    def _ai_response(self, user_message):
        """Use OpenAI for intelligent responses"""
        system_prompt = f"""You are an expert e-commerce sales assistant for a tech store.
You help customers find products, answer questions, and close sales.
Product catalog: {json.dumps(self.products)}
Be friendly, helpful, and guide customers toward purchases."""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=200
            )
            reply = response.choices[0].message.content
            self.conversation_history.append({"role": "assistant", "content": reply})
            return reply
        except Exception as e:
            return f"AI unavailable: {e}. Using basic mode."
    
    def _rule_based_response(self, user_message):
        """Fallback rule-based responses"""
        msg = user_message.lower()
        
        if 'price' in msg or 'cost' in msg:
            for p in self.products:
                if p['name'].lower() in msg:
                    return f"{p['name']}: ${p['price']} - {p['desc']}"
            return "Which product interests you? I can check prices."
        
        if 'recommend' in msg or 'best' in msg:
            top = self.products[:3]
            return "My top picks:\n" + "\n".join([f"• {p['name']} - ${p['price']}" for p in top])
        
        return "I can help you find products, check prices, or get recommendations. What do you need?"

def demo():
    api_key = os.environ.get("OPENAI_API_KEY")
    bot = SmartEcommerceChatbot(api_key)
    
    print("=== Smart AI E-commerce Chatbot ===")
    print(f"AI Mode: {'Enabled' if bot.client else 'Disabled (rule-based)'}\n")
    
    questions = [
        "Hi! What do you have?",
        "What's the best product you have?",
        "How much is the Smart Watch?"
    ]
    
    for q in questions:
        print(f"Customer: {q}")
        print(f"Bot: {bot.chat(q)}\n")

if __name__ == "__main__":
    demo()
