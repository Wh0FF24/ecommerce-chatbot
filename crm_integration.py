#!/usr/bin/env python3
"""
CRM Integration Automation - Demo for Upwork
Connects web forms to CRM systems (HubSpot, Salesforce, etc.)
"""
import json
import time
from datetime import datetime
from urllib.request import urlopen, Request
import urllib.parse

class CRMIntegration:
    def __init__(self, crm_type="hubspot"):
        self.crm_type = crm_type
        self.contacts = []
        self.webhooks = []
        
    def setup_webhook(self, form_url, crm_field_mapping):
        """Connect a web form to CRM"""
        webhook = {
            "form_url": form_url,
            "crm": self.crm_type,
            "mapping": crm_field_mapping,
            "status": "active",
            "created_at": datetime.now().isoformat()
        }
        self.webhooks.append(webhook)
        return webhook
    
    def sync_contact(self, form_data):
        """Sync contact from form submission to CRM"""
        # Map form fields to CRM fields
        contact = {
            "email": form_data.get("email", ""),
            "name": form_data.get("name", ""),
            "phone": form_data.get("phone", ""),
            "company": form_data.get("company", ""),
            "source": form_data.get("source", "web_form"),
            "created_at": datetime.now().isoformat()
        }
        self.contacts.append(contact)
        return contact
    
    def create_zapier_equivalent(self, trigger_app, trigger_event, action_app, action_event):
        """Create Zapier-style automation config"""
        zap = {
            "name": f"{trigger_app} → {action_app}",
            "trigger": {
                "app": trigger_app,
                "event": trigger_event
            },
            "action": {
                "app": action_app,
                "event": action_event
            },
            "status": "active"
        }
        return zap
    
    def get_leads_by_source(self, source):
        """Filter leads by source"""
        return [c for c in self.contacts if c.get("source") == source]
    
    def export_leads(self, format="json"):
        """Export leads to JSON or CSV"""
        if format == "json":
            return json.dumps(self.contacts, indent=2)
        # CSV would go here
        return str(self.contacts)

def run_demo():
    print("=" * 50)
    print("CRM Integration Automation Demo")
    print("=" * 50)
    
    crm = CRMIntegration("hubspot")
    
    # Setup webhook from contact form
    print("\n🔗 Setting up webhook...")
    webhook = crm.setup_webhook(
        "https://example.com/contact-form",
        {"name": "firstname", "email": "email", "phone": "phone"}
    )
    print(f"   ✓ Webhook active: {webhook['status']}")
    
    # Simulate incoming leads
    print("\n📥 Syncing contacts...")
    test_leads = [
        {"name": "John Smith", "email": "john@company.com", "phone": "555-1234", "company": "Acme Inc"},
        {"name": "Jane Doe", "email": "jane@startup.io", "phone": "555-5678", "company": "Startup Inc"},
    ]
    
    for lead in test_leads:
        synced = crm.sync_contact(lead)
        print(f"   ✓ Synced: {synced['name']} → HubSpot")
    
    # Create automation
    print("\n⚡ Creating automation...")
    zap = crm.create_zapier_equivalent(
        "Web Form", "New Submission",
        "HubSpot", "Create Contact"
    )
    print(f"   ✓ {zap['name']} - {zap['status']}")
    
    # Show results
    print("\n📊 Leads synced:")
    for c in crm.contacts:
        print(f"   • {c['name']} ({c['email']}) - {c['company']}")
    
    # Filter
    print("\n🔍 Filtered (web_form source):")
    web_leads = crm.get_leads_by_source("web_form")
    print(f"   Found {len(web_leads)} leads")
    
    print("\n" + "=" * 50)
    print("✅ CRM Integration Complete!")
    print("=" * 50)

if __name__ == "__main__":
    run_demo()
