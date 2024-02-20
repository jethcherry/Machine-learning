import csv
import random

# Define the factors that affect business growth
factors = [
    "Revenue (Shillings)", "Profit (Shillings)", "Loss (Shillings)",
    "Customer Acquisition Cost (Shillings)", "Customer Lifetime Value (Shillings)",
    "Market Share (Percentage)", "Customer Satisfaction (Percentage)",
    "Employee Satisfaction (Percentage)", "Product Quality (Rating out of 10)",
    "Innovation (Rating out of 10)", "Market Trends (Rating out of 10)",
    "Type of Business", "Business Size", "Geographic Location",
    "Industry Trends (Percentage)", "Business Reputation (Percentage)",
    "Customer Retention Rate (Percentage)", "Employee Turnover Rate (Percentage)",
    "Market Saturation (Percentage)", "Pricing Strategy (Rating out of 10)",
    "Cost Management (Rating out of 10)", "Legal and Regulatory Compliance (Percentage)",
    "Brand Awareness (Percentage)", "Distribution Channels", "Customer Demographics",
    "Market Entry Barriers (Rating out of 10)", "Technological Disruption (Rating out of 10)",
    "Intellectual Property Protection (Percentage)", "Market Positioning (Percentage)",
    "Seasonal Variations (Percentage)", "Economic Indicators (Percentage)",
    "Partnerships and Alliances", "Quality of Leadership (Rating out of 10)",
    "Employee Morale (Rating out of 10)", "Financial Stability (Percentage)",
    "Customer Loyalty Programs (Percentage)", "Online Presence and E-commerce Strategy (Percentage)",
    "External Economic Factors (Percentage)",
    "Target"  # Add target as a factor
]

# Generate random data for each factor
dataset = []
zeros_count = 15000  # Equal number of 0s and 1s
ones_count = 15000
for _ in range(30000):  # Number of rows in the dataset
    row = {factor: random.uniform(0, 50000) if "Shillings" in factor else random.uniform(0, 10) if "Rating" in factor else random.uniform(0, 100) for factor in factors[:-1]}
    
    # Map categorical variables to integers
    row['Type of Business'] = random.randint(0, 20)  # Assuming 20 categories
    row['Business Size'] = random.randint(0, 2)  # 0 for Small, 1 for Medium, 2 for Large
    row['Geographic Location'] = random.randint(0, 2)  # 0 for Urban, 1 for Suburban, 2 for Rural
    row['Distribution Channels'] = random.randint(0, 2)  # 0 for Online, 1 for Offline, 2 for Both
    row['Customer Demographics'] = random.randint(0, 3)  # 0 for Youth, 1 for Adults, 2 for Seniors, 3 for Mixed
    row['Partnerships and Alliances'] = random.randint(0, 1)  # 0 for No, 1 for Yes
    
    # Assign the 'Target' variable with equal distribution of 0s and 1s
    if zeros_count > 0 and ones_count > 0:
        row['Target'] = random.choice([0, 1])
        if row['Target'] == 0:
            zeros_count -= 1
        else:
            ones_count -= 1
    elif zeros_count > 0:
        row['Target'] = 0
        zeros_count -= 1
    else:
        row['Target'] = 1
        ones_count -= 1
    
    dataset.append(row)

# Write the dataset to a CSV file
csv_file = "business_growth_dataset.csv"
with open(csv_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=factors)
    writer.writeheader()
    writer.writerows(dataset)

print(f"Dataset has been saved to {csv_file}")
