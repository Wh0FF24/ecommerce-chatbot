#!/usr/bin/env python3
"""
E-commerce AI Chatbot - Proof of Concept
Built by Atlas for Upwork proposal demonstration
"""
import json
import random
from datetime import datetime

class EcommerceChatbot:
    def __init__(self, store_name="TechStore"):
        self.store_name = store_name
        self.products = [
            {"id": 1, "name": "Wireless Headphones", "price": 79.99, "category": "electronics"},
            {"id": 2, "name": "Smart Watch Pro", "price": 299.99, "category": "electronics"},
            {"id": 3, "name": "Running Shoes", "price": 89.99, "category": "sports"},
            {"id": 4, "name": "Laptop Stand", "price": 49.99, "category": "accessories"},
            {"id": 5, "name": "USB-C Hub", "price": 39.99, "category": "accessories"},
        ]
        self.conversation_state = {}
        
    def process_message(self, user_message):
        """Process user message and return response"""
        user_message = user_message.lower()
        
        # Greeting
        if any(word in user_message for word in ['hi', 'hello', 'hey']):
            return self._greeting()
        
        # Product search
        if any(word in user_message for word in ['product', 'search', 'find', 'looking for', 'buy']):
            return self._search_products(user_message)
        
        # Price inquiry
        if any(word in user_message for word in ['price', 'cost', 'how much']):
            return self._handle_price(user_message)
        
        # Recommendations
        if any(word in user_message for word in ['recommend', 'suggestion', 'best']):
            return self._recommend()
        
        # Cart/order
        if any(word in user_message for word in ['cart', 'order', 'buy', 'purchase']):
            return self._handle_order(user_message)
        
        # Support
        if any(word in user_message for word in ['help', 'support', 'problem', 'issue']):
            return self._support()
        
        return self._fallback()
    
    def _greeting(self):
        return f"Hi! Welcome to {self.store_name}. I'm your AI shopping assistant. I can help you:\n- Find products\n- Check prices\n- Get recommendations\n- Place orders\n\nWhat are you looking for today?"
    
    def _search_products(self, query):
        # Extract category if mentioned
        categories = ['electronics', 'sports', 'accessories', 'clothing']
        found = self.products
        
        for cat in categories:
            if cat in query:
                found = [p for p in self.products if p['category'] == cat]
                break
        
        if found:
            response = "Here are some products I found:\n\n"
            for p in found:
                response += f"• {p['name']} - ${p['price']}\n"
            response += "\nWould you like to add any of these to your cart?"
            return response
        return "I couldn't find products matching your search. Can you try different keywords?"
    
    def _handle_price(self, query):
        # Extract product name
        for product in self.products:
            if product['name'].lower() in query:
                return f"The {product['name']} costs ${product['price']}. Would you like to add it to your cart?"
        return "Which product's price would you like to know? I can search our catalog."
    
    def _recommend(self):
        featured = random.sample(self.products, 3)
        response = "Here are my top recommendations:\n\n"
        for i, p in enumerate(featured, 1):
            response += f"{i}. {p['name']} - ${p['price']}\n"
        response += "\nWould any of these interest you?"
        return response
    
    def _handle_order(self, query):
        return "I'd be happy to help you place an order! Which product would you like to buy? Or would you like me to show you our cart?"
    
    def _support(self):
        return "I'm here to help! For technical issues, I can connect you with our support team. What seems to be the problem?"
    
    def _fallback(self):
        responses = [
            "I'm not sure I understood that. Can you rephrase?",
            "I can help you find products, check prices, or place orders. What would you like?",
            "Let me help you find what you need. What are you looking for?"
        ]
        return random.choice(responses)

def demo():
    """Demo the chatbot"""
    bot = EcommerceChatbot("TechStore")
    
    test_messages = [
        "Hi there!",
        "I want to buy headphones",
        "How much are they?",
        "What do you recommend?",
    ]
    
    print("=== E-commerce AI Chatbot Demo ===\n")
    for msg in test_messages:
        print(f"User: {msg}")
        print(f"Bot: {bot.process_message(msg)}")
        print()

if __name__ == "__main__":
    demo()
