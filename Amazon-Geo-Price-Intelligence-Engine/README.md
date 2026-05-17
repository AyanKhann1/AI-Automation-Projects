# Amazon Geo-Price Intelligence Engine

## Business Problem: The Geographic Price Gap
In large e-commerce markets like India, pricing and availability are not uniform. Amazon's algorithm often awards the **Buybox** and determines **Lightning Deal eligibility** based on **regional inventory** and local competition.

**The Challenge:**
Standard automated trackers often scrape data based on the server's location. This creates a **"blind spot"** for sellers. A seller might have the lowest price in Mumbai, but a competitor might be undercutting them in **Bangalore or Delhi**—the high-velocity zones where the majority of sales are generated and primary warehouses are located.

When competitors lower prices in these key regions, sellers can lose their **"Deal" tags** (Lightning Deals, Limited Time Offers) without warning, leading to **significant revenue leakage** and loss of marketplace momentum.

## Objective
To build a **localized competitive intelligence tool** that simulates user behavior across high-priority regions (via Pincodes) to monitor **real-time pricing**, **Buybox winners**, and **promotional deal status**.

## Key Features
- **Geographic Context Switching:** Automatically overrides browser location settings to scrape data as a user in specific target cities (e.g., Bangalore, Delhi).
- **Buybox Winner Identification:** Detects if the Buybox is held by Amazon or a third-party competitor.
- **Promotional Tag Tracking:** Monitors **"Deal of the Day"** and **"Lightning Deal"** status to ensure deal protection.
- **Regional Availability Check:** Identifies stock-outs that affect specific delivery hubs.

## Impact & Business Value
- **Deal Protection:** Rapidly identify when a competitor's price drop threatens a scheduled Lightning Deal.
- **Localized Strategy:** Adjust pricing based on **regional competitive intensity** rather than a national average.
- **Inventory Optimization:** Understand stock status from the perspective of the customer in specific **warehouse zones**.

## Skills Demonstrated
- **Advanced Web Automation:** Handling complex, state-dependent UI components (Amazon Location Popover).
- **Competitor Intelligence:** Real-time extraction of localized marketplace metrics.
- **Business Logic Integration:** Solving a critical e-commerce revenue leakage problem through **AI-assisted automation**.

## Repository Structure
```text
.
├── src/
│   └── amazon_regional_scraper.py   # Core automation engine
├── assets/                          # Dashboard & Output screenshots
└── README.md                        # Business case study
```

## How It Works
The system utilizes **Selenium** to:
1. Navigate to the marketplace gateway.
2. Interact with the **Global Location Popover** to inject a specific Pincode.
3. Refresh the session context to reflect **regional pricing**.
4. Iterate through a product portfolio to extract localized metrics into a **structured Excel report**.

---
*Note: This tool was developed to bridge the gap where national price tracking failed to capture regional competitive shifts affecting high-velocity sales zones.*
