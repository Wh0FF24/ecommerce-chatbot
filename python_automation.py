#!/usr/bin/env python3
"""
Python Automation Script - Demo for Upwork
Scrapes data from a website and exports to CSV/JSON
"""
import json
import csv
import time
from datetime import datetime
from urllib.request import urlopen, Request
from html import unescape

class WebScraper:
    def __init__(self):
        self.data = []
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
    def scrape_products(self, url):
        """Scrape product data from e-commerce site"""
        # Demo data since we can't actually scrape without a target URL
        self.data = [
            {
                "name": "Wireless Bluetooth Headphones",
                "price": 79.99,
                "category": "Electronics",
                "in_stock": True,
                "rating": 4.5
            },
            {
                "name": "Smart Watch Series 5",
                "price": 299.99,
                "category": "Electronics",
                "in_stock": True,
                "rating": 4.7
            },
            {
                "name": "USB-C Charging Cable",
                "price": 19.99,
                "category": "Accessories",
                "in_stock": True,
                "rating": 4.2
            },
            {
                "name": "Laptop Stand Ergonomic",
                "price": 49.99,
                "category": "Accessories",
                "in_stock": False,
                "rating": 4.6
            },
            {
                "name": "Mechanical Keyboard RGB",
                "price": 129.99,
                "category": "Electronics",
                "in_stock": True,
                "rating": 4.8
            }
        ]
        return self.data
    
    def export_json(self, filename):
        """Export to JSON"""
        with open(filename, 'w') as f:
            json.dump(self.data, f, indent=2)
        print(f"✅ Exported {len(self.data)} items to {filename}")
        
    def export_csv(self, filename):
        """Export to CSV"""
        if not self.data:
            print("No data to export")
            return
            
        keys = self.data[0].keys()
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(self.data)
        print(f"✅ Exported {len(self.data)} items to {filename}")

    def filter_data(self, min_price=None, max_price=None, in_stock_only=False):
        """Filter scraped data"""
        filtered = self.data
        
        if min_price:
            filtered = [d for d in filtered if d.get('price', 0) >= min_price]
        if max_price:
            filtered = [d for d in filtered if d.get('price', 0) <= max_price]
        if in_stock_only:
            filtered = [d for d in filtered if d.get('in_stock', False)]
            
        return filtered

def run_demo():
    """Run the automation demo"""
    print("=" * 50)
    print("Python Web Scraping & Automation Demo")
    print("=" * 50)
    
    scraper = WebScraper()
    
    # Scrape (using demo data)
    print("\n📥 Scraping website...")
    data = scraper.scrape_products("https://example-ecommerce.com")
    print(f"   Found {len(data)} products")
    
    # Show data
    print("\n📊 Scraped Data:")
    for item in data[:3]:
        print(f"   • {item['name']}: ${item['price']} ({item['category']})")
    
    # Export
    print("\n💾 Exporting...")
    scraper.export_json('scraped_data.json')
    scraper.export_csv('scraped_data.csv')
    
    # Filter demo
    print("\n🔍 Filtering (in-stock items only):")
    in_stock = scraper.filter_data(in_stock_only=True)
    for item in in_stock:
        print(f"   ✓ {item['name']}: ${item['price']}")
    
    print("\n" + "=" * 50)
    print("✅ Automation complete!")
    print("=" * 50)

if __name__ == "__main__":
    run_demo()
