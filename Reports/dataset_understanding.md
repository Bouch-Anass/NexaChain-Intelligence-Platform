# Dataset Understanding & Architecture Report
**Project:** NexaChain Intelligence Platform
**Phase:** Task 2 - Dataset Familiarization

## 1. Dataset Portfolio Overview
Based on the official metadata document, the NexaChain ecosystem consists of 5 core enterprise datasets comprising over 310,000 records.

1. **Orders (`orders.csv`):** The central fact table capturing customer orders, fulfillment, and profitability. (120,000+ rows)
2. **Inventory (`inventory.csv`):** Daily inventory snapshots tracking stock levels, warehouse movements, and stockout risks. (55,000+ rows)
3. **Vendors (`vendors.csv`):** Monthly vendor performance snapshots powering the Vendor Risk Intelligence Score (VRIS). (22,000+ rows)
4. **Logistics (`logistics.csv`):** Shipment records capturing carrier performance, route details, and delivery delays. (85,000+ rows)
5. **Financials (`financials.csv`):** Weekly financial records integrating revenue, OPEX, and working capital metrics. (65,000+ rows)

## 2. Dataset Relationship Diagram (ERD)
The datasets are interconnected via shared foreign keys to enable multi-domain analytics. The Orders dataset serves as the central hub.

```mermaid
erDiagram
    VENDORS ||--o{ ORDERS : "receives (via vendor_id)"
    ORDERS ||--o{ LOGISTICS : "ships via (via order_id)"
    ORDERS ||--|| FINANCIALS : "billed in (via order_id)"
    VENDORS ||--o{ FINANCIALS : "has transactions (via vendor_id)"
    LOGISTICS ||--|| FINANCIALS : "costs recorded in (via shipment_id)"
    INVENTORY }o--o{ ORDERS : "linked by (via product_id)"
    VENDORS ||--o{ INVENTORY : "sources (via vendor_id)"

    ORDERS {
        string order_id PK
        string vendor_id FK
        string product_id FK
        date order_date
        decimal order_value_usd
        string order_status
    }
    
    INVENTORY {
        string inventory_id PK
        string product_id FK
        string vendor_id FK
        string warehouse_id
        int stock_on_hand
        int reorder_point
    }
    
    VENDORS {
        string vendor_record_id PK
        string vendor_id FK
        string vendor_name
        decimal vris_score
        string risk_category
    }
    
    LOGISTICS {
        string shipment_id PK
        string order_id FK
        date actual_delivery_date
        int delay_days
        int delay_flag
    }
    
    FINANCIALS {
        string finance_record_id PK
        string order_id FK
        string vendor_id FK
        string shipment_id FK
        decimal revenue_usd
        decimal working_capital_usd
    }
```

## 3. Key Relationships
* **Orders ↔ Logistics (1:N):** 1 order may have multiple shipments (split deliveries). Linked via `order_id`.
* **Orders ↔ Inventory (M:N):** Orders contain products, which are tracked in inventory. Linked via `product_id`.
* **Orders ↔ Vendors (N:1):** Multiple orders come from the same vendor. Linked via `vendor_id`.
* **Orders ↔ Financials (1:1):** Each order has a corresponding financial record. Linked via `order_id`.
* **Logistics ↔ Financials (1:1):** Each shipment has cost records in Financials. Linked via `shipment_id`.

## 4. Known Data Quality Issues (To verify in Task 3)
* **Orders:** ~3% duplicate `order_id`, ~5% NULL `delivery_date`.
* **Inventory:** ~4% NULL `reorder_point`, negative `stock_on_hand` values.
* **Vendors:** ~8% NULL `quality_score`, past `contract_expiry_date` without renewal.
* **Logistics:** ~6% `fuel_cost_usd` outliers, missing `delay_reason` for late shipments.
* **Financials:** ~6% NULL `working_capital_ratio`, duplicate records from AS/400.
