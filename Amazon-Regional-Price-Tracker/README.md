# Amazon Regional Price & Buybox Protection System

## Business Problem: The Geographic Price Gap
In large e-commerce markets like India, pricing and availability are not uniform. Amazon's algorithm often awards the **Buybox** and determines **Lightning Deal eligibility** based on regional inventory and local competition.

**The Challenge:**
Standard automated trackers often scrape data based on the server's or the scraper's current location. This creates a "blind spot" for sellers. For example, a seller might appear to have the lowest price in Mumbai, but a competitor might be undercutting them in **Bangalore or Delhi**—where the majority of their sales are generated and where their primary warehouses are located. 

When competitors lower prices in these key regions, the seller may lose their "Deal" tags (Lightning Deals, Limited Time Offers) without even being aware of it, leading to significant revenue leakage and loss of marketplace momentum.

## Objective
To build a localized competitive intelligence tool that simulates user behavior across specific high-priority regions (via Pincodes) to monitor real-time pricing, Buybox winners, and promotional deal status.

## Key Features
- **Geographic Context Switching:** Automatically overrides the browser's location settings to scrape data as a user in a specific target city (e.g., Bangalore, Delhi).
- **Buybox Winner Identification:** Detects if the Buybox is held by Amazon or a third-party competitor.
- **Promotional Tag Tracking:** Monitors "Deal of the Day" and "Lightning Deal" status to ensure deal protection.
- **Regional Availability Check:** Identifies stock-outs that only affect specific delivery hubs.

## Impact & Business Value
- **Deal Protection:** Rapidly identify when a competitor's price drop threatens a scheduled Lightning Deal.
- **Localized Strategy:** Adjust pricing based on regional competitive intensity rather than a national average.
- **Inventory Optimization:** Understand stock status from the perspective of the customer in specific warehouse zones.

## Skills Demonstrated
- **Advanced Web Automation:** Handling complex, state-dependent UI components (Amazon Location Popover).
- **Competitor Intelligence:** Real-time extraction of marketplace metrics.
- **Business Logic Integration:** Solving a real-world e-commerce revenue leakage problem through AI-assisted automation.

## Repository Structure
```text
.
├── src/
│   └── amazon_regional_scraper.py   # Core automation engine
├── assets/                          # Dashboard & Output screenshots
└── README.md                        # Business case study
```

## How It Works
The script utilizes Selenium to:
1. Navigate to the marketplace gateway.
2. Interact with the Global Location Popover to inject a specific Pincode.
3. Refresh the session context to reflect regional pricing.
4. Iterate through a product portfolio to extract localized metrics into an Excel report.

---
*Note: This tool was developed to solve a critical business gap where national price tracking failed to capture regional competitive shifts affecting high-velocity sales zones.*
